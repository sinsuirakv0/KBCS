# v16.0.2 → v16.0.3 · 最優先の変更候補 (11)

[一覧の目次](README.md)

<a id="compare-c52333e517375edaa3c641d58f184f65"></a>

### [`004fe468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md) → [`004fe788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fe788.md) _ZN5Botan8read_cfgERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 23件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00494cbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00494/00494cbc.md) [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)
- 新版 呼出元 0件  · 呼出先 23件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00494fdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00494/00494fdc.md) [`004a6bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.55% / 新版 98.55%

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
      "definition_site": "004feb8c",
      "incomplete_value": false,
      "site": "004feb90",
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
            "const:785:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe86c",
      "incomplete_value": false,
      "site": "004fe870",
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
    "ordinal": 20,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004febe8",
      "incomplete_value": false,
      "site": "004febf4",
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
            "const:6ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe8c8",
      "incomplete_value": false,
      "site": "004fe8d4",
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
            "const:555:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004febfc",
      "incomplete_value": false,
      "site": "004fec04",
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
            "const:cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fe8dc",
      "incomplete_value": false,
      "site": "004fe8e4",
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
            "const:8b:8"
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
      "004fe840",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "004fe874",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004feb8c",
      "PARAM",
      [
        "storage",
        "002c8735",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004fe840",
      "READ",
      [
        "storage",
        "00c9bcd0",
        null,
        "pointer"
      ]
    ],
    [
      "004fe874",
      "PARAM",
      [
        "storage",
        "01128ed8",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004feb8c",
      "PARAM",
      [
        "storage",
        "002c8785",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fe870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe870) · [`004fe8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe8d4) · [`004fe8e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fe468.md#insn-004fe8e4)
- 新版 [`004feb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fe788.md#insn-004feb90) · [`004febf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fe788.md#insn-004febf4) · [`004fec04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fe788.md#insn-004fec04)

~~~diff
- 004fe870 ["INT_ADD", "register:40f0:8", ["const:4fe870:8", "const:4:8"]]
- 004fe870 ["CALL", null, ["callee:00494fdc:8"]]
+ 004feb90 ["INT_ADD", "register:40f0:8", ["const:4feb90:8", "const:4:8"]]
+ 004feb90 ["CALL", null, ["callee:00494fdc:8"]]
- 004fe870 bytes 1359fe97
+ 004feb90 bytes 1359fe97
- 004fe8d4 ["INT_ADD", "register:40f0:8", ["const:4fe8d4:8", "const:4:8"]]
- 004fe8d4 ["CALL", null, ["callee:00c59150:8"]]
+ 004febf4 ["INT_ADD", "register:40f0:8", ["const:4febf4:8", "const:4:8"]]
+ 004febf4 ["CALL", null, ["callee:00c59150:8"]]
- 004fe8d4 bytes 2b661d94
+ 004febf4 bytes 57691d94
- 004fe8e4 ["INT_ADD", "register:40f0:8", ["const:4fe8e4:8", "const:4:8"]]
- 004fe8e4 ["CALL", null, ["callee:00c59010:8"]]
+ 004fec04 ["INT_ADD", "register:40f0:8", ["const:4fec04:8", "const:4:8"]]
+ 004fec04 ["CALL", null, ["callee:00c59010:8"]]
- 004fe8e4 bytes d7651d94
+ 004fec04 bytes 03691d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc891ef88c9cd4c8c3ccca33ad93f161"></a>

### [`004feb58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb58.md) → [`004fee78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fee78.md) _ZN5Botan18short_version_cstrEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004fee7c",
      "incomplete_value": false,
      "site": "004fee80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:a97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004feb5c",
      "incomplete_value": false,
      "site": "004feb60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "004fee7c",
      "DATA",
      [
        "storage",
        "002af9c0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fee7c",
      "DATA",
      [
        "storage",
        "002afa97",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb58.md#insn-004feb5c)
- 新版 [`004fee7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fee78.md#insn-004fee7c)

~~~diff
- 004feb5c ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 004feb5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feb5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feb5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fee7c ["COPY", "tmp:0:8", ["const:a97:8"]]
+ 004fee7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fee7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fee7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feb5c bytes 00002791
+ 004fee7c bytes 005c2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c5a7f58811c066afa1f74ded7fa80a2"></a>

### [`004feb64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb64.md) → [`004fee84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fee84.md) _ZN5Botan12version_cstrEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "004fee88",
      "incomplete_value": false,
      "site": "004fee8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004feb68",
      "incomplete_value": false,
      "site": "004feb6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bc000:8"
          ],
          [
            "leaf",
            "const:57a:8"
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
      "004fee88",
      "DATA",
      [
        "storage",
        "002bc57a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004fee88",
      "DATA",
      [
        "storage",
        "002bc658",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feb68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feb64.md#insn-004feb68)
- 新版 [`004fee88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fee84.md#insn-004fee88)

~~~diff
- 004feb68 ["COPY", "tmp:0:8", ["const:57a:8"]]
- 004feb68 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004feb68 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004feb68 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004fee88 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 004fee88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004fee88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004fee88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004feb68 bytes 00e81591
+ 004fee88 bytes 00601991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b49984372be30aa6670db88e35f3c91"></a>

### [`004fec1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md) → [`004fef3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fef3c.md) _ZN5Botan21runtime_version_checkEjjj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59040.md) [`00c59050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fef84",
      "incomplete_value": true,
      "site": "004fef94",
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
      "definition_site": "004fec64",
      "incomplete_value": true,
      "site": "004fec74",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004fef8c",
      "incomplete_value": true,
      "site": "004fef9c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004fec6c",
      "incomplete_value": true,
      "site": "004fec7c",
      "value": [
        "LOAD",
        "8",
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
                "const:8:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004fefa4",
      "incomplete_value": true,
      "site": "004fefa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "004fec84",
      "incomplete_value": true,
      "site": "004fec84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "004fef70",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004fef74",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004fef8c",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004fef70",
      "READ",
      [
        "storage",
        "00c9bd28",
        null,
        "pointer"
      ]
    ],
    [
      "004fef74",
      "READ",
      [
        "storage",
        "00c9bc58",
        null,
        "pointer"
      ]
    ],
    [
      "004fef8c",
      "READ",
      [
        "storage",
        "00c942a8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004fed04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fed04) · [`004fed40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fed40) · [`004fed50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md#insn-004fed50)
- 新版 [`004ff024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fef3c.md#insn-004ff024) · [`004ff060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fef3c.md#insn-004ff060) · [`004ff070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004fe/004fef3c.md#insn-004ff070)

~~~diff
- 004fed04 ["INT_ADD", "register:40f0:8", ["const:4fed04:8", "const:4:8"]]
- 004fed04 ["CALL", null, ["callee:00459830:8"]]
+ 004ff024 ["INT_ADD", "register:40f0:8", ["const:4ff024:8", "const:4:8"]]
+ 004ff024 ["CALL", null, ["callee:00459830:8"]]
- 004fed04 bytes 036afd97
+ 004ff024 bytes 036afd97
- 004fed40 ["INT_ADD", "register:40f0:8", ["const:4fed40:8", "const:4:8"]]
- 004fed40 ["CALL", null, ["callee:00459830:8"]]
+ 004ff060 ["INT_ADD", "register:40f0:8", ["const:4ff060:8", "const:4:8"]]
+ 004ff060 ["CALL", null, ["callee:00459830:8"]]
- 004fed40 bytes f469fd97
+ 004ff060 bytes f469fd97
- 004fed50 ["INT_ADD", "register:40f0:8", ["const:4fed50:8", "const:4:8"]]
- 004fed50 ["CALL", null, ["callee:00459830:8"]]
+ 004ff070 ["INT_ADD", "register:40f0:8", ["const:4ff070:8", "const:4:8"]]
+ 004ff070 ["CALL", null, ["callee:00459830:8"]]
- 004fed50 bytes f069fd97
+ 004ff070 bytes f069fd97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c1b7641350e9df4285d1491b9ca5059"></a>

### [`004feeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md) → [`004ff1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff1d0.md) _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59be0.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c59a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a20.md)
- 新版 呼出元 1件 [`00c5abb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abb0.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c5a9f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a9f0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ff21c",
      "incomplete_value": true,
      "site": "004ff244",
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
      "definition_site": "004feefc",
      "incomplete_value": true,
      "site": "004fef24",
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
      "004ff200",
      "READ",
      [
        "storage",
        "00c9b198",
        null,
        "pointer"
      ]
    ],
    [
      "004ff244",
      "DATA",
      [
        "storage",
        "00c67838",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ff2c4",
      "DATA",
      [
        "storage",
        "00495255",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ff200",
      "READ",
      [
        "storage",
        "00c9c168",
        null,
        "pointer"
      ]
    ],
    [
      "004ff244",
      "DATA",
      [
        "storage",
        "00c68808",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004feed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004feed4) · [`004feee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004feee0) · [`004fef4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004feeb0.md#insn-004fef4c)
- 新版 [`004ff1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff1d0.md#insn-004ff1f4) · [`004ff200`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff1d0.md#insn-004ff200) · [`004ff26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff1d0.md#insn-004ff26c)

~~~diff
- 004feed4 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 004ff1f4 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 004feed4 bytes e93c00b0
+ 004ff1f4 bytes e93c00b0
- 004feee0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:198:8"]]
- 004feee0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ff200 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:168:8"]]
+ 004ff200 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004feee0 bytes 29cd40f9
+ 004ff200 bytes 29b540f9
- 004fef4c ["INT_ADD", "register:40f0:8", ["const:4fef4c:8", "const:4:8"]]
- 004fef4c ["CALL", null, ["callee:00c5a9f0:8"]]
+ 004ff26c ["INT_ADD", "register:40f0:8", ["const:4ff26c:8", "const:4:8"]]
+ 004ff26c ["CALL", null, ["callee:00c5a9f0:8"]]
- 004fef4c bytes b56a1d94
+ 004ff26c bytes e16d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94f6bbcdca2e2516918fb38cc0b1c784"></a>

### [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) → [`004ffe0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md) FUN_004ffe0c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`004ff878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff878.md) · 呼出先 13件 [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`005480d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005480d8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004ffb98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffb98.md) · 呼出先 13件 [`0050891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md) [`00515104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`005483f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005483f8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.15% / 新版 94.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffe90",
      "incomplete_value": true,
      "site": "004ffe90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ffb70",
      "incomplete_value": true,
      "site": "004ffb70",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffe90",
      "incomplete_value": true,
      "site": "004ffe90",
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
      "definition_site": "004ffb70",
      "incomplete_value": true,
      "site": "004ffb70",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ffe84",
      "incomplete_value": true,
      "site": "004ffe98",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004ffb64",
      "incomplete_value": true,
      "site": "004ffb78",
      "value": [
        "LOAD",
        "8",
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
      "004ffe68",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe80",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe84",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "004ffe68",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "004ffe80",
      "READ",
      [
        "storage",
        "00c94188",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ffe84",
      "READ",
      [
        "storage",
        "00c941c8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ffd78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffd78) · [`004ffb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffb30) · [`004ffb3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md#insn-004ffb3c)
- 新版 [`00500098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md#insn-00500098) · [`004ffe50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md#insn-004ffe50) · [`004ffe5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md#insn-004ffe5c)

~~~diff
- 004ffd78 ["INT_ADD", "register:40f0:8", ["const:4ffd78:8", "const:4:8"]]
- 004ffd78 ["CALL", null, ["callee:00c59260:8"]]
+ 00500098 ["INT_ADD", "register:40f0:8", ["const:500098:8", "const:4:8"]]
+ 00500098 ["CALL", null, ["callee:00c59260:8"]]
- 004ffd78 bytes 46611d94
+ 00500098 bytes 72641d94
- 004ffb30 ["INT_ADD", "register:40f0:8", ["const:4ffb30:8", "const:4:8"]]
- 004ffb30 ["CALL", null, ["callee:005483f8:8"]]
+ 004ffe50 ["INT_ADD", "register:40f0:8", ["const:4ffe50:8", "const:4:8"]]
+ 004ffe50 ["CALL", null, ["callee:005483f8:8"]]
- 004ffb30 bytes 6a210194
+ 004ffe50 bytes 6a210194
- 004ffb3c ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 004ffe5c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 004ffb3c bytes c83c00f0
+ 004ffe5c bytes e83c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-290bcfd5bb15e7c6ec8eb09af247850d"></a>

### [`004ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md) → [`00500180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500180.md) _ZN5Botan15AlternativeName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 28件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`004ff3bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ff3bc.md) [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md)
- 新版 呼出元 0件  · 呼出先 28件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`004ff6dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ff6dc.md) [`005072f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.29% / 新版 96.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 7件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005001f0",
      "incomplete_value": true,
      "site": "005001f4",
      "value": [
        "LOAD",
        "8",
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
    "old": {
      "definition_site": "004ffed0",
      "incomplete_value": true,
      "site": "004ffed4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00500200",
      "incomplete_value": true,
      "site": "00500200",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ffee0",
      "incomplete_value": true,
      "site": "004ffee0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00500200",
      "incomplete_value": true,
      "site": "00500200",
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
      "definition_site": "004ffee0",
      "incomplete_value": true,
      "site": "004ffee0",
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
      "005001d4",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "005001ec",
      "READ",
      [
        "storage",
        "00c931b8",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "005001f0",
      "READ",
      [
        "storage",
        "00c931f8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "005001d4",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "005001ec",
      "READ",
      [
        "storage",
        "00c94188",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "005001f0",
      "READ",
      [
        "storage",
        "00c941c8",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005002b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-005002b4) · [`00500314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-00500314) · [`00500700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md#insn-00500700)
- 新版 [`005005d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500180.md#insn-005005d4) · [`00500634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500180.md#insn-00500634) · [`00500a20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500180.md#insn-00500a20)

~~~diff
- 005002b4 ["INT_ADD", "register:40f0:8", ["const:5002b4:8", "const:4:8"]]
- 005002b4 ["CALL", null, ["callee:00c59260:8"]]
+ 005005d4 ["INT_ADD", "register:40f0:8", ["const:5005d4:8", "const:4:8"]]
+ 005005d4 ["CALL", null, ["callee:00c59260:8"]]
- 005002b4 bytes f75f1d94
+ 005005d4 bytes 23631d94
- 00500314 ["COPY", "register:0:8", ["register:4048:8"]]
- 00500314 ["INT_ADD", "register:40f0:8", ["const:500314:8", "const:4:8"]]
- 00500314 ["CALLIND", null, ["register:0:8"]]
+ 00500634 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00500634 ["INT_ADD", "register:40f0:8", ["const:500634:8", "const:4:8"]]
+ 00500634 ["CALLIND", null, ["register:0:8"]]
- 00500314 bytes 20013fd6
+ 00500634 bytes 20013fd6
- 00500700 ["COPY", "register:0:8", ["register:4048:8"]]
- 00500700 ["INT_ADD", "register:40f0:8", ["const:500700:8", "const:4:8"]]
- 00500700 ["CALLIND", null, ["register:0:8"]]
+ 00500a20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00500a20 ["INT_ADD", "register:40f0:8", ["const:500a20:8", "const:4:8"]]
+ 00500a20 ["CALLIND", null, ["register:0:8"]]
- 00500700 bytes 20013fd6
+ 00500a20 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1318dac052c63b3166d1d42ece22e61d"></a>

### [`00500b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md) → [`00500e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500e5c.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_7X509_DNE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a70.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5aa40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa40.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050119c",
      "incomplete_value": false,
      "site": "005011a4",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500e7c",
      "incomplete_value": false,
      "site": "00500e84",
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
            "const:a8b:8"
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
      "005010c8",
      "PARAM",
      [
        "storage",
        "002b8f90",
        null,
        null
      ]
    ],
    [
      "0050111c",
      "PARAM",
      [
        "storage",
        "002a66f6",
        null,
        null
      ]
    ],
    [
      "0050114c",
      "PARAM",
      [
        "storage",
        "002b5ecd",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "005010c8",
      "PARAM",
      [
        "storage",
        "002b905f",
        null,
        null
      ]
    ],
    [
      "0050111c",
      "PARAM",
      [
        "storage",
        "002a684e",
        null,
        null
      ]
    ],
    [
      "0050114c",
      "PARAM",
      [
        "storage",
        "002b5f9c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500e84) · [`00500b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500b7c) · [`00500b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500b3c.md#insn-00500b94)
- 新版 [`005011a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500e5c.md#insn-005011a4) · [`00500e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500e5c.md#insn-00500e9c) · [`00500eb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500e5c.md#insn-00500eb4)

~~~diff
- 00500e84 ["INT_ADD", "register:40f0:8", ["const:500e84:8", "const:4:8"]]
- 00500e84 ["CALL", null, ["callee:00459830:8"]]
+ 005011a4 ["INT_ADD", "register:40f0:8", ["const:5011a4:8", "const:4:8"]]
+ 005011a4 ["CALL", null, ["callee:00459830:8"]]
- 00500e84 bytes a361fd97
+ 005011a4 bytes a361fd97
- 00500b7c ["INT_ADD", "register:40f0:8", ["const:500b7c:8", "const:4:8"]]
- 00500b7c ["CALL", null, ["callee:00c5aa50:8"]]
+ 00500e9c ["INT_ADD", "register:40f0:8", ["const:500e9c:8", "const:4:8"]]
+ 00500e9c ["CALL", null, ["callee:00c5aa50:8"]]
- 00500b7c bytes c1631d94
+ 00500e9c bytes ed661d94
- 00500b94 ["COPY", "register:40a0:8", ["const:2b8000:8"]]
+ 00500eb4 ["COPY", "register:40a0:8", ["const:2b9000:8"]]
- 00500b94 bytes d4edff90
+ 00500eb4 bytes d4edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94126912db32827341e1dcd0dd7a0536"></a>

### [`00500f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md) → [`005012a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005012a0.md) _ZN5Botan9to_stringENS_23Certificate_Status_CodeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a90.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00c5aa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa60.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 83.46% / 新版 83.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 45件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "005012f4",
      "incomplete_value": false,
      "site": "005012f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00500fd4",
      "incomplete_value": false,
      "site": "00500fd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2af000:8"
          ],
          [
            "leaf",
            "const:9d1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00501330",
      "incomplete_value": false,
      "site": "00501334",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e67:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00501010",
      "incomplete_value": false,
      "site": "00501014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:d89:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00501364",
      "incomplete_value": false,
      "site": "00501368",
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
            "const:7fe:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00501044",
      "incomplete_value": false,
      "site": "00501048",
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
            "const:6a6:8"
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
      "005012f4",
      "DATA",
      [
        "storage",
        "002af9d1",
        null,
        "string"
      ]
    ],
    [
      "00501330",
      "DATA",
      [
        "storage",
        "002bed89",
        null,
        "string"
      ]
    ],
    [
      "00501364",
      "DATA",
      [
        "storage",
        "002a66a6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005012f4",
      "DATA",
      [
        "storage",
        "002afaa8",
        null,
        "string"
      ]
    ],
    [
      "00501330",
      "DATA",
      [
        "storage",
        "002bee67",
        null,
        "string"
      ]
    ],
    [
      "00501364",
      "DATA",
      [
        "storage",
        "002a67fe",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00500fd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md#insn-00500fd4) · [`005012f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md#insn-005012f8) · [`00501368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00500/00500f80.md#insn-00501368)
- 新版 [`005012f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005012a0.md#insn-005012f4) · [`00501618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005012a0.md#insn-00501618) · [`00501688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005012a0.md#insn-00501688)

~~~diff
- 00500fd4 ["COPY", "tmp:0:8", ["const:9d1:8"]]
- 00500fd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00500fd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00500fd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 005012f4 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 005012f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 005012f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 005012f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00500fd4 bytes 00442791
+ 005012f4 bytes 00a02a91
- 005012f8 ["COPY", "register:4000:8", ["const:2b8000:8"]]
+ 00501618 ["COPY", "register:4000:8", ["const:2b9000:8"]]
- 005012f8 bytes a0edfff0
+ 00501618 bytes c0edff90
- 00501368 ["COPY", "tmp:0:8", ["const:440:8"]]
- 00501368 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00501368 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00501368 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00501688 ["COPY", "tmp:0:8", ["const:50d:8"]]
+ 00501688 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00501688 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00501688 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00501368 bytes 00001191
+ 00501688 bytes 00341491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9a265fe24fd2b97a057a9acff424680"></a>

### [`005013c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md) → [`005016e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005016e8.md) _ZN5Botan27Certificate_Store_In_Memory15add_certificateERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59aa0.md) · 呼出先 10件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`005483e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483e8.md) [`005483f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483f8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5aa70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa70.md) · 呼出先 10件 [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) [`00548708`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548708.md) [`00548718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548718.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

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
      "definition_site": "005017c4",
      "incomplete_value": true,
      "site": "005017c8",
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
      "definition_site": "005014a4",
      "incomplete_value": true,
      "site": "005014a8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005017e0",
      "incomplete_value": true,
      "site": "005017e8",
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
      "definition_site": "005014c0",
      "incomplete_value": true,
      "site": "005014c8",
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
      "005017bc",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "005017c8",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005017dc",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005017bc",
      "READ",
      [
        "storage",
        "00c9c178",
        null,
        "pointer"
      ]
    ],
    [
      "005017c8",
      "DATA",
      [
        "storage",
        "00c6b7e0",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005017dc",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050144c) · [`0050145c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050145c) · [`0050147c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/005013c8.md#insn-0050147c)
- 新版 [`0050176c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005016e8.md#insn-0050176c) · [`0050177c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005016e8.md#insn-0050177c) · [`0050179c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/005016e8.md#insn-0050179c)

~~~diff
- 0050144c ["INT_ADD", "register:40f0:8", ["const:50144c:8", "const:4:8"]]
- 0050144c ["CALL", null, ["callee:00c590f0:8"]]
+ 0050176c ["INT_ADD", "register:40f0:8", ["const:50176c:8", "const:4:8"]]
+ 0050176c ["CALL", null, ["callee:00c590f0:8"]]
- 0050144c bytes 355b1d94
+ 0050176c bytes 615e1d94
- 0050145c ["INT_ADD", "register:40f0:8", ["const:50145c:8", "const:4:8"]]
- 0050145c ["CALL", null, ["callee:00c59740:8"]]
+ 0050177c ["INT_ADD", "register:40f0:8", ["const:50177c:8", "const:4:8"]]
+ 0050177c ["CALL", null, ["callee:00c59740:8"]]
- 0050145c bytes c55c1d94
+ 0050177c bytes f15f1d94
- 0050147c ["INT_ADD", "register:40f0:8", ["const:50147c:8", "const:4:8"]]
- 0050147c ["CALL", null, ["callee:00c590f0:8"]]
+ 0050179c ["INT_ADD", "register:40f0:8", ["const:50179c:8", "const:4:8"]]
+ 0050179c ["CALL", null, ["callee:00c590f0:8"]]
- 0050147c bytes 295b1d94
+ 0050179c bytes 555e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e352c6beda13433337d7eec9637e375"></a>

### [`00501e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md) → [`005021b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005021b0.md) _ZNK5Botan27Certificate_Store_In_Memory24find_cert_by_pubkey_sha1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005023c8",
      "incomplete_value": false,
      "site": "005023d0",
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
            "const:ba4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005020a8",
      "incomplete_value": false,
      "site": "005020b0",
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
            "const:b5a:8"
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
      "definition_site": "00502400",
      "incomplete_value": true,
      "site": "0050240c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005020e0",
      "incomplete_value": true,
      "site": "005020ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005023fc",
      "incomplete_value": false,
      "site": "0050240c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "005020dc",
      "incomplete_value": false,
      "site": "005020ec",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005023c8",
      "PARAM",
      [
        "storage",
        "002b2b5a",
        null,
        "string"
      ]
    ],
    [
      "005023fc",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00502400",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005023c8",
      "PARAM",
      [
        "storage",
        "002b2ba4",
        null,
        "string"
      ]
    ],
    [
      "005023fc",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00502400",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005020b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-005020b0) · [`005020ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-005020ec) · [`00501f04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501e90.md#insn-00501f04)
- 新版 [`005023d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005021b0.md#insn-005023d0) · [`0050240c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005021b0.md#insn-0050240c) · [`00502224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005021b0.md#insn-00502224)

~~~diff
- 005020b0 ["INT_ADD", "register:40f0:8", ["const:5020b0:8", "const:4:8"]]
- 005020b0 ["CALL", null, ["callee:0043e138:8"]]
+ 005023d0 ["INT_ADD", "register:40f0:8", ["const:5023d0:8", "const:4:8"]]
+ 005023d0 ["CALL", null, ["callee:0043e138:8"]]
- 005020b0 bytes 5aeffc97
+ 005023d0 bytes 5aeffc97
- 005020ec ["INT_ADD", "register:40f0:8", ["const:5020ec:8", "const:4:8"]]
- 005020ec ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050240c ["INT_ADD", "register:40f0:8", ["const:50240c:8", "const:4:8"]]
+ 0050240c ["CALL", null, ["callee:00c58fb0:8"]]
- 005020ec bytes bd571d94
+ 0050240c bytes e95a1d94
- 00501f04 ["INT_ADD", "register:40f0:8", ["const:501f04:8", "const:4:8"]]
- 00501f04 ["CALL", null, ["callee:00c59e90:8"]]
+ 00502224 ["INT_ADD", "register:40f0:8", ["const:502224:8", "const:4:8"]]
+ 00502224 ["CALL", null, ["callee:00c59e90:8"]]
- 00501f04 bytes ef5b1d94
+ 00502224 bytes 1b5f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94d8b8177ed16003343f461658b7216"></a>

### [`005021a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md) → [`005024c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024c8.md) _ZNK5Botan27Certificate_Store_In_Memory34find_cert_by_raw_subject_dn_sha256ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005026e8",
      "incomplete_value": false,
      "site": "005026f0",
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
            "const:6dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005023c8",
      "incomplete_value": false,
      "site": "005023d0",
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
            "const:585:8"
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
      "definition_site": "00502720",
      "incomplete_value": true,
      "site": "0050272c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00502400",
      "incomplete_value": true,
      "site": "0050240c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050271c",
      "incomplete_value": false,
      "site": "0050272c",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "005023fc",
      "incomplete_value": false,
      "site": "0050240c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005026e8",
      "PARAM",
      [
        "storage",
        "002a5585",
        null,
        "string"
      ]
    ],
    [
      "0050271c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00502720",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005026e8",
      "PARAM",
      [
        "storage",
        "002a56dd",
        null,
        "string"
      ]
    ],
    [
      "0050271c",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00502720",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005023d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-005023d0) · [`0050240c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-0050240c) · [`00502224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005021a8.md#insn-00502224)
- 新版 [`005026f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024c8.md#insn-005026f0) · [`0050272c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024c8.md#insn-0050272c) · [`00502544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005024c8.md#insn-00502544)

~~~diff
- 005023d0 ["INT_ADD", "register:40f0:8", ["const:5023d0:8", "const:4:8"]]
- 005023d0 ["CALL", null, ["callee:0043e138:8"]]
+ 005026f0 ["INT_ADD", "register:40f0:8", ["const:5026f0:8", "const:4:8"]]
+ 005026f0 ["CALL", null, ["callee:0043e138:8"]]
- 005023d0 bytes 92eefc97
+ 005026f0 bytes 92eefc97
- 0050240c ["INT_ADD", "register:40f0:8", ["const:50240c:8", "const:4:8"]]
- 0050240c ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050272c ["INT_ADD", "register:40f0:8", ["const:50272c:8", "const:4:8"]]
+ 0050272c ["CALL", null, ["callee:00c58fb0:8"]]
- 0050240c bytes f5561d94
+ 0050272c bytes 215a1d94
- 00502224 ["INT_ADD", "register:40f0:8", ["const:502224:8", "const:4:8"]]
- 00502224 ["CALL", null, ["callee:00c59e90:8"]]
+ 00502544 ["INT_ADD", "register:40f0:8", ["const:502544:8", "const:4:8"]]
+ 00502544 ["CALL", null, ["callee:00c59e90:8"]]
- 00502224 bytes 275b1d94
+ 00502544 bytes 535e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3226434ee8178ae8b060d458e4575392"></a>

### [`005024c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md) → [`005027e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027e8.md) _ZN5Botan27Certificate_Store_In_Memory7add_crlERKNS_8X509_CRLE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00548b08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548b08.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) [`00548e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548e28.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

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
      "definition_site": "00502830",
      "incomplete_value": true,
      "site": "00502834",
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
      "definition_site": "00502510",
      "incomplete_value": true,
      "site": "00502514",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050284c",
      "incomplete_value": true,
      "site": "00502854",
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
      "definition_site": "0050252c",
      "incomplete_value": true,
      "site": "00502534",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502828",
      "READ",
      [
        "storage",
        "00c9b1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00502834",
      "DATA",
      [
        "storage",
        "00c6a860",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00502848",
      "READ",
      [
        "storage",
        "00c9b1c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502828",
      "READ",
      [
        "storage",
        "00c9c188",
        null,
        "pointer"
      ]
    ],
    [
      "00502834",
      "DATA",
      [
        "storage",
        "00c6b830",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "00502848",
      "READ",
      [
        "storage",
        "00c9c190",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005024f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-005024f8) · [`005024fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-005024fc) · [`00502508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/005024c8.md#insn-00502508)
- 新版 [`00502818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027e8.md#insn-00502818) · [`0050281c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027e8.md#insn-0050281c) · [`00502828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/005027e8.md#insn-00502828)

~~~diff
- 005024f8 ["INT_ADD", "register:40f0:8", ["const:5024f8:8", "const:4:8"]]
- 005024f8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00502818 ["INT_ADD", "register:40f0:8", ["const:502818:8", "const:4:8"]]
+ 00502818 ["CALL", null, ["callee:00c58f30:8"]]
- 005024f8 bytes 9a561d94
+ 00502818 bytes c6591d94
- 005024fc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0050281c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005024fc bytes c83c00b0
+ 0050281c bytes c83c00d0
- 00502508 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b8:8"]]
- 00502508 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:188:8"]]
+ 00502828 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502508 bytes 08dd40f9
+ 00502828 bytes 08c540f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affa3efd7a9ee4d84ffe31092033a225"></a>

### [`00502838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md) → [`00502b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md) FUN_00502b58

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00501780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00501/00501780.md) [`0050263c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/0050263c.md) [`00529374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529374.md) [`00529df8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00529/00529df8.md) [`00548734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548734.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0053aae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053aae4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 5件 [`00501aa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00501/00501aa0.md) [`0050295c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/0050295c.md) [`00529694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00529/00529694.md) [`0052a118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052a/0052a118.md) [`00548a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548a54.md) · 呼出先 4件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0053ae04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053a/0053ae04.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.16% / 新版 95.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502b98",
      "incomplete_value": true,
      "site": "00502ba0",
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
      "definition_site": "00502878",
      "incomplete_value": true,
      "site": "00502880",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502b88",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00502ba0",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00502b88",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "00502ba0",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050285c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-0050285c) · [`00502868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-00502868) · [`005028a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502838.md#insn-005028a8)
- 新版 [`00502b7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md#insn-00502b7c) · [`00502b88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md#insn-00502b88) · [`00502bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502b58.md#insn-00502bc8)

~~~diff
- 0050285c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00502b7c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0050285c bytes c83c00b0
+ 00502b7c bytes c83c00d0
- 00502868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
- 00502868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502b88 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
+ 00502b88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502868 bytes 08d140f9
+ 00502b88 bytes 08b940f9
- 005028a8 ["INT_ADD", "register:40f0:8", ["const:5028a8:8", "const:4:8"]]
- 005028a8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00502bc8 ["INT_ADD", "register:40f0:8", ["const:502bc8:8", "const:4:8"]]
+ 00502bc8 ["CALL", null, ["callee:00c58f30:8"]]
- 005028a8 bytes ae551d94
+ 00502bc8 bytes da581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c2a537b38c405463f3b942a1bd83c21"></a>

### [`00502b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md) → [`00502e9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e9c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59aa0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aa70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa70.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502ec0",
      "incomplete_value": true,
      "site": "00502ec4",
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
      "definition_site": "00502ba0",
      "incomplete_value": true,
      "site": "00502ba4",
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
      "00502eb8",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00502ec4",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00502eb8",
      "READ",
      [
        "storage",
        "00c9c198",
        null,
        "pointer"
      ]
    ],
    [
      "00502ec4",
      "DATA",
      [
        "storage",
        "00c68838",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md#insn-00502b90) · [`00502b98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md#insn-00502b98) · [`00502b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502b7c.md#insn-00502b9c)
- 新版 [`00502eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e9c.md#insn-00502eb0) · [`00502eb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502e9c.md#insn-00502eb8)

~~~diff
- 00502b90 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00502eb0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00502b90 bytes c83c00b0
+ 00502eb0 bytes c83c00d0
- 00502b98 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
- 00502b98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502eb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
+ 00502eb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502b98 bytes 08e540f9
+ 00502eb8 bytes 08cd40f9
- 00502b9c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00502b9c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3e05e2de6b4e8dea265376a8bb08b00"></a>

### [`00502c7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md) → [`00502f9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f9c.md) _ZN5Botan27Certificate_Store_In_MemoryC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`005483f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/005483f8.md) [`00548db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548db8.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00548718`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/00548718.md) [`005490d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005490d8.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00502fd4",
      "incomplete_value": true,
      "site": "00502fdc",
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
      "definition_site": "00502cb4",
      "incomplete_value": true,
      "site": "00502cbc",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00502fc8",
      "READ",
      [
        "storage",
        "00c9b1c8",
        null,
        "pointer"
      ]
    ],
    [
      "00502fdc",
      "DATA",
      [
        "storage",
        "00c67868",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00503024",
      "READ",
      [
        "storage",
        "00c9b1d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00502fc8",
      "READ",
      [
        "storage",
        "00c9c198",
        null,
        "pointer"
      ]
    ],
    [
      "00502fdc",
      "DATA",
      [
        "storage",
        "00c68838",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "00503024",
      "READ",
      [
        "storage",
        "00c9c1a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502c9c) · [`00502ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502ca8) · [`00502cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502c7c.md#insn-00502cf0)
- 新版 [`00502fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f9c.md#insn-00502fbc) · [`00502fc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f9c.md#insn-00502fc8) · [`00503010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00502/00502f9c.md#insn-00503010)

~~~diff
- 00502c9c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00502fbc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00502c9c bytes c83c00b0
+ 00502fbc bytes c83c00d0
- 00502ca8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
- 00502ca8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00502fc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:198:8"]]
+ 00502fc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00502ca8 bytes 08e540f9
+ 00502fc8 bytes 08cd40f9
- 00502cf0 ["INT_ADD", "register:40f0:8", ["const:502cf0:8", "const:4:8"]]
- 00502cf0 ["CALL", null, ["callee:00c5a8d0:8"]]
+ 00503010 ["INT_ADD", "register:40f0:8", ["const:503010:8", "const:4:8"]]
+ 00503010 ["CALL", null, ["callee:00c5a8d0:8"]]
- 00502cf0 bytes 045b1d94
+ 00503010 bytes 305e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24e305e52130e05d2ca41d541b7b8ac6"></a>

### [`00502f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md) → [`00503270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503270.md) _ZN5Botan9CRL_EntryC2ERKNS_16X509_CertificateENS_8CRL_CodeE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58650`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58650.md) [`00c59ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59ac0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`005491c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005491c8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59620`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59620.md) [`00c5aa90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005032a8",
      "incomplete_value": true,
      "site": "005032b0",
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
      "definition_site": "00502f88",
      "incomplete_value": true,
      "site": "00502f90",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005032dc",
      "incomplete_value": true,
      "site": "005032dc",
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
      "definition_site": "00502fbc",
      "incomplete_value": true,
      "site": "00502fbc",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503300",
      "incomplete_value": true,
      "site": "00503300",
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
      "definition_site": "00502fe0",
      "incomplete_value": true,
      "site": "00502fe0",
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
      "00503298",
      "READ",
      [
        "storage",
        "00c9b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "005032b0",
      "DATA",
      [
        "storage",
        "00c678b8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005032cc",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00503298",
      "READ",
      [
        "storage",
        "00c9c1a8",
        null,
        "pointer"
      ]
    ],
    [
      "005032b0",
      "DATA",
      [
        "storage",
        "00c68888",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005032cc",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00502f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00502f6c) · [`00502f78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00502f78) · [`00502fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00502/00502f50.md#insn-00502fa0)
- 新版 [`0050328c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503270.md#insn-0050328c) · [`00503298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503270.md#insn-00503298) · [`005032c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503270.md#insn-005032c0)

~~~diff
- 00502f6c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 0050328c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00502f6c bytes c93c00b0
+ 0050328c bytes c93c00b0
- 00502f78 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1d8:8"]]
- 00502f78 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00503298 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1a8:8"]]
+ 00503298 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00502f78 bytes 29ed40f9
+ 00503298 bytes 29d540f9
- 00502fa0 ["INT_ADD", "register:40f0:8", ["const:502fa0:8", "const:4:8"]]
- 00502fa0 ["CALL", null, ["callee:00c58f30:8"]]
+ 005032c0 ["INT_ADD", "register:40f0:8", ["const:5032c0:8", "const:4:8"]]
+ 005032c0 ["CALL", null, ["callee:00c58f30:8"]]
- 00502fa0 bytes f0531d94
+ 005032c0 bytes 1c571d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-782b175a019ac32ffa352e99f9f52648"></a>

### [`00503104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md) → [`00503424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503424.md) _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b50.md) · 呼出先 17件 [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053d768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d768.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md)
- 新版 呼出元 1件 [`00c5ab20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab20.md) · 呼出先 17件 [`00516f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0053da88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053da88.md) [`0054bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bca4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005035f8",
      "incomplete_value": true,
      "site": "005035f8",
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
      "definition_site": "005032d8",
      "incomplete_value": true,
      "site": "005032d8",
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
      "definition_site": "0050363c",
      "incomplete_value": true,
      "site": "00503640",
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
      "definition_site": "0050331c",
      "incomplete_value": true,
      "site": "00503320",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050354c",
      "incomplete_value": false,
      "site": "00503554",
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
            "const:d17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050322c",
      "incomplete_value": false,
      "site": "00503234",
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
            "const:c40:8"
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
      "0050354c",
      "PARAM",
      [
        "storage",
        "002b0c40",
        null,
        "string"
      ]
    ],
    [
      "00503598",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050359c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050354c",
      "PARAM",
      [
        "storage",
        "002b0d17",
        null,
        "string"
      ]
    ],
    [
      "00503598",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0050359c",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-00503234) · [`00503288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-00503288) · [`00503144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503104.md#insn-00503144)
- 新版 [`00503554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503424.md#insn-00503554) · [`005035a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503424.md#insn-005035a8) · [`00503464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503424.md#insn-00503464)

~~~diff
- 00503234 ["INT_ADD", "register:40f0:8", ["const:503234:8", "const:4:8"]]
- 00503234 ["CALL", null, ["callee:00c59010:8"]]
+ 00503554 ["INT_ADD", "register:40f0:8", ["const:503554:8", "const:4:8"]]
+ 00503554 ["CALL", null, ["callee:00c59010:8"]]
- 00503234 bytes 83531d94
+ 00503554 bytes af561d94
- 00503288 ["INT_ADD", "register:40f0:8", ["const:503288:8", "const:4:8"]]
- 00503288 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005035a8 ["INT_ADD", "register:40f0:8", ["const:5035a8:8", "const:4:8"]]
+ 005035a8 ["CALL", null, ["callee:00c58fb0:8"]]
- 00503288 bytes 56531d94
+ 005035a8 bytes 82561d94
- 00503144 ["COPY", "register:0:8", ["register:4048:8"]]
- 00503144 ["INT_ADD", "register:40f0:8", ["const:503144:8", "const:4:8"]]
- 00503144 ["CALLIND", null, ["register:0:8"]]
+ 00503464 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00503464 ["INT_ADD", "register:40f0:8", ["const:503464:8", "const:4:8"]]
+ 00503464 ["CALLIND", null, ["register:0:8"]]
- 00503144 bytes 20013fd6
+ 00503464 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb16d14eff73f643e9a9eb295d40cd56"></a>

### [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) → [`00503acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md) _ZN5Botan9CRL_Entry11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b80.md) · 呼出先 16件 [`004aeab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeab4.md) [`00503b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md) [`00517690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/00517690.md) [`00548e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548e14.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md)
- 新版 呼出元 1件 [`00c5ab50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab50.md) · 呼出先 16件 [`004aedd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aedd4.md) [`00503e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503e40.md) [`005179b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005179b0.md) [`00549134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549134.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.94% / 新版 94.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503b20",
      "incomplete_value": true,
      "site": "00503b20",
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
      "definition_site": "00503800",
      "incomplete_value": true,
      "site": "00503800",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503b44",
      "incomplete_value": true,
      "site": "00503b44",
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
      "definition_site": "00503824",
      "incomplete_value": true,
      "site": "00503824",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00503c2c",
      "incomplete_value": true,
      "site": "00503c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:670:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050390c",
      "incomplete_value": true,
      "site": "0050390c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:518:8"
              ]
            ]
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
      "00503b10",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00503b20",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503b30",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00503b10",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ],
    [
      "00503b20",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00503b30",
      "READ",
      [
        "storage",
        "00c9c1b0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503a00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-00503a00) · [`00503a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-00503a40) · [`005037e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md#insn-005037e8)
- 新版 [`00503d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md#insn-00503d20) · [`00503d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md#insn-00503d60) · [`00503b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md#insn-00503b08)

~~~diff
- 00503a00 ["COPY", "register:0:8", ["register:4048:8"]]
- 00503a00 ["INT_ADD", "register:40f0:8", ["const:503a00:8", "const:4:8"]]
- 00503a00 ["CALLIND", null, ["register:0:8"]]
+ 00503d20 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00503d20 ["INT_ADD", "register:40f0:8", ["const:503d20:8", "const:4:8"]]
+ 00503d20 ["CALLIND", null, ["register:0:8"]]
- 00503a00 bytes 20013fd6
+ 00503d20 bytes 20013fd6
- 00503a40 ["COPY", "register:0:8", ["register:4048:8"]]
- 00503a40 ["INT_ADD", "register:40f0:8", ["const:503a40:8", "const:4:8"]]
- 00503a40 ["CALLIND", null, ["register:0:8"]]
+ 00503d60 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00503d60 ["INT_ADD", "register:40f0:8", ["const:503d60:8", "const:4:8"]]
+ 00503d60 ["CALLIND", null, ["register:0:8"]]
- 00503a40 bytes 20013fd6
+ 00503d60 bytes 20013fd6
- 005037e8 ["INT_ADD", "register:40f0:8", ["const:5037e8:8", "const:4:8"]]
- 005037e8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00503b08 ["INT_ADD", "register:40f0:8", ["const:503b08:8", "const:4:8"]]
+ 00503b08 ["CALL", null, ["callee:00c58f30:8"]]
- 005037e8 bytes de511d94
+ 00503b08 bytes 0a551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86773e77e0dbe25b7475d58415135d50"></a>

### [`00503b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md) → [`00503e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503e40.md) FUN_00503e40

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005037ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/005037ac.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00503acc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503acc.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00503e7c",
      "incomplete_value": true,
      "site": "00503e7c",
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
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503b5c",
      "incomplete_value": true,
      "site": "00503b5c",
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
                "const:0:8"
              ]
            ]
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
      "definition_site": "00503eb8",
      "incomplete_value": false,
      "site": "00503ec0",
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
            "const:38e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503b98",
      "incomplete_value": false,
      "site": "00503ba0",
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
            "const:2c3:8"
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
      "definition_site": "00503ef4",
      "incomplete_value": true,
      "site": "00503f00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503bd4",
      "incomplete_value": true,
      "site": "00503be0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
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
      "00503e6c",
      "READ",
      [
        "storage",
        "00c9b1e8",
        null,
        "pointer"
      ]
    ],
    [
      "00503eb8",
      "PARAM",
      [
        "storage",
        "002a42c3",
        null,
        "string"
      ]
    ],
    [
      "00503ef0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00503e6c",
      "READ",
      [
        "storage",
        "00c9c1b8",
        null,
        "pointer"
      ]
    ],
    [
      "00503eb8",
      "PARAM",
      [
        "storage",
        "002a438e",
        null,
        "string"
      ]
    ],
    [
      "00503ef0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503ba0) · [`00503be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503be0) · [`00503b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503b20.md#insn-00503b40)
- 新版 [`00503ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503e40.md#insn-00503ec0) · [`00503f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503e40.md#insn-00503f00) · [`00503e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503e40.md#insn-00503e60)

~~~diff
- 00503ba0 ["INT_ADD", "register:40f0:8", ["const:503ba0:8", "const:4:8"]]
- 00503ba0 ["CALL", null, ["callee:0043e138:8"]]
+ 00503ec0 ["INT_ADD", "register:40f0:8", ["const:503ec0:8", "const:4:8"]]
+ 00503ec0 ["CALL", null, ["callee:0043e138:8"]]
- 00503ba0 bytes 9ee8fc97
+ 00503ec0 bytes 9ee8fc97
- 00503be0 ["INT_ADD", "register:40f0:8", ["const:503be0:8", "const:4:8"]]
- 00503be0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00503f00 ["INT_ADD", "register:40f0:8", ["const:503f00:8", "const:4:8"]]
+ 00503f00 ["CALL", null, ["callee:00c58fb0:8"]]
- 00503be0 bytes 00511d94
+ 00503f00 bytes 2c541d94
- 00503b40 ["INT_ADD", "register:40f0:8", ["const:503b40:8", "const:4:8"]]
- 00503b40 ["CALL", null, ["callee:00c5ab60:8"]]
+ 00503e60 ["INT_ADD", "register:40f0:8", ["const:503e60:8", "const:4:8"]]
+ 00503e60 ["CALL", null, ["callee:00c5ab60:8"]]
- 00503b40 bytes 14581d94
+ 00503e60 bytes 405b1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9df938da061eb8de712f30d0720debe0"></a>

### [`00503cdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md) → [`00503ffc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ffc.md) _ZNK5Botan9CRL_Entry4dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b70.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5ab40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab40.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050405c",
      "incomplete_value": false,
      "site": "00504064",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503d3c",
      "incomplete_value": false,
      "site": "00503d44",
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
            "const:180:8"
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
      "definition_site": "00504098",
      "incomplete_value": true,
      "site": "005040a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00503d78",
      "incomplete_value": true,
      "site": "00503d84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00504094",
      "incomplete_value": false,
      "site": "005040a4",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00503d74",
      "incomplete_value": false,
      "site": "00503d84",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0050405c",
      "PARAM",
      [
        "storage",
        "002a1180",
        null,
        "string"
      ]
    ],
    [
      "00504094",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504098",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050405c",
      "PARAM",
      [
        "storage",
        "002a11c0",
        null,
        "string"
      ]
    ],
    [
      "00504094",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00504098",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00503d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d44) · [`00503d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d84) · [`00503d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503cdc.md#insn-00503d30)
- 新版 [`00504064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ffc.md#insn-00504064) · [`005040a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ffc.md#insn-005040a4) · [`00504050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503ffc.md#insn-00504050)

~~~diff
- 00503d44 ["INT_ADD", "register:40f0:8", ["const:503d44:8", "const:4:8"]]
- 00503d44 ["CALL", null, ["callee:0043e138:8"]]
+ 00504064 ["INT_ADD", "register:40f0:8", ["const:504064:8", "const:4:8"]]
+ 00504064 ["CALL", null, ["callee:0043e138:8"]]
- 00503d44 bytes 35e8fc97
+ 00504064 bytes 35e8fc97
- 00503d84 ["INT_ADD", "register:40f0:8", ["const:503d84:8", "const:4:8"]]
- 00503d84 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005040a4 ["INT_ADD", "register:40f0:8", ["const:5040a4:8", "const:4:8"]]
+ 005040a4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00503d84 bytes 97501d94
+ 005040a4 bytes c3531d94
- 00503d30 ["INT_ADD", "register:40f0:8", ["const:503d30:8", "const:4:8"]]
- 00503d30 ["CALL", null, ["callee:00c58f90:8"]]
+ 00504050 ["INT_ADD", "register:40f0:8", ["const:504050:8", "const:4:8"]]
+ 00504050 ["CALL", null, ["callee:00c58f90:8"]]
- 00503d30 bytes a4501d94
+ 00504050 bytes d0531d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac4f7b1397bc728e3dd886f01a368ef9"></a>

### [`005042f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md) → [`00504618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504618.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504718",
      "incomplete_value": false,
      "site": "00504724",
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
            "const:2bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005043f8",
      "incomplete_value": false,
      "site": "00504404",
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
            "const:1f0:8"
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
      "definition_site": "00504754",
      "incomplete_value": true,
      "site": "00504760",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504434",
      "incomplete_value": true,
      "site": "00504440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00504750",
      "incomplete_value": false,
      "site": "00504760",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00504430",
      "incomplete_value": false,
      "site": "00504440",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504718",
      "PARAM",
      [
        "storage",
        "002a41f0",
        null,
        "string"
      ]
    ],
    [
      "00504750",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504754",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504718",
      "PARAM",
      [
        "storage",
        "002a42bb",
        null,
        "string"
      ]
    ],
    [
      "00504750",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00504754",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504404) · [`00504440`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504440) · [`00504464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005042f8.md#insn-00504464)
- 新版 [`00504724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504618.md#insn-00504724) · [`00504760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504618.md#insn-00504760) · [`00504784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504618.md#insn-00504784)

~~~diff
- 00504404 ["INT_ADD", "register:40f0:8", ["const:504404:8", "const:4:8"]]
- 00504404 ["CALL", null, ["callee:00c59150:8"]]
+ 00504724 ["INT_ADD", "register:40f0:8", ["const:504724:8", "const:4:8"]]
+ 00504724 ["CALL", null, ["callee:00c59150:8"]]
- 00504404 bytes 5f4f1d94
+ 00504724 bytes 8b521d94
- 00504440 ["INT_ADD", "register:40f0:8", ["const:504440:8", "const:4:8"]]
- 00504440 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00504760 ["INT_ADD", "register:40f0:8", ["const:504760:8", "const:4:8"]]
+ 00504760 ["CALL", null, ["callee:00c58fb0:8"]]
- 00504440 bytes e84e1d94
+ 00504760 bytes 14521d94
- 00504464 ["INT_ADD", "register:40f0:8", ["const:504464:8", "const:4:8"]]
- 00504464 ["CALL", null, ["callee:00c59150:8"]]
+ 00504784 ["INT_ADD", "register:40f0:8", ["const:504784:8", "const:4:8"]]
+ 00504784 ["CALL", null, ["callee:00c59150:8"]]
- 00504464 bytes 474f1d94
+ 00504784 bytes 73521d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbbf07698f369d49b3df4e4cc6c9a5e5"></a>

### [`00504508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md) → [`00504828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504828.md) _ZNK5Botan10Data_Store4get1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504938",
      "incomplete_value": false,
      "site": "00504944",
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
            "const:9ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504618",
      "incomplete_value": false,
      "site": "00504624",
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
            "const:853:8"
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
      "definition_site": "00504974",
      "incomplete_value": true,
      "site": "00504980",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504654",
      "incomplete_value": true,
      "site": "00504660",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00504970",
      "incomplete_value": false,
      "site": "00504980",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00504650",
      "incomplete_value": false,
      "site": "00504660",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504938",
      "PARAM",
      [
        "storage",
        "002a7853",
        null,
        "string"
      ]
    ],
    [
      "00504970",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504974",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504938",
      "PARAM",
      [
        "storage",
        "002a79ab",
        null,
        "string"
      ]
    ],
    [
      "00504970",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00504974",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504624) · [`00504660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504660) · [`00504538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504508.md#insn-00504538)
- 新版 [`00504944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504828.md#insn-00504944) · [`00504980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504828.md#insn-00504980) · [`00504858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504828.md#insn-00504858)

~~~diff
- 00504624 ["INT_ADD", "register:40f0:8", ["const:504624:8", "const:4:8"]]
- 00504624 ["CALL", null, ["callee:00c59150:8"]]
+ 00504944 ["INT_ADD", "register:40f0:8", ["const:504944:8", "const:4:8"]]
+ 00504944 ["CALL", null, ["callee:00c59150:8"]]
- 00504624 bytes d74e1d94
+ 00504944 bytes 03521d94
- 00504660 ["INT_ADD", "register:40f0:8", ["const:504660:8", "const:4:8"]]
- 00504660 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00504980 ["INT_ADD", "register:40f0:8", ["const:504980:8", "const:4:8"]]
+ 00504980 ["CALL", null, ["callee:00c58fb0:8"]]
- 00504660 bytes 604e1d94
+ 00504980 bytes 8c511d94
- 00504538 ["INT_ADD", "register:40f0:8", ["const:504538:8", "const:4:8"]]
- 00504538 ["CALL", null, ["callee:00c5ab80:8"]]
+ 00504858 ["INT_ADD", "register:40f0:8", ["const:504858:8", "const:4:8"]]
+ 00504858 ["CALL", null, ["callee:00c5ab80:8"]]
- 00504538 bytes 9e551d94
+ 00504858 bytes ca581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb7ee73ae7cdefc58ca0efda44cb1a4"></a>

### [`005046c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md) → [`005049e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005049e0.md) _ZNK5Botan10Data_Store11get1_memvecERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.70% / 新版 97.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504aec",
      "incomplete_value": false,
      "site": "00504af8",
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
            "const:ebf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005047cc",
      "incomplete_value": false,
      "site": "005047d8",
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
            "const:de1:8"
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
      "definition_site": "00504b28",
      "incomplete_value": true,
      "site": "00504b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504808",
      "incomplete_value": true,
      "site": "00504814",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00504b24",
      "incomplete_value": false,
      "site": "00504b34",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00504804",
      "incomplete_value": false,
      "site": "00504814",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504aec",
      "PARAM",
      [
        "storage",
        "002bfde1",
        null,
        "string"
      ]
    ],
    [
      "00504b24",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504b28",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504aec",
      "PARAM",
      [
        "storage",
        "002bfebf",
        null,
        "string"
      ]
    ],
    [
      "00504b24",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00504b28",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005047d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-005047d8) · [`00504814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-00504814) · [`005046ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/005046c0.md#insn-005046ec)
- 新版 [`00504af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005049e0.md#insn-00504af8) · [`00504b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005049e0.md#insn-00504b34) · [`00504a0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/005049e0.md#insn-00504a0c)

~~~diff
- 005047d8 ["INT_ADD", "register:40f0:8", ["const:5047d8:8", "const:4:8"]]
- 005047d8 ["CALL", null, ["callee:00c59150:8"]]
+ 00504af8 ["INT_ADD", "register:40f0:8", ["const:504af8:8", "const:4:8"]]
+ 00504af8 ["CALL", null, ["callee:00c59150:8"]]
- 005047d8 bytes 6a4e1d94
+ 00504af8 bytes 96511d94
- 00504814 ["INT_ADD", "register:40f0:8", ["const:504814:8", "const:4:8"]]
- 00504814 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00504b34 ["INT_ADD", "register:40f0:8", ["const:504b34:8", "const:4:8"]]
+ 00504b34 ["CALL", null, ["callee:00c58fb0:8"]]
- 00504814 bytes f34d1d94
+ 00504b34 bytes 1f511d94
- 005046ec ["INT_ADD", "register:40f0:8", ["const:5046ec:8", "const:4:8"]]
- 005046ec ["CALL", null, ["callee:00c5ab80:8"]]
+ 00504a0c ["INT_ADD", "register:40f0:8", ["const:504a0c:8", "const:4:8"]]
+ 00504a0c ["CALL", null, ["callee:00c5ab80:8"]]
- 005046ec bytes 31551d94
+ 00504a0c bytes 5d581d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70742927058a576ecadcd7a5193f3448"></a>

### [`00504874`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md) → [`00504b94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504b94.md) _ZNK5Botan10Data_Store11get1_uint32ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEj

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00504c7c",
      "incomplete_value": false,
      "site": "00504c88",
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
            "const:72a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050495c",
      "incomplete_value": false,
      "site": "00504968",
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
            "const:5d2:8"
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
      "definition_site": "00504cb8",
      "incomplete_value": true,
      "site": "00504cc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504998",
      "incomplete_value": true,
      "site": "005049a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00504cb4",
      "incomplete_value": false,
      "site": "00504cc4",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00504994",
      "incomplete_value": false,
      "site": "005049a4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00504c7c",
      "PARAM",
      [
        "storage",
        "002a55d2",
        null,
        "string"
      ]
    ],
    [
      "00504cb4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00504cb8",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00504c7c",
      "PARAM",
      [
        "storage",
        "002a572a",
        null,
        "string"
      ]
    ],
    [
      "00504cb4",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00504cb8",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-00504968) · [`005049a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-005049a4) · [`005048a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504874.md#insn-005048a0)
- 新版 [`00504c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504b94.md#insn-00504c88) · [`00504cc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504b94.md#insn-00504cc4) · [`00504bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00504/00504b94.md#insn-00504bc0)

~~~diff
- 00504968 ["INT_ADD", "register:40f0:8", ["const:504968:8", "const:4:8"]]
- 00504968 ["CALL", null, ["callee:00c59150:8"]]
+ 00504c88 ["INT_ADD", "register:40f0:8", ["const:504c88:8", "const:4:8"]]
+ 00504c88 ["CALL", null, ["callee:00c59150:8"]]
- 00504968 bytes 064e1d94
+ 00504c88 bytes 32511d94
- 005049a4 ["INT_ADD", "register:40f0:8", ["const:5049a4:8", "const:4:8"]]
- 005049a4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00504cc4 ["INT_ADD", "register:40f0:8", ["const:504cc4:8", "const:4:8"]]
+ 00504cc4 ["CALL", null, ["callee:00c58fb0:8"]]
- 005049a4 bytes 8f4d1d94
+ 00504cc4 bytes bb501d94
- 005048a0 ["INT_ADD", "register:40f0:8", ["const:5048a0:8", "const:4:8"]]
- 005048a0 ["CALL", null, ["callee:00c5ab80:8"]]
+ 00504bc0 ["INT_ADD", "register:40f0:8", ["const:504bc0:8", "const:4:8"]]
+ 00504bc0 ["CALL", null, ["callee:00c5ab80:8"]]
- 005048a0 bytes c4541d94
+ 00504bc0 bytes f0571d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a925a0aab97fb116f05c66e6f33bf41"></a>

### [`00504e50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md) → [`00505170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505170.md) _ZN5Botan9create_dnERKNS_10Data_StoreE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0054928c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/0054928c.md) [`00549290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549290.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`005495ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005495ac.md) [`005495b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005495b0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00505190",
      "incomplete_value": false,
      "site": "005051a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00504e70",
      "incomplete_value": false,
      "site": "00504e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "0050520c",
      "incomplete_value": true,
      "site": "0050520c",
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
      "definition_site": "00504eec",
      "incomplete_value": true,
      "site": "00504eec",
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
      "005051a0",
      "DATA",
      [
        "storage",
        "00c6a950",
        null,
        "undefined *"
      ]
    ],
    [
      "005051d8",
      "READ",
      [
        "storage",
        "00c6a970",
        null,
        "pointer"
      ]
    ],
    [
      "005051d8",
      "READ",
      [
        "storage",
        "00c6a978",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005051a0",
      "DATA",
      [
        "storage",
        "00c6b920",
        null,
        "undefined *"
      ]
    ],
    [
      "005051d8",
      "READ",
      [
        "storage",
        "00c6b940",
        null,
        "pointer"
      ]
    ],
    [
      "005051d8",
      "READ",
      [
        "storage",
        "00c6b948",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00504e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504e6c) · [`00504e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504e70) · [`00504e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00504/00504e50.md#insn-00504e90)
- 新版 [`0050518c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505170.md#insn-0050518c) · [`00505190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505170.md#insn-00505190) · [`005051b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505170.md#insn-005051b0)

~~~diff
- 00504e6c ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 0050518c ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 00504e6c bytes 293b00d0
+ 0050518c bytes 293b00d0
- 00504e70 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00504e70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00504e70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00504e70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505190 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 00505190 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505190 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505190 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00504e70 bytes 29412591
+ 00505190 bytes 29812491
- 00504e90 ["INT_ADD", "register:40f0:8", ["const:504e90:8", "const:4:8"]]
- 00504e90 ["CALL", null, ["callee:00c5ab70:8"]]
+ 005051b0 ["INT_ADD", "register:40f0:8", ["const:5051b0:8", "const:4:8"]]
+ 005051b0 ["CALL", null, ["callee:00c5ab70:8"]]
- 00504e90 bytes 44531d94
+ 005051b0 bytes 70561d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64ab88c0f9563ea206fc32c5f7909f7f"></a>

### [`005050c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md) → [`005053e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005053e0.md) _ZN5Botan15create_alt_nameERKNS_10Data_StoreE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00549394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549394.md) [`00549398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549398.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`005496b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005496b4.md) [`005496b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005496b8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.96% / 新版 97.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00505410",
      "incomplete_value": false,
      "site": "00505410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005050f0",
      "incomplete_value": false,
      "site": "005050f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "00505410",
      "DATA",
      [
        "storage",
        "00c6a9e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00505448",
      "READ",
      [
        "storage",
        "00c6aa00",
        null,
        "pointer"
      ]
    ],
    [
      "00505448",
      "READ",
      [
        "storage",
        "00c6aa08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00505410",
      "DATA",
      [
        "storage",
        "00c6b9b0",
        null,
        "undefined *"
      ]
    ],
    [
      "00505448",
      "READ",
      [
        "storage",
        "00c6b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00505448",
      "READ",
      [
        "storage",
        "00c6b9d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005050dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-005050dc) · [`005050e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-005050e0) · [`00505100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/005050c0.md#insn-00505100)
- 新版 [`005053fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005053e0.md#insn-005053fc) · [`00505400`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005053e0.md#insn-00505400) · [`00505420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/005053e0.md#insn-00505420)

~~~diff
- 005050dc ["COPY", "register:4048:8", ["const:c6a000:8"]]
+ 005053fc ["COPY", "register:4048:8", ["const:c6b000:8"]]
- 005050dc bytes 293b00b0
+ 005053fc bytes 293b00d0
- 005050e0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 005050e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005050e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005050e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505400 ["COPY", "tmp:0:8", ["const:9b0:8"]]
+ 00505400 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505400 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505400 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005050e0 bytes 29812791
+ 00505400 bytes 29c12691
- 00505100 ["INT_ADD", "register:40f0:8", ["const:505100:8", "const:4:8"]]
- 00505100 ["CALL", null, ["callee:00c5ab70:8"]]
+ 00505420 ["INT_ADD", "register:40f0:8", ["const:505420:8", "const:4:8"]]
+ 00505420 ["CALL", null, ["callee:00c5ab70:8"]]
- 00505100 bytes a8521d94
+ 00505420 bytes d4551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-302b17c2ef61f8aba105261b0df09c50"></a>

### [`00505344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md) → [`00505664`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505664.md) _ZN5Botan25key_constraints_to_stringENS_15Key_ConstraintsE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59bf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bf0.md) · 呼出先 9件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5abc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abc0.md) · 呼出先 9件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.80% / 新版 88.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 33件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005056d0",
      "incomplete_value": true,
      "site": "005056d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005053b0",
      "incomplete_value": true,
      "site": "005053b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:87e:8"
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
      "definition_site": "005056d4",
      "incomplete_value": true,
      "site": "005056d4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005053b4",
      "incomplete_value": true,
      "site": "005053b4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00505708",
      "incomplete_value": true,
      "site": "00505708",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005053e8",
      "incomplete_value": true,
      "site": "005053e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b9d:8"
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
      "005056c0",
      "READ",
      [
        "storage",
        "002a787e",
        null,
        "string"
      ]
    ],
    [
      "005056c4",
      "READ",
      [
        "storage",
        "002a7884",
        null,
        "string"
      ]
    ],
    [
      "005056f0",
      "READ",
      [
        "storage",
        "002b2b9d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005056c0",
      "READ",
      [
        "storage",
        "002a79d6",
        null,
        "string"
      ]
    ],
    [
      "005056c4",
      "READ",
      [
        "storage",
        "002a79dc",
        null,
        "string"
      ]
    ],
    [
      "005056f0",
      "READ",
      [
        "storage",
        "002b2be7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005053c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-005053c8) · [`005056d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-005056d0) · [`005057d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505344.md#insn-005057d0)
- 新版 [`005056e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505664.md#insn-005056e8) · [`005059f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505664.md#insn-005059f0) · [`00505af0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00505/00505664.md#insn-00505af0)

~~~diff
- 005053c8 ["COPY", "tmp:0:8", ["const:b9d:8"]]
- 005053c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005053c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005053c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005056e8 ["COPY", "tmp:0:8", ["const:be7:8"]]
+ 005056e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005056e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005056e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005053c8 bytes 29752e91
+ 005056e8 bytes 299d2f91
- 005056d0 ["COPY", "tmp:0:8", ["const:8f4:8"]]
- 005056d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005056d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005056d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005059f0 ["COPY", "tmp:0:8", ["const:944:8"]]
+ 005059f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005059f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005059f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005056d0 bytes 29d12391
+ 005059f0 bytes 29112591
- 005057d0 ["COPY", "tmp:0:8", ["const:954:8"]]
- 005057d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005057d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005057d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00505af0 ["COPY", "tmp:0:8", ["const:9a4:8"]]
+ 00505af0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00505af0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00505af0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005057d0 bytes 29512591
+ 00505af0 bytes 29912691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33bffaa78062ec7e3d5d2e3c3b211b0c"></a>

### [`00505f3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md) → [`0050625c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/0050625c.md) _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c00.md) · 呼出先 10件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5abd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abd0.md) · 呼出先 10件 [`004a6bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6bac.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

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
      "definition_site": "00506514",
      "incomplete_value": false,
      "site": "00506520",
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
            "const:149:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005061f4",
      "incomplete_value": false,
      "site": "00506200",
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
            "const:109:8"
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
      "definition_site": "00506528",
      "incomplete_value": false,
      "site": "00506530",
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
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506208",
      "incomplete_value": false,
      "site": "00506210",
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
            "const:6e8:8"
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
      "definition_site": "00506598",
      "incomplete_value": true,
      "site": "005065a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506278",
      "incomplete_value": true,
      "site": "00506284",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "00506514",
      "PARAM",
      [
        "storage",
        "002a0109",
        null,
        "string"
      ]
    ],
    [
      "00506528",
      "PARAM",
      [
        "storage",
        "002a66e8",
        null,
        "string"
      ]
    ],
    [
      "00506594",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00506514",
      "PARAM",
      [
        "storage",
        "002a0149",
        null,
        "string"
      ]
    ],
    [
      "00506528",
      "PARAM",
      [
        "storage",
        "002a6840",
        null,
        "string"
      ]
    ],
    [
      "00506594",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506200) · [`00506210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506210) · [`00506284`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00505/00505f3c.md#insn-00506284)
- 新版 [`00506520`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/0050625c.md#insn-00506520) · [`00506530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/0050625c.md#insn-00506530) · [`005065a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/0050625c.md#insn-005065a4)

~~~diff
- 00506200 ["INT_ADD", "register:40f0:8", ["const:506200:8", "const:4:8"]]
- 00506200 ["CALL", null, ["callee:00c59150:8"]]
+ 00506520 ["INT_ADD", "register:40f0:8", ["const:506520:8", "const:4:8"]]
+ 00506520 ["CALL", null, ["callee:00c59150:8"]]
- 00506200 bytes e0471d94
+ 00506520 bytes 0c4b1d94
- 00506210 ["INT_ADD", "register:40f0:8", ["const:506210:8", "const:4:8"]]
- 00506210 ["CALL", null, ["callee:00c59010:8"]]
+ 00506530 ["INT_ADD", "register:40f0:8", ["const:506530:8", "const:4:8"]]
+ 00506530 ["CALL", null, ["callee:00c59010:8"]]
- 00506210 bytes 8c471d94
+ 00506530 bytes b84a1d94
- 00506284 ["INT_ADD", "register:40f0:8", ["const:506284:8", "const:4:8"]]
- 00506284 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005065a4 ["INT_ADD", "register:40f0:8", ["const:5065a4:8", "const:4:8"]]
+ 005065a4 ["CALL", null, ["callee:00c58fb0:8"]]
- 00506284 bytes 57471d94
+ 005065a4 bytes 834a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6412aad61ef57cc47045cacfbe6cad91"></a>

### [`00506370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md) → [`00506690`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506690.md) _ZN5Botan11GeneralNameC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c50.md) · 呼出先 12件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5ac20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac20.md) · 呼出先 12件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.14% / 新版 97.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005066d4",
      "incomplete_value": true,
      "site": "005066dc",
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
      "definition_site": "005063b4",
      "incomplete_value": true,
      "site": "005063bc",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005068b8",
      "incomplete_value": false,
      "site": "005068c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:db6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506598",
      "incomplete_value": false,
      "site": "005065a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:d6c:8"
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
      "definition_site": "005068f0",
      "incomplete_value": true,
      "site": "005068fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005065d0",
      "incomplete_value": true,
      "site": "005065dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "005066bc",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "005066dc",
      "DATA",
      [
        "storage",
        "00c681a0",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005068b8",
      "PARAM",
      [
        "storage",
        "002b1d6c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005066bc",
      "READ",
      [
        "storage",
        "00c9c1c8",
        null,
        "pointer"
      ]
    ],
    [
      "005066dc",
      "DATA",
      [
        "storage",
        "00c69170",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005068b8",
      "PARAM",
      [
        "storage",
        "002b1db6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005065a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-005065a0) · [`005065dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-005065dc) · [`00506390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506370.md#insn-00506390)
- 新版 [`005068c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506690.md#insn-005068c0) · [`005068fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506690.md#insn-005068fc) · [`005066b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506690.md#insn-005066b0)

~~~diff
- 005065a0 ["INT_ADD", "register:40f0:8", ["const:5065a0:8", "const:4:8"]]
- 005065a0 ["CALL", null, ["callee:0043e138:8"]]
+ 005068c0 ["INT_ADD", "register:40f0:8", ["const:5068c0:8", "const:4:8"]]
+ 005068c0 ["CALL", null, ["callee:0043e138:8"]]
- 005065a0 bytes 1edefc97
+ 005068c0 bytes 1edefc97
- 005065dc ["INT_ADD", "register:40f0:8", ["const:5065dc:8", "const:4:8"]]
- 005065dc ["CALL", null, ["callee:00c58fb0:8"]]
+ 005068fc ["INT_ADD", "register:40f0:8", ["const:5068fc:8", "const:4:8"]]
+ 005068fc ["CALL", null, ["callee:00c58fb0:8"]]
- 005065dc bytes 81461d94
+ 005068fc bytes ad491d94
- 00506390 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005066b0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00506390 bytes a83c00b0
+ 005066b0 bytes a83c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67592eb2924c09c8710255d6d20bcd99"></a>

### [`00506688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md) → [`005069a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/005069a8.md) _ZNK5Botan11GeneralName11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c595b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c595b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c5a580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "definition_site": "005069dc",
      "incomplete_value": true,
      "site": "005069f8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
              ],
              [
                "leaf",
                "const:e81:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005066bc",
      "incomplete_value": true,
      "site": "005066d8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2be000:8"
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00506a24",
      "incomplete_value": true,
      "site": "00506a30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00506704",
      "incomplete_value": true,
      "site": "00506710",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
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
      "definition_site": "00506a20",
      "incomplete_value": false,
      "site": "00506a30",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00506700",
      "incomplete_value": false,
      "site": "00506710",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "005069dc",
      "READ",
      [
        "storage",
        "002beda3",
        null,
        "string"
      ]
    ],
    [
      "00506a20",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00506a24",
      "READ",
      [
        "storage",
        "00c9b0a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005069dc",
      "READ",
      [
        "storage",
        "002bee81",
        null,
        "string"
      ]
    ],
    [
      "00506a20",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00506a24",
      "READ",
      [
        "storage",
        "00c9c070",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-00506710) · [`005066ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-005066ac) · [`005066b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506688.md#insn-005066b4)
- 新版 [`00506a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/005069a8.md#insn-00506a30) · [`005069cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/005069a8.md#insn-005069cc) · [`005069d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/005069a8.md#insn-005069d4)

~~~diff
- 00506710 ["INT_ADD", "register:40f0:8", ["const:506710:8", "const:4:8"]]
- 00506710 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00506a30 ["INT_ADD", "register:40f0:8", ["const:506a30:8", "const:4:8"]]
+ 00506a30 ["CALL", null, ["callee:00c58fb0:8"]]
- 00506710 bytes 34461d94
+ 00506a30 bytes 60491d94
- 005066ac ["INT_ADD", "register:40f0:8", ["const:5066ac:8", "const:4:8"]]
- 005066ac ["CALL", null, ["callee:00c58f90:8"]]
+ 005069cc ["INT_ADD", "register:40f0:8", ["const:5069cc:8", "const:4:8"]]
+ 005069cc ["CALL", null, ["callee:00c58f90:8"]]
- 005066ac bytes 45461d94
+ 005069cc bytes 71491d94
- 005066b4 ["COPY", "tmp:0:8", ["const:da3:8"]]
- 005066b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005066b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005066b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005069d4 ["COPY", "tmp:0:8", ["const:e81:8"]]
+ 005069d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005069d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005069d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005066b4 bytes 298d3691
+ 005069d4 bytes 29053a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50a877297d5d857410b972fdb08be0a7"></a>

### [`00506758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md) → [`00506a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506a78.md) _ZN5Botan11GeneralName11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 29件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)
- 新版 呼出元 0件  · 呼出先 29件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00506b04",
      "incomplete_value": true,
      "site": "00506b04",
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
      "definition_site": "005067e4",
      "incomplete_value": true,
      "site": "005067e4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00506b88",
      "incomplete_value": true,
      "site": "00506b90",
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
      "definition_site": "00506868",
      "incomplete_value": true,
      "site": "00506870",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00506b98",
      "incomplete_value": true,
      "site": "00506b98",
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
                "const:b0:8"
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
      "definition_site": "00506878",
      "incomplete_value": true,
      "site": "00506878",
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
                "const:b0:8"
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
    "ordinal": 22,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00506aec",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00506b04",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506b70",
      "PARAM",
      [
        "storage",
        "002ba2d6",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00506aec",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "00506b04",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00506b70",
      "PARAM",
      [
        "storage",
        "002ba3b4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00506858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-00506858) · [`005068f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-005068f4) · [`00506afc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506758.md#insn-00506afc)
- 新版 [`00506b78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506a78.md#insn-00506b78) · [`00506c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506a78.md#insn-00506c14) · [`00506e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00506/00506a78.md#insn-00506e1c)

~~~diff
- 00506858 ["INT_ADD", "register:40f0:8", ["const:506858:8", "const:4:8"]]
- 00506858 ["CALL", null, ["callee:00c59230:8"]]
+ 00506b78 ["INT_ADD", "register:40f0:8", ["const:506b78:8", "const:4:8"]]
+ 00506b78 ["CALL", null, ["callee:00c59230:8"]]
- 00506858 bytes 82461d94
+ 00506b78 bytes ae491d94
- 005068f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005068f4 ["INT_ADD", "register:40f0:8", ["const:5068f4:8", "const:4:8"]]
- 005068f4 ["CALLIND", null, ["register:0:8"]]
+ 00506c14 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00506c14 ["INT_ADD", "register:40f0:8", ["const:506c14:8", "const:4:8"]]
+ 00506c14 ["CALLIND", null, ["register:0:8"]]
- 005068f4 bytes 20013fd6
+ 00506c14 bytes 20013fd6
- 00506afc ["COPY", "register:0:8", ["register:4048:8"]]
- 00506afc ["INT_ADD", "register:40f0:8", ["const:506afc:8", "const:4:8"]]
- 00506afc ["CALLIND", null, ["register:0:8"]]
+ 00506e1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 00506e1c ["INT_ADD", "register:40f0:8", ["const:506e1c:8", "const:4:8"]]
+ 00506e1c ["CALLIND", null, ["register:0:8"]]
- 00506afc bytes 20013fd6
+ 00506e1c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59872705501e516893ed4e41bf0f3902"></a>

### [`00506fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md) → [`005072f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md) _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004ffe60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffe60.md) [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) [`00c59c10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c10.md) · 呼出先 12件 [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 3件 [`00500180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00500/00500180.md) [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) [`00c5abe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abe0.md) · 呼出先 12件 [`004a5ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md) [`005491c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005491c8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00507384",
      "incomplete_value": true,
      "site": "00507384",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00507064",
      "incomplete_value": true,
      "site": "00507064",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "005074bc",
      "incomplete_value": true,
      "site": "005074bc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050719c",
      "incomplete_value": true,
      "site": "0050719c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00507544",
      "incomplete_value": true,
      "site": "00507544",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00507224",
      "incomplete_value": true,
      "site": "00507224",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
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
      "00507374",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005074ac",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00507534",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00507374",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005074ac",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00507534",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00507064`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-00507064) · [`0050719c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-0050719c) · [`00507224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00506/00506fd0.md#insn-00507224)
- 新版 [`00507384`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md#insn-00507384) · [`005074bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md#insn-005074bc) · [`00507544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005072f0.md#insn-00507544)

~~~diff
- 00507064 ["COPY", "register:0:8", ["register:4048:8"]]
- 00507064 ["INT_ADD", "register:40f0:8", ["const:507064:8", "const:4:8"]]
- 00507064 ["CALLIND", null, ["register:0:8"]]
+ 00507384 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00507384 ["INT_ADD", "register:40f0:8", ["const:507384:8", "const:4:8"]]
+ 00507384 ["CALLIND", null, ["register:0:8"]]
- 00507064 bytes 20013fd6
+ 00507384 bytes 20013fd6
- 0050719c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050719c ["INT_ADD", "register:40f0:8", ["const:50719c:8", "const:4:8"]]
- 0050719c ["CALLIND", null, ["register:0:8"]]
+ 005074bc ["COPY", "register:0:8", ["register:4048:8"]]
+ 005074bc ["INT_ADD", "register:40f0:8", ["const:5074bc:8", "const:4:8"]]
+ 005074bc ["CALLIND", null, ["register:0:8"]]
- 0050719c bytes 20013fd6
+ 005074bc bytes 20013fd6
- 00507224 ["COPY", "register:0:8", ["register:4048:8"]]
- 00507224 ["INT_ADD", "register:40f0:8", ["const:507224:8", "const:4:8"]]
- 00507224 ["CALLIND", null, ["register:0:8"]]
+ 00507544 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00507544 ["INT_ADD", "register:40f0:8", ["const:507544:8", "const:4:8"]]
+ 00507544 ["CALLIND", null, ["register:0:8"]]
- 00507224 bytes 20013fd6
+ 00507544 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dda1b06fa661197937a1694170d0ecd"></a>

### [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) → [`005076cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md) _ZNK5Botan11GeneralName7matchesERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c20.md) · 呼出先 23件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459db4.md) [`00507af4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507af4.md)
- 新版 呼出元 1件 [`00c5abf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5abf0.md) · 呼出先 23件 [`00441220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/00441220.md) [`004412bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00441/004412bc.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`0045a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0045a/0045a0d4.md) [`00507e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e14.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.49% / 新版 95.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050779c",
      "incomplete_value": true,
      "site": "0050779c",
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
      "definition_site": "0050747c",
      "incomplete_value": true,
      "site": "0050747c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050779c",
      "incomplete_value": true,
      "site": "0050779c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050747c",
      "incomplete_value": true,
      "site": "0050747c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:208:8"
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
      "definition_site": "0050781c",
      "incomplete_value": true,
      "site": "0050781c",
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
      "definition_site": "005074fc",
      "incomplete_value": true,
      "site": "005074fc",
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
      "0050777c",
      "READ",
      [
        "storage",
        "00c9b200",
        null,
        "pointer"
      ]
    ],
    [
      "00507780",
      "READ",
      [
        "storage",
        "00c9b208",
        null,
        "pointer"
      ]
    ],
    [
      "0050779c",
      "DATA",
      [
        "storage",
        "00c6aa60",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0050777c",
      "READ",
      [
        "storage",
        "00c9c1d0",
        null,
        "pointer"
      ]
    ],
    [
      "00507780",
      "READ",
      [
        "storage",
        "00c9c1d8",
        null,
        "pointer"
      ]
    ],
    [
      "0050779c",
      "DATA",
      [
        "storage",
        "00c6ba30",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050759c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-0050759c) · [`005073f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-005073f0) · [`005073fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md#insn-005073fc)
- 新版 [`005078bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md#insn-005078bc) · [`00507710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md#insn-00507710) · [`0050771c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md#insn-0050771c)

~~~diff
- 0050759c ["INT_ADD", "register:40f0:8", ["const:50759c:8", "const:4:8"]]
- 0050759c ["CALL", null, ["callee:00c5aa20:8"]]
+ 005078bc ["INT_ADD", "register:40f0:8", ["const:5078bc:8", "const:4:8"]]
+ 005078bc ["CALL", null, ["callee:00c5aa20:8"]]
- 0050759c bytes 2d491d94
+ 005078bc bytes 594c1d94
- 005073f0 ["INT_ADD", "register:40f0:8", ["const:5073f0:8", "const:4:8"]]
- 005073f0 ["CALL", null, ["callee:00c5aa90:8"]]
+ 00507710 ["INT_ADD", "register:40f0:8", ["const:507710:8", "const:4:8"]]
+ 00507710 ["CALL", null, ["callee:00c5aa90:8"]]
- 005073f0 bytes b4491d94
+ 00507710 bytes e04c1d94
- 005073fc ["INT_ADD", "register:40f0:8", ["const:5073fc:8", "const:4:8"]]
- 005073fc ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050771c ["INT_ADD", "register:40f0:8", ["const:50771c:8", "const:4:8"]]
+ 0050771c ["CALL", null, ["callee:00c5aa90:8"]]
- 005073fc bytes b1491d94
+ 0050771c bytes dd4c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d67672ddda8ed7cd5e512c95e9864820"></a>

### [`00507b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md) → [`00507e2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e2c.md) _ZNK5Botan11GeneralName11matches_dnsERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`005076cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md) · 呼出先 9件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.49% / 新版 99.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00507f38",
      "incomplete_value": false,
      "site": "00507f48",
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
            "const:4e7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00507c18",
      "incomplete_value": false,
      "site": "00507c28",
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
            "const:38f:8"
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
      "00507f38",
      "PARAM",
      [
        "storage",
        "002a638f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00507f38",
      "PARAM",
      [
        "storage",
        "002a64e7",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00507c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507c28) · [`00507ba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507ba4) · [`00507c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507b0c.md#insn-00507c18)
- 新版 [`00507f48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e2c.md#insn-00507f48) · [`00507ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e2c.md#insn-00507ec4) · [`00507f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/00507e2c.md#insn-00507f38)

~~~diff
- 00507c28 ["INT_ADD", "register:40f0:8", ["const:507c28:8", "const:4:8"]]
- 00507c28 ["CALL", null, ["callee:00c59150:8"]]
+ 00507f48 ["INT_ADD", "register:40f0:8", ["const:507f48:8", "const:4:8"]]
+ 00507f48 ["CALL", null, ["callee:00c59150:8"]]
- 00507c28 bytes 56411d94
+ 00507f48 bytes 82441d94
- 00507ba4 ["INT_ADD", "register:40f0:8", ["const:507ba4:8", "const:4:8"]]
- 00507ba4 ["CALL", null, ["callee:00c590f0:8"]]
+ 00507ec4 ["INT_ADD", "register:40f0:8", ["const:507ec4:8", "const:4:8"]]
+ 00507ec4 ["CALL", null, ["callee:00c590f0:8"]]
- 00507ba4 bytes 5f411d94
+ 00507ec4 bytes 8b441d94
- 00507c18 ["COPY", "tmp:0:8", ["const:38f:8"]]
- 00507c18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00507c18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00507c18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00507f38 ["COPY", "tmp:0:8", ["const:4e7:8"]]
+ 00507f38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00507f38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00507f38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00507c18 bytes 003c0e91
+ 00507f38 bytes 009c1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24f7ca8002cfacb228fc3ec914cdd5b8"></a>

### [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) → [`00508308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md) _ZNK5Botan11GeneralName10matches_dnERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 13件 [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) [`00508c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md) [`0053afd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053a/0053afd0.md) [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00549708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549708.md)
- 新版 呼出元 1件 [`005076cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md) · 呼出先 13件 [`0050891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md) [`00508f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508f88.md) [`0053b2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b2f0.md) [`005499c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005499c8.md) [`00549a28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549a28.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.66% / 新版 94.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508378",
      "incomplete_value": true,
      "site": "00508378",
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
      "definition_site": "00508058",
      "incomplete_value": true,
      "site": "00508058",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00508384",
      "incomplete_value": true,
      "site": "00508384",
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
      "definition_site": "00508064",
      "incomplete_value": true,
      "site": "00508064",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508574",
      "incomplete_value": true,
      "site": "0050857c",
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
      "definition_site": "00508254",
      "incomplete_value": true,
      "site": "0050825c",
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
      "00508360",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00508378",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508384",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508360",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "00508378",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00508384",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508020`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-00508020) · [`00508030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-00508030) · [`00508034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md#insn-00508034)
- 新版 [`00508340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md#insn-00508340) · [`00508350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md#insn-00508350) · [`00508354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md#insn-00508354)

~~~diff
- 00508020 ["INT_ADD", "register:40f0:8", ["const:508020:8", "const:4:8"]]
- 00508020 ["CALL", null, ["callee:0050891c:8"]]
+ 00508340 ["INT_ADD", "register:40f0:8", ["const:508340:8", "const:4:8"]]
+ 00508340 ["CALL", null, ["callee:0050891c:8"]]
- 00508020 bytes 77010094
+ 00508340 bytes 77010094
- 00508030 ["INT_ADD", "register:40f0:8", ["const:508030:8", "const:4:8"]]
- 00508030 ["CALL", null, ["callee:0050891c:8"]]
+ 00508350 ["INT_ADD", "register:40f0:8", ["const:508350:8", "const:4:8"]]
+ 00508350 ["CALL", null, ["callee:0050891c:8"]]
- 00508030 bytes 73010094
+ 00508350 bytes 73010094
- 00508034 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00508354 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00508034 bytes 883c00f0
+ 00508354 bytes a83c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d0a648884f05a5b4d8df9de4327d515"></a>

### [`005083a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md) → [`005086c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/005086c4.md) _ZNK5Botan11GeneralName10matches_ipERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`005073ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/005073ac.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00486db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00486/00486db8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)
- 新版 呼出元 1件 [`005076cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00507/005076cc.md) · 呼出先 12件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004870d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00487/004870d8.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00547ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ecc.md) [`00547ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ed0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005086f8",
      "incomplete_value": false,
      "site": "00508700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005083d8",
      "incomplete_value": false,
      "site": "005083e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "definition_site": "00508824",
      "incomplete_value": false,
      "site": "0050882c",
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
            "const:152:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508504",
      "incomplete_value": false,
      "site": "0050850c",
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
            "const:112:8"
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
      "definition_site": "0050885c",
      "incomplete_value": true,
      "site": "00508868",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050853c",
      "incomplete_value": true,
      "site": "00508548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
      "00508700",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "00508748",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "00508748",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00508700",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ],
    [
      "00508748",
      "READ",
      [
        "storage",
        "00c6b770",
        null,
        "pointer"
      ]
    ],
    [
      "00508748",
      "READ",
      [
        "storage",
        "00c6b778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050850c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-0050850c) · [`00508548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-00508548) · [`005083d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005083a4.md#insn-005083d0)
- 新版 [`0050882c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/005086c4.md#insn-0050882c) · [`00508868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/005086c4.md#insn-00508868) · [`005086f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/005086c4.md#insn-005086f0)

~~~diff
- 0050850c ["INT_ADD", "register:40f0:8", ["const:50850c:8", "const:4:8"]]
- 0050850c ["CALL", null, ["callee:0043e138:8"]]
+ 0050882c ["INT_ADD", "register:40f0:8", ["const:50882c:8", "const:4:8"]]
+ 0050882c ["CALL", null, ["callee:0043e138:8"]]
- 0050850c bytes 43d6fc97
+ 0050882c bytes 43d6fc97
- 00508548 ["INT_ADD", "register:40f0:8", ["const:508548:8", "const:4:8"]]
- 00508548 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00508868 ["INT_ADD", "register:40f0:8", ["const:508868:8", "const:4:8"]]
+ 00508868 ["CALL", null, ["callee:00c58fb0:8"]]
- 00508548 bytes a63e1d94
+ 00508868 bytes d2411d94
- 005083d0 ["INT_ADD", "register:40f0:8", ["const:5083d0:8", "const:4:8"]]
- 005083d0 ["CALL", null, ["callee:00c5a9a0:8"]]
+ 005086f0 ["INT_ADD", "register:40f0:8", ["const:5086f0:8", "const:4:8"]]
+ 005086f0 ["CALL", null, ["callee:00c5a9a0:8"]]
- 005083d0 bytes 80451d94
+ 005086f0 bytes ac481d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32d027c6c10aabd82afaaa915b394813"></a>

### [`005085fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md) → [`0050891c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md) FUN_0050891c

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) · 呼出先 4件 [`00548298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548298.md) [`00c582b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582b0.md) [`00c582c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582c0.md) [`00c58500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58500.md)
- 新版 呼出元 2件 [`004ffe0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md) [`00508308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md) · 呼出先 4件 [`005485b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00548/005485b8.md) [`00c59280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59280.md) [`00c59290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59290.md) [`00c594d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c594d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 78.08% / 新版 78.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050896c",
      "incomplete_value": true,
      "site": "0050896c",
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
      "definition_site": "0050864c",
      "incomplete_value": true,
      "site": "0050864c",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508970",
      "incomplete_value": true,
      "site": "00508970",
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
      "definition_site": "00508650",
      "incomplete_value": true,
      "site": "00508650",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508968",
      "incomplete_value": true,
      "site": "00508978",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00508648",
      "incomplete_value": true,
      "site": "00508658",
      "value": [
        "LOAD",
        "8",
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
      "00508944",
      "READ",
      [
        "storage",
        "00c9ace8",
        null,
        "pointer"
      ]
    ],
    [
      "00508950",
      "READ",
      [
        "storage",
        "00c9ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00508968",
      "READ",
      [
        "storage",
        "00c931c8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00508944",
      "READ",
      [
        "storage",
        "00c9bcb8",
        null,
        "pointer"
      ]
    ],
    [
      "00508950",
      "READ",
      [
        "storage",
        "00c9bcb0",
        null,
        "pointer"
      ]
    ],
    [
      "00508968",
      "READ",
      [
        "storage",
        "00c94198",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md#insn-00508618) · [`0050861c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md#insn-0050861c) · [`00508624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/005085fc.md#insn-00508624)
- 新版 [`00508938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md#insn-00508938) · [`0050893c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md#insn-0050893c) · [`00508944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/0050891c.md#insn-00508944)

~~~diff
- 00508618 ["COPY", "register:40c8:8", ["const:c9a000:8"]]
+ 00508938 ["COPY", "register:40c8:8", ["const:c9b000:8"]]
- 00508618 bytes 993c00d0
+ 00508938 bytes 993c00f0
- 0050861c ["COPY", "register:40c0:8", ["const:c9a000:8"]]
+ 0050893c ["COPY", "register:40c0:8", ["const:c9b000:8"]]
- 0050861c bytes 983c00d0
+ 0050893c bytes 983c00f0
- 00508624 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ce8:8"]]
- 00508624 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508944 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:cb8:8"]]
+ 00508944 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 00508624 bytes 397746f9
+ 00508944 bytes 395f46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1005a772b4ac1ca3087a71b4143a93a"></a>

### [`00508768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md) → [`00508a88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508a88.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_7X509_DNE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a60.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005153b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/005153b0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5aa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aa30.md) · 呼出先 12件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`005156d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/005156d0.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508d6c",
      "incomplete_value": false,
      "site": "00508d74",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508a4c",
      "incomplete_value": false,
      "site": "00508a54",
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
            "const:6f8:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508da4",
      "incomplete_value": true,
      "site": "00508db0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00508a84",
      "incomplete_value": true,
      "site": "00508a90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00508da0",
      "incomplete_value": false,
      "site": "00508db0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00508a80",
      "incomplete_value": false,
      "site": "00508a90",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 18,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00508d6c",
      "PARAM",
      [
        "storage",
        "002a66f8",
        null,
        "string"
      ]
    ],
    [
      "00508da0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00508da4",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00508d6c",
      "PARAM",
      [
        "storage",
        "002a6850",
        null,
        "string"
      ]
    ],
    [
      "00508da0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00508da4",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-00508a54) · [`00508a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-00508a90) · [`005087f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508768.md#insn-005087f4)
- 新版 [`00508d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508a88.md#insn-00508d74) · [`00508db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508a88.md#insn-00508db0) · [`00508b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508a88.md#insn-00508b14)

~~~diff
- 00508a54 ["INT_ADD", "register:40f0:8", ["const:508a54:8", "const:4:8"]]
- 00508a54 ["CALL", null, ["callee:0043e138:8"]]
+ 00508d74 ["INT_ADD", "register:40f0:8", ["const:508d74:8", "const:4:8"]]
+ 00508d74 ["CALL", null, ["callee:0043e138:8"]]
- 00508a54 bytes f1d4fc97
+ 00508d74 bytes f1d4fc97
- 00508a90 ["INT_ADD", "register:40f0:8", ["const:508a90:8", "const:4:8"]]
- 00508a90 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00508db0 ["INT_ADD", "register:40f0:8", ["const:508db0:8", "const:4:8"]]
+ 00508db0 ["CALL", null, ["callee:00c58fb0:8"]]
- 00508a90 bytes 543d1d94
+ 00508db0 bytes 80401d94
- 005087f4 ["INT_ADD", "register:40f0:8", ["const:5087f4:8", "const:4:8"]]
- 005087f4 ["CALL", null, ["callee:005156d0:8"]]
+ 00508b14 ["INT_ADD", "register:40f0:8", ["const:508b14:8", "const:4:8"]]
+ 00508b14 ["CALL", null, ["callee:005156d0:8"]]
- 005087f4 bytes ef320094
+ 00508b14 bytes ef320094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46dbb6f8f825e75b45752b936822900d"></a>

### [`00508c68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md) → [`00508f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508f88.md) FUN_00508f88

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00507fe8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00507/00507fe8.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00508308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508308.md) · 呼出先 6件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00508fc0",
      "incomplete_value": true,
      "site": "00508fc4",
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
      "definition_site": "00508ca0",
      "incomplete_value": true,
      "site": "00508ca4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00508fb0",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00508fc4",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00508fb0",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00508fc4",
      "DATA",
      [
        "storage",
        "00c67328",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00508c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508c84) · [`00508c90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508c90) · [`00508cb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508c68.md#insn-00508cb8)
- 新版 [`00508fa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508f88.md#insn-00508fa4) · [`00508fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508f88.md#insn-00508fb0) · [`00508fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00508/00508f88.md#insn-00508fd8)

~~~diff
- 00508c84 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 00508fa4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 00508c84 bytes 883c00d0
+ 00508fa4 bytes 883c00f0
- 00508c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 00508c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00508fb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 00508fb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00508c90 bytes 080947f9
+ 00508fb0 bytes 08f146f9
- 00508cb8 ["INT_ADD", "register:40f0:8", ["const:508cb8:8", "const:4:8"]]
- 00508cb8 ["CALL", null, ["callee:00c58f30:8"]]
+ 00508fd8 ["INT_ADD", "register:40f0:8", ["const:508fd8:8", "const:4:8"]]
+ 00508fd8 ["CALL", null, ["callee:00c58f30:8"]]
- 00508cb8 bytes aa3c1d94
+ 00508fd8 bytes d63f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8de115ee151f36a3ca969fb38a9c18dc"></a>

### [`00508d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md) → [`005090a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005090a8.md) _ZN5Botan14GeneralSubtreeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0044295c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/0044295c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043bac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043bac4.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00442c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c7c.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.63% / 新版 96.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005090f8",
      "incomplete_value": true,
      "site": "005090f8",
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
      "definition_site": "00508dd8",
      "incomplete_value": true,
      "site": "00508dd8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005090f8",
      "incomplete_value": true,
      "site": "005090f8",
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
      "definition_site": "00508dd8",
      "incomplete_value": true,
      "site": "00508dd8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050939c",
      "incomplete_value": false,
      "site": "005093a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:db6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050907c",
      "incomplete_value": false,
      "site": "00509084",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:d6c:8"
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
      "005090d4",
      "READ",
      [
        "storage",
        "00c9b220",
        null,
        "pointer"
      ]
    ],
    [
      "005090dc",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ],
    [
      "005090f8",
      "DATA",
      [
        "storage",
        "00c681e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005090d4",
      "READ",
      [
        "storage",
        "00c9c1f0",
        null,
        "pointer"
      ]
    ],
    [
      "005090dc",
      "READ",
      [
        "storage",
        "00c9c1c8",
        null,
        "pointer"
      ]
    ],
    [
      "005090f8",
      "DATA",
      [
        "storage",
        "00c691b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-00509084) · [`005090c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-005090c0) · [`00508dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00508/00508d88.md#insn-00508dac)
- 新版 [`005093a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005090a8.md#insn-005093a4) · [`005093e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005090a8.md#insn-005093e0) · [`005090cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005090a8.md#insn-005090cc)

~~~diff
- 00509084 ["INT_ADD", "register:40f0:8", ["const:509084:8", "const:4:8"]]
- 00509084 ["CALL", null, ["callee:0043e138:8"]]
+ 005093a4 ["INT_ADD", "register:40f0:8", ["const:5093a4:8", "const:4:8"]]
+ 005093a4 ["CALL", null, ["callee:0043e138:8"]]
- 00509084 bytes 65d3fc97
+ 005093a4 bytes 65d3fc97
- 005090c0 ["INT_ADD", "register:40f0:8", ["const:5090c0:8", "const:4:8"]]
- 005090c0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005093e0 ["INT_ADD", "register:40f0:8", ["const:5093e0:8", "const:4:8"]]
+ 005093e0 ["CALL", null, ["callee:00c58fb0:8"]]
- 005090c0 bytes c83b1d94
+ 005093e0 bytes f43e1d94
- 00508dac ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005090cc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00508dac bytes 883c00f0
+ 005090cc bytes 883c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a84ca180bc835350c1bf2bc9a5ac20f6"></a>

### [`005091ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md) → [`005094cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005094cc.md) _ZNK5Botan14GeneralSubtree11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050950c",
      "incomplete_value": true,
      "site": "00509520",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005091ec",
      "incomplete_value": true,
      "site": "00509200",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:20:8"
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
      "definition_site": "00509510",
      "incomplete_value": true,
      "site": "00509524",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "005091f0",
      "incomplete_value": true,
      "site": "00509204",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509514",
      "incomplete_value": true,
      "site": "00509528",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005091f4",
      "incomplete_value": true,
      "site": "00509208",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0050950c",
      "READ",
      [
        "storage",
        "002a2020",
        null,
        "string"
      ]
    ],
    [
      "00509510",
      "READ",
      [
        "storage",
        "002a2030",
        null,
        "string"
      ]
    ],
    [
      "00509514",
      "READ",
      [
        "storage",
        "002c22e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050950c",
      "READ",
      [
        "storage",
        "002a2060",
        null,
        "string"
      ]
    ],
    [
      "00509510",
      "READ",
      [
        "storage",
        "002a2070",
        null,
        "string"
      ]
    ],
    [
      "00509514",
      "READ",
      [
        "storage",
        "002c2330",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-00509244) · [`005091d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-005091d0) · [`005091dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005091ac.md#insn-005091dc)
- 新版 [`00509564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005094cc.md#insn-00509564) · [`005094f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005094cc.md#insn-005094f0) · [`005094fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005094cc.md#insn-005094fc)

~~~diff
- 00509244 ["INT_ADD", "register:40f0:8", ["const:509244:8", "const:4:8"]]
- 00509244 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00509564 ["INT_ADD", "register:40f0:8", ["const:509564:8", "const:4:8"]]
+ 00509564 ["CALL", null, ["callee:00c58fb0:8"]]
- 00509244 bytes 673b1d94
+ 00509564 bytes 933e1d94
- 005091d0 ["INT_ADD", "register:40f0:8", ["const:5091d0:8", "const:4:8"]]
- 005091d0 ["CALL", null, ["callee:00c58f90:8"]]
+ 005094f0 ["INT_ADD", "register:40f0:8", ["const:5094f0:8", "const:4:8"]]
+ 005094f0 ["CALL", null, ["callee:00c58f90:8"]]
- 005091d0 bytes 7c3b1d94
+ 005094f0 bytes a83e1d94
- 005091dc ["INT_ADD", "register:40f0:8", ["const:5091dc:8", "const:4:8"]]
- 005091dc ["CALL", null, ["callee:00c58f30:8"]]
+ 005094fc ["INT_ADD", "register:40f0:8", ["const:5094fc:8", "const:4:8"]]
+ 005094fc ["CALL", null, ["callee:00c58f30:8"]]
- 005091dc bytes 613b1d94
+ 005094fc bytes 8d3e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c2790c83a596b9d7ca007f6f86515d"></a>

### [`00509294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md) → [`005095b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005095b4.md) _ZN5Botan14GeneralSubtree11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c60.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5ac30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac30.md) · 呼出先 11件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050965c",
      "incomplete_value": true,
      "site": "0050965c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050933c",
      "incomplete_value": true,
      "site": "0050933c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "005096ac",
      "incomplete_value": false,
      "site": "005096b4",
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
            "const:da9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050938c",
      "incomplete_value": false,
      "site": "00509394",
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
            "const:c51:8"
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
      "definition_site": "005096e4",
      "incomplete_value": true,
      "site": "005096f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005093c4",
      "incomplete_value": true,
      "site": "005093d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
      "0050964c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "005096ac",
      "PARAM",
      [
        "storage",
        "002a8c51",
        null,
        "string"
      ]
    ],
    [
      "005096e0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050964c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "005096ac",
      "PARAM",
      [
        "storage",
        "002a8da9",
        null,
        "string"
      ]
    ],
    [
      "005096e0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050933c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-0050933c) · [`00509394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-00509394) · [`005093d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509294.md#insn-005093d0)
- 新版 [`0050965c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005095b4.md#insn-0050965c) · [`005096b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005095b4.md#insn-005096b4) · [`005096f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/005095b4.md#insn-005096f0)

~~~diff
- 0050933c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050933c ["INT_ADD", "register:40f0:8", ["const:50933c:8", "const:4:8"]]
- 0050933c ["CALLIND", null, ["register:0:8"]]
+ 0050965c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050965c ["INT_ADD", "register:40f0:8", ["const:50965c:8", "const:4:8"]]
+ 0050965c ["CALLIND", null, ["register:0:8"]]
- 0050933c bytes 20013fd6
+ 0050965c bytes 20013fd6
- 00509394 ["INT_ADD", "register:40f0:8", ["const:509394:8", "const:4:8"]]
- 00509394 ["CALL", null, ["callee:0043e138:8"]]
+ 005096b4 ["INT_ADD", "register:40f0:8", ["const:5096b4:8", "const:4:8"]]
+ 005096b4 ["CALL", null, ["callee:0043e138:8"]]
- 00509394 bytes a1d2fc97
+ 005096b4 bytes a1d2fc97
- 005093d0 ["INT_ADD", "register:40f0:8", ["const:5093d0:8", "const:4:8"]]
- 005093d0 ["CALL", null, ["callee:00c58fb0:8"]]
+ 005096f0 ["INT_ADD", "register:40f0:8", ["const:5096f0:8", "const:4:8"]]
+ 005096f0 ["CALL", null, ["callee:00c58fb0:8"]]
- 005093d0 bytes 043b1d94
+ 005096f0 bytes 303e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d1f264e9de49021bbcba69b1ddd22f"></a>

### [`00509438`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md) → [`00509758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509758.md) FUN_00509758

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0051ae6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0051a/0051ae6c.md) · 呼出先 5件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c582d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c582d0.md)
- 新版 呼出元 1件 [`0051b18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0051b/0051b18c.md) · 呼出先 5件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c592a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c592a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.47% / 新版 92.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005097c4",
      "incomplete_value": true,
      "site": "005097c8",
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
      "definition_site": "005094a4",
      "incomplete_value": true,
      "site": "005094a8",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00509794",
      "incomplete_value": false,
      "site": "00509798",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509474",
      "incomplete_value": false,
      "site": "00509478",
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
            "const:a8b:8"
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
      "definition_site": "00509850",
      "incomplete_value": false,
      "site": "00509858",
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
            "const:a42:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509530",
      "incomplete_value": false,
      "site": "00509538",
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
      "00509794",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        null
      ]
    ],
    [
      "005097a4",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        null
      ]
    ],
    [
      "005097bc",
      "READ",
      [
        "storage",
        "00c9b1f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509794",
      "PARAM",
      [
        "storage",
        "002a9b58",
        null,
        null
      ]
    ],
    [
      "005097a4",
      "PARAM",
      [
        "storage",
        "002a9b58",
        null,
        null
      ]
    ],
    [
      "005097bc",
      "READ",
      [
        "storage",
        "00c9c1c8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509478`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509478) · [`00509538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509538) · [`00509464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509438.md#insn-00509464)
- 新版 [`00509798`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509758.md#insn-00509798) · [`00509858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509758.md#insn-00509858) · [`00509784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509758.md#insn-00509784)

~~~diff
- 00509478 ["INT_ADD", "register:40f0:8", ["const:509478:8", "const:4:8"]]
- 00509478 ["CALL", null, ["callee:00459830:8"]]
+ 00509798 ["INT_ADD", "register:40f0:8", ["const:509798:8", "const:4:8"]]
+ 00509798 ["CALL", null, ["callee:00459830:8"]]
- 00509478 bytes 2640fd97
+ 00509798 bytes 2640fd97
- 00509538 ["INT_ADD", "register:40f0:8", ["const:509538:8", "const:4:8"]]
- 00509538 ["CALL", null, ["callee:00459830:8"]]
+ 00509858 ["INT_ADD", "register:40f0:8", ["const:509858:8", "const:4:8"]]
+ 00509858 ["CALL", null, ["callee:00459830:8"]]
- 00509538 bytes f63ffd97
+ 00509858 bytes f63ffd97
- 00509464 ["INT_ADD", "register:40f0:8", ["const:509464:8", "const:4:8"]]
- 00509464 ["CALL", null, ["callee:00c592a0:8"]]
+ 00509784 ["INT_ADD", "register:40f0:8", ["const:509784:8", "const:4:8"]]
+ 00509784 ["CALL", null, ["callee:00c592a0:8"]]
- 00509464 bytes 9b3b1d94
+ 00509784 bytes c73e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c523ac596cc4f067cb0d4284c89c67"></a>

### [`005095e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md) → [`00509908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509908.md) _ZN5Botan4OCSP7RequestC2ERKNS_16X509_CertificateES4_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509944",
      "incomplete_value": true,
      "site": "00509948",
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
      "definition_site": "00509624",
      "incomplete_value": true,
      "site": "00509628",
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
    "kind": "call_target",
    "new": {
      "definition_site": "005099c8",
      "incomplete_value": true,
      "site": "005099c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005096a8",
      "incomplete_value": true,
      "site": "005096a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00509a34",
      "incomplete_value": false,
      "site": "00509a3c",
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
            "const:f6f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509714",
      "incomplete_value": false,
      "site": "0050971c",
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
            "const:e91:8"
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
      "00509940",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00509948",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005099b8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509940",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ],
    [
      "00509948",
      "DATA",
      [
        "storage",
        "00c68b28",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "005099b8",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005096a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-005096a8) · [`0050971c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-0050971c) · [`00509758`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005095e8.md#insn-00509758)
- 新版 [`005099c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509908.md#insn-005099c8) · [`00509a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509908.md#insn-00509a3c) · [`00509a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509908.md#insn-00509a78)

~~~diff
- 005096a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005096a8 ["INT_ADD", "register:40f0:8", ["const:5096a8:8", "const:4:8"]]
- 005096a8 ["CALLIND", null, ["register:0:8"]]
+ 005099c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005099c8 ["INT_ADD", "register:40f0:8", ["const:5099c8:8", "const:4:8"]]
+ 005099c8 ["CALLIND", null, ["register:0:8"]]
- 005096a8 bytes 20013fd6
+ 005099c8 bytes 20013fd6
- 0050971c ["INT_ADD", "register:40f0:8", ["const:50971c:8", "const:4:8"]]
- 0050971c ["CALL", null, ["callee:0043e138:8"]]
+ 00509a3c ["INT_ADD", "register:40f0:8", ["const:509a3c:8", "const:4:8"]]
+ 00509a3c ["CALL", null, ["callee:0043e138:8"]]
- 0050971c bytes bfd1fc97
+ 00509a3c bytes bfd1fc97
- 00509758 ["INT_ADD", "register:40f0:8", ["const:509758:8", "const:4:8"]]
- 00509758 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00509a78 ["INT_ADD", "register:40f0:8", ["const:509a78:8", "const:4:8"]]
+ 00509a78 ["CALL", null, ["callee:00c58fb0:8"]]
- 00509758 bytes 223a1d94
+ 00509a78 bytes 4e3d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f04d5859bdb71d7172ec6f2b8746322a"></a>

### [`00509894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md) → [`00509bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509bb4.md) FUN_00509bb4

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

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
      "definition_site": "00509bd0",
      "incomplete_value": true,
      "site": "00509bd4",
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
      "definition_site": "005098b0",
      "incomplete_value": true,
      "site": "005098b4",
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
      "definition_site": "00509c10",
      "incomplete_value": true,
      "site": "00509c14",
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
      "definition_site": "005098f0",
      "incomplete_value": true,
      "site": "005098f4",
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
      "00509bc8",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00509bd4",
      "DATA",
      [
        "storage",
        "00c67b58",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509c08",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509bc8",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ],
    [
      "00509bd4",
      "DATA",
      [
        "storage",
        "00c68b28",
        null,
        "undefined1[72]"
      ]
    ],
    [
      "00509c08",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005098a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098a0) · [`005098a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098a8) · [`005098c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509894.md#insn-005098c4)
- 新版 [`00509bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509bb4.md#insn-00509bc0) · [`00509bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509bb4.md#insn-00509bc8) · [`00509be4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509bb4.md#insn-00509be4)

~~~diff
- 005098a0 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00509bc0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005098a0 bytes 883c00d0
+ 00509bc0 bytes 883c00f0
- 005098a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1b0:8"]]
- 005098a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00509bc8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:180:8"]]
+ 00509bc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005098a8 bytes 08d940f9
+ 00509bc8 bytes 08c140f9
- 005098c4 ["INT_ADD", "register:40f0:8", ["const:5098c4:8", "const:4:8"]]
- 005098c4 ["CALL", null, ["callee:00c54d90:8"]]
+ 00509be4 ["INT_ADD", "register:40f0:8", ["const:509be4:8", "const:4:8"]]
+ 00509be4 ["CALL", null, ["callee:00c54d90:8"]]
- 005098c4 bytes 37291d94
+ 00509be4 bytes 6b2c1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a284e6341783d60c7349b43719dc062f"></a>

### [`005099c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md) → [`00509ce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ce4.md) _ZNK5Botan4OCSP7Request10BER_encodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c80.md) · 呼出先 10件 [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)
- 新版 呼出元 1件 [`00c5ac50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac50.md) · 呼出先 10件 [`004a7110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a7110.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00509d90",
      "incomplete_value": true,
      "site": "00509d90",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509a70",
      "incomplete_value": true,
      "site": "00509a70",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00509e64",
      "incomplete_value": true,
      "site": "00509e64",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00509b44",
      "incomplete_value": true,
      "site": "00509b44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40b8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 18,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00509d80",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00509e54",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509d80",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00509e54",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509a70) · [`00509b44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509b44) · [`00509a08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/005099c4.md#insn-00509a08)
- 新版 [`00509d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ce4.md#insn-00509d90) · [`00509e64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ce4.md#insn-00509e64) · [`00509d28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509ce4.md#insn-00509d28)

~~~diff
- 00509a70 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509a70 ["INT_ADD", "register:40f0:8", ["const:509a70:8", "const:4:8"]]
- 00509a70 ["CALLIND", null, ["register:0:8"]]
+ 00509d90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509d90 ["INT_ADD", "register:40f0:8", ["const:509d90:8", "const:4:8"]]
+ 00509d90 ["CALLIND", null, ["register:0:8"]]
- 00509a70 bytes 20013fd6
+ 00509d90 bytes 20013fd6
- 00509b44 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509b44 ["INT_ADD", "register:40f0:8", ["const:509b44:8", "const:4:8"]]
- 00509b44 ["CALLIND", null, ["register:0:8"]]
+ 00509e64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00509e64 ["INT_ADD", "register:40f0:8", ["const:509e64:8", "const:4:8"]]
+ 00509e64 ["CALLIND", null, ["register:0:8"]]
- 00509b44 bytes 20013fd6
+ 00509e64 bytes 20013fd6
- 00509a08 ["INT_ADD", "register:40f0:8", ["const:509a08:8", "const:4:8"]]
- 00509a08 ["CALL", null, ["callee:00c59750:8"]]
+ 00509d28 ["INT_ADD", "register:40f0:8", ["const:509d28:8", "const:4:8"]]
+ 00509d28 ["CALL", null, ["callee:00c59750:8"]]
- 00509a08 bytes 5e3b1d94
+ 00509d28 bytes 8a3e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ad0691bb9168bae12284e628af3a05"></a>

### [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) → [`00509f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md) _ZN5Botan4OCSP8ResponseC2EPKhm

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 41件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md) [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`004aeab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeab4.md) [`0050a9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md)
- 新版 呼出元 0件  · 呼出先 41件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`004a5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5adc.md) [`004a5ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5ce0.md) [`004aedd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aedd4.md) [`0050acdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050a/0050acdc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.76% / 新版 94.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 10件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00509ffc",
      "incomplete_value": true,
      "site": "00509ffc",
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
      "definition_site": "00509cdc",
      "incomplete_value": true,
      "site": "00509cdc",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050a024",
      "incomplete_value": true,
      "site": "0050a024",
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
      "definition_site": "00509d04",
      "incomplete_value": true,
      "site": "00509d04",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050a050",
      "incomplete_value": true,
      "site": "0050a050",
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
      "definition_site": "00509d30",
      "incomplete_value": true,
      "site": "00509d30",
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
      "00509ff0",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "00509ffc",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050a00c",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00509ff0",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ],
    [
      "00509ffc",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050a00c",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00509dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509dd0) · [`00509e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509e8c) · [`00509fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md#insn-00509fbc)
- 新版 [`0050a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md#insn-0050a0f0) · [`0050a1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md#insn-0050a1ac) · [`0050a2dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md#insn-0050a2dc)

~~~diff
- 00509dd0 ["COPY", "register:0:8", ["register:4048:8"]]
- 00509dd0 ["INT_ADD", "register:40f0:8", ["const:509dd0:8", "const:4:8"]]
- 00509dd0 ["CALLIND", null, ["register:0:8"]]
+ 0050a0f0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050a0f0 ["INT_ADD", "register:40f0:8", ["const:50a0f0:8", "const:4:8"]]
+ 0050a0f0 ["CALLIND", null, ["register:0:8"]]
- 00509dd0 bytes 20013fd6
+ 0050a0f0 bytes 20013fd6
- 00509e8c ["COPY", "register:0:8", ["register:4048:8"]]
- 00509e8c ["INT_ADD", "register:40f0:8", ["const:509e8c:8", "const:4:8"]]
- 00509e8c ["CALLIND", null, ["register:0:8"]]
+ 0050a1ac ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050a1ac ["INT_ADD", "register:40f0:8", ["const:50a1ac:8", "const:4:8"]]
+ 0050a1ac ["CALLIND", null, ["register:0:8"]]
- 00509e8c bytes 20013fd6
+ 0050a1ac bytes 20013fd6
- 00509fbc ["COPY", "register:0:8", ["register:4048:8"]]
- 00509fbc ["INT_ADD", "register:40f0:8", ["const:509fbc:8", "const:4:8"]]
- 00509fbc ["CALLIND", null, ["register:0:8"]]
+ 0050a2dc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050a2dc ["INT_ADD", "register:40f0:8", ["const:50a2dc:8", "const:4:8"]]
+ 0050a2dc ["CALLIND", null, ["register:0:8"]]
- 00509fbc bytes 20013fd6
+ 0050a2dc bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8282e77ad7dd3a2ae2cb60f5203c3535"></a>

### [`0050a9bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md) → [`0050acdc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050a/0050acdc.md) FUN_0050acdc

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00509c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00509/00509c54.md) · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00509f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00509/00509f74.md) · 呼出先 7件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

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
      "definition_site": "0050ade4",
      "incomplete_value": true,
      "site": "0050adec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050aac4",
      "incomplete_value": true,
      "site": "0050aacc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050ade0",
      "incomplete_value": false,
      "site": "0050adec",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0050aac0",
      "incomplete_value": false,
      "site": "0050aacc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 6,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050ade0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050ade4",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0050ade4",
      "PARAM",
      [
        "storage",
        "00c66390",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0050ade0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0050ade4",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ],
    [
      "0050ade4",
      "PARAM",
      [
        "storage",
        "00c67360",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050aacc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050aacc) · [`0050a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050a9f4) · [`0050aa04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050a9bc.md#insn-0050aa04)
- 新版 [`0050adec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050a/0050acdc.md#insn-0050adec) · [`0050ad14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050a/0050acdc.md#insn-0050ad14) · [`0050ad24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050a/0050acdc.md#insn-0050ad24)

~~~diff
- 0050aacc ["INT_ADD", "register:40f0:8", ["const:50aacc:8", "const:4:8"]]
- 0050aacc ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050adec ["INT_ADD", "register:40f0:8", ["const:50adec:8", "const:4:8"]]
+ 0050adec ["CALL", null, ["callee:00c58fb0:8"]]
- 0050aacc bytes 45351d94
+ 0050adec bytes 71381d94
- 0050a9f4 ["INT_ADD", "register:40f0:8", ["const:50a9f4:8", "const:4:8"]]
- 0050a9f4 ["CALL", null, ["callee:00c59730:8"]]
+ 0050ad14 ["INT_ADD", "register:40f0:8", ["const:50ad14:8", "const:4:8"]]
+ 0050ad14 ["CALL", null, ["callee:00c59730:8"]]
- 0050a9f4 bytes 5b371d94
+ 0050ad14 bytes 873a1d94
- 0050aa04 ["INT_ADD", "register:40f0:8", ["const:50aa04:8", "const:4:8"]]
- 0050aa04 ["CALL", null, ["callee:00c58f50:8"]]
+ 0050ad24 ["INT_ADD", "register:40f0:8", ["const:50ad24:8", "const:4:8"]]
+ 0050ad24 ["CALL", null, ["callee:00c58f50:8"]]
- 0050aa04 bytes 5f351d94
+ 0050ad24 bytes 8b381d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f5c253f44d70717609298fa540a3f6"></a>

### [`0050aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md) → [`0050b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b1d8.md) _ZN5Botan11BER_Decoder11decode_listINS_4OCSP14SingleResponseEEERS0_RNSt6__ndk16vectorIT_NS5_9allocatorIS7_EEEENS_8ASN1_TagESC_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cb0.md) · 呼出先 10件 [`0050cef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md) [`005498c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005498c8.md) [`00549acc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/00549acc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 1件 [`00c5ac80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac80.md) · 呼出先 10件 [`0050d214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d214.md) [`00549be8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549be8.md) [`00549dec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/00549dec.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.53% / 新版 90.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b31c",
      "incomplete_value": true,
      "site": "0050b31c",
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
      "definition_site": "0050affc",
      "incomplete_value": true,
      "site": "0050affc",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b33c",
      "incomplete_value": true,
      "site": "0050b33c",
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
      "definition_site": "0050b01c",
      "incomplete_value": true,
      "site": "0050b01c",
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
    "ordinal": 39,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b338",
      "incomplete_value": true,
      "site": "0050b348",
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
      "definition_site": "0050b018",
      "incomplete_value": true,
      "site": "0050b028",
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
      "0050b22c",
      "READ",
      [
        "storage",
        "00c9b230",
        null,
        "pointer"
      ]
    ],
    [
      "0050b230",
      "READ",
      [
        "storage",
        "00c9b238",
        null,
        "pointer"
      ]
    ],
    [
      "0050b234",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050b22c",
      "READ",
      [
        "storage",
        "00c9c200",
        null,
        "pointer"
      ]
    ],
    [
      "0050b230",
      "READ",
      [
        "storage",
        "00c9c208",
        null,
        "pointer"
      ]
    ],
    [
      "0050b234",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050b080) · [`0050b114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050b114) · [`0050aefc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md#insn-0050aefc)
- 新版 [`0050b3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b1d8.md#insn-0050b3a0) · [`0050b434`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b1d8.md#insn-0050b434) · [`0050b21c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b1d8.md#insn-0050b21c)

~~~diff
- 0050b080 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050b080 ["INT_ADD", "register:40f0:8", ["const:50b080:8", "const:4:8"]]
- 0050b080 ["CALLIND", null, ["register:0:8"]]
+ 0050b3a0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b3a0 ["INT_ADD", "register:40f0:8", ["const:50b3a0:8", "const:4:8"]]
+ 0050b3a0 ["CALLIND", null, ["register:0:8"]]
- 0050b080 bytes 20013fd6
+ 0050b3a0 bytes 20013fd6
- 0050b114 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050b114 ["INT_ADD", "register:40f0:8", ["const:50b114:8", "const:4:8"]]
- 0050b114 ["CALLIND", null, ["register:0:8"]]
+ 0050b434 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050b434 ["INT_ADD", "register:40f0:8", ["const:50b434:8", "const:4:8"]]
+ 0050b434 ["CALLIND", null, ["register:0:8"]]
- 0050b114 bytes 20013fd6
+ 0050b434 bytes 20013fd6
- 0050aefc ["INT_ADD", "register:40f0:8", ["const:50aefc:8", "const:4:8"]]
- 0050aefc ["CALL", null, ["callee:00c597a0:8"]]
+ 0050b21c ["INT_ADD", "register:40f0:8", ["const:50b21c:8", "const:4:8"]]
+ 0050b21c ["CALL", null, ["callee:00c597a0:8"]]
- 0050aefc bytes 35361d94
+ 0050b21c bytes 61391d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffa36ac2c89ad9fba402de1182a51282"></a>

### [`0050b504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md) → [`0050b824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b824.md) _ZNK5Botan4OCSP8Response16verify_signatureERKNS_16X509_CertificateE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cd0.md) · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md) [`00547b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547b54.md) [`00547bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bac.md) [`00547bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00547/00547bb0.md)
- 新版 呼出元 1件 [`00c5aca0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aca0.md) · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md) [`00547e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547e74.md) [`00547ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ecc.md) [`00547ed0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00547/00547ed0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.95% / 新版 98.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0050b874",
      "incomplete_value": false,
      "site": "0050b874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6b000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050b554",
      "incomplete_value": false,
      "site": "0050b554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c6a000:8"
          ],
          [
            "leaf",
            "const:780:8"
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
      "0050b874",
      "DATA",
      [
        "storage",
        "00c6a780",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b8b8",
      "READ",
      [
        "storage",
        "00c6a7a0",
        null,
        "pointer"
      ]
    ],
    [
      "0050b8b8",
      "READ",
      [
        "storage",
        "00c6a7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0050b874",
      "DATA",
      [
        "storage",
        "00c6b750",
        null,
        "undefined *"
      ]
    ],
    [
      "0050b8b8",
      "READ",
      [
        "storage",
        "00c6b770",
        null,
        "pointer"
      ]
    ],
    [
      "0050b8b8",
      "READ",
      [
        "storage",
        "00c6b778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b534) · [`0050b544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b544) · [`0050b548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b504.md#insn-0050b548)
- 新版 [`0050b854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b824.md#insn-0050b854) · [`0050b864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b824.md#insn-0050b864) · [`0050b868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b824.md#insn-0050b868)

~~~diff
- 0050b534 ["INT_ADD", "register:40f0:8", ["const:50b534:8", "const:4:8"]]
- 0050b534 ["CALL", null, ["callee:00c5acb0:8"]]
+ 0050b854 ["INT_ADD", "register:40f0:8", ["const:50b854:8", "const:4:8"]]
+ 0050b854 ["CALL", null, ["callee:00c5acb0:8"]]
- 0050b534 bytes eb391d94
+ 0050b854 bytes 173d1d94
- 0050b544 ["INT_ADD", "register:40f0:8", ["const:50b544:8", "const:4:8"]]
- 0050b544 ["CALL", null, ["callee:00c59950:8"]]
+ 0050b864 ["INT_ADD", "register:40f0:8", ["const:50b864:8", "const:4:8"]]
+ 0050b864 ["CALL", null, ["callee:00c59950:8"]]
- 0050b544 bytes 0f351d94
+ 0050b864 bytes 3b381d94
- 0050b548 ["COPY", "register:4040:8", ["const:c6a000:8"]]
+ 0050b868 ["COPY", "register:4040:8", ["const:c6b000:8"]]
- 0050b548 bytes e83a00f0
+ 0050b868 bytes 083b0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed1886edf542a7bb4b5e73e3790428ea"></a>

### [`0050b92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md) → [`0050bc4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050bc4c.md) _ZNK5Botan4OCSP8Response15check_signatureERKNSt6__ndk16vectorIPNS_17Certificate_StoreENS2_9allocatorIS5_EEEERKNS3_INS2_10shared_ptrIKNS_16X5

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59cf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59cf0.md) · 呼出先 13件 [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md) [`00c53d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53d70.md) [`00c53da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53da0.md) [`00c57f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f50.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5acc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5acc0.md) · 呼出先 13件 [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md) [`00c54d60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d60.md) [`00c54d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54d90.md) [`00c58f20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f20.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.35% / 新版 97.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050bf50",
      "incomplete_value": true,
      "site": "0050bf5c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dc9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bc30",
      "incomplete_value": true,
      "site": "0050bc3c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ceb:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050c0e4",
      "incomplete_value": true,
      "site": "0050c0e8",
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
      "definition_site": "0050bdc4",
      "incomplete_value": true,
      "site": "0050bdc8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050c118",
      "incomplete_value": true,
      "site": "0050c11c",
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
      "definition_site": "0050bdf8",
      "incomplete_value": true,
      "site": "0050bdfc",
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
      "0050bf50",
      "READ",
      [
        "storage",
        "002b4ceb",
        null,
        "string"
      ]
    ],
    [
      "0050c0dc",
      "READ",
      [
        "storage",
        "00c9b1a8",
        null,
        "pointer"
      ]
    ],
    [
      "0050c0e8",
      "DATA",
      [
        "storage",
        "00c6a810",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0050bf50",
      "READ",
      [
        "storage",
        "002b4dc9",
        null,
        "string"
      ]
    ],
    [
      "0050c0dc",
      "READ",
      [
        "storage",
        "00c9c178",
        null,
        "pointer"
      ]
    ],
    [
      "0050c0e8",
      "DATA",
      [
        "storage",
        "00c6b7e0",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050b9b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050b9b0) · [`0050b9d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050b9d0) · [`0050b9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b92c.md#insn-0050b9e8)
- 新版 [`0050bcd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050bc4c.md#insn-0050bcd0) · [`0050bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050bc4c.md#insn-0050bcf0) · [`0050bd08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050bc4c.md#insn-0050bd08)

~~~diff
- 0050b9b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050b9b0 ["INT_ADD", "register:40f0:8", ["const:50b9b0:8", "const:4:8"]]
- 0050b9b0 ["CALLIND", null, ["register:0:8"]]
+ 0050bcd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050bcd0 ["INT_ADD", "register:40f0:8", ["const:50bcd0:8", "const:4:8"]]
+ 0050bcd0 ["CALLIND", null, ["register:0:8"]]
- 0050b9b0 bytes 20013fd6
+ 0050bcd0 bytes 20013fd6
- 0050b9d0 ["INT_ADD", "register:40f0:8", ["const:50b9d0:8", "const:4:8"]]
- 0050b9d0 ["CALL", null, ["callee:00c54d90:8"]]
+ 0050bcf0 ["INT_ADD", "register:40f0:8", ["const:50bcf0:8", "const:4:8"]]
+ 0050bcf0 ["CALL", null, ["callee:00c54d90:8"]]
- 0050b9d0 bytes f4201d94
+ 0050bcf0 bytes 28241d94
- 0050b9e8 ["INT_ADD", "register:40f0:8", ["const:50b9e8:8", "const:4:8"]]
- 0050b9e8 ["CALL", null, ["callee:00c54d90:8"]]
+ 0050bd08 ["INT_ADD", "register:40f0:8", ["const:50bd08:8", "const:4:8"]]
+ 0050bd08 ["CALL", null, ["callee:00c54d90:8"]]
- 0050b9e8 bytes ee201d94
+ 0050bd08 bytes 22241d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7557cab41ba19cdcb14a8080ade0369e"></a>

### [`0050bf04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md) → [`0050c224`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c224.md) _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d00.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5acd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5acd0.md) · 呼出先 7件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050c29c",
      "incomplete_value": false,
      "site": "0050c2a4",
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
            "const:239:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bf7c",
      "incomplete_value": false,
      "site": "0050bf84",
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
            "const:1ef:8"
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
      "definition_site": "0050c2d8",
      "incomplete_value": true,
      "site": "0050c2e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050bfb8",
      "incomplete_value": true,
      "site": "0050bfc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e68:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050c2d4",
      "incomplete_value": false,
      "site": "0050c2e4",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0050bfb4",
      "incomplete_value": false,
      "site": "0050bfc4",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0050c29c",
      "PARAM",
      [
        "storage",
        "002c11ef",
        null,
        "string"
      ]
    ],
    [
      "0050c2d4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050c2d8",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050c29c",
      "PARAM",
      [
        "storage",
        "002c1239",
        null,
        "string"
      ]
    ],
    [
      "0050c2d4",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0050c2d8",
      "READ",
      [
        "storage",
        "00c9be38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050bf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bf84) · [`0050bfc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bfc4) · [`0050bf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050bf04.md#insn-0050bf28)
- 新版 [`0050c2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c224.md#insn-0050c2a4) · [`0050c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c224.md#insn-0050c2e4) · [`0050c248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c224.md#insn-0050c248)

~~~diff
- 0050bf84 ["INT_ADD", "register:40f0:8", ["const:50bf84:8", "const:4:8"]]
- 0050bf84 ["CALL", null, ["callee:0043e138:8"]]
+ 0050c2a4 ["INT_ADD", "register:40f0:8", ["const:50c2a4:8", "const:4:8"]]
+ 0050c2a4 ["CALL", null, ["callee:0043e138:8"]]
- 0050bf84 bytes a5c7fc97
+ 0050c2a4 bytes a5c7fc97
- 0050bfc4 ["INT_ADD", "register:40f0:8", ["const:50bfc4:8", "const:4:8"]]
- 0050bfc4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050c2e4 ["INT_ADD", "register:40f0:8", ["const:50c2e4:8", "const:4:8"]]
+ 0050c2e4 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050bfc4 bytes 07301d94
+ 0050c2e4 bytes 33331d94
- 0050bf28 ["INT_ADD", "register:40f0:8", ["const:50bf28:8", "const:4:8"]]
- 0050bf28 ["CALL", null, ["callee:00c5aa90:8"]]
+ 0050c248 ["INT_ADD", "register:40f0:8", ["const:50c248:8", "const:4:8"]]
+ 0050c248 ["CALL", null, ["callee:00c5aa90:8"]]
- 0050bf28 bytes e6361d94
+ 0050c248 bytes 123a1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6af3acf6716cc822ed1da69fa30fb94"></a>

### [`0050c178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md) → [`0050c498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c498.md) _ZNK5Botan4OCSP8Response10status_forERKNS_16X509_CertificateES4_NSt6__ndk16chrono10time_pointINS6_12system_clockENS6_8durationIxNS5_5ratioIL

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d20.md) · 呼出先 4件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) [`00c59b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b40.md) [`00c59d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d30.md)
- 新版 呼出元 1件 [`00c5acf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5acf0.md) · 呼出先 4件 [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59a80.md) [`00c5ab10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab10.md) [`00c5ad00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad00.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050c558",
      "incomplete_value": true,
      "site": "0050c560",
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
      "definition_site": "0050c238",
      "incomplete_value": true,
      "site": "0050c240",
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
      "0050c54c",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "0050c560",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c59c",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050c54c",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ],
    [
      "0050c560",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050c59c",
      "DATA",
      [
        "storage",
        "00c67418",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c1c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c1c0) · [`0050c208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c208) · [`0050c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c178.md#insn-0050c220)
- 新版 [`0050c4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c498.md#insn-0050c4e0) · [`0050c528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c498.md#insn-0050c528) · [`0050c540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050c498.md#insn-0050c540)

~~~diff
- 0050c1c0 ["INT_ADD", "register:40f0:8", ["const:50c1c0:8", "const:4:8"]]
- 0050c1c0 ["CALL", null, ["callee:00c5ad00:8"]]
+ 0050c4e0 ["INT_ADD", "register:40f0:8", ["const:50c4e0:8", "const:4:8"]]
+ 0050c4e0 ["CALL", null, ["callee:00c5ad00:8"]]
- 0050c1c0 bytes dc361d94
+ 0050c4e0 bytes 083a1d94
- 0050c208 ["INT_ADD", "register:40f0:8", ["const:50c208:8", "const:4:8"]]
- 0050c208 ["CALL", null, ["callee:00c5ab10:8"]]
+ 0050c528 ["INT_ADD", "register:40f0:8", ["const:50c528:8", "const:4:8"]]
+ 0050c528 ["CALL", null, ["callee:00c5ab10:8"]]
- 0050c208 bytes 4e361d94
+ 0050c528 bytes 7a391d94
- 0050c220 ["COPY", "register:4098:8", ["const:c9a000:8"]]
+ 0050c540 ["COPY", "register:4098:8", ["const:c9b000:8"]]
- 0050c220 bytes 733c00d0
+ 0050c540 bytes 733c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1049a17e9ea03adc4747ae5813d48109"></a>

### [`0050c6f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md) → [`0050ca18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050ca18.md) _ZN5Botan4OCSP6CertIDC2ERKNS_16X509_CertificateERKNS_6BigIntE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c70.md) · 呼出先 14件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`0054371c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/0054371c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`00c5ac40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac40.md) · 呼出先 14件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`004b3868`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004b3/004b3868.md) [`00543a3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00543/00543a3c.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ca64",
      "incomplete_value": true,
      "site": "0050ca70",
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
      "definition_site": "0050c744",
      "incomplete_value": true,
      "site": "0050c750",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050ca74",
      "incomplete_value": true,
      "site": "0050ca74",
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
      "definition_site": "0050c754",
      "incomplete_value": true,
      "site": "0050c754",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050cca8",
      "incomplete_value": true,
      "site": "0050cca8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050c988",
      "incomplete_value": true,
      "site": "0050c988",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050ca54",
      "READ",
      [
        "storage",
        "00c9b238",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca58",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca70",
      "DATA",
      [
        "storage",
        "00c678e8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050ca54",
      "READ",
      [
        "storage",
        "00c9c208",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca58",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050ca70",
      "DATA",
      [
        "storage",
        "00c688b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050c988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050c988) · [`0050ca70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050ca70) · [`0050c71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050c6f8.md#insn-0050c71c)
- 新版 [`0050cca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050ca18.md#insn-0050cca8) · [`0050cd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050ca18.md#insn-0050cd90) · [`0050ca3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050c/0050ca18.md#insn-0050ca3c)

~~~diff
- 0050c988 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050c988 ["INT_ADD", "register:40f0:8", ["const:50c988:8", "const:4:8"]]
- 0050c988 ["CALLIND", null, ["register:0:8"]]
+ 0050cca8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050cca8 ["INT_ADD", "register:40f0:8", ["const:50cca8:8", "const:4:8"]]
+ 0050cca8 ["CALLIND", null, ["register:0:8"]]
- 0050c988 bytes 20013fd6
+ 0050cca8 bytes 20013fd6
- 0050ca70 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050ca70 ["INT_ADD", "register:40f0:8", ["const:50ca70:8", "const:4:8"]]
- 0050ca70 ["CALLIND", null, ["register:0:8"]]
+ 0050cd90 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050cd90 ["INT_ADD", "register:40f0:8", ["const:50cd90:8", "const:4:8"]]
+ 0050cd90 ["CALLIND", null, ["register:0:8"]]
- 0050ca70 bytes 20013fd6
+ 0050cd90 bytes 20013fd6
- 0050c71c ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 0050ca3c ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 0050c71c bytes 693c00f0
+ 0050ca3c bytes 893c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b4f72f9fa729da4a4e84352c49182a5"></a>

### [`0050ce0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md) → [`0050d12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d12c.md) _ZNK5Botan4OCSP14SingleResponse11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 77.50% / 新版 77.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d16c",
      "incomplete_value": true,
      "site": "0050d180",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:201:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce4c",
      "incomplete_value": true,
      "site": "0050ce60",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:1b7:8"
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
      "definition_site": "0050d170",
      "incomplete_value": true,
      "site": "0050d184",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce50",
      "incomplete_value": true,
      "site": "0050ce64",
      "value": [
        "LOAD",
        "16",
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
                "const:b:8"
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
      "definition_site": "0050d174",
      "incomplete_value": true,
      "site": "0050d188",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:710:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ce54",
      "incomplete_value": true,
      "site": "0050ce68",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c0:8"
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
      "0050d16c",
      "READ",
      [
        "storage",
        "002c11b7",
        null,
        "string"
      ]
    ],
    [
      "0050d170",
      "READ",
      [
        "storage",
        "002c11c2",
        null,
        "string"
      ]
    ],
    [
      "0050d174",
      "READ",
      [
        "storage",
        "002c26c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d16c",
      "READ",
      [
        "storage",
        "002c1201",
        null,
        "string"
      ]
    ],
    [
      "0050d170",
      "READ",
      [
        "storage",
        "002c120c",
        null,
        "string"
      ]
    ],
    [
      "0050d174",
      "READ",
      [
        "storage",
        "002c2710",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050cea4) · [`0050ce30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050ce30) · [`0050ce3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050ce0c.md#insn-0050ce3c)
- 新版 [`0050d1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d12c.md#insn-0050d1c4) · [`0050d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d12c.md#insn-0050d150) · [`0050d15c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d12c.md#insn-0050d15c)

~~~diff
- 0050cea4 ["INT_ADD", "register:40f0:8", ["const:50cea4:8", "const:4:8"]]
- 0050cea4 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050d1c4 ["INT_ADD", "register:40f0:8", ["const:50d1c4:8", "const:4:8"]]
+ 0050d1c4 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050cea4 bytes 4f2c1d94
+ 0050d1c4 bytes 7b2f1d94
- 0050ce30 ["INT_ADD", "register:40f0:8", ["const:50ce30:8", "const:4:8"]]
- 0050ce30 ["CALL", null, ["callee:00c58f90:8"]]
+ 0050d150 ["INT_ADD", "register:40f0:8", ["const:50d150:8", "const:4:8"]]
+ 0050d150 ["CALL", null, ["callee:00c58f90:8"]]
- 0050ce30 bytes 642c1d94
+ 0050d150 bytes 902f1d94
- 0050ce3c ["INT_ADD", "register:40f0:8", ["const:50ce3c:8", "const:4:8"]]
- 0050ce3c ["CALL", null, ["callee:00c58f30:8"]]
+ 0050d15c ["INT_ADD", "register:40f0:8", ["const:50d15c:8", "const:4:8"]]
+ 0050d15c ["CALL", null, ["callee:00c58f30:8"]]
- 0050ce3c bytes 492c1d94
+ 0050d15c bytes 752f1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eec3fe1583a83344b5799a12b0d1df42"></a>

### [`0050cef4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md) → [`0050d214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d214.md) _ZN5Botan4OCSP14SingleResponse11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0050aeb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050a/0050aeb8.md) · 呼出先 10件 [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md)
- 新版 呼出元 1件 [`0050b1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b1d8.md) · 呼出先 10件 [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c597a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c597a0.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.97% / 新版 94.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件, `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d25c",
      "incomplete_value": true,
      "site": "0050d25c",
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
      "definition_site": "0050cf3c",
      "incomplete_value": true,
      "site": "0050cf3c",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d2e4",
      "incomplete_value": true,
      "site": "0050d2e4",
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
      "definition_site": "0050cfc4",
      "incomplete_value": true,
      "site": "0050cfc4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d3cc",
      "incomplete_value": true,
      "site": "0050d3cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d0ac",
      "incomplete_value": true,
      "site": "0050d0ac",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c8:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050d248",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d25c",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050d2d4",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d248",
      "READ",
      [
        "storage",
        "00c9c1b0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d25c",
      "DATA",
      [
        "storage",
        "00c69960",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050d2d4",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d0ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050d0ac) · [`0050d134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050d134) · [`0050cf14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050c/0050cef4.md#insn-0050cf14)
- 新版 [`0050d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d214.md#insn-0050d3cc) · [`0050d454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d214.md#insn-0050d454) · [`0050d234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d214.md#insn-0050d234)

~~~diff
- 0050d0ac ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d0ac ["INT_ADD", "register:40f0:8", ["const:50d0ac:8", "const:4:8"]]
- 0050d0ac ["CALLIND", null, ["register:0:8"]]
+ 0050d3cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d3cc ["INT_ADD", "register:40f0:8", ["const:50d3cc:8", "const:4:8"]]
+ 0050d3cc ["CALLIND", null, ["register:0:8"]]
- 0050d0ac bytes 20013fd6
+ 0050d3cc bytes 20013fd6
- 0050d134 ["COPY", "register:0:8", ["register:4040:8"]]
- 0050d134 ["INT_ADD", "register:40f0:8", ["const:50d134:8", "const:4:8"]]
- 0050d134 ["CALLIND", null, ["register:0:8"]]
+ 0050d454 ["COPY", "register:0:8", ["register:4040:8"]]
+ 0050d454 ["INT_ADD", "register:40f0:8", ["const:50d454:8", "const:4:8"]]
+ 0050d454 ["CALLIND", null, ["register:0:8"]]
- 0050d134 bytes 00013fd6
+ 0050d454 bytes 00013fd6
- 0050cf14 ["COPY", "register:40a0:8", ["const:c9b000:8"]]
+ 0050d234 ["COPY", "register:40a0:8", ["const:c9c000:8"]]
- 0050cf14 bytes 743c00f0
+ 0050d234 bytes 743c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a6145a7be4f9290c3c678be98bdeb49"></a>

### [`0050d384`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d384.md) → [`0050d6a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d6a4.md) _ZNK5Botan14PKCS10_Request9PEM_labelEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
      "definition_site": "0050d6b0",
      "incomplete_value": true,
      "site": "0050d6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:69:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d390",
      "incomplete_value": true,
      "site": "0050d3a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:29:8"
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
      "0050d6b0",
      "READ",
      [
        "storage",
        "0029f029",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0050d6b0",
      "READ",
      [
        "storage",
        "0029f069",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d384.md#insn-0050d388)
- 新版 [`0050d6a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d6a4.md#insn-0050d6a8)

~~~diff
- 0050d388 ["COPY", "tmp:0:8", ["const:29:8"]]
- 0050d388 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0050d388 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0050d388 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0050d6a8 ["COPY", "tmp:0:8", ["const:69:8"]]
+ 0050d6a8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d6a8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0050d6a8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0050d388 bytes 4aa50091
+ 0050d6a8 bytes 4aa50191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2de9fe89aec69f613f52c475f9a2bb4"></a>

### [`0050d3b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md) → [`0050d6d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d6d0.md) _ZNK5Botan14PKCS10_Request20alternate_PEM_labelsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00473580`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00473/00473580.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`004738a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00473/004738a0.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d704",
      "incomplete_value": true,
      "site": "0050d714",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:a5e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d3e4",
      "incomplete_value": true,
      "site": "0050d3f4",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2bd000:8"
              ],
              [
                "leaf",
                "const:980:8"
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
      "definition_site": "0050d718",
      "incomplete_value": true,
      "site": "0050d718",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050d3f8",
      "incomplete_value": true,
      "site": "0050d3f8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d70c",
      "incomplete_value": true,
      "site": "0050d71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d3ec",
      "incomplete_value": true,
      "site": "0050d3fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
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
      "0050d704",
      "READ",
      [
        "storage",
        "002bd980",
        null,
        "string"
      ]
    ],
    [
      "0050d708",
      "READ",
      [
        "storage",
        "002bd98f",
        null,
        "string"
      ]
    ],
    [
      "0050d70c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050d704",
      "READ",
      [
        "storage",
        "002bda5e",
        null,
        "string"
      ]
    ],
    [
      "0050d708",
      "READ",
      [
        "storage",
        "002bda6d",
        null,
        "string"
      ]
    ],
    [
      "0050d70c",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md#insn-0050d3d4) · [`0050d3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md#insn-0050d3dc) · [`0050d3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d3b0.md#insn-0050d3e0)
- 新版 [`0050d6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d6d0.md#insn-0050d6f4) · [`0050d6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d6d0.md#insn-0050d6fc)

~~~diff
- 0050d3d4 ["INT_ADD", "register:40f0:8", ["const:50d3d4:8", "const:4:8"]]
- 0050d3d4 ["CALL", null, ["callee:00c58f30:8"]]
+ 0050d6f4 ["INT_ADD", "register:40f0:8", ["const:50d6f4:8", "const:4:8"]]
+ 0050d6f4 ["CALL", null, ["callee:00c58f30:8"]]
- 0050d3d4 bytes e32a1d94
+ 0050d6f4 bytes 0f2e1d94
- 0050d3dc ["COPY", "tmp:0:8", ["const:980:8"]]
- 0050d3dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050d3dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050d3dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050d6fc ["COPY", "tmp:0:8", ["const:a5e:8"]]
+ 0050d6fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d6fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050d6fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050d3dc bytes 08012691
+ 0050d6fc bytes 08792991
- 0050d3e0 ["COPY", "register:4048:8", ["const:2c2000:8"]]
- 0050d3e0 bytes a9edffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3cdaeb7055919558524373afa796f6b"></a>

### [`0050d474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md) → [`0050d794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d794.md) _ZN5Botan14PKCS10_RequestC2ERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d7d4",
      "incomplete_value": true,
      "site": "0050d7d4",
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
      "definition_site": "0050d4b4",
      "incomplete_value": true,
      "site": "0050d4b4",
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
      "definition_site": "0050d7d4",
      "incomplete_value": true,
      "site": "0050d7d4",
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
      "definition_site": "0050d4b4",
      "incomplete_value": true,
      "site": "0050d4b4",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050d814",
      "incomplete_value": true,
      "site": "0050d81c",
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
      "definition_site": "0050d4f4",
      "incomplete_value": true,
      "site": "0050d4fc",
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
      "0050d7b4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7bc",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7d4",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050d7b4",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7bc",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050d7d4",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d48c) · [`0050d490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d490) · [`0050d494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d474.md#insn-0050d494)
- 新版 [`0050d7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d794.md#insn-0050d7ac) · [`0050d7b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d794.md#insn-0050d7b0) · [`0050d7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d794.md#insn-0050d7b4)

~~~diff
- 0050d48c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0050d7ac ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0050d48c bytes 683c00d0
+ 0050d7ac bytes 683c00f0
- 0050d490 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0050d7b0 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0050d490 bytes 6a3c00b0
+ 0050d7b0 bytes 6a3c00d0
- 0050d494 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 0050d494 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050d7b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 0050d7b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050d494 bytes 081541f9
+ 0050d7b4 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dca6928aa4835bc41407dc57b29e16b0"></a>

### [`0050d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md) → [`0050d898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d898.md) _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md) · 呼出先 18件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`004a6fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6fdc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md)
- 新版 呼出元 1件 [`00c5ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad20.md) · 呼出先 18件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0045001c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00450/0045001c.md) [`004a72fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a7/004a72fc.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00540604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540604.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050d930",
      "incomplete_value": true,
      "site": "0050d930",
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
      "definition_site": "0050d610",
      "incomplete_value": true,
      "site": "0050d610",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050d96c",
      "incomplete_value": true,
      "site": "0050d96c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d64c",
      "incomplete_value": true,
      "site": "0050d64c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0050da44",
      "incomplete_value": true,
      "site": "0050da44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050d724",
      "incomplete_value": true,
      "site": "0050d724",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050d920",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050d930",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d95c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050d920",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "0050d930",
      "DATA",
      [
        "storage",
        "00c68428",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050d95c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050d5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d5fc) · [`0050d628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d628) · [`0050d64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md#insn-0050d64c)
- 新版 [`0050d91c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d898.md#insn-0050d91c) · [`0050d948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d898.md#insn-0050d948) · [`0050d96c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050d/0050d898.md#insn-0050d96c)

~~~diff
- 0050d5fc ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050d91c ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050d5fc bytes 683c00b0
+ 0050d91c bytes 683c00d0
- 0050d628 ["COPY", "register:40a8:8", ["const:c67000:8"]]
+ 0050d948 ["COPY", "register:40a8:8", ["const:c68000:8"]]
- 0050d628 bytes d53a00d0
+ 0050d948 bytes d53a00f0
- 0050d64c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050d64c ["INT_ADD", "register:40f0:8", ["const:50d64c:8", "const:4:8"]]
- 0050d64c ["CALLIND", null, ["register:0:8"]]
+ 0050d96c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050d96c ["INT_ADD", "register:40f0:8", ["const:50d96c:8", "const:4:8"]]
+ 0050d96c ["CALLIND", null, ["register:0:8"]]
- 0050d64c bytes 20013fd6
+ 0050d96c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0a076a22d356235e082cd8f088b7d03"></a>

### [`0050dde0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md) → [`0050e100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e100.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5a040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a040.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00c5b010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5b010.md) · 呼出先 7件 [`00540728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e140",
      "incomplete_value": true,
      "site": "0050e140",
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
      "definition_site": "0050de20",
      "incomplete_value": true,
      "site": "0050de20",
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
      "definition_site": "0050e140",
      "incomplete_value": true,
      "site": "0050e140",
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
      "definition_site": "0050de20",
      "incomplete_value": true,
      "site": "0050de20",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e188",
      "incomplete_value": true,
      "site": "0050e194",
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
      "definition_site": "0050de68",
      "incomplete_value": true,
      "site": "0050de74",
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
      "0050e120",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050e128",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050e140",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050e120",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e128",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e140",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050decc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050decc) · [`0050ddf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050ddf8) · [`0050ddfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050dde0.md#insn-0050ddfc)
- 新版 [`0050e1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e100.md#insn-0050e1ec) · [`0050e118`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e100.md#insn-0050e118) · [`0050e11c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e100.md#insn-0050e11c)

~~~diff
- 0050decc ["COPY", "register:0:8", ["register:4048:8"]]
- 0050decc ["INT_ADD", "register:40f0:8", ["const:50decc:8", "const:4:8"]]
- 0050decc ["CALLIND", null, ["register:0:8"]]
+ 0050e1ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050e1ec ["INT_ADD", "register:40f0:8", ["const:50e1ec:8", "const:4:8"]]
+ 0050e1ec ["CALLIND", null, ["register:0:8"]]
- 0050decc bytes 20013fd6
+ 0050e1ec bytes 20013fd6
- 0050ddf8 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0050e118 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0050ddf8 bytes 683c00d0
+ 0050e118 bytes 683c00d0
- 0050ddfc ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0050e11c ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0050ddfc bytes 6a3c00b0
+ 0050e11c bytes 6a3c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b607fa1a6b5fae8c60c799e4c1eb3d79"></a>

### [`0050df58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md) → [`0050e278`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e278.md) _ZN5Botan14PKCS10_RequestC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a700.md) [`00c5a710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a710.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e2b8",
      "incomplete_value": true,
      "site": "0050e2b8",
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
      "definition_site": "0050df98",
      "incomplete_value": true,
      "site": "0050df98",
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
      "definition_site": "0050e2b8",
      "incomplete_value": true,
      "site": "0050e2b8",
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
      "definition_site": "0050df98",
      "incomplete_value": true,
      "site": "0050df98",
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
    "kind": "store_value",
    "new": {
      "definition_site": "0050e2f8",
      "incomplete_value": true,
      "site": "0050e300",
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
      "definition_site": "0050dfd8",
      "incomplete_value": true,
      "site": "0050dfe0",
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
      "0050e298",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "0050e2a0",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050e2b8",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "0050e298",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e2a0",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e2b8",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050df70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050df70) · [`0050df74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050df74) · [`0050df78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050df58.md#insn-0050df78)
- 新版 [`0050e290`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e278.md#insn-0050e290) · [`0050e294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e278.md#insn-0050e294) · [`0050e298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e278.md#insn-0050e298)

~~~diff
- 0050df70 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0050e290 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0050df70 bytes 683c00d0
+ 0050e290 bytes 683c00d0
- 0050df74 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 0050e294 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0050df74 bytes 6a3c00b0
+ 0050e294 bytes 6a3c00b0
- 0050df78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 0050df78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0050e298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 0050e298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0050df78 bytes 081541f9
+ 0050e298 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60d1cec5796695486d1a1a6ddce79c93"></a>

### [`0050e084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) → [`0050e3a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md) _ZN5Botan14PKCS10_Request12force_decodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 40件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`004a5fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) [`004a6c5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6c5c.md)
- 新版 呼出元 0件  · 呼出先 40件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`004a6300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6300.md) [`004a6f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a6/004a6f7c.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.45% / 新版 96.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 4件, `call_target` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e57c",
      "incomplete_value": true,
      "site": "0050e59c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e25c",
      "incomplete_value": true,
      "site": "0050e27c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e814",
      "incomplete_value": true,
      "site": "0050e824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050e4f4",
      "incomplete_value": true,
      "site": "0050e504",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ffd:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 58,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050e828",
      "incomplete_value": true,
      "site": "0050e828",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050e508",
      "incomplete_value": true,
      "site": "0050e508",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0050e570",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      "0050e57c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ],
    [
      "0050e5c4",
      "DATA",
      [
        "storage",
        "00c662a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0050e570",
      "READ",
      [
        "storage",
        "00c9bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "0050e57c",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ],
    [
      "0050e5c4",
      "DATA",
      [
        "storage",
        "00c67278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050e3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e3ac) · [`0050e3dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e3dc) · [`0050e5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md#insn-0050e5e8)
- 新版 [`0050e6cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md#insn-0050e6cc) · [`0050e6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md#insn-0050e6fc) · [`0050e908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050e/0050e3a4.md#insn-0050e908)

~~~diff
- 0050e3ac ["INT_ADD", "register:40f0:8", ["const:50e3ac:8", "const:4:8"]]
- 0050e3ac ["CALL", null, ["callee:00c58f50:8"]]
+ 0050e6cc ["INT_ADD", "register:40f0:8", ["const:50e6cc:8", "const:4:8"]]
+ 0050e6cc ["CALL", null, ["callee:00c58f50:8"]]
- 0050e3ac bytes f5261d94
+ 0050e6cc bytes 212a1d94
- 0050e3dc ["INT_ADD", "register:40f0:8", ["const:50e3dc:8", "const:4:8"]]
- 0050e3dc ["CALL", null, ["callee:00c58f30:8"]]
+ 0050e6fc ["INT_ADD", "register:40f0:8", ["const:50e6fc:8", "const:4:8"]]
+ 0050e6fc ["CALL", null, ["callee:00c58f30:8"]]
- 0050e3dc bytes e1261d94
+ 0050e6fc bytes 0d2a1d94
- 0050e5e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 0050e5e8 ["INT_ADD", "register:40f0:8", ["const:50e5e8:8", "const:4:8"]]
- 0050e5e8 ["CALLIND", null, ["register:0:8"]]
+ 0050e908 ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050e908 ["INT_ADD", "register:40f0:8", ["const:50e908:8", "const:4:8"]]
+ 0050e908 ["CALLIND", null, ["register:0:8"]]
- 0050e5e8 bytes 20013fd6
+ 0050e908 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd6a4a3a4535b5b94f44b16d3631b4b"></a>

### [`0050edec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md) → [`0050f10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f10c.md) _ZNK5Botan11X509_Object15check_signatureEPKNS_10Public_KeyE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d70.md) · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)
- 新版 呼出元 1件 [`00c5ad40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad40.md) · 呼出先 8件 [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md) [`00c59000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59000.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.89% / 新版 95.89%

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
      "definition_site": "0050f1a0",
      "incomplete_value": false,
      "site": "0050f1ac",
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
            "const:f03:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050ee80",
      "incomplete_value": false,
      "site": "0050ee8c",
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
            "const:e25:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f1cc",
      "incomplete_value": false,
      "site": "0050f1d4",
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
            "const:e5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eeac",
      "incomplete_value": false,
      "site": "0050eeb4",
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
            "const:a5:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f21c",
      "incomplete_value": true,
      "site": "0050f228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050eefc",
      "incomplete_value": true,
      "site": "0050ef08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "0050f1a0",
      "PARAM",
      [
        "storage",
        "002bfe25",
        null,
        "string"
      ]
    ],
    [
      "0050f1cc",
      "PARAM",
      [
        "storage",
        "0029f0a5",
        null,
        "string"
      ]
    ],
    [
      "0050f218",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f1a0",
      "PARAM",
      [
        "storage",
        "002bff03",
        null,
        "string"
      ]
    ],
    [
      "0050f1cc",
      "PARAM",
      [
        "storage",
        "0029f0e5",
        null,
        "string"
      ]
    ],
    [
      "0050f218",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050ee8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050ee8c) · [`0050eeb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050eeb4) · [`0050ef08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050edec.md#insn-0050ef08)
- 新版 [`0050f1ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f10c.md#insn-0050f1ac) · [`0050f1d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f10c.md#insn-0050f1d4) · [`0050f228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f10c.md#insn-0050f228)

~~~diff
- 0050ee8c ["INT_ADD", "register:40f0:8", ["const:50ee8c:8", "const:4:8"]]
- 0050ee8c ["CALL", null, ["callee:00c59000:8"]]
+ 0050f1ac ["INT_ADD", "register:40f0:8", ["const:50f1ac:8", "const:4:8"]]
+ 0050f1ac ["CALL", null, ["callee:00c59000:8"]]
- 0050ee8c bytes 69241d94
+ 0050f1ac bytes 95271d94
- 0050eeb4 ["INT_ADD", "register:40f0:8", ["const:50eeb4:8", "const:4:8"]]
- 0050eeb4 ["CALL", null, ["callee:00c59010:8"]]
+ 0050f1d4 ["INT_ADD", "register:40f0:8", ["const:50f1d4:8", "const:4:8"]]
+ 0050f1d4 ["CALL", null, ["callee:00c59010:8"]]
- 0050eeb4 bytes 63241d94
+ 0050f1d4 bytes 8f271d94
- 0050ef08 ["INT_ADD", "register:40f0:8", ["const:50ef08:8", "const:4:8"]]
- 0050ef08 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050f228 ["INT_ADD", "register:40f0:8", ["const:50f228:8", "const:4:8"]]
+ 0050f228 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050ef08 bytes 36241d94
+ 0050f228 bytes 62271d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0d8417f8901f3e4017085ef6720a47"></a>

### [`0050efcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md) → [`0050f2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f2ec.md) _ZNK5Botan14PKCS10_Request18subject_public_keyEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d60.md) · 呼出先 6件 [`00536d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536d44.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c597a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597a0.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 1件 [`00c5ad30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad30.md) · 呼出先 6件 [`00537064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00537/00537064.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c5a770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a770.md) [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f324",
      "incomplete_value": true,
      "site": "0050f324",
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
      "definition_site": "0050f004",
      "incomplete_value": true,
      "site": "0050f004",
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
    "kind": "call_target",
    "new": {
      "definition_site": "0050f36c",
      "incomplete_value": true,
      "site": "0050f36c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c68000:8"
              ],
              [
                "leaf",
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f04c",
      "incomplete_value": true,
      "site": "0050f04c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c67000:8"
              ],
              [
                "leaf",
                "const:808:8"
              ]
            ]
          ]
        ]
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
      "0050f314",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0050f324",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050f35c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f314",
      "READ",
      [
        "storage",
        "00c9be80",
        null,
        "pointer"
      ]
    ],
    [
      "0050f324",
      "DATA",
      [
        "storage",
        "00c68428",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0050f35c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050f04c) · [`0050efec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050efec) · [`0050eff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050efcc.md#insn-0050eff0)
- 新版 [`0050f36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f2ec.md#insn-0050f36c) · [`0050f30c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f2ec.md#insn-0050f30c) · [`0050f310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f2ec.md#insn-0050f310)

~~~diff
- 0050f04c ["COPY", "register:0:8", ["register:4048:8"]]
- 0050f04c ["INT_ADD", "register:40f0:8", ["const:50f04c:8", "const:4:8"]]
- 0050f04c ["CALLIND", null, ["register:0:8"]]
+ 0050f36c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0050f36c ["INT_ADD", "register:40f0:8", ["const:50f36c:8", "const:4:8"]]
+ 0050f36c ["CALLIND", null, ["register:0:8"]]
- 0050f04c bytes 20013fd6
+ 0050f36c bytes 20013fd6
- 0050efec ["INT_ADD", "register:40f0:8", ["const:50efec:8", "const:4:8"]]
- 0050efec ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f30c ["INT_ADD", "register:40f0:8", ["const:50f30c:8", "const:4:8"]]
+ 0050f30c ["CALL", null, ["callee:00c5ad60:8"]]
- 0050efec bytes 692b1d94
+ 0050f30c bytes 952e1d94
- 0050eff0 ["COPY", "register:4040:8", ["const:c9a000:8"]]
+ 0050f310 ["COPY", "register:4040:8", ["const:c9b000:8"]]
- 0050eff0 bytes 683c0090
+ 0050f310 bytes 683c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46731a2e80609de8ed28445b51d9ed96"></a>

### [`0050f0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md) → [`0050f408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f408.md) _ZNK5Botan14PKCS10_Request4dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)
- 新版 呼出元 1件 [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md) [`00c58fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050f468",
      "incomplete_value": false,
      "site": "0050f470",
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
            "const:1dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f148",
      "incomplete_value": false,
      "site": "0050f150",
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
            "const:19d:8"
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
      "definition_site": "0050f4a4",
      "incomplete_value": true,
      "site": "0050f4b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f184",
      "incomplete_value": true,
      "site": "0050f190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
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
      "definition_site": "0050f4a0",
      "incomplete_value": false,
      "site": "0050f4b0",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0050f180",
      "incomplete_value": false,
      "site": "0050f190",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0050f468",
      "PARAM",
      [
        "storage",
        "002a119d",
        null,
        "string"
      ]
    ],
    [
      "0050f4a0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050f4a4",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f468",
      "PARAM",
      [
        "storage",
        "002a11dd",
        null,
        "string"
      ]
    ],
    [
      "0050f4a0",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0050f4a4",
      "READ",
      [
        "storage",
        "00c9bdf0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f150) · [`0050f190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f190) · [`0050f13c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f0e8.md#insn-0050f13c)
- 新版 [`0050f470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f408.md#insn-0050f470) · [`0050f4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f408.md#insn-0050f4b0) · [`0050f45c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f408.md#insn-0050f45c)

~~~diff
- 0050f150 ["INT_ADD", "register:40f0:8", ["const:50f150:8", "const:4:8"]]
- 0050f150 ["CALL", null, ["callee:0043e138:8"]]
+ 0050f470 ["INT_ADD", "register:40f0:8", ["const:50f470:8", "const:4:8"]]
+ 0050f470 ["CALL", null, ["callee:0043e138:8"]]
- 0050f150 bytes 32bbfc97
+ 0050f470 bytes 32bbfc97
- 0050f190 ["INT_ADD", "register:40f0:8", ["const:50f190:8", "const:4:8"]]
- 0050f190 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050f4b0 ["INT_ADD", "register:40f0:8", ["const:50f4b0:8", "const:4:8"]]
+ 0050f4b0 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050f190 bytes 94231d94
+ 0050f4b0 bytes c0261d94
- 0050f13c ["INT_ADD", "register:40f0:8", ["const:50f13c:8", "const:4:8"]]
- 0050f13c ["CALL", null, ["callee:00c58f90:8"]]
+ 0050f45c ["INT_ADD", "register:40f0:8", ["const:50f45c:8", "const:4:8"]]
+ 0050f45c ["CALL", null, ["callee:00c58f90:8"]]
- 0050f13c bytes a1231d94
+ 0050f45c bytes cd261d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eedaefb49e42a76fdd9afb281f7f3114"></a>

### [`0050f280`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md) → [`0050f5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f5a0.md) _ZNK5Botan14PKCS10_Request11constraintsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59da0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59da0.md) · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md) [`00c59d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d90.md)
- 新版 呼出元 1件 [`00c5ad70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad70.md) · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab60.md) [`00c5ad60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad60.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f5e4",
      "incomplete_value": true,
      "site": "0050f5e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:c56:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f2c4",
      "incomplete_value": true,
      "site": "0050f2c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:b89:8"
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
      "definition_site": "0050f5d8",
      "incomplete_value": true,
      "site": "0050f5e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f2b8",
      "incomplete_value": true,
      "site": "0050f2c8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0050f650",
      "incomplete_value": true,
      "site": "0050f650",
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
                "const:0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f330",
      "incomplete_value": true,
      "site": "0050f330",
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
                "const:0:8"
              ]
            ]
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
      "0050f5d0",
      "READ",
      [
        "storage",
        "002a9b89",
        null,
        "string"
      ]
    ],
    [
      "0050f5d8",
      "READ",
      [
        "storage",
        "002a9b90",
        null,
        "string"
      ]
    ],
    [
      "0050f640",
      "READ",
      [
        "storage",
        "00c9b248",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050f5d0",
      "READ",
      [
        "storage",
        "002a9c56",
        null,
        "string"
      ]
    ],
    [
      "0050f5d8",
      "READ",
      [
        "storage",
        "002a9c5d",
        null,
        "string"
      ]
    ],
    [
      "0050f640",
      "READ",
      [
        "storage",
        "00c9c218",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f2a0) · [`0050f2ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f2ac) · [`0050f2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f280.md#insn-0050f2d4)
- 新版 [`0050f5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f5a0.md#insn-0050f5c0) · [`0050f5cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f5a0.md#insn-0050f5cc) · [`0050f5f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f5a0.md#insn-0050f5f4)

~~~diff
- 0050f2a0 ["INT_ADD", "register:40f0:8", ["const:50f2a0:8", "const:4:8"]]
- 0050f2a0 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f5c0 ["INT_ADD", "register:40f0:8", ["const:50f5c0:8", "const:4:8"]]
+ 0050f5c0 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f2a0 bytes bc2a1d94
+ 0050f5c0 bytes e82d1d94
- 0050f2ac ["COPY", "tmp:0:8", ["const:b89:8"]]
- 0050f2ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0050f2ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0050f2ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0050f5cc ["COPY", "tmp:0:8", ["const:c56:8"]]
+ 0050f5cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f5cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0050f5cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0050f2ac bytes 29252e91
+ 0050f5cc bytes 29593191
- 0050f2d4 ["INT_ADD", "register:40f0:8", ["const:50f2d4:8", "const:4:8"]]
- 0050f2d4 ["CALL", null, ["callee:00c59720:8"]]
+ 0050f5f4 ["INT_ADD", "register:40f0:8", ["const:50f5f4:8", "const:4:8"]]
+ 0050f5f4 ["CALL", null, ["callee:00c59720:8"]]
- 0050f2d4 bytes 1f251d94
+ 0050f5f4 bytes 4b281d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5ceacdeaf11046231db6fbdbbb227e9"></a>

### [`0050f42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md) → [`0050f74c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md) _ZNK5Botan14PKCS10_Request14ex_constraintsEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59dc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59dc0.md) · 呼出先 12件 [`00531bc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531bc4.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 1件 [`00c5ad90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad90.md) · 呼出先 12件 [`00531ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531ee4.md) [`0053f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f1d0.md) [`0053f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md) [`00540a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540a34.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_condition, store_value

命令の説明率　旧版 93.50% / 新版 93.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f794",
      "incomplete_value": true,
      "site": "0050f7a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:283:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f474",
      "incomplete_value": true,
      "site": "0050f484",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1a5:8"
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
      "definition_site": "0050f7a8",
      "incomplete_value": true,
      "site": "0050f7a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f488",
      "incomplete_value": true,
      "site": "0050f488",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f79c",
      "incomplete_value": true,
      "site": "0050f7ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f47c",
      "incomplete_value": true,
      "site": "0050f48c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
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
      "0050f794",
      "READ",
      [
        "storage",
        "002ba1a5",
        null,
        "string"
      ]
    ],
    [
      "0050f798",
      "READ",
      [
        "storage",
        "002ba1b4",
        null,
        "string"
      ]
    ],
    [
      "0050f79c",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f794",
      "READ",
      [
        "storage",
        "002ba283",
        null,
        "string"
      ]
    ],
    [
      "0050f798",
      "READ",
      [
        "storage",
        "002ba292",
        null,
        "string"
      ]
    ],
    [
      "0050f79c",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f458) · [`0050f464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f464) · [`0050f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f42c.md#insn-0050f46c)
- 新版 [`0050f778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md#insn-0050f778) · [`0050f784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md#insn-0050f784) · [`0050f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f74c.md#insn-0050f78c)

~~~diff
- 0050f458 ["INT_ADD", "register:40f0:8", ["const:50f458:8", "const:4:8"]]
- 0050f458 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f778 ["INT_ADD", "register:40f0:8", ["const:50f778:8", "const:4:8"]]
+ 0050f778 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f458 bytes 4e2a1d94
+ 0050f778 bytes 7a2d1d94
- 0050f464 ["INT_ADD", "register:40f0:8", ["const:50f464:8", "const:4:8"]]
- 0050f464 ["CALL", null, ["callee:00c58f30:8"]]
+ 0050f784 ["INT_ADD", "register:40f0:8", ["const:50f784:8", "const:4:8"]]
+ 0050f784 ["CALL", null, ["callee:00c58f30:8"]]
- 0050f464 bytes bf221d94
+ 0050f784 bytes eb251d94
- 0050f46c ["COPY", "tmp:0:8", ["const:1a5:8"]]
- 0050f46c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050f46c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050f46c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050f78c ["COPY", "tmp:0:8", ["const:283:8"]]
+ 0050f78c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f78c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f78c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050f46c bytes 08950691
+ 0050f78c bytes 080d0a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dffbf4b74f0a5569c27308a5033a68e"></a>

### [`0050f654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md) → [`0050f974`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f974.md) _ZNK5Botan14PKCS10_Request5is_CAEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59dd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59dd0.md) · 呼出先 7件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md)
- 新版 呼出元 1件 [`00c5ada0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ada0.md) · 呼出先 7件 [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab60.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.33% / 新版 89.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f9b0",
      "incomplete_value": true,
      "site": "0050f9c0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:b1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f690",
      "incomplete_value": true,
      "site": "0050f6a0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:67:8"
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
      "definition_site": "0050f9c4",
      "incomplete_value": true,
      "site": "0050f9c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f6a4",
      "incomplete_value": true,
      "site": "0050f6a4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050f9b8",
      "incomplete_value": true,
      "site": "0050f9c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f698",
      "incomplete_value": true,
      "site": "0050f6a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
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
      "0050f9b0",
      "READ",
      [
        "storage",
        "002c1067",
        null,
        "string"
      ]
    ],
    [
      "0050f9b4",
      "READ",
      [
        "storage",
        "002c1076",
        null,
        "string"
      ]
    ],
    [
      "0050f9b8",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050f9b0",
      "READ",
      [
        "storage",
        "002c10b1",
        null,
        "string"
      ]
    ],
    [
      "0050f9b4",
      "READ",
      [
        "storage",
        "002c10c0",
        null,
        "string"
      ]
    ],
    [
      "0050f9b8",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f674) · [`0050f680`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f680) · [`0050f688`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f654.md#insn-0050f688)
- 新版 [`0050f994`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f974.md#insn-0050f994) · [`0050f9a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f974.md#insn-0050f9a0) · [`0050f9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050f974.md#insn-0050f9a8)

~~~diff
- 0050f674 ["INT_ADD", "register:40f0:8", ["const:50f674:8", "const:4:8"]]
- 0050f674 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050f994 ["INT_ADD", "register:40f0:8", ["const:50f994:8", "const:4:8"]]
+ 0050f994 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f674 bytes c7291d94
+ 0050f994 bytes f32c1d94
- 0050f680 ["INT_ADD", "register:40f0:8", ["const:50f680:8", "const:4:8"]]
- 0050f680 ["CALL", null, ["callee:00c58f30:8"]]
+ 0050f9a0 ["INT_ADD", "register:40f0:8", ["const:50f9a0:8", "const:4:8"]]
+ 0050f9a0 ["CALL", null, ["callee:00c58f30:8"]]
- 0050f680 bytes 38221d94
+ 0050f9a0 bytes 64251d94
- 0050f688 ["COPY", "tmp:0:8", ["const:67:8"]]
- 0050f688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050f688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050f688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050f9a8 ["COPY", "tmp:0:8", ["const:b1:8"]]
+ 0050f9a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f9a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050f9a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050f688 bytes 089d0191
+ 0050f9a8 bytes 08c50291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8a3014ebaa2b4942bc049fd2134daa4"></a>

### [`0050f7e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md) → [`0050fb00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fb00.md) _ZNK5Botan14PKCS10_Request10path_limitEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59de0.md) · 呼出先 9件 [`00531028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00531/00531028.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)
- 新版 呼出元 1件 [`00c5adb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5adb0.md) · 呼出先 9件 [`00531348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00531/00531348.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.24% / 新版 90.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fb3c",
      "incomplete_value": true,
      "site": "0050fb4c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:b1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f81c",
      "incomplete_value": true,
      "site": "0050f82c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2c1000:8"
              ],
              [
                "leaf",
                "const:67:8"
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
      "definition_site": "0050fb50",
      "incomplete_value": true,
      "site": "0050fb50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0050f830",
      "incomplete_value": true,
      "site": "0050f830",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fb44",
      "incomplete_value": true,
      "site": "0050fb54",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f824",
      "incomplete_value": true,
      "site": "0050f834",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:490:8"
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
      "0050fb3c",
      "READ",
      [
        "storage",
        "002c1067",
        null,
        "string"
      ]
    ],
    [
      "0050fb40",
      "READ",
      [
        "storage",
        "002c1076",
        null,
        "string"
      ]
    ],
    [
      "0050fb44",
      "READ",
      [
        "storage",
        "002c2490",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0050fb3c",
      "READ",
      [
        "storage",
        "002c10b1",
        null,
        "string"
      ]
    ],
    [
      "0050fb40",
      "READ",
      [
        "storage",
        "002c10c0",
        null,
        "string"
      ]
    ],
    [
      "0050fb44",
      "READ",
      [
        "storage",
        "002c24e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f800) · [`0050f80c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f80c) · [`0050f814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f7e0.md#insn-0050f814)
- 新版 [`0050fb20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fb00.md#insn-0050fb20) · [`0050fb2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fb00.md#insn-0050fb2c) · [`0050fb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fb00.md#insn-0050fb34)

~~~diff
- 0050f800 ["INT_ADD", "register:40f0:8", ["const:50f800:8", "const:4:8"]]
- 0050f800 ["CALL", null, ["callee:00c5ad60:8"]]
+ 0050fb20 ["INT_ADD", "register:40f0:8", ["const:50fb20:8", "const:4:8"]]
+ 0050fb20 ["CALL", null, ["callee:00c5ad60:8"]]
- 0050f800 bytes 64291d94
+ 0050fb20 bytes 902c1d94
- 0050f80c ["INT_ADD", "register:40f0:8", ["const:50f80c:8", "const:4:8"]]
- 0050f80c ["CALL", null, ["callee:00c58f30:8"]]
+ 0050fb2c ["INT_ADD", "register:40f0:8", ["const:50fb2c:8", "const:4:8"]]
+ 0050fb2c ["CALL", null, ["callee:00c58f30:8"]]
- 0050f80c bytes d5211d94
+ 0050fb2c bytes 01251d94
- 0050f814 ["COPY", "tmp:0:8", ["const:67:8"]]
- 0050f814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0050f814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0050f814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0050fb34 ["COPY", "tmp:0:8", ["const:b1:8"]]
+ 0050fb34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0050fb34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0050fb34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0050f814 bytes 089d0191
+ 0050fb34 bytes 08c50291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fc46b7bc3b34553dab758c684d88d3b"></a>

### [`0050f988`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md) → [`0050fca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fca8.md) _ZNK5Botan14Cert_Extension17Basic_Constraints14get_path_limitEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59df0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5adc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5adc0.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050fd0c",
      "incomplete_value": false,
      "site": "0050fd14",
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
            "const:c5b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050f9ec",
      "incomplete_value": false,
      "site": "0050f9f4",
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
            "const:c11:8"
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
      "definition_site": "0050fd48",
      "incomplete_value": true,
      "site": "0050fd54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fa28",
      "incomplete_value": true,
      "site": "0050fa34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "0050fd44",
      "incomplete_value": false,
      "site": "0050fd54",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "0050fa24",
      "incomplete_value": false,
      "site": "0050fa34",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "0050fd0c",
      "PARAM",
      [
        "storage",
        "002b2c11",
        null,
        "string"
      ]
    ],
    [
      "0050fd44",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0050fd48",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050fd0c",
      "PARAM",
      [
        "storage",
        "002b2c5b",
        null,
        "string"
      ]
    ],
    [
      "0050fd44",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0050fd48",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050f9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050f9f4) · [`0050fa34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050fa34) · [`0050f9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050f988.md#insn-0050f9e0)
- 新版 [`0050fd14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fca8.md#insn-0050fd14) · [`0050fd54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fca8.md#insn-0050fd54) · [`0050fd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fca8.md#insn-0050fd00)

~~~diff
- 0050f9f4 ["INT_ADD", "register:40f0:8", ["const:50f9f4:8", "const:4:8"]]
- 0050f9f4 ["CALL", null, ["callee:0043e138:8"]]
+ 0050fd14 ["INT_ADD", "register:40f0:8", ["const:50fd14:8", "const:4:8"]]
+ 0050fd14 ["CALL", null, ["callee:0043e138:8"]]
- 0050f9f4 bytes 09b9fc97
+ 0050fd14 bytes 09b9fc97
- 0050fa34 ["INT_ADD", "register:40f0:8", ["const:50fa34:8", "const:4:8"]]
- 0050fa34 ["CALL", null, ["callee:00c58fb0:8"]]
+ 0050fd54 ["INT_ADD", "register:40f0:8", ["const:50fd54:8", "const:4:8"]]
+ 0050fd54 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050fa34 bytes 6b211d94
+ 0050fd54 bytes 97241d94
- 0050f9e0 ["INT_ADD", "register:40f0:8", ["const:50f9e0:8", "const:4:8"]]
- 0050f9e0 ["CALL", null, ["callee:00c58f90:8"]]
+ 0050fd00 ["INT_ADD", "register:40f0:8", ["const:50fd00:8", "const:4:8"]]
+ 0050fd00 ["CALL", null, ["callee:00c58f90:8"]]
- 0050f9e0 bytes 78211d94
+ 0050fd00 bytes a4241d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618072b015b4b2ba2fcba997d88505a3"></a>

### [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) → [`0050fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md) _ZN5Botan7X509_CAC2ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk112basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEEERNS_21Ra

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`0050ff68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050ff68.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00510288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510288.md) [`005103c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.38% / 新版 97.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fdf0",
      "incomplete_value": true,
      "site": "0050fdf0",
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
      "definition_site": "0050fad0",
      "incomplete_value": true,
      "site": "0050fad0",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0050fe2c",
      "incomplete_value": true,
      "site": "0050fe30",
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
      "definition_site": "0050fb0c",
      "incomplete_value": true,
      "site": "0050fb10",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0050ff48",
      "incomplete_value": false,
      "site": "0050ff54",
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
            "const:d07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0050fc28",
      "incomplete_value": false,
      "site": "0050fc34",
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
            "const:c30:8"
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
      "0050fdd4",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "0050fdf0",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fe28",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0050fdd4",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "0050fdf0",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0050fe28",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0050fc34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fc34) · [`0050fdd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fdd8) · [`0050fe14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md#insn-0050fe14)
- 新版 [`0050ff54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md#insn-0050ff54) · [`005100f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md#insn-005100f8) · [`00510134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md#insn-00510134)

~~~diff
- 0050fc34 ["INT_ADD", "register:40f0:8", ["const:50fc34:8", "const:4:8"]]
- 0050fc34 ["CALL", null, ["callee:00510288:8"]]
+ 0050ff54 ["INT_ADD", "register:40f0:8", ["const:50ff54:8", "const:4:8"]]
+ 0050ff54 ["CALL", null, ["callee:00510288:8"]]
- 0050fc34 bytes cd000094
+ 0050ff54 bytes cd000094
- 0050fdd8 ["INT_ADD", "register:40f0:8", ["const:50fdd8:8", "const:4:8"]]
- 0050fdd8 ["CALL", null, ["callee:0043e138:8"]]
+ 005100f8 ["INT_ADD", "register:40f0:8", ["const:5100f8:8", "const:4:8"]]
+ 005100f8 ["CALL", null, ["callee:0043e138:8"]]
- 0050fdd8 bytes 10b8fc97
+ 005100f8 bytes 10b8fc97
- 0050fe14 ["INT_ADD", "register:40f0:8", ["const:50fe14:8", "const:4:8"]]
- 0050fe14 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00510134 ["INT_ADD", "register:40f0:8", ["const:510134:8", "const:4:8"]]
+ 00510134 ["CALL", null, ["callee:00c58fb0:8"]]
- 0050fe14 bytes 73201d94
+ 00510134 bytes 9f231d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47daf4092a130ec05011b7db2574f81d"></a>

### [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) → [`005103c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md) FUN_005103c0

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0050fa88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050f/0050fa88.md) [`00510a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md) [`005127ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/005127ec.md) [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 16件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md) [`0046d5e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d5e8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 5件 [`0050fda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050f/0050fda8.md) [`00510d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510d5c.md) [`00512b0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512b0c.md) [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 16件 [`00442c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/00442c90.md) [`0046d908`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d908.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.76% / 新版 97.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510528",
      "incomplete_value": false,
      "site": "00510534",
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
            "const:453:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510208",
      "incomplete_value": false,
      "site": "00510214",
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
            "const:375:8"
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
      "definition_site": "00510568",
      "incomplete_value": true,
      "site": "00510574",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510248",
      "incomplete_value": true,
      "site": "00510254",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e00:8"
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
      "definition_site": "00510564",
      "incomplete_value": false,
      "site": "00510574",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00510244",
      "incomplete_value": false,
      "site": "00510254",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "ordinal": 7,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00510528",
      "PARAM",
      [
        "storage",
        "002ba375",
        null,
        "string"
      ]
    ],
    [
      "00510564",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "00510568",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510528",
      "PARAM",
      [
        "storage",
        "002ba453",
        null,
        "string"
      ]
    ],
    [
      "00510564",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "00510568",
      "READ",
      [
        "storage",
        "00c9bdd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-00510214) · [`00510254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-00510254) · [`005102a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md#insn-005102a0)
- 新版 [`00510534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md#insn-00510534) · [`00510574`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md#insn-00510574) · [`005105c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md#insn-005105c0)

~~~diff
- 00510214 ["INT_ADD", "register:40f0:8", ["const:510214:8", "const:4:8"]]
- 00510214 ["CALL", null, ["callee:00c59150:8"]]
+ 00510534 ["INT_ADD", "register:40f0:8", ["const:510534:8", "const:4:8"]]
+ 00510534 ["CALL", null, ["callee:00c59150:8"]]
- 00510214 bytes db1f1d94
+ 00510534 bytes 07231d94
- 00510254 ["INT_ADD", "register:40f0:8", ["const:510254:8", "const:4:8"]]
- 00510254 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00510574 ["INT_ADD", "register:40f0:8", ["const:510574:8", "const:4:8"]]
+ 00510574 ["CALL", null, ["callee:00c58fb0:8"]]
- 00510254 bytes 631f1d94
+ 00510574 bytes 8f221d94
- 005102a0 ["INT_ADD", "register:40f0:8", ["const:5102a0:8", "const:4:8"]]
- 005102a0 ["CALL", null, ["callee:00c59150:8"]]
+ 005105c0 ["INT_ADD", "register:40f0:8", ["const:5105c0:8", "const:4:8"]]
+ 005105c0 ["CALL", null, ["callee:00c59150:8"]]
- 005102a0 bytes b81f1d94
+ 005105c0 bytes e4221d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11cb5ba90e394e8db5b6637ef050c58a"></a>

### [`00510a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md) → [`00510d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510d5c.md) _ZN5Botan7X509_CAC1ERKNS_16X509_CertificateERKNS_11Private_KeyERKNSt6__ndk13mapINS7_12basic_stringIcNS7_11char_traitsIcEENS7_9allocatorIcEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005100a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/005100a0.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0053b040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`005103c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/005103c0.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`0053b360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.28% / 新版 95.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510da8",
      "incomplete_value": true,
      "site": "00510da8",
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
      "definition_site": "00510a88",
      "incomplete_value": true,
      "site": "00510a88",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00510de4",
      "incomplete_value": true,
      "site": "00510de8",
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
      "definition_site": "00510ac4",
      "incomplete_value": true,
      "site": "00510ac8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00510eb8",
      "incomplete_value": false,
      "site": "00510ec0",
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
            "const:7d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00510b98",
      "incomplete_value": false,
      "site": "00510ba0",
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
            "const:3d:8"
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
      "00510d88",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00510da8",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510de0",
      "READ",
      [
        "storage",
        "00c9b1b0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00510d88",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00510da8",
      "DATA",
      [
        "storage",
        "00c67248",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "00510de0",
      "READ",
      [
        "storage",
        "00c9c180",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00510ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510ba0) · [`00510bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510bdc) · [`00510a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510a3c.md#insn-00510a5c)
- 新版 [`00510ec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510d5c.md#insn-00510ec0) · [`00510efc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510d5c.md#insn-00510efc) · [`00510d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00510/00510d5c.md#insn-00510d7c)

~~~diff
- 00510ba0 ["INT_ADD", "register:40f0:8", ["const:510ba0:8", "const:4:8"]]
- 00510ba0 ["CALL", null, ["callee:0043e138:8"]]
+ 00510ec0 ["INT_ADD", "register:40f0:8", ["const:510ec0:8", "const:4:8"]]
+ 00510ec0 ["CALL", null, ["callee:0043e138:8"]]
- 00510ba0 bytes 9eb4fc97
+ 00510ec0 bytes 9eb4fc97
- 00510bdc ["INT_ADD", "register:40f0:8", ["const:510bdc:8", "const:4:8"]]
- 00510bdc ["CALL", null, ["callee:00c58fb0:8"]]
+ 00510efc ["INT_ADD", "register:40f0:8", ["const:510efc:8", "const:4:8"]]
+ 00510efc ["CALL", null, ["callee:00c58fb0:8"]]
- 00510bdc bytes 011d1d94
+ 00510efc bytes 2d201d94
- 00510a5c ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00510d7c ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00510a5c bytes 493c00d0
+ 00510d7c bytes 493c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c91051cbe3018c83c2c596307fe7869"></a>

### [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) → [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) _ZNK5Botan7X509_CA12sign_requestERKNS_14PKCS10_RequestERNS_21RandomNumberGeneratorERKNS_9X509_TimeES8_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 25件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`0050b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050b/0050b39c.md) [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) [`00511678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511678.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md)
- 新版 呼出元 0件  · 呼出先 25件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`0050b6bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0050b/0050b6bc.md) [`00511584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md) [`00511998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511998.md) [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005111a4",
      "incomplete_value": true,
      "site": "005111a8",
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
      "definition_site": "00510e84",
      "incomplete_value": true,
      "site": "00510e88",
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
    "kind": "store_value",
    "new": {
      "definition_site": "005111d8",
      "incomplete_value": true,
      "site": "005111dc",
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
      "definition_site": "00510eb8",
      "incomplete_value": true,
      "site": "00510ebc",
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
      "definition_site": "00511218",
      "incomplete_value": true,
      "site": "00511224",
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
      "definition_site": "00510ef8",
      "incomplete_value": true,
      "site": "00510f04",
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
      "00511198",
      "READ",
      [
        "storage",
        "00c9b258",
        null,
        "pointer"
      ]
    ],
    [
      "005111a8",
      "DATA",
      [
        "storage",
        "00c67a20",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "005111d0",
      "READ",
      [
        "storage",
        "00c9b248",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511198",
      "READ",
      [
        "storage",
        "00c9c228",
        null,
        "pointer"
      ]
    ],
    [
      "005111a8",
      "DATA",
      [
        "storage",
        "00c689f0",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "005111d0",
      "READ",
      [
        "storage",
        "00c9c218",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00511224) · [`00510de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00510de4) · [`00510dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md#insn-00510dfc)
- 新版 [`00511544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md#insn-00511544) · [`00511104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md#insn-00511104) · [`0051111c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md#insn-0051111c)

~~~diff
- 00511224 ["INT_ADD", "register:40f0:8", ["const:511224:8", "const:4:8"]]
- 00511224 ["CALL", null, ["callee:00c58f50:8"]]
+ 00511544 ["INT_ADD", "register:40f0:8", ["const:511544:8", "const:4:8"]]
+ 00511544 ["CALL", null, ["callee:00c58f50:8"]]
- 00511224 bytes 571b1d94
+ 00511544 bytes 831e1d94
- 00510de4 ["INT_ADD", "register:40f0:8", ["const:510de4:8", "const:4:8"]]
- 00510de4 ["CALL", null, ["callee:00c5ada0:8"]]
+ 00511104 ["INT_ADD", "register:40f0:8", ["const:511104:8", "const:4:8"]]
+ 00511104 ["CALL", null, ["callee:00c5ada0:8"]]
- 00510de4 bytes fb231d94
+ 00511104 bytes 27271d94
- 00510dfc ["INT_ADD", "register:40f0:8", ["const:510dfc:8", "const:4:8"]]
- 00510dfc ["CALL", null, ["callee:00c5ad30:8"]]
+ 0051111c ["INT_ADD", "register:40f0:8", ["const:51111c:8", "const:4:8"]]
+ 0051111c ["CALL", null, ["callee:00c5ad30:8"]]
- 00510dfc bytes d9231d94
+ 0051111c bytes 05271d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae7b3145241fb50604fc0c93ee0cb454"></a>

### [`00511264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md) → [`00511584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md) FUN_00511584

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00510d98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00510/00510d98.md) [`00526a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00526/00526a10.md) [`0052d550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052d/0052d550.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 7件 [`0053c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053c/0053c44c.md) [`0053eeb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053e/0053eeb0.md) [`0053f044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053f/0053f044.md) [`00540714`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540714.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md)
- 新版 呼出元 4件 [`005110b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/005110b8.md) [`00526d30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00526/00526d30.md) [`0052d870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052d/0052d870.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 7件 [`0053c76c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053c76c.md) [`0053f1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f1d0.md) [`0053f364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053f/0053f364.md) [`00540a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540a34.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005115c8",
      "incomplete_value": true,
      "site": "005115dc",
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
      "definition_site": "005112a8",
      "incomplete_value": true,
      "site": "005112bc",
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
      "005115b8",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "005115dc",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "005115b8",
      "READ",
      [
        "storage",
        "00c9c1b0",
        null,
        "pointer"
      ]
    ],
    [
      "005115dc",
      "DATA",
      [
        "storage",
        "00c69960",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00511288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-00511288) · [`00511298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-00511298) · [`005112d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/00511264.md#insn-005112d8)
- 新版 [`005115a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md#insn-005115a8) · [`005115b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md#insn-005115b8) · [`005115f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511584.md#insn-005115f8)

~~~diff
- 00511288 ["COPY", "register:4048:8", ["const:c9b000:8"]]
+ 005115a8 ["COPY", "register:4048:8", ["const:c9c000:8"]]
- 00511288 bytes 493c00d0
+ 005115a8 bytes 493c00f0
- 00511298 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1e0:8"]]
- 00511298 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 005115b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1b0:8"]]
+ 005115b8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00511298 bytes 29f140f9
+ 005115b8 bytes 29d940f9
- 005112d8 ["INT_ADD", "register:40f0:8", ["const:5112d8:8", "const:4:8"]]
- 005112d8 ["CALL", null, ["callee:00c58f30:8"]]
+ 005115f8 ["INT_ADD", "register:40f0:8", ["const:5115f8:8", "const:4:8"]]
+ 005115f8 ["CALL", null, ["callee:00c58f30:8"]]
- 005112d8 bytes 221b1d94
+ 005115f8 bytes 4e1e1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebf9e6323f0f46f33f074f26a0a174ae"></a>

### [`0051140c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md) → [`0051172c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/0051172c.md) _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e00.md) · 呼出先 13件 [`00516c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516c04.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`0053d768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053d/0053d768.md) [`0054b984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054b984.md) [`0054bc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054b/0054bc3c.md)
- 新版 呼出元 1件 [`00c5add0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5add0.md) · 呼出先 13件 [`00516f24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516f24.md) [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`0053da88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053d/0053da88.md) [`0054bca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bca4.md) [`0054bf5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054b/0054bf5c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.83% / 新版 97.83%

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
      "definition_site": "005117c0",
      "incomplete_value": true,
      "site": "005117c0",
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
      "definition_site": "005114a0",
      "incomplete_value": true,
      "site": "005114a0",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00511804",
      "incomplete_value": true,
      "site": "00511808",
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
      "definition_site": "005114e4",
      "incomplete_value": true,
      "site": "005114e8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005117b0",
      "READ",
      [
        "storage",
        "00c9b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "005117c0",
      "DATA",
      [
        "storage",
        "00c6a508",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005117f8",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "005117b0",
      "READ",
      [
        "storage",
        "00c9c1c0",
        null,
        "pointer"
      ]
    ],
    [
      "005117c0",
      "DATA",
      [
        "storage",
        "00c6b4d8",
        null,
        "undefined1[56]"
      ]
    ],
    [
      "005117f8",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051144c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-0051144c) · [`00511458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-00511458) · [`00511468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/0051140c.md#insn-00511468)
- 新版 [`0051176c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/0051172c.md#insn-0051176c) · [`00511778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/0051172c.md#insn-00511778) · [`00511788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/0051172c.md#insn-00511788)

~~~diff
- 0051144c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051144c ["INT_ADD", "register:40f0:8", ["const:51144c:8", "const:4:8"]]
- 0051144c ["CALLIND", null, ["register:0:8"]]
+ 0051176c ["COPY", "register:0:8", ["register:4048:8"]]
+ 0051176c ["INT_ADD", "register:40f0:8", ["const:51176c:8", "const:4:8"]]
+ 0051176c ["CALLIND", null, ["register:0:8"]]
- 0051144c bytes 20013fd6
+ 0051176c bytes 20013fd6
- 00511458 ["INT_ADD", "register:40f0:8", ["const:511458:8", "const:4:8"]]
- 00511458 ["CALL", null, ["callee:0054c274:8"]]
+ 00511778 ["INT_ADD", "register:40f0:8", ["const:511778:8", "const:4:8"]]
+ 00511778 ["CALL", null, ["callee:0054c274:8"]]
- 00511458 bytes bfea0094
+ 00511778 bytes bfea0094
- 00511468 ["INT_ADD", "register:40f0:8", ["const:511468:8", "const:4:8"]]
- 00511468 ["CALL", null, ["callee:00c58f50:8"]]
+ 00511788 ["INT_ADD", "register:40f0:8", ["const:511788:8", "const:4:8"]]
+ 00511788 ["CALL", null, ["callee:00c58f50:8"]]
- 00511468 bytes c61a1d94
+ 00511788 bytes f21d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80d20da0d5e1d7663636f05ac3d5419"></a>

### [`005116f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md) → [`00511a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511a10.md) _ZN5Botan7X509_CA9make_certEPNS_9PK_SignerERNS_21RandomNumberGeneratorERKNS_19AlgorithmIdentifierERKNSt6__ndk16vectorIhNS8_9allocatorIhEEEER

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e20.md) · 呼出先 16件 [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)
- 新版 呼出元 1件 [`00c5adf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5adf0.md) · 呼出先 16件 [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58fe0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00511ae4",
      "incomplete_value": true,
      "site": "00511ae4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005117c4",
      "incomplete_value": true,
      "site": "005117c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00511cac",
      "incomplete_value": true,
      "site": "00511cac",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051198c",
      "incomplete_value": true,
      "site": "0051198c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00511d18",
      "incomplete_value": true,
      "site": "00511d18",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005119f8",
      "incomplete_value": true,
      "site": "005119f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00511ad4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00511c9c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "00511d08",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00511ad4",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00511c9c",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ],
    [
      "00511d08",
      "READ",
      [
        "storage",
        "00c687d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005117c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-005117c4) · [`0051198c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-0051198c) · [`005119f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00511/005116f0.md#insn-005119f8)
- 新版 [`00511ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511a10.md#insn-00511ae4) · [`00511cac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511a10.md#insn-00511cac) · [`00511d18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00511/00511a10.md#insn-00511d18)

~~~diff
- 005117c4 ["COPY", "register:0:8", ["register:4048:8"]]
- 005117c4 ["INT_ADD", "register:40f0:8", ["const:5117c4:8", "const:4:8"]]
- 005117c4 ["CALLIND", null, ["register:0:8"]]
+ 00511ae4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00511ae4 ["INT_ADD", "register:40f0:8", ["const:511ae4:8", "const:4:8"]]
+ 00511ae4 ["CALLIND", null, ["register:0:8"]]
- 005117c4 bytes 20013fd6
+ 00511ae4 bytes 20013fd6
- 0051198c ["COPY", "register:0:8", ["register:4048:8"]]
- 0051198c ["INT_ADD", "register:40f0:8", ["const:51198c:8", "const:4:8"]]
- 0051198c ["CALLIND", null, ["register:0:8"]]
+ 00511cac ["COPY", "register:0:8", ["register:4048:8"]]
+ 00511cac ["INT_ADD", "register:40f0:8", ["const:511cac:8", "const:4:8"]]
+ 00511cac ["CALLIND", null, ["register:0:8"]]
- 0051198c bytes 20013fd6
+ 00511cac bytes 20013fd6
- 005119f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005119f8 ["INT_ADD", "register:40f0:8", ["const:5119f8:8", "const:4:8"]]
- 005119f8 ["CALLIND", null, ["register:0:8"]]
+ 00511d18 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00511d18 ["INT_ADD", "register:40f0:8", ["const:511d18:8", "const:4:8"]]
+ 00511d18 ["CALLIND", null, ["register:0:8"]]
- 005119f8 bytes 20013fd6
+ 00511d18 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1710c89ece50a269da11d46bbed38f46"></a>

### [`0051211c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md) → [`0051243c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051243c.md) _ZNK5Botan7X509_CA8make_crlERKNSt6__ndk16vectorINS_9CRL_EntryENS1_9allocatorIS3_EEEEjRNS_21RandomNumberGeneratorENS1_6chrono10time_pointINSB

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59e40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e40.md) · 呼出先 21件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005172d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00517/005172d0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0053b464`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053b464.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)
- 新版 呼出元 1件 [`00c5ae10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae10.md) · 呼出先 21件 [`0049f78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0049f/0049f78c.md) [`005175f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/005175f0.md) [`00535ee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ee0.md) [`0053b784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053b/0053b784.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.50% / 新版 94.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512490",
      "incomplete_value": true,
      "site": "00512490",
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
      "definition_site": "00512170",
      "incomplete_value": true,
      "site": "00512170",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005124e0",
      "incomplete_value": true,
      "site": "005124ec",
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
      "definition_site": "005121c0",
      "incomplete_value": true,
      "site": "005121cc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512550",
      "incomplete_value": true,
      "site": "00512554",
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
      "definition_site": "00512230",
      "incomplete_value": true,
      "site": "00512234",
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
      "00512478",
      "READ",
      [
        "storage",
        "00c9b1e0",
        null,
        "pointer"
      ]
    ],
    [
      "00512490",
      "DATA",
      [
        "storage",
        "00c68990",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005124d0",
      "READ",
      [
        "storage",
        "00c9b260",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00512478",
      "READ",
      [
        "storage",
        "00c9c1b0",
        null,
        "pointer"
      ]
    ],
    [
      "00512490",
      "DATA",
      [
        "storage",
        "00c69960",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "005124d0",
      "READ",
      [
        "storage",
        "00c9c230",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005122a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-005122a8) · [`00512444`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-00512444) · [`005124b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/0051211c.md#insn-005124b0)
- 新版 [`005125c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051243c.md#insn-005125c8) · [`00512764`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051243c.md#insn-00512764) · [`005127d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/0051243c.md#insn-005127d0)

~~~diff
- 005122a8 ["COPY", "register:0:8", ["register:4048:8"]]
- 005122a8 ["INT_ADD", "register:40f0:8", ["const:5122a8:8", "const:4:8"]]
- 005122a8 ["CALLIND", null, ["register:0:8"]]
+ 005125c8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005125c8 ["INT_ADD", "register:40f0:8", ["const:5125c8:8", "const:4:8"]]
+ 005125c8 ["CALLIND", null, ["register:0:8"]]
- 005122a8 bytes 20013fd6
+ 005125c8 bytes 20013fd6
- 00512444 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512444 ["INT_ADD", "register:40f0:8", ["const:512444:8", "const:4:8"]]
- 00512444 ["CALLIND", null, ["register:0:8"]]
+ 00512764 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512764 ["INT_ADD", "register:40f0:8", ["const:512764:8", "const:4:8"]]
+ 00512764 ["CALLIND", null, ["register:0:8"]]
- 00512444 bytes 20013fd6
+ 00512764 bytes 20013fd6
- 005124b0 ["COPY", "register:0:8", ["register:4048:8"]]
- 005124b0 ["INT_ADD", "register:40f0:8", ["const:5124b0:8", "const:4:8"]]
- 005124b0 ["CALLIND", null, ["register:0:8"]]
+ 005127d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 005127d0 ["INT_ADD", "register:40f0:8", ["const:5127d0:8", "const:4:8"]]
+ 005127d0 ["CALLIND", null, ["register:0:8"]]
- 005124b0 bytes 20013fd6
+ 005127d0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f2b5d6f2bdc72800b8c1f4318f5abd5"></a>

### [`00512950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md) → [`00512c70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512c70.md) _ZN5Botan8X509_CRLC1ERNS_10DataSourceE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59d50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59d50.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ad20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512cb0",
      "incomplete_value": true,
      "site": "00512cb0",
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
      "definition_site": "00512990",
      "incomplete_value": true,
      "site": "00512990",
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
      "definition_site": "00512cb0",
      "incomplete_value": true,
      "site": "00512cb0",
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
      "definition_site": "00512990",
      "incomplete_value": true,
      "site": "00512990",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512cf0",
      "incomplete_value": true,
      "site": "00512cf8",
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
      "definition_site": "005129d0",
      "incomplete_value": true,
      "site": "005129d8",
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
      "00512c90",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512c98",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512cb0",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512c90",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00512c98",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00512cb0",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-00512968) · [`0051296c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-0051296c) · [`00512970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512950.md#insn-00512970)
- 新版 [`00512c88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512c70.md#insn-00512c88) · [`00512c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512c70.md#insn-00512c8c) · [`00512c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512c70.md#insn-00512c90)

~~~diff
- 00512968 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00512c88 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00512968 bytes 483c00b0
+ 00512c88 bytes 483c00d0
- 0051296c ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00512c8c ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 0051296c bytes 4a3c0090
+ 00512c8c bytes 4a3c00b0
- 00512970 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00512970 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512c90 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 00512c90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512970 bytes 081541f9
+ 00512c90 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5584b966ed862dda24a34c5fda9bacfe"></a>

### [`00512aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md) → [`00512dc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512dc4.md) _ZN5Botan8X509_CRLC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59e60.md) · 呼出先 7件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00c5ae30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae30.md) · 呼出先 7件 [`00540728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/00540728.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59700.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.72% / 新版 84.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512e04",
      "incomplete_value": true,
      "site": "00512e04",
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
      "definition_site": "00512ae4",
      "incomplete_value": true,
      "site": "00512ae4",
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
      "definition_site": "00512e04",
      "incomplete_value": true,
      "site": "00512e04",
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
      "definition_site": "00512ae4",
      "incomplete_value": true,
      "site": "00512ae4",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512e4c",
      "incomplete_value": true,
      "site": "00512e58",
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
      "definition_site": "00512b2c",
      "incomplete_value": true,
      "site": "00512b38",
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
      "00512de4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512dec",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512e04",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512de4",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00512dec",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00512e04",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512b90) · [`00512abc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512abc) · [`00512ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512aa4.md#insn-00512ac0)
- 新版 [`00512eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512dc4.md#insn-00512eb0) · [`00512ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512dc4.md#insn-00512ddc) · [`00512de0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512dc4.md#insn-00512de0)

~~~diff
- 00512b90 ["COPY", "register:0:8", ["register:4048:8"]]
- 00512b90 ["INT_ADD", "register:40f0:8", ["const:512b90:8", "const:4:8"]]
- 00512b90 ["CALLIND", null, ["register:0:8"]]
+ 00512eb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00512eb0 ["INT_ADD", "register:40f0:8", ["const:512eb0:8", "const:4:8"]]
+ 00512eb0 ["CALLIND", null, ["register:0:8"]]
- 00512b90 bytes 20013fd6
+ 00512eb0 bytes 20013fd6
- 00512abc ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00512ddc ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00512abc bytes 483c00b0
+ 00512ddc bytes 483c00d0
- 00512ac0 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00512de0 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00512ac0 bytes 4a3c0090
+ 00512de0 bytes 4a3c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34dcbff110777ec6557c5d7799b830ce"></a>

### [`00512c1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md) → [`00512f3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512f3c.md) _ZN5Botan8X509_CRLC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) [`00c59730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59730.md) [`00c59740`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59740.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md) [`00c5a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a700.md) [`00c5a710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5a710.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00512f7c",
      "incomplete_value": true,
      "site": "00512f7c",
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
      "definition_site": "00512c5c",
      "incomplete_value": true,
      "site": "00512c5c",
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
      "definition_site": "00512f7c",
      "incomplete_value": true,
      "site": "00512f7c",
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
      "definition_site": "00512c5c",
      "incomplete_value": true,
      "site": "00512c5c",
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
    "kind": "store_value",
    "new": {
      "definition_site": "00512fbc",
      "incomplete_value": true,
      "site": "00512fc4",
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
      "definition_site": "00512c9c",
      "incomplete_value": true,
      "site": "00512ca4",
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
      "00512f5c",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "00512f64",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "00512f7c",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "00512f5c",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "00512f64",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00512f7c",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c34) · [`00512c38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c38) · [`00512c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512c1c.md#insn-00512c3c)
- 新版 [`00512f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512f3c.md#insn-00512f54) · [`00512f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512f3c.md#insn-00512f58) · [`00512f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00512/00512f3c.md#insn-00512f5c)

~~~diff
- 00512c34 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00512f54 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00512c34 bytes 483c00b0
+ 00512f54 bytes 483c00d0
- 00512c38 ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00512f58 ["COPY", "register:4050:8", ["const:c9b000:8"]]
- 00512c38 bytes 4a3c0090
+ 00512f58 bytes 4a3c00b0
- 00512c3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00512c3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00512f5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 00512f5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512c3c bytes 081541f9
+ 00512f5c bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afe7b6e4b2fa267ae32735fc41956c48"></a>

### [`00512d48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md) → [`00513068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513068.md) _ZN5Botan8X509_CRLC1ERKNS_7X509_DNERKNS_9X509_TimeES6_RKNSt6__ndk16vectorINS_9CRL_EntryENS7_9allocatorIS9_EEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0053bdb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0053b/0053bdb8.md) [`00548ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00548/00548ea8.md) [`0054aba4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0054a/0054aba4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0053c0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0053c/0053c0d8.md) [`005491c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005491c8.md) [`0054aec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0054a/0054aec4.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.61% / 新版 85.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005130dc",
      "incomplete_value": true,
      "site": "005130dc",
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
      "definition_site": "00512dbc",
      "incomplete_value": true,
      "site": "00512dbc",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005130dc",
      "incomplete_value": true,
      "site": "005130dc",
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
      "definition_site": "00512dbc",
      "incomplete_value": true,
      "site": "00512dbc",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513118",
      "incomplete_value": true,
      "site": "00513120",
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
      "definition_site": "00512df8",
      "incomplete_value": true,
      "site": "00512e00",
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
      "005130c4",
      "READ",
      [
        "storage",
        "00c9b228",
        null,
        "pointer"
      ]
    ],
    [
      "005130c8",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "005130dc",
      "DATA",
      [
        "storage",
        "00c69af0",
        null,
        "undefined1[72]"
      ]
    ]
  ],
  "added": [
    [
      "005130c4",
      "READ",
      [
        "storage",
        "00c9c1f8",
        null,
        "pointer"
      ]
    ],
    [
      "005130c8",
      "READ",
      [
        "storage",
        "00c9bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "005130dc",
      "DATA",
      [
        "storage",
        "00c6aac0",
        null,
        "undefined1[72]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00512d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512d70) · [`00512d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512d90) · [`00512da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00512/00512d48.md#insn-00512da4)
- 新版 [`00513090`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513068.md#insn-00513090) · [`005130b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513068.md#insn-005130b0) · [`005130c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513068.md#insn-005130c4)

~~~diff
- 00512d70 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00513090 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00512d70 bytes 493c0090
+ 00513090 bytes 493c0090
- 00512d90 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 005130b0 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00512d90 bytes 483c00b0
+ 005130b0 bytes 483c00b0
- 00512da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:228:8"]]
- 00512da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005130c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f8:8"]]
+ 005130c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00512da4 bytes 081541f9
+ 005130c4 bytes 08fd40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c6db8cbac32be0ddb703debfbb9e19a"></a>

### [`005132f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md) → [`00513610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md) _ZN5Botan8X509_CRL12force_decodeEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 42件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`004a57bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a57bc.md)
- 新版 呼出元 0件  · 呼出先 42件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`00451c10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00451/00451c10.md) [`00459830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00459/00459830.md) [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`004a5adc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004a5/004a5adc.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.77% / 新版 90.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 6件, `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513670",
      "incomplete_value": true,
      "site": "00513670",
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
      "definition_site": "00513350",
      "incomplete_value": true,
      "site": "00513350",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513690",
      "incomplete_value": true,
      "site": "00513690",
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
      "definition_site": "00513370",
      "incomplete_value": true,
      "site": "00513370",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00513698",
      "incomplete_value": true,
      "site": "00513698",
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
      "definition_site": "00513378",
      "incomplete_value": true,
      "site": "00513378",
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
      "00513654",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00513670",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051367c",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00513654",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "00513670",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0051367c",
      "READ",
      [
        "storage",
        "00c9be50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051337c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-0051337c) · [`005135cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-005135cc) · [`00513620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/005132f0.md#insn-00513620)
- 新版 [`0051369c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md#insn-0051369c) · [`005138ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md#insn-005138ec) · [`00513940`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00513/00513610.md#insn-00513940)

~~~diff
- 0051337c ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 0051369c ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 0051337c bytes 483c0090
+ 0051369c bytes 483c00b0
- 005135cc ["COPY", "register:0:8", ["register:4048:8"]]
- 005135cc ["INT_ADD", "register:40f0:8", ["const:5135cc:8", "const:4:8"]]
- 005135cc ["CALLIND", null, ["register:0:8"]]
+ 005138ec ["COPY", "register:0:8", ["register:4048:8"]]
+ 005138ec ["INT_ADD", "register:40f0:8", ["const:5138ec:8", "const:4:8"]]
+ 005138ec ["CALLIND", null, ["register:0:8"]]
- 005135cc bytes 20013fd6
+ 005138ec bytes 20013fd6
- 00513620 ["COPY", "register:0:8", ["register:4048:8"]]
- 00513620 ["INT_ADD", "register:40f0:8", ["const:513620:8", "const:4:8"]]
- 00513620 ["CALLIND", null, ["register:0:8"]]
+ 00513940 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00513940 ["INT_ADD", "register:40f0:8", ["const:513940:8", "const:4:8"]]
+ 00513940 ["CALLIND", null, ["register:0:8"]]
- 00513620 bytes 20013fd6
+ 00513940 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-510ede3ed5f3b8564cf04532a468f7f2"></a>

### [`00513e90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md) → [`005141b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005141b0.md) _ZNK5Botan8X509_CRL4dataEv

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b20.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)
- 新版 呼出元 1件 [`00c5aaf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aaf0.md) · 呼出先 6件 [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004aefc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ae/004aefc4.md) [`00535bc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535bc8.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c58f90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00514210",
      "incomplete_value": false,
      "site": "00514218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:e9d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513ef0",
      "incomplete_value": false,
      "site": "00513ef8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:dbf:8"
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
      "definition_site": "0051424c",
      "incomplete_value": true,
      "site": "00514258",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00513f2c",
      "incomplete_value": true,
      "site": "00513f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "definition_site": "00514248",
      "incomplete_value": false,
      "site": "00514258",
      "value": [
        "leaf",
        "const:535bc8:8"
      ]
    },
    "old": {
      "definition_site": "00513f28",
      "incomplete_value": false,
      "site": "00513f38",
      "value": [
        "leaf",
        "const:5358a8:8"
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
      "00514210",
      "PARAM",
      [
        "storage",
        "002bedbf",
        null,
        "string"
      ]
    ],
    [
      "00514248",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "0051424c",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00514210",
      "PARAM",
      [
        "storage",
        "002bee9d",
        null,
        "string"
      ]
    ],
    [
      "00514248",
      "PARAM",
      [
        "storage",
        "00535bc8",
        null,
        null
      ]
    ],
    [
      "0051424c",
      "READ",
      [
        "storage",
        "00c9bde8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00513ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513ef8) · [`00513f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513f38) · [`00513ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00513/00513e90.md#insn-00513ee4)
- 新版 [`00514218`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005141b0.md#insn-00514218) · [`00514258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005141b0.md#insn-00514258) · [`00514204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005141b0.md#insn-00514204)

~~~diff
- 00513ef8 ["INT_ADD", "register:40f0:8", ["const:513ef8:8", "const:4:8"]]
- 00513ef8 ["CALL", null, ["callee:0043e138:8"]]
+ 00514218 ["INT_ADD", "register:40f0:8", ["const:514218:8", "const:4:8"]]
+ 00514218 ["CALL", null, ["callee:0043e138:8"]]
- 00513ef8 bytes c8a7fc97
+ 00514218 bytes c8a7fc97
- 00513f38 ["INT_ADD", "register:40f0:8", ["const:513f38:8", "const:4:8"]]
- 00513f38 ["CALL", null, ["callee:00c58fb0:8"]]
+ 00514258 ["INT_ADD", "register:40f0:8", ["const:514258:8", "const:4:8"]]
+ 00514258 ["CALL", null, ["callee:00c58fb0:8"]]
- 00513f38 bytes 2a101d94
+ 00514258 bytes 56131d94
- 00513ee4 ["INT_ADD", "register:40f0:8", ["const:513ee4:8", "const:4:8"]]
- 00513ee4 ["CALL", null, ["callee:00c58f90:8"]]
+ 00514204 ["INT_ADD", "register:40f0:8", ["const:514204:8", "const:4:8"]]
+ 00514204 ["CALL", null, ["callee:00c58f90:8"]]
- 00513ee4 bytes 37101d94
+ 00514204 bytes 63131d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b720cc890db2ae5f81bdf1e58b80234"></a>

### [`0051400c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md) → [`0051432c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051432c.md) _ZN5Botan7X509_DNC2ERKNSt6__ndk18multimapINS_3OIDENS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS1_4lessIS3_EENS7_INS1_4pair

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5aba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514374",
      "incomplete_value": true,
      "site": "0051437c",
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
      "definition_site": "00514054",
      "incomplete_value": true,
      "site": "0051405c",
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
      "00514368",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "0051437c",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00514368",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "0051437c",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md#insn-00514030) · [`00514048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md#insn-00514048) · [`00514084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051400c.md#insn-00514084)
- 新版 [`00514350`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051432c.md#insn-00514350) · [`00514368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051432c.md#insn-00514368) · [`005143a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051432c.md#insn-005143a4)

~~~diff
- 00514030 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00514350 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00514030 bytes 283c00f0
+ 00514350 bytes 483c0090
- 00514048 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
- 00514048 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00514368 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
+ 00514368 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00514048 bytes 08d140f9
+ 00514368 bytes 08b940f9
- 00514084 ["INT_ADD", "register:40f0:8", ["const:514084:8", "const:4:8"]]
- 00514084 ["CALL", null, ["callee:00c5aba0:8"]]
+ 005143a4 ["INT_ADD", "register:40f0:8", ["const:5143a4:8", "const:4:8"]]
+ 005143a4 ["CALL", null, ["callee:00c5aba0:8"]]
- 00514084 bytes d3161d94
+ 005143a4 bytes ff191d94
~~~


<a id="compare-0d4844a5e5dfcacc103f6ac7bf31b994"></a>

### [`005142ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md) → [`005145cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005145cc.md) _ZN5Botan7X509_DNC1ERKNSt6__ndk18multimapINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES8_NS1_4lessIS8_EENS6_INS1_4pairIKS8_

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) [`00c59bd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59bd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59720`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59720.md) [`00c5aba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5aba0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514628",
      "incomplete_value": true,
      "site": "00514630",
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
      "definition_site": "00514308",
      "incomplete_value": true,
      "site": "00514310",
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
      "0051461c",
      "READ",
      [
        "storage",
        "00c9b1a0",
        null,
        "pointer"
      ]
    ],
    [
      "00514630",
      "DATA",
      [
        "storage",
        "00c67ac8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0051461c",
      "READ",
      [
        "storage",
        "00c9c170",
        null,
        "pointer"
      ]
    ],
    [
      "00514630",
      "DATA",
      [
        "storage",
        "00c68a98",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005142e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-005142e4) · [`005142fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-005142fc) · [`00514334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/005142ac.md#insn-00514334)
- 新版 [`00514604`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005145cc.md#insn-00514604) · [`0051461c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005145cc.md#insn-0051461c) · [`00514654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/005145cc.md#insn-00514654)

~~~diff
- 005142e4 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00514604 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 005142e4 bytes 283c00f0
+ 00514604 bytes 483c0090
- 005142fc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a0:8"]]
- 005142fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0051461c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:170:8"]]
+ 0051461c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005142fc bytes 08d140f9
+ 0051461c bytes 08b940f9
- 00514334 ["INT_ADD", "register:40f0:8", ["const:514334:8", "const:4:8"]]
- 00514334 ["CALL", null, ["callee:00c59720:8"]]
+ 00514654 ["INT_ADD", "register:40f0:8", ["const:514654:8", "const:4:8"]]
+ 00514654 ["CALL", null, ["callee:00c59720:8"]]
- 00514334 bytes 07111d94
+ 00514654 bytes 33141d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7162b31ad159a0ed250ec8c58747a7ca"></a>

### [`0051464c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md) → [`0051496c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051496c.md) _ZN5Botan7X509_DN16deref_info_fieldERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59c40.md) · 呼出先 3件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md)
- 新版 呼出元 1件 [`00c5ac10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ac10.md) · 呼出先 3件 [`0043be80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043b/0043be80.md) [`0043e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0043e/0043e138.md) [`004421f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00442/004421f4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.41% / 新版 86.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00514af0",
      "incomplete_value": true,
      "site": "00514af0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005147d0",
      "incomplete_value": true,
      "site": "005147d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
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
      "definition_site": "00514b4c",
      "incomplete_value": true,
      "site": "00514b4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:67a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0051482c",
      "incomplete_value": true,
      "site": "0051482c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:522:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00514b40",
      "incomplete_value": true,
      "site": "00514b50",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00514820",
      "incomplete_value": true,
      "site": "00514830",
      "value": [
        "LOAD",
        "8",
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
      "00514ac0",
      "PARAM",
      [
        "storage",
        "002b61bc",
        null,
        null
      ]
    ],
    [
      "00514adc",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ],
    [
      "00514b00",
      "PARAM",
      [
        "storage",
        "002c11d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00514ac0",
      "PARAM",
      [
        "storage",
        "002b628b",
        null,
        null
      ]
    ],
    [
      "00514adc",
      "READ",
      [
        "storage",
        "002bb3b4",
        null,
        "string"
      ]
    ],
    [
      "00514b00",
      "PARAM",
      [
        "storage",
        "002c121d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005147a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147a8) · [`005147e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147e8) · [`005147fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/0051464c.md#insn-005147fc)
- 新版 [`00514ac8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051496c.md#insn-00514ac8) · [`00514b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051496c.md#insn-00514b08) · [`00514b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00514/0051496c.md#insn-00514b1c)

~~~diff
- 005147a8 ["INT_ADD", "register:40f0:8", ["const:5147a8:8", "const:4:8"]]
- 005147a8 ["CALL", null, ["callee:004421f4:8"]]
+ 00514ac8 ["INT_ADD", "register:40f0:8", ["const:514ac8:8", "const:4:8"]]
+ 00514ac8 ["CALL", null, ["callee:004421f4:8"]]
- 005147a8 bytes cbb5fc97
+ 00514ac8 bytes cbb5fc97
- 005147e8 ["INT_ADD", "register:40f0:8", ["const:5147e8:8", "const:4:8"]]
- 005147e8 ["CALL", null, ["callee:004421f4:8"]]
+ 00514b08 ["INT_ADD", "register:40f0:8", ["const:514b08:8", "const:4:8"]]
+ 00514b08 ["CALL", null, ["callee:004421f4:8"]]
- 005147e8 bytes bbb5fc97
+ 00514b08 bytes bbb5fc97
- 005147fc ["INT_ADD", "register:40f0:8", ["const:5147fc:8", "const:4:8"]]
- 005147fc ["CALL", null, ["callee:004421f4:8"]]
+ 00514b1c ["INT_ADD", "register:40f0:8", ["const:514b1c:8", "const:4:8"]]
+ 00514b1c ["CALL", null, ["callee:004421f4:8"]]
- 005147fc bytes b6b5fc97
+ 00514b1c bytes b6b5fc97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4a2035d3838f9c475761627075e0911"></a>

### [`00514de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md) → [`00515104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md) _ZNK5Botan7X509_DN11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`004ffaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ff/004ffaec.md) [`0052e374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0052e/0052e374.md) · 呼出先 11件 [`00515140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515140.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005496a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00549/005496a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)
- 新版 呼出元 2件 [`004ffe0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/004ff/004ffe0c.md) [`0052e694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0052e/0052e694.md) · 呼出先 11件 [`00515460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515460.md) [`0054084c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00540/0054084c.md) [`005499c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00549/005499c8.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 84.38% / 新版 84.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00515194",
      "incomplete_value": true,
      "site": "00515194",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514e74",
      "incomplete_value": true,
      "site": "00514e74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d6:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "005151dc",
      "incomplete_value": true,
      "site": "005151dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:68a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514ebc",
      "incomplete_value": true,
      "site": "00514ebc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2a6000:8"
              ],
              [
                "leaf",
                "const:532:8"
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
      "definition_site": "00515224",
      "incomplete_value": true,
      "site": "00515224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:75:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00514f04",
      "incomplete_value": true,
      "site": "00514f04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa6:8"
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
      "00515180",
      "READ",
      [
        "storage",
        "002bb2d6",
        null,
        "string"
      ]
    ],
    [
      "005151cc",
      "READ",
      [
        "storage",
        "002a6532",
        null,
        "string"
      ]
    ],
    [
      "00515214",
      "READ",
      [
        "storage",
        "002b5fa6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00515180",
      "READ",
      [
        "storage",
        "002bb3b4",
        null,
        "string"
      ]
    ],
    [
      "005151cc",
      "READ",
      [
        "storage",
        "002a668a",
        null,
        "string"
      ]
    ],
    [
      "00515214",
      "READ",
      [
        "storage",
        "002b6075",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00514e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514e14) · [`00514e24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514e24) · [`00514e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00514/00514de4.md#insn-00514e4c)
- 新版 [`00515134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md#insn-00515134) · [`00515144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md#insn-00515144) · [`0051516c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515104.md#insn-0051516c)

~~~diff
- 00514e14 ["INT_ADD", "register:40f0:8", ["const:514e14:8", "const:4:8"]]
- 00514e14 ["CALL", null, ["callee:00c5aac0:8"]]
+ 00515134 ["INT_ADD", "register:40f0:8", ["const:515134:8", "const:4:8"]]
+ 00515134 ["CALL", null, ["callee:00c5aac0:8"]]
- 00514e14 bytes 37131d94
+ 00515134 bytes 63161d94
- 00514e24 ["INT_ADD", "register:40f0:8", ["const:514e24:8", "const:4:8"]]
- 00514e24 ["CALL", null, ["callee:00c59750:8"]]
+ 00515144 ["INT_ADD", "register:40f0:8", ["const:515144:8", "const:4:8"]]
+ 00515144 ["CALL", null, ["callee:00c59750:8"]]
- 00514e24 bytes 570e1d94
+ 00515144 bytes 83111d94
- 00514e4c ["INT_ADD", "register:40f0:8", ["const:514e4c:8", "const:4:8"]]
- 00514e4c ["CALL", null, ["callee:00c59760:8"]]
+ 0051516c ["INT_ADD", "register:40f0:8", ["const:51516c:8", "const:4:8"]]
+ 0051516c ["CALL", null, ["callee:00c59760:8"]]
- 00514e4c bytes 510e1d94
+ 0051516c bytes 7d111d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4bbb05e02b17ff1e4f640a932ba92e3"></a>

### [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) → [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) _ZN5Botan10Extensions15create_extn_objERKNS_3OIDEbRKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c59eb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59eb0.md) · 呼出先 27件 [`0046d4d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0046d/0046d4d0.md) [`00503c34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00503/00503c34.md) [`005166a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md) [`00516748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md) [`005167f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md)
- 新版 呼出元 1件 [`00c5ae80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ae80.md) · 呼出先 27件 [`0046d7f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/0046d/0046d7f0.md) [`00503f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00503/00503f54.md) [`005169c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/005169c0.md) [`00516a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516a68.md) [`00516b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516b10.md)

変更の種類 call, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00515a88",
      "incomplete_value": true,
      "site": "00515a88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515768",
      "incomplete_value": true,
      "site": "00515768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d3c:8"
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
      "definition_site": "00515b58",
      "incomplete_value": true,
      "site": "00515b58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515838",
      "incomplete_value": true,
      "site": "00515838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:781:8"
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
      "definition_site": "00515c78",
      "incomplete_value": true,
      "site": "00515c78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3aa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00515958",
      "incomplete_value": true,
      "site": "00515958",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2cc:8"
              ]
            ]
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
      "00515a78",
      "READ",
      [
        "storage",
        "002b4d3c",
        null,
        "string"
      ]
    ],
    [
      "00515b20",
      "READ",
      [
        "storage",
        "00c9b280",
        null,
        "pointer"
      ]
    ],
    [
      "00515b2c",
      "DATA",
      [
        "storage",
        "00c67af8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00515a78",
      "READ",
      [
        "storage",
        "002b4e1a",
        null,
        "string"
      ]
    ],
    [
      "00515b20",
      "READ",
      [
        "storage",
        "00c9c250",
        null,
        "pointer"
      ]
    ],
    [
      "00515b2c",
      "DATA",
      [
        "storage",
        "00c68ac8",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00515f38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515f38) · [`00515748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515748) · [`00515750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md#insn-00515750)
- 新版 [`00516258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md#insn-00516258) · [`00515a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md#insn-00515a68) · [`00515a70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md#insn-00515a70)

~~~diff
- 00515f38 ["INT_ADD", "register:40f0:8", ["const:515f38:8", "const:4:8"]]
- 00515f38 ["CALL", null, ["ram:503c34:8"]]
+ 00516258 ["INT_ADD", "register:40f0:8", ["const:516258:8", "const:4:8"]]
+ 00516258 ["CALL", null, ["ram:503f54:8"]]
- 00515f38 bytes 3fb7ff97
+ 00516258 bytes 3fb7ff97
- 00515748 ["INT_ADD", "register:40f0:8", ["const:515748:8", "const:4:8"]]
- 00515748 ["CALL", null, ["callee:00c598a0:8"]]
+ 00515a68 ["INT_ADD", "register:40f0:8", ["const:515a68:8", "const:4:8"]]
+ 00515a68 ["CALL", null, ["callee:00c598a0:8"]]
- 00515748 bytes 620c1d94
+ 00515a68 bytes 8e0f1d94
- 00515750 ["COPY", "tmp:0:8", ["const:d3c:8"]]
- 00515750 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00515750 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00515750 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00515a70 ["COPY", "tmp:0:8", ["const:e1a:8"]]
+ 00515a70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00515a70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00515a70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00515750 bytes 29f13491
+ 00515a70 bytes 29693891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8af9a9aec0fe3cfef3301faab6e63f0"></a>

### [`005166a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md) → [`005169c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/005169c0.md) FUN_005169c0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "005169f8",
      "incomplete_value": true,
      "site": "005169f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:181:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005166d8",
      "incomplete_value": true,
      "site": "005166d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b6:8"
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
      "005169e8",
      "READ",
      [
        "storage",
        "002a40b6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "005169e8",
      "READ",
      [
        "storage",
        "002a4181",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005166bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166bc) · [`005166e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166e4) · [`005166f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005166a0.md#insn-005166f4)
- 新版 [`005169dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/005169c0.md#insn-005169dc) · [`00516a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/005169c0.md#insn-00516a04) · [`00516a14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/005169c0.md#insn-00516a14)

~~~diff
- 005166bc ["COPY", "tmp:0:8", ["const:b6:8"]]
- 005166bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005166bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005166bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005169dc ["COPY", "tmp:0:8", ["const:181:8"]]
+ 005169dc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005169dc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005169dc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005166bc bytes 29d90291
+ 005169dc bytes 29050691
- 005166e4 ["INT_ADD", "register:40f0:8", ["const:5166e4:8", "const:4:8"]]
- 005166e4 ["CALL", null, ["callee:00c59730:8"]]
+ 00516a04 ["INT_ADD", "register:40f0:8", ["const:516a04:8", "const:4:8"]]
+ 00516a04 ["CALL", null, ["callee:00c59730:8"]]
- 005166e4 bytes 1f081d94
+ 00516a04 bytes 4b0b1d94
- 005166f4 ["INT_ADD", "register:40f0:8", ["const:5166f4:8", "const:4:8"]]
- 005166f4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00516a14 ["INT_ADD", "register:40f0:8", ["const:516a14:8", "const:4:8"]]
+ 00516a14 ["CALL", null, ["callee:00c58f50:8"]]
- 005166f4 bytes 23061d94
+ 00516a14 bytes 4f091d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21b3f1cdaa4e07c8e9141d897f98623b"></a>

### [`00516748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md) → [`00516a68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516a68.md) FUN_00516a68

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516aa0",
      "incomplete_value": true,
      "site": "00516aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:f60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516780",
      "incomplete_value": true,
      "site": "00516780",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29e000:8"
              ],
              [
                "leaf",
                "const:f20:8"
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
      "00516a90",
      "READ",
      [
        "storage",
        "0029ef20",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516a90",
      "READ",
      [
        "storage",
        "0029ef60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-00516764) · [`0051678c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-0051678c) · [`0051679c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516748.md#insn-0051679c)
- 新版 [`00516a84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516a68.md#insn-00516a84) · [`00516aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516a68.md#insn-00516aac) · [`00516abc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516a68.md#insn-00516abc)

~~~diff
- 00516764 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00516764 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516764 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516764 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516a84 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00516a84 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a84 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516a84 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516764 bytes 29813c91
+ 00516a84 bytes 29813d91
- 0051678c ["INT_ADD", "register:40f0:8", ["const:51678c:8", "const:4:8"]]
- 0051678c ["CALL", null, ["callee:00c59730:8"]]
+ 00516aac ["INT_ADD", "register:40f0:8", ["const:516aac:8", "const:4:8"]]
+ 00516aac ["CALL", null, ["callee:00c59730:8"]]
- 0051678c bytes f5071d94
+ 00516aac bytes 210b1d94
- 0051679c ["INT_ADD", "register:40f0:8", ["const:51679c:8", "const:4:8"]]
- 0051679c ["CALL", null, ["callee:00c58f50:8"]]
+ 00516abc ["INT_ADD", "register:40f0:8", ["const:516abc:8", "const:4:8"]]
+ 00516abc ["CALL", null, ["callee:00c58f50:8"]]
- 0051679c bytes f9051d94
+ 00516abc bytes 25091d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08694c261d609d2fcc228701f3fb29fe"></a>

### [`005167f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md) → [`00516b10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516b10.md) FUN_00516b10

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516b48",
      "incomplete_value": true,
      "site": "00516b48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:885:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516828",
      "incomplete_value": true,
      "site": "00516828",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:72d:8"
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
      "00516b38",
      "READ",
      [
        "storage",
        "002a772d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516b38",
      "READ",
      [
        "storage",
        "002a7885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051680c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-0051680c) · [`00516834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-00516834) · [`00516844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005167f0.md#insn-00516844)
- 新版 [`00516b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516b10.md#insn-00516b2c) · [`00516b54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516b10.md#insn-00516b54) · [`00516b64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516b10.md#insn-00516b64)

~~~diff
- 0051680c ["COPY", "tmp:0:8", ["const:72d:8"]]
- 0051680c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051680c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051680c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516b2c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00516b2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516b2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516b2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051680c bytes 29b51c91
+ 00516b2c bytes 29152291
- 00516834 ["INT_ADD", "register:40f0:8", ["const:516834:8", "const:4:8"]]
- 00516834 ["CALL", null, ["callee:00c59730:8"]]
+ 00516b54 ["INT_ADD", "register:40f0:8", ["const:516b54:8", "const:4:8"]]
+ 00516b54 ["CALL", null, ["callee:00c59730:8"]]
- 00516834 bytes cb071d94
+ 00516b54 bytes f70a1d94
- 00516844 ["INT_ADD", "register:40f0:8", ["const:516844:8", "const:4:8"]]
- 00516844 ["CALL", null, ["callee:00c58f50:8"]]
+ 00516b64 ["INT_ADD", "register:40f0:8", ["const:516b64:8", "const:4:8"]]
+ 00516b64 ["CALL", null, ["callee:00c58f50:8"]]
- 00516844 bytes cf051d94
+ 00516b64 bytes fb081d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ae2535ea9759f3951c37a5c7f302176"></a>

### [`00516898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md) → [`00516bb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516bb8.md) FUN_00516bb8

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516bf0",
      "incomplete_value": true,
      "site": "00516bf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:567:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005168d0",
      "incomplete_value": true,
      "site": "005168d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:489:8"
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
      "00516be0",
      "READ",
      [
        "storage",
        "002bc489",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516be0",
      "READ",
      [
        "storage",
        "002bc567",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005168b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168b4) · [`005168dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168dc) · [`005168ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516898.md#insn-005168ec)
- 新版 [`00516bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516bb8.md#insn-00516bd4) · [`00516bfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516bb8.md#insn-00516bfc) · [`00516c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516bb8.md#insn-00516c0c)

~~~diff
- 005168b4 ["COPY", "tmp:0:8", ["const:489:8"]]
- 005168b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005168b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005168b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516bd4 ["COPY", "tmp:0:8", ["const:567:8"]]
+ 00516bd4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516bd4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516bd4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005168b4 bytes 29251291
+ 00516bd4 bytes 299d1591
- 005168dc ["INT_ADD", "register:40f0:8", ["const:5168dc:8", "const:4:8"]]
- 005168dc ["CALL", null, ["callee:00c59730:8"]]
+ 00516bfc ["INT_ADD", "register:40f0:8", ["const:516bfc:8", "const:4:8"]]
+ 00516bfc ["CALL", null, ["callee:00c59730:8"]]
- 005168dc bytes a1071d94
+ 00516bfc bytes cd0a1d94
- 005168ec ["INT_ADD", "register:40f0:8", ["const:5168ec:8", "const:4:8"]]
- 005168ec ["CALL", null, ["callee:00c58f50:8"]]
+ 00516c0c ["INT_ADD", "register:40f0:8", ["const:516c0c:8", "const:4:8"]]
+ 00516c0c ["CALL", null, ["callee:00c58f50:8"]]
- 005168ec bytes a5051d94
+ 00516c0c bytes d1081d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92d063c03efb911c47eeaf6f04631347"></a>

### [`00516940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md) → [`00516c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516c60.md) FUN_00516c60

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516c98",
      "incomplete_value": true,
      "site": "00516c98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:7b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516978",
      "incomplete_value": true,
      "site": "00516978",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ad000:8"
              ],
              [
                "leaf",
                "const:6e5:8"
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
      "00516c88",
      "READ",
      [
        "storage",
        "002ad6e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516c88",
      "READ",
      [
        "storage",
        "002ad7b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0051695c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-0051695c) · [`00516984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-00516984) · [`00516994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516940.md#insn-00516994)
- 新版 [`00516c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516c60.md#insn-00516c7c) · [`00516ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516c60.md#insn-00516ca4) · [`00516cb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516c60.md#insn-00516cb4)

~~~diff
- 0051695c ["COPY", "tmp:0:8", ["const:6e5:8"]]
- 0051695c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0051695c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0051695c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516c7c ["COPY", "tmp:0:8", ["const:7b2:8"]]
+ 00516c7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516c7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516c7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0051695c bytes 29951b91
+ 00516c7c bytes 29c91e91
- 00516984 ["INT_ADD", "register:40f0:8", ["const:516984:8", "const:4:8"]]
- 00516984 ["CALL", null, ["callee:00c59730:8"]]
+ 00516ca4 ["INT_ADD", "register:40f0:8", ["const:516ca4:8", "const:4:8"]]
+ 00516ca4 ["CALL", null, ["callee:00c59730:8"]]
- 00516984 bytes 77071d94
+ 00516ca4 bytes a30a1d94
- 00516994 ["INT_ADD", "register:40f0:8", ["const:516994:8", "const:4:8"]]
- 00516994 ["CALL", null, ["callee:00c58f50:8"]]
+ 00516cb4 ["INT_ADD", "register:40f0:8", ["const:516cb4:8", "const:4:8"]]
+ 00516cb4 ["CALL", null, ["callee:00c58f50:8"]]
- 00516994 bytes 7b051d94
+ 00516cb4 bytes a7081d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ca198bc41639a68f5b265ee51a708f1"></a>

### [`005169e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md) → [`00516d08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516d08.md) FUN_00516d08

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516d40",
      "incomplete_value": true,
      "site": "00516d40",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
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
    "old": {
      "definition_site": "00516a20",
      "incomplete_value": true,
      "site": "00516a20",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2ab000:8"
              ],
              [
                "leaf",
                "const:3bb:8"
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
      "00516d30",
      "READ",
      [
        "storage",
        "002ab3bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516d30",
      "READ",
      [
        "storage",
        "002ab488",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a04) · [`00516a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a2c) · [`00516a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/005169e8.md#insn-00516a3c)
- 新版 [`00516d24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516d08.md#insn-00516d24) · [`00516d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516d08.md#insn-00516d4c) · [`00516d5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516d08.md#insn-00516d5c)

~~~diff
- 00516a04 ["COPY", "tmp:0:8", ["const:3bb:8"]]
- 00516a04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516a04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516a04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516d24 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00516d24 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516d24 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516d24 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516a04 bytes 29ed0e91
+ 00516d24 bytes 29211291
- 00516a2c ["INT_ADD", "register:40f0:8", ["const:516a2c:8", "const:4:8"]]
- 00516a2c ["CALL", null, ["callee:00c59730:8"]]
+ 00516d4c ["INT_ADD", "register:40f0:8", ["const:516d4c:8", "const:4:8"]]
+ 00516d4c ["CALL", null, ["callee:00c59730:8"]]
- 00516a2c bytes 4d071d94
+ 00516d4c bytes 790a1d94
- 00516a3c ["INT_ADD", "register:40f0:8", ["const:516a3c:8", "const:4:8"]]
- 00516a3c ["CALL", null, ["callee:00c58f50:8"]]
+ 00516d5c ["INT_ADD", "register:40f0:8", ["const:516d5c:8", "const:4:8"]]
+ 00516d5c ["CALL", null, ["callee:00c58f50:8"]]
- 00516a3c bytes 51051d94
+ 00516d5c bytes 7d081d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9081c14fe0d536735a5916ba955cc548"></a>

### [`00516a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md) → [`00516db0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516db0.md) FUN_00516db0

採用 · 移動量 `+0x320` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 3件 [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c58f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f80.md) [`00c59730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c59730.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516dd8",
      "incomplete_value": true,
      "site": "00516de8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:b12:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516ab8",
      "incomplete_value": true,
      "site": "00516ac8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2b0000:8"
              ],
              [
                "leaf",
                "const:a3b:8"
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
      "00516dd8",
      "READ",
      [
        "storage",
        "002b0a3b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00516dd8",
      "READ",
      [
        "storage",
        "002b0b12",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516aac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516aac) · [`00516ad4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516ad4) · [`00516ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516a90.md#insn-00516ae4)
- 新版 [`00516dcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516db0.md#insn-00516dcc) · [`00516df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516db0.md#insn-00516df4) · [`00516e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516db0.md#insn-00516e04)

~~~diff
- 00516aac ["COPY", "tmp:0:8", ["const:a3b:8"]]
- 00516aac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00516aac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00516aac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00516dcc ["COPY", "tmp:0:8", ["const:b12:8"]]
+ 00516dcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00516dcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00516dcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00516aac bytes 29ed2891
+ 00516dcc bytes 29492c91
- 00516ad4 ["INT_ADD", "register:40f0:8", ["const:516ad4:8", "const:4:8"]]
- 00516ad4 ["CALL", null, ["callee:00c59730:8"]]
+ 00516df4 ["INT_ADD", "register:40f0:8", ["const:516df4:8", "const:4:8"]]
+ 00516df4 ["CALL", null, ["callee:00c59730:8"]]
- 00516ad4 bytes 23071d94
+ 00516df4 bytes 4f0a1d94
- 00516ae4 ["INT_ADD", "register:40f0:8", ["const:516ae4:8", "const:4:8"]]
- 00516ae4 ["CALL", null, ["callee:00c58f50:8"]]
+ 00516e04 ["INT_ADD", "register:40f0:8", ["const:516e04:8", "const:4:8"]]
+ 00516e04 ["CALL", null, ["callee:00c58f50:8"]]
- 00516ae4 bytes 27051d94
+ 00516e04 bytes 53081d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e41887dc5ca37b46c846fdbe28b7c639"></a>

### [`00516b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md) → [`00516e58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516e58.md) FUN_00516e58

採用 · 移動量 `+0x320` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00515704`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00515/00515704.md) · 呼出先 5件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)
- 新版 呼出元 1件 [`00515a24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00515/00515a24.md) · 呼出先 5件 [`00535ecc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00535/00535ecc.md) [`00c54fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c54/00c54fec.md) [`00c58f30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f30.md) [`00c58f50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c58/00c58f50.md) [`00c590a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c590a0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516ea0",
      "incomplete_value": true,
      "site": "00516ea0",
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
      "definition_site": "00516b80",
      "incomplete_value": true,
      "site": "00516b80",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00516ea0",
      "incomplete_value": true,
      "site": "00516ea0",
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
      "definition_site": "00516b80",
      "incomplete_value": true,
      "site": "00516b80",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00516e80",
      "READ",
      [
        "storage",
        "00c9b2b0",
        null,
        "pointer"
      ]
    ],
    [
      "00516e8c",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "00516ea0",
      "DATA",
      [
        "storage",
        "00c68fb8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00516e80",
      "READ",
      [
        "storage",
        "00c9c280",
        null,
        "pointer"
      ]
    ],
    [
      "00516e8c",
      "READ",
      [
        "storage",
        "00c9bde0",
        null,
        "pointer"
      ]
    ],
    [
      "00516ea0",
      "DATA",
      [
        "storage",
        "00c69f88",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md#insn-00516b50) · [`00516b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md#insn-00516b54) · [`00516b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516b38.md#insn-00516b60)
- 新版 [`00516e70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516e58.md#insn-00516e70) · [`00516e74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516e58.md#insn-00516e74) · [`00516e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00516/00516e58.md#insn-00516e80)

~~~diff
- 00516b50 ["COPY", "register:4040:8", ["const:c9b000:8"]]
+ 00516e70 ["COPY", "register:4040:8", ["const:c9c000:8"]]
- 00516b50 bytes 283c00b0
+ 00516e70 bytes 283c00d0
- 00516b54 ["COPY", "register:4048:8", ["const:c9a000:8"]]
+ 00516e74 ["COPY", "register:4048:8", ["const:c9b000:8"]]
- 00516b54 bytes 293c0090
+ 00516e74 bytes 293c00b0
- 00516b60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
- 00516b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00516e80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00516e80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00516b60 bytes 085941f9
+ 00516e80 bytes 084141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6a42706c654db2465f55e80b6b73a67"></a>

### [`00516e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md) → [`0051714c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/0051714c.md) _ZNK5Botan10Extensions20get_extension_objectERKNS_3OIDE

採用 · 移動量 `+0x320` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b90.md) · 呼出先 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)
- 新版 呼出元 1件 [`00c5ab60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5a/00c5ab60.md) · 呼出先 1件 [`00c596f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c59/00c596f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517244",
      "incomplete_value": false,
      "site": "00517264",
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
            "const:da3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516f24",
      "incomplete_value": false,
      "site": "00516f44",
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
            "const:cd6:8"
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
      "definition_site": "0051724c",
      "incomplete_value": false,
      "site": "00517264",
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
      "definition_site": "00516f2c",
      "incomplete_value": false,
      "site": "00516f44",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00517254",
      "incomplete_value": false,
      "site": "00517264",
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
            "const:341:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00516f34",
      "incomplete_value": false,
      "site": "00516f44",
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
            "const:2f7:8"
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
      "00517244",
      "PARAM",
      [
        "storage",
        "002a9cd6",
        null,
        "string"
      ]
    ],
    [
      "0051724c",
      "PARAM",
      [
        "storage",
        "002a638e",
        null,
        "undefined1"
      ]
    ],
    [
      "00517254",
      "PARAM",
      [
        "storage",
        "002c12f7",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00517244",
      "PARAM",
      [
        "storage",
        "002a9da3",
        null,
        "string"
      ]
    ],
    [
      "0051724c",
      "PARAM",
      [
        "storage",
        "002a64e6",
        null,
        "undefined1"
      ]
    ],
    [
      "00517254",
      "PARAM",
      [
        "storage",
        "002c1341",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00516f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f44) · [`00516f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f24) · [`00516f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00516/00516e2c.md#insn-00516f2c)
- 新版 [`00517264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/0051714c.md#insn-00517264) · [`00517244`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/0051714c.md#insn-00517244) · [`0051724c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00517/0051714c.md#insn-0051724c)

~~~diff
- 00516f44 ["INT_ADD", "register:40f0:8", ["const:516f44:8", "const:4:8"]]
- 00516f44 ["CALL", null, ["callee:00c596f0:8"]]
+ 00517264 ["INT_ADD", "register:40f0:8", ["const:517264:8", "const:4:8"]]
+ 00517264 ["CALL", null, ["callee:00c596f0:8"]]
- 00516f44 bytes f7051d94
+ 00517264 bytes 23091d94
- 00516f24 ["COPY", "tmp:0:8", ["const:cd6:8"]]
- 00516f24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00516f24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00516f24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00517244 ["COPY", "tmp:0:8", ["const:da3:8"]]
+ 00517244 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00517244 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00517244 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00516f24 bytes 00583391
+ 00517244 bytes 008c3691
- 00516f2c ["COPY", "tmp:0:8", ["const:38e:8"]]
- 00516f2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00516f2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00516f2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0051724c ["COPY", "tmp:0:8", ["const:4e6:8"]]
+ 0051724c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0051724c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0051724c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00516f2c bytes 21380e91
+ 0051724c bytes 21981391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

