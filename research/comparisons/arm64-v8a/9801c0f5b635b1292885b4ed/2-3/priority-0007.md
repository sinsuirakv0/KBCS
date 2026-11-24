# v16.0.1 → v16.0.2 · 最優先の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-f22cfc0d954bd73a4ca98a2c026460bc"></a>

### [`0049f8e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) → [`0049f920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) FUN_0049f920

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049c378`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) [`0049cadc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049da20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049e904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) · 呼出先 1件 [`00442930`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 4件 [`0049c3b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) [`0049cb1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049da60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049e944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) · 呼出先 1件 [`00442970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

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
      "definition_site": "0049f92c",
      "incomplete_value": false,
      "site": "0049f930",
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
      "definition_site": "0049f8ec",
      "incomplete_value": false,
      "site": "0049f8f0",
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
      "0049f92c",
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
      "0049f92c",
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

- 旧版 [`0049f8f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md#insn-0049f8f0) · [`0049f8ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md#insn-0049f8ec)
- 新版 `0049f930`（命令位置の公開資料なし） · `0049f92c`（命令位置の公開資料なし）

~~~diff
- 0049f8f0 ["INT_ADD", "register:40f0:8", ["const:49f8f0:8", "const:4:8"]]
- 0049f8f0 ["CALL", null, ["callee:00442970:8"]]
+ 0049f930 ["INT_ADD", "register:40f0:8", ["const:49f930:8", "const:4:8"]]
+ 0049f930 ["CALL", null, ["callee:00442970:8"]]
- 0049f8f0 bytes 108cfe97
+ 0049f930 bytes 108cfe97
- 0049f8ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 0049f8ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0049f8ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0049f8ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0049f92c ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 0049f92c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f92c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0049f92c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0049f8ec bytes 00303d91
+ 0049f92c bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a280deee391ef9d76415dca89c8ecff7"></a>

### [`0049fa7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md) → [`0049fabc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md) FUN_0049fabc

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fb18",
      "incomplete_value": false,
      "site": "0049fb20",
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
            "const:9ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fad8",
      "incomplete_value": false,
      "site": "0049fae0",
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
            "const:97d:8"
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
      "definition_site": "0049fb28",
      "incomplete_value": true,
      "site": "0049fb2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fae8",
      "incomplete_value": true,
      "site": "0049faec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0049fb20",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "0049fb28",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "0049fb28",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0049fb20",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "0049fb28",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "0049fb28",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049faec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md#insn-0049faec) · [`0049fad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md#insn-0049fad0) · [`0049fad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md#insn-0049fad8)
- 新版 `0049fb2c`（命令位置の公開資料なし） · `0049fb10`（命令位置の公開資料なし） · `0049fb18`（命令位置の公開資料なし）

~~~diff
- 0049faec ["INT_ADD", "register:40f0:8", ["const:49faec:8", "const:4:8"]]
- 0049faec ["CALL", null, ["callee:00c57fe0:8"]]
+ 0049fb2c ["INT_ADD", "register:40f0:8", ["const:49fb2c:8", "const:4:8"]]
+ 0049fb2c ["CALL", null, ["callee:00c57fe0:8"]]
- 0049faec bytes 09e11e94
+ 0049fb2c bytes 2de11e94
- 0049fad0 ["INT_ADD", "register:40f0:8", ["const:49fad0:8", "const:4:8"]]
- 0049fad0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 0049fb10 ["INT_ADD", "register:40f0:8", ["const:49fb10:8", "const:4:8"]]
+ 0049fb10 ["CALL", null, ["callee:00c57fc0:8"]]
- 0049fad0 bytes 08e11e94
+ 0049fb10 bytes 2ce11e94
- 0049fad8 ["COPY", "tmp:0:8", ["const:97d:8"]]
- 0049fad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049fad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049fad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049fb18 ["COPY", "tmp:0:8", ["const:9ae:8"]]
+ 0049fb18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fb18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049fb18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049fad8 bytes 08f52591
+ 0049fb18 bytes 08b92691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1a40fa26540771c521cf29bfa7a974a"></a>

### [`0049faf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md) → [`0049fb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md) FUN_0049fb30

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fbb4",
      "incomplete_value": true,
      "site": "0049fbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fb74",
      "incomplete_value": true,
      "site": "0049fb8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cd0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fc1c",
      "incomplete_value": false,
      "site": "0049fc24",
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
            "const:ad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fbdc",
      "incomplete_value": false,
      "site": "0049fbe4",
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
            "const:6d:8"
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
      "definition_site": "0049fc40",
      "incomplete_value": false,
      "site": "0049fc44",
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
            "const:26:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fc00",
      "incomplete_value": false,
      "site": "0049fc04",
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
            "const:7a:8"
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
      "0049fbb4",
      "READ",
      [
        "storage",
        "002c2cd0",
        null,
        null
      ]
    ],
    [
      "0049fc24",
      "DATA",
      [
        "storage",
        "002b806d",
        null,
        "string"
      ]
    ],
    [
      "0049fc2c",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fbb4",
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      "0049fc24",
      "DATA",
      [
        "storage",
        "002b80ad",
        null,
        "string"
      ]
    ],
    [
      "0049fc2c",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fb4c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md#insn-0049fb4c) · [`0049fbf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md#insn-0049fbf0) · [`0049fc24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md#insn-0049fc24)
- 新版 `0049fb8c`（命令位置の公開資料なし） · `0049fc30`（命令位置の公開資料なし） · `0049fc64`（命令位置の公開資料なし）

~~~diff
- 0049fb4c ["INT_ADD", "register:40f0:8", ["const:49fb4c:8", "const:4:8"]]
- 0049fb4c ["CALL", null, ["callee:0049b4e0:8"]]
+ 0049fb8c ["INT_ADD", "register:40f0:8", ["const:49fb8c:8", "const:4:8"]]
+ 0049fb8c ["CALL", null, ["callee:0049b4e0:8"]]
- 0049fb4c bytes 55eeff97
+ 0049fb8c bytes 55eeff97
- 0049fbf0 ["INT_ADD", "register:40f0:8", ["const:49fbf0:8", "const:4:8"]]
- 0049fbf0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0049fc30 ["INT_ADD", "register:40f0:8", ["const:49fc30:8", "const:4:8"]]
+ 0049fc30 ["CALL", null, ["callee:00c57fe0:8"]]
- 0049fbf0 bytes c8e01e94
+ 0049fc30 bytes ece01e94
- 0049fc24 ["INT_ADD", "register:40f0:8", ["const:49fc24:8", "const:4:8"]]
- 0049fc24 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0049fc64 ["INT_ADD", "register:40f0:8", ["const:49fc64:8", "const:4:8"]]
+ 0049fc64 ["CALL", null, ["callee:00c57fe0:8"]]
- 0049fc24 bytes bbe01e94
+ 0049fc64 bytes dfe01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eb50c192a86fff62b30ad2f15bc9f8ea"></a>

### [`0049fc68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md) → [`0049fca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md) FUN_0049fca8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.59% / 新版 93.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fd6c",
      "incomplete_value": true,
      "site": "0049fd78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd2c",
      "incomplete_value": true,
      "site": "0049fd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4d0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fdb4",
      "incomplete_value": false,
      "site": "0049fdb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:96e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd74",
      "incomplete_value": false,
      "site": "0049fd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:93d:8"
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
      "definition_site": "0049fdd4",
      "incomplete_value": true,
      "site": "0049fdd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fd94",
      "incomplete_value": true,
      "site": "0049fd98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "0049fd6c",
      "READ",
      [
        "storage",
        "002c24d0",
        null,
        null
      ]
    ],
    [
      "0049fdb8",
      "DATA",
      [
        "storage",
        "002b393d",
        null,
        "string"
      ]
    ],
    [
      "0049fdd4",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fd6c",
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ],
    [
      "0049fdb8",
      "DATA",
      [
        "storage",
        "002b396e",
        null,
        "string"
      ]
    ],
    [
      "0049fdd4",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fd98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md#insn-0049fd98) · [`0049fc98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md#insn-0049fc98) · [`0049fcf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md#insn-0049fcf0)
- 新版 `0049fdd8`（命令位置の公開資料なし） · `0049fcd8`（命令位置の公開資料なし） · `0049fd30`（命令位置の公開資料なし）

~~~diff
- 0049fd98 ["INT_ADD", "register:40f0:8", ["const:49fd98:8", "const:4:8"]]
- 0049fd98 ["CALL", null, ["callee:00c57fe0:8"]]
+ 0049fdd8 ["INT_ADD", "register:40f0:8", ["const:49fdd8:8", "const:4:8"]]
+ 0049fdd8 ["CALL", null, ["callee:00c57fe0:8"]]
- 0049fd98 bytes 5ee01e94
+ 0049fdd8 bytes 82e01e94
- 0049fc98 ["INT_ADD", "register:40f0:8", ["const:49fc98:8", "const:4:8"]]
- 0049fc98 ["CALL", null, ["callee:0049b408:8"]]
+ 0049fcd8 ["INT_ADD", "register:40f0:8", ["const:49fcd8:8", "const:4:8"]]
+ 0049fcd8 ["CALL", null, ["callee:0049b408:8"]]
- 0049fc98 bytes ccedff97
+ 0049fcd8 bytes ccedff97
- 0049fcf0 ["INT_ADD", "register:40f0:8", ["const:49fcf0:8", "const:4:8"]]
- 0049fcf0 ["CALL", null, ["callee:0049b4e0:8"]]
+ 0049fd30 ["INT_ADD", "register:40f0:8", ["const:49fd30:8", "const:4:8"]]
+ 0049fd30 ["CALL", null, ["callee:0049b4e0:8"]]
- 0049fcf0 bytes ecedff97
+ 0049fd30 bytes ecedff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f73dfb8a078d5d875c60f9f509ac734"></a>

### [`0049fdd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md) → [`0049fe10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fe10.md) FUN_0049fe10

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 6件 [`0049b3c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 6件 [`0049b408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049fee8",
      "incomplete_value": true,
      "site": "0049fef4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:830:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fea8",
      "incomplete_value": true,
      "site": "0049feb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7f0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0049ff34",
      "incomplete_value": false,
      "site": "0049ff38",
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
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fef4",
      "incomplete_value": false,
      "site": "0049fef8",
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
            "const:bdc:8"
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
      "definition_site": "0049fe7c",
      "incomplete_value": true,
      "site": "0049fe84",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:860:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049fe3c",
      "incomplete_value": true,
      "site": "0049fe44",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:790:8"
              ]
            ]
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
      "0049fe7c",
      "READ",
      [
        "storage",
        "00ca3790",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe7c",
      "PARAM",
      [
        "storage",
        "002bc414",
        null,
        "string"
      ]
    ],
    [
      "0049fe8c",
      "READ",
      [
        "storage",
        "00ca3790",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0049fe7c",
      "READ",
      [
        "storage",
        "00ca3860",
        null,
        "pointer"
      ]
    ],
    [
      "0049fe7c",
      "PARAM",
      [
        "storage",
        "002bc3c0",
        null,
        "string"
      ]
    ],
    [
      "0049fe8c",
      "READ",
      [
        "storage",
        "00ca3860",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049fe04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md#insn-0049fe04) · [`0049fe44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md#insn-0049fe44) · [`0049fef4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md#insn-0049fef4)
- 新版 `0049fe44`（命令位置の公開資料なし） · `0049fe84`（命令位置の公開資料なし） · `0049ff34`（命令位置の公開資料なし）

~~~diff
- 0049fe04 ["INT_ADD", "register:40f0:8", ["const:49fe04:8", "const:4:8"]]
- 0049fe04 ["CALL", null, ["callee:0049b408:8"]]
+ 0049fe44 ["INT_ADD", "register:40f0:8", ["const:49fe44:8", "const:4:8"]]
+ 0049fe44 ["CALL", null, ["callee:0049b408:8"]]
- 0049fe04 bytes 71edff97
+ 0049fe44 bytes 71edff97
- 0049fe44 ["INT_ADD", "register:40f0:8", ["const:49fe44:8", "const:4:8"]]
- 0049fe44 ["CALL", null, ["callee:00c58700:8"]]
+ 0049fe84 ["INT_ADD", "register:40f0:8", ["const:49fe84:8", "const:4:8"]]
+ 0049fe84 ["CALL", null, ["callee:00c58700:8"]]
- 0049fe44 bytes fbe11e94
+ 0049fe84 bytes 1fe21e94
- 0049fef4 ["COPY", "tmp:0:8", ["const:bdc:8"]]
- 0049fef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0049fef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0049fef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0049ff34 ["COPY", "tmp:0:8", ["const:b88:8"]]
+ 0049ff34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0049ff34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0049ff34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0049fef4 bytes 08712f91
+ 0049ff34 bytes 08212e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a602f4c14679059838d0117ddbcd7aeb"></a>

### [`004a0278`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md) → [`004a02b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a02b8.md) FUN_004a02b8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b68c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049b6cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.34% / 新版 94.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004a0374",
      "incomplete_value": false,
      "site": "004a037c",
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
            "const:9ae:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0334",
      "incomplete_value": false,
      "site": "004a033c",
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
            "const:97d:8"
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
      "definition_site": "004a0384",
      "incomplete_value": true,
      "site": "004a0388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0344",
      "incomplete_value": true,
      "site": "004a0348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a037c",
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      "004a0384",
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      "004a0384",
      "PARAM",
      [
        "storage",
        "00c96c40",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a037c",
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      "004a0384",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      "004a0384",
      "PARAM",
      [
        "storage",
        "00c96d10",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0348`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md#insn-004a0348) · [`004a032c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md#insn-004a032c) · [`004a0334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md#insn-004a0334)
- 新版 `004a0388`（命令位置の公開資料なし） · `004a036c`（命令位置の公開資料なし） · `004a0374`（命令位置の公開資料なし）

~~~diff
- 004a0348 ["INT_ADD", "register:40f0:8", ["const:4a0348:8", "const:4:8"]]
- 004a0348 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a0388 ["INT_ADD", "register:40f0:8", ["const:4a0388:8", "const:4:8"]]
+ 004a0388 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a0348 bytes f2de1e94
+ 004a0388 bytes 16df1e94
- 004a032c ["INT_ADD", "register:40f0:8", ["const:4a032c:8", "const:4:8"]]
- 004a032c ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a036c ["INT_ADD", "register:40f0:8", ["const:4a036c:8", "const:4:8"]]
+ 004a036c ["CALL", null, ["callee:00c57fc0:8"]]
- 004a032c bytes f1de1e94
+ 004a036c bytes 15df1e94
- 004a0334 ["COPY", "tmp:0:8", ["const:97d:8"]]
- 004a0334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004a0334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004a0334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004a0374 ["COPY", "tmp:0:8", ["const:9ae:8"]]
+ 004a0374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004a0374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004a0334 bytes 08f52591
+ 004a0374 bytes 08b92691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e929bf3388a8609d74599f359504125e"></a>

### [`004a04e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md) → [`004a0528`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0528.md) FUN_004a0528

採用 · 移動量 `+0x40` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a0368`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md) · 呼出先 1件 [`0043b778`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`004a03a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md) · 呼出先 1件 [`0043b7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

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
      "definition_site": "004a0534",
      "incomplete_value": false,
      "site": "004a0538",
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
      "definition_site": "004a04f4",
      "incomplete_value": false,
      "site": "004a04f8",
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
      "004a0534",
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
      "004a0534",
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

- 旧版 [`004a04f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md#insn-004a04f8) · [`004a04f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md#insn-004a04f4)
- 新版 `004a0538`（命令位置の公開資料なし） · `004a0534`（命令位置の公開資料なし）

~~~diff
- 004a04f8 ["INT_ADD", "register:40f0:8", ["const:4a04f8:8", "const:4:8"]]
- 004a04f8 ["CALL", null, ["callee:0043b7b8:8"]]
+ 004a0538 ["INT_ADD", "register:40f0:8", ["const:4a0538:8", "const:4:8"]]
+ 004a0538 ["CALL", null, ["callee:0043b7b8:8"]]
- 004a04f8 bytes a06cfe97
+ 004a0538 bytes a06cfe97
- 004a04f4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
- 004a04f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a04f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a04f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a0534 ["COPY", "tmp:0:8", ["const:f8c:8"]]
+ 004a0534 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0534 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a0534 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a04f4 bytes 00303d91
+ 004a0534 bytes 00303e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e67f3ffe579bdd602cd1880bf7f4853"></a>

### [`004a0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) → [`004a05a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a05a8.md) _ZNK5Botan7AES_1289encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a0668",
      "incomplete_value": true,
      "site": "004a0674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0628",
      "incomplete_value": true,
      "site": "004a0634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0664",
      "incomplete_value": false,
      "site": "004a0674",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a0624",
      "incomplete_value": false,
      "site": "004a0634",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a0664",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a0668",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a0668",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a0664",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a0668",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a0668",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a05f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md#insn-004a05f4) · [`004a0634`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md#insn-004a0634) · [`004a05dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md#insn-004a05dc)
- 新版 `004a0634`（命令位置の公開資料なし） · `004a0674`（命令位置の公開資料なし） · `004a061c`（命令位置の公開資料なし）

~~~diff
- 004a05f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a05f4 ["INT_ADD", "register:40f0:8", ["const:4a05f4:8", "const:4:8"]]
- 004a05f4 ["CALLIND", null, ["register:0:8"]]
+ 004a0634 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a0634 ["INT_ADD", "register:40f0:8", ["const:4a0634:8", "const:4:8"]]
+ 004a0634 ["CALLIND", null, ["register:0:8"]]
- 004a05f4 bytes 20013fd6
+ 004a0634 bytes 20013fd6
- 004a0634 ["INT_ADD", "register:40f0:8", ["const:4a0634:8", "const:4:8"]]
- 004a0634 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a0674 ["INT_ADD", "register:40f0:8", ["const:4a0674:8", "const:4:8"]]
+ 004a0674 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a0634 bytes 37de1e94
+ 004a0674 bytes 5bde1e94
- 004a05dc ["INT_ADD", "register:40f0:8", ["const:4a05dc:8", "const:4:8"]]
- 004a05dc ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a061c ["INT_ADD", "register:40f0:8", ["const:4a061c:8", "const:4:8"]]
+ 004a061c ["CALL", null, ["callee:00c57fc0:8"]]
- 004a05dc bytes 45de1e94
+ 004a061c bytes 69de1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c876f378d707c7d85f5dbb4e32287bca"></a>

### [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) → [`004a06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) FUN_004a06c8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a0568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) [`004a1b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) [`004a1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) · 呼出先 4件 [`0053593c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/0053593c.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 3件 [`004a05a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a05a8.md) [`004a1bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1bb0.md) [`004a1ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1ecc.md) · 呼出先 4件 [`0053597c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/0053597c.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a0708",
      "incomplete_value": true,
      "site": "004a0708",
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
      "definition_site": "004a06c8",
      "incomplete_value": true,
      "site": "004a06c8",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0c14",
      "incomplete_value": false,
      "site": "004a0c34",
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
            "const:544:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0bd4",
      "incomplete_value": false,
      "site": "004a0bf4",
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
            "const:5a0:8"
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
      "definition_site": "004a0c1c",
      "incomplete_value": false,
      "site": "004a0c34",
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
            "const:1ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0bdc",
      "incomplete_value": false,
      "site": "004a0bf4",
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
            "const:237:8"
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
      "004a0700",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004a0704",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0710",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a0700",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004a0704",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0710",
      "WRITE",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0be8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md#insn-004a0be8) · [`004a0bf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md#insn-004a0bf4) · [`004a0c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md#insn-004a0c10)
- 新版 `004a0c28`（命令位置の公開資料なし） · `004a0c34`（命令位置の公開資料なし） · `004a0c50`（命令位置の公開資料なし）

~~~diff
- 004a0be8 ["COPY", "register:4018:8", ["const:29e000:8"]]
+ 004a0c28 ["COPY", "register:4018:8", ["const:2b1000:8"]]
- 004a0be8 bytes e3efffd0
+ 004a0c28 bytes 83f0ffb0
- 004a0bf4 ["INT_ADD", "register:40f0:8", ["const:4a0bf4:8", "const:4:8"]]
- 004a0bf4 ["CALL", null, ["callee:00c58720:8"]]
+ 004a0c34 ["INT_ADD", "register:40f0:8", ["const:4a0c34:8", "const:4:8"]]
+ 004a0c34 ["CALL", null, ["callee:00c58720:8"]]
- 004a0bf4 bytes 97de1e94
+ 004a0c34 bytes bbde1e94
- 004a0c10 ["INT_ADD", "register:40f0:8", ["const:4a0c10:8", "const:4:8"]]
- 004a0c10 ["CALL", null, ["callee:00c57f20:8"]]
+ 004a0c50 ["INT_ADD", "register:40f0:8", ["const:4a0c50:8", "const:4:8"]]
+ 004a0c50 ["CALL", null, ["callee:00c57f20:8"]]
- 004a0c10 bytes 90dc1e94
+ 004a0c50 bytes b4dc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-857aad48e9c0dd83fe57136ccf57c251"></a>

### [`004a0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) → [`004a0c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0c88.md) _ZNK5Botan7AES_1289decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a0d48",
      "incomplete_value": true,
      "site": "004a0d54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a0d08",
      "incomplete_value": true,
      "site": "004a0d14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a0d44",
      "incomplete_value": false,
      "site": "004a0d54",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a0d04",
      "incomplete_value": false,
      "site": "004a0d14",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a0d44",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a0d48",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d48",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a0d44",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a0d48",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a0d48",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a0cd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md#insn-004a0cd4) · [`004a0d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md#insn-004a0d14) · [`004a0cbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md#insn-004a0cbc)
- 新版 `004a0d14`（命令位置の公開資料なし） · `004a0d54`（命令位置の公開資料なし） · `004a0cfc`（命令位置の公開資料なし）

~~~diff
- 004a0cd4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a0cd4 ["INT_ADD", "register:40f0:8", ["const:4a0cd4:8", "const:4:8"]]
- 004a0cd4 ["CALLIND", null, ["register:0:8"]]
+ 004a0d14 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a0d14 ["INT_ADD", "register:40f0:8", ["const:4a0d14:8", "const:4:8"]]
+ 004a0d14 ["CALLIND", null, ["register:0:8"]]
- 004a0cd4 bytes 20013fd6
+ 004a0d14 bytes 20013fd6
- 004a0d14 ["INT_ADD", "register:40f0:8", ["const:4a0d14:8", "const:4:8"]]
- 004a0d14 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a0d54 ["INT_ADD", "register:40f0:8", ["const:4a0d54:8", "const:4:8"]]
+ 004a0d54 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a0d14 bytes 7fdc1e94
+ 004a0d54 bytes a3dc1e94
- 004a0cbc ["INT_ADD", "register:40f0:8", ["const:4a0cbc:8", "const:4:8"]]
- 004a0cbc ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a0cfc ["INT_ADD", "register:40f0:8", ["const:4a0cfc:8", "const:4:8"]]
+ 004a0cfc ["CALL", null, ["callee:00c57fc0:8"]]
- 004a0cbc bytes 8ddc1e94
+ 004a0cfc bytes b1dc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccbefef55718c794d5e888ce5c57f6e0"></a>

### [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) → [`004a0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) FUN_004a0da8

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`004a0c48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) [`004a1c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) [`004a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) · 呼出先 4件 [`00535a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`00c57e50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 3件 [`004a0c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0c88.md) [`004a1cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1cd0.md) [`004a1fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1fec.md) · 呼出先 4件 [`00535a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535a74.md) [`00c57f20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004a0de8",
      "incomplete_value": true,
      "site": "004a0de8",
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
      "definition_site": "004a0da8",
      "incomplete_value": true,
      "site": "004a0da8",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1300",
      "incomplete_value": false,
      "site": "004a1320",
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
            "const:1f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a12c0",
      "incomplete_value": false,
      "site": "004a12e0",
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
            "const:23f:8"
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
      "definition_site": "004a1308",
      "incomplete_value": false,
      "site": "004a1320",
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
            "const:1ea:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a12c8",
      "incomplete_value": false,
      "site": "004a12e0",
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
            "const:237:8"
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
      "004a0de0",
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      "004a0de4",
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0df0",
      "WRITE",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004a0de0",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004a0de4",
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "004a0df0",
      "WRITE",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a12d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md#insn-004a12d4) · [`004a12e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md#insn-004a12e0) · [`004a12fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md#insn-004a12fc)
- 新版 `004a1314`（命令位置の公開資料なし） · `004a1320`（命令位置の公開資料なし） · `004a133c`（命令位置の公開資料なし）

~~~diff
- 004a12d4 ["COPY", "register:4018:8", ["const:29e000:8"]]
+ 004a1314 ["COPY", "register:4018:8", ["const:2b1000:8"]]
- 004a12d4 bytes e3efffb0
+ 004a1314 bytes 83f0ff90
- 004a12e0 ["INT_ADD", "register:40f0:8", ["const:4a12e0:8", "const:4:8"]]
- 004a12e0 ["CALL", null, ["callee:00c58720:8"]]
+ 004a1320 ["INT_ADD", "register:40f0:8", ["const:4a1320:8", "const:4:8"]]
+ 004a1320 ["CALL", null, ["callee:00c58720:8"]]
- 004a12e0 bytes dcdc1e94
+ 004a1320 bytes 00dd1e94
- 004a12fc ["INT_ADD", "register:40f0:8", ["const:4a12fc:8", "const:4:8"]]
- 004a12fc ["CALL", null, ["callee:00c57f20:8"]]
+ 004a133c ["INT_ADD", "register:40f0:8", ["const:4a133c:8", "const:4:8"]]
+ 004a133c ["CALL", null, ["callee:00c57f20:8"]]
- 004a12fc bytes d5da1e94
+ 004a133c bytes f9da1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-265ffb956220e3d5a261b165622309b0"></a>

### [`004a1354`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md) → [`004a1394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1394.md) FUN_004a1394

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a1334`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1334.md) [`004a1db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1db0.md) [`004a20cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20cc.md) · 呼出先 15件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535a34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 3件 [`004a1374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1374.md) [`004a1df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1df0.md) [`004a210c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a210c.md) · 呼出先 15件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535a74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535a74.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a178c",
      "value": [
        "leaf",
        "ram:535a74:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a174c",
      "value": [
        "leaf",
        "ram:535a34:8"
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
      "site": "004a17a8",
      "value": [
        "leaf",
        "ram:535a74:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1768",
      "value": [
        "leaf",
        "ram:535a34:8"
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a17c4",
      "value": [
        "leaf",
        "ram:535a74:8"
      ]
    },
    "old": {
      "definition_site": null,
      "incomplete_value": true,
      "site": "004a1784",
      "value": [
        "leaf",
        "ram:535a34:8"
      ]
    },
    "ordinal": 9,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a1508",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      "004a150c",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      "004a1510",
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a1508",
      "DATA",
      [
        "storage",
        "002cf380",
        null,
        null
      ]
    ],
    [
      "004a150c",
      "DATA",
      [
        "storage",
        "002cf380",
        null,
        null
      ]
    ],
    [
      "004a1510",
      "DATA",
      [
        "storage",
        "002cf380",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1744`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md#insn-004a1744) · [`004a174c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md#insn-004a174c) · [`004a1760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md#insn-004a1760)
- 新版 `004a1784`（命令位置の公開資料なし） · `004a178c`（命令位置の公開資料なし） · `004a17a0`（命令位置の公開資料なし）

~~~diff
- 004a1744 ["INT_ADD", "register:40f0:8", ["const:4a1744:8", "const:4:8"]]
- 004a1744 ["CALL", null, ["callee:00c57f20:8"]]
+ 004a1784 ["INT_ADD", "register:40f0:8", ["const:4a1784:8", "const:4:8"]]
+ 004a1784 ["CALL", null, ["callee:00c57f20:8"]]
- 004a1744 bytes c3d91e94
+ 004a1784 bytes e7d91e94
- 004a174c ["INT_ADD", "register:40f0:8", ["const:4a174c:8", "const:4:8"]]
- 004a174c ["CALL", null, ["ram:535a34:8"]]
+ 004a178c ["INT_ADD", "register:40f0:8", ["const:4a178c:8", "const:4:8"]]
+ 004a178c ["CALL", null, ["ram:535a74:8"]]
- 004a174c bytes ba500294
+ 004a178c bytes ba500294
- 004a1760 ["INT_ADD", "register:40f0:8", ["const:4a1760:8", "const:4:8"]]
- 004a1760 ["CALL", null, ["callee:00c57f20:8"]]
+ 004a17a0 ["INT_ADD", "register:40f0:8", ["const:4a17a0:8", "const:4:8"]]
+ 004a17a0 ["CALL", null, ["callee:00c57f20:8"]]
- 004a1760 bytes bcd91e94
+ 004a17a0 bytes e0d91e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b863d40804f157536dca64d97b69247"></a>

### [`004a1b70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) → [`004a1bb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1bb0.md) _ZNK5Botan7AES_1929encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a1c70",
      "incomplete_value": true,
      "site": "004a1c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1c30",
      "incomplete_value": true,
      "site": "004a1c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1c6c",
      "incomplete_value": false,
      "site": "004a1c7c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a1c2c",
      "incomplete_value": false,
      "site": "004a1c3c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a1c6c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1c70",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c70",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1c6c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a1c70",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a1c70",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1bfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md#insn-004a1bfc) · [`004a1c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md#insn-004a1c3c) · [`004a1be4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md#insn-004a1be4)
- 新版 `004a1c3c`（命令位置の公開資料なし） · `004a1c7c`（命令位置の公開資料なし） · `004a1c24`（命令位置の公開資料なし）

~~~diff
- 004a1bfc ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1bfc ["INT_ADD", "register:40f0:8", ["const:4a1bfc:8", "const:4:8"]]
- 004a1bfc ["CALLIND", null, ["register:0:8"]]
+ 004a1c3c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1c3c ["INT_ADD", "register:40f0:8", ["const:4a1c3c:8", "const:4:8"]]
+ 004a1c3c ["CALLIND", null, ["register:0:8"]]
- 004a1bfc bytes 20013fd6
+ 004a1c3c bytes 20013fd6
- 004a1c3c ["INT_ADD", "register:40f0:8", ["const:4a1c3c:8", "const:4:8"]]
- 004a1c3c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a1c7c ["INT_ADD", "register:40f0:8", ["const:4a1c7c:8", "const:4:8"]]
+ 004a1c7c ["CALL", null, ["callee:00c57fe0:8"]]
- 004a1c3c bytes b5d81e94
+ 004a1c7c bytes d9d81e94
- 004a1be4 ["INT_ADD", "register:40f0:8", ["const:4a1be4:8", "const:4:8"]]
- 004a1be4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a1c24 ["INT_ADD", "register:40f0:8", ["const:4a1c24:8", "const:4:8"]]
+ 004a1c24 ["CALL", null, ["callee:00c57fc0:8"]]
- 004a1be4 bytes c3d81e94
+ 004a1c24 bytes e7d81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff18db0a31e84f332b9fc2ac080f10be"></a>

### [`004a1c90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) → [`004a1cd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1cd0.md) _ZNK5Botan7AES_1929decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a1d90",
      "incomplete_value": true,
      "site": "004a1d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1d50",
      "incomplete_value": true,
      "site": "004a1d5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1d8c",
      "incomplete_value": false,
      "site": "004a1d9c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a1d4c",
      "incomplete_value": false,
      "site": "004a1d5c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a1d8c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1d90",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1d90",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1d8c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a1d90",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a1d90",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1d1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md#insn-004a1d1c) · [`004a1d5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md#insn-004a1d5c) · [`004a1d04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md#insn-004a1d04)
- 新版 `004a1d5c`（命令位置の公開資料なし） · `004a1d9c`（命令位置の公開資料なし） · `004a1d44`（命令位置の公開資料なし）

~~~diff
- 004a1d1c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1d1c ["INT_ADD", "register:40f0:8", ["const:4a1d1c:8", "const:4:8"]]
- 004a1d1c ["CALLIND", null, ["register:0:8"]]
+ 004a1d5c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1d5c ["INT_ADD", "register:40f0:8", ["const:4a1d5c:8", "const:4:8"]]
+ 004a1d5c ["CALLIND", null, ["register:0:8"]]
- 004a1d1c bytes 20013fd6
+ 004a1d5c bytes 20013fd6
- 004a1d5c ["INT_ADD", "register:40f0:8", ["const:4a1d5c:8", "const:4:8"]]
- 004a1d5c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a1d9c ["INT_ADD", "register:40f0:8", ["const:4a1d9c:8", "const:4:8"]]
+ 004a1d9c ["CALL", null, ["callee:00c57fe0:8"]]
- 004a1d5c bytes 6dd81e94
+ 004a1d9c bytes 91d81e94
- 004a1d04 ["INT_ADD", "register:40f0:8", ["const:4a1d04:8", "const:4:8"]]
- 004a1d04 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a1d44 ["INT_ADD", "register:40f0:8", ["const:4a1d44:8", "const:4:8"]]
+ 004a1d44 ["CALL", null, ["callee:00c57fc0:8"]]
- 004a1d04 bytes 7bd81e94
+ 004a1d44 bytes 9fd81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb42b3eb866a9765a27872f06cbbc3c"></a>

### [`004a1e8c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) → [`004a1ecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1ecc.md) _ZNK5Botan7AES_2569encrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a1f8c",
      "incomplete_value": true,
      "site": "004a1f98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a1f4c",
      "incomplete_value": true,
      "site": "004a1f58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a1f88",
      "incomplete_value": false,
      "site": "004a1f98",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a1f48",
      "incomplete_value": false,
      "site": "004a1f58",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a1f88",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a1f8c",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a1f8c",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a1f88",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a1f8c",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a1f8c",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a1f18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md#insn-004a1f18) · [`004a1f58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md#insn-004a1f58) · [`004a1f00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md#insn-004a1f00)
- 新版 `004a1f58`（命令位置の公開資料なし） · `004a1f98`（命令位置の公開資料なし） · `004a1f40`（命令位置の公開資料なし）

~~~diff
- 004a1f18 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a1f18 ["INT_ADD", "register:40f0:8", ["const:4a1f18:8", "const:4:8"]]
- 004a1f18 ["CALLIND", null, ["register:0:8"]]
+ 004a1f58 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a1f58 ["INT_ADD", "register:40f0:8", ["const:4a1f58:8", "const:4:8"]]
+ 004a1f58 ["CALLIND", null, ["register:0:8"]]
- 004a1f18 bytes 20013fd6
+ 004a1f58 bytes 20013fd6
- 004a1f58 ["INT_ADD", "register:40f0:8", ["const:4a1f58:8", "const:4:8"]]
- 004a1f58 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a1f98 ["INT_ADD", "register:40f0:8", ["const:4a1f98:8", "const:4:8"]]
+ 004a1f98 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a1f58 bytes eed71e94
+ 004a1f98 bytes 12d81e94
- 004a1f00 ["INT_ADD", "register:40f0:8", ["const:4a1f00:8", "const:4:8"]]
- 004a1f00 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a1f40 ["INT_ADD", "register:40f0:8", ["const:4a1f40:8", "const:4:8"]]
+ 004a1f40 ["CALL", null, ["callee:00c57fc0:8"]]
- 004a1f00 bytes fcd71e94
+ 004a1f40 bytes 20d81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82aa1ea4f2813f0a604b66504826aa29"></a>

### [`004a1fac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) → [`004a1fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1fec.md) _ZNK5Botan7AES_2569decrypt_nEPKhPhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004a20ac",
      "incomplete_value": true,
      "site": "004a20b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a206c",
      "incomplete_value": true,
      "site": "004a2078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a20a8",
      "incomplete_value": false,
      "site": "004a20b8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a2068",
      "incomplete_value": false,
      "site": "004a2078",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a20a8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a20ac",
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      "004a20ac",
      "PARAM",
      [
        "storage",
        "00c69b58",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a20a8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a20ac",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004a20ac",
      "PARAM",
      [
        "storage",
        "00c69c28",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2038`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md#insn-004a2038) · [`004a2078`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md#insn-004a2078) · [`004a2020`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md#insn-004a2020)
- 新版 `004a2078`（命令位置の公開資料なし） · `004a20b8`（命令位置の公開資料なし） · `004a2060`（命令位置の公開資料なし）

~~~diff
- 004a2038 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a2038 ["INT_ADD", "register:40f0:8", ["const:4a2038:8", "const:4:8"]]
- 004a2038 ["CALLIND", null, ["register:0:8"]]
+ 004a2078 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a2078 ["INT_ADD", "register:40f0:8", ["const:4a2078:8", "const:4:8"]]
+ 004a2078 ["CALLIND", null, ["register:0:8"]]
- 004a2038 bytes 20013fd6
+ 004a2078 bytes 20013fd6
- 004a2078 ["INT_ADD", "register:40f0:8", ["const:4a2078:8", "const:4:8"]]
- 004a2078 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a20b8 ["INT_ADD", "register:40f0:8", ["const:4a20b8:8", "const:4:8"]]
+ 004a20b8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a2078 bytes a6d71e94
+ 004a20b8 bytes cad71e94
- 004a2020 ["INT_ADD", "register:40f0:8", ["const:4a2020:8", "const:4:8"]]
- 004a2020 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a2060 ["INT_ADD", "register:40f0:8", ["const:4a2060:8", "const:4:8"]]
+ 004a2060 ["CALL", null, ["callee:00c57fc0:8"]]
- 004a2020 bytes b4d71e94
+ 004a2060 bytes d8d71e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e65614ea16d441a507927020a063b63"></a>

### [`004a21a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) → [`004a21e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a21e8.md) _ZN5Botan19AlgorithmIdentifierC1ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59440`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59440.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c59510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59510.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2230",
      "incomplete_value": true,
      "site": "004a2230",
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
      "definition_site": "004a21f0",
      "incomplete_value": true,
      "site": "004a21f0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2230",
      "incomplete_value": true,
      "site": "004a2230",
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
      "definition_site": "004a21f0",
      "incomplete_value": true,
      "site": "004a21f0",
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
      "004a2210",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a221c",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a2230",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a2210",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004a221c",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "004a2230",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a21d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md#insn-004a21d0) · [`004a21d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md#insn-004a21d8) · [`004a21dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md#insn-004a21dc)
- 新版 `004a2210`（命令位置の公開資料なし） · `004a221c`（命令位置の公開資料なし）

~~~diff
- 004a21d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
- 004a21d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2210 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
+ 004a2210 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a21d0 bytes 089d46f9
+ 004a2210 bytes 080547f9
- 004a21d8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a21d8 bytes f30300aa
- 004a21dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 004a21dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a221c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 004a221c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a21dc bytes 29a146f9
+ 004a221c bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d26c2b2161b896e623455895268633a"></a>

### [`004a22e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md) → [`004a2324`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a2324.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58e20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e20.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c58ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ef0.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2350",
      "incomplete_value": true,
      "site": "004a2350",
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
      "definition_site": "004a2310",
      "incomplete_value": true,
      "site": "004a2310",
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
      "004a2340",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a2350",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a2340",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004a2350",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a2350`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md#insn-004a2350) · [`004a2300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md#insn-004a2300) · [`004a2308`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md#insn-004a2308)
- 新版 `004a2390`（命令位置の公開資料なし） · `004a2340`（命令位置の公開資料なし）

~~~diff
- 004a2350 ["INT_ADD", "register:40f0:8", ["const:4a2350:8", "const:4:8"]]
- 004a2350 ["CALL", null, ["callee:00c580d0:8"]]
+ 004a2390 ["INT_ADD", "register:40f0:8", ["const:4a2390:8", "const:4:8"]]
+ 004a2390 ["CALL", null, ["callee:00c580d0:8"]]
- 004a2350 bytes 2cd71e94
+ 004a2390 bytes 50d71e94
- 004a2300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
- 004a2300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a2340 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
+ 004a2340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a2300 bytes 089d46f9
+ 004a2340 bytes 080547f9
- 004a2308 ["COPY", "register:4040:8", ["register:4000:8"]]
- 004a2308 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02be7ae7d3a42dca1564c276825fc696"></a>

### [`004a23b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md) → [`004a23f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a23f0.md) _ZN5Botan4OIDS6lookupERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call, call_argument_candidate, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 27.75% / 新版 27.75%

CFGの説明率　旧版 25.97% / 新版 25.97%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 89件, `store_value` 12件, `unresolved_branch_alignment` 122件, `unresolved_call_alignment` 416件

アドレスに依存する影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a25ac",
      "incomplete_value": true,
      "site": "004a25bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cfc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a256c",
      "incomplete_value": true,
      "site": "004a257c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ccb:8"
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
      "definition_site": "004a25c0",
      "incomplete_value": true,
      "site": "004a25c0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a2580",
      "incomplete_value": true,
      "site": "004a2580",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a2614",
      "incomplete_value": true,
      "site": "004a2624",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:182:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a25d4",
      "incomplete_value": true,
      "site": "004a25e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:142:8"
              ]
            ]
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
      "004a253c",
      "PARAM",
      [
        "storage",
        "002a8b70",
        null,
        "string"
      ]
    ],
    [
      "004a2548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:004a252c"
      ]
    ],
    [
      "unmatched:004a2510",
      "PARAM",
      [
        "storage",
        "002bb2d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a253c",
      "PARAM",
      [
        "storage",
        "002a8b14",
        null,
        "string"
      ]
    ],
    [
      "004a2548",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004a256c"
      ]
    ],
    [
      "004a2550",
      "PARAM",
      [
        "storage",
        "002bb27d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a24fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md#insn-004a24fc) · [`004a253c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md#insn-004a253c) · [`004a2564`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md#insn-004a2564)
- 新版 `004a253c`（命令位置の公開資料なし） · `004a25a4`（命令位置の公開資料なし）

~~~diff
- 004a24fc ["COPY", "tmp:0:8", ["const:b70:8"]]
- 004a24fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a24fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a24fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["COPY", "tmp:0:8", ["const:b14:8"]]
+ 004a253c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a24fc bytes 21c02d91
+ 004a253c bytes 21502c91
- 004a253c ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004a253c ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004a253c ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004a253c ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004a253c bytes c0020036
- 004a2564 ["COPY", "tmp:0:8", ["const:ccb:8"]]
- 004a2564 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004a2564 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004a2564 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004a25a4 ["COPY", "tmp:0:8", ["const:cfc:8"]]
+ 004a25a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004a25a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004a25a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004a2564 bytes 292d3391
+ 004a25a4 bytes 29f13391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5137ffa5871634acd6854e94d3979cc5"></a>

### [`004a502c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md) → [`004a506c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a506c.md) _ZN5Botan19AlgorithmIdentifierC2ERKNS_3OIDENS0_15Encoding_OptionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md) · 呼出先 5件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c597f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597f0.md) · 呼出先 5件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a50b4",
      "incomplete_value": true,
      "site": "004a50b4",
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
      "definition_site": "004a5074",
      "incomplete_value": true,
      "site": "004a5074",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a50b4",
      "incomplete_value": true,
      "site": "004a50b4",
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
      "definition_site": "004a5074",
      "incomplete_value": true,
      "site": "004a5074",
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
      "004a5094",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a50a0",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a50b4",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5094",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004a50a0",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "004a50b4",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5054`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md#insn-004a5054) · [`004a505c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md#insn-004a505c) · [`004a5060`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md#insn-004a5060)
- 新版 `004a5094`（命令位置の公開資料なし） · `004a50a0`（命令位置の公開資料なし）

~~~diff
- 004a5054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
- 004a5054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
+ 004a5094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5054 bytes 089d46f9
+ 004a5094 bytes 080547f9
- 004a505c ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a505c bytes f30300aa
- 004a5060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 004a5060 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a50a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 004a50a0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5060 bytes 29a146f9
+ 004a50a0 bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c6e397488f22e7a5177a105fe8c09a"></a>

### [`004a5118`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md) → [`004a5158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5158.md) _ZN5Botan19AlgorithmIdentifierC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e10.md) · 呼出先 2件 [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c58ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ee0.md) · 呼出先 2件 [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5174",
      "incomplete_value": true,
      "site": "004a5178",
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
      "definition_site": "004a5134",
      "incomplete_value": true,
      "site": "004a5138",
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
      "004a5170",
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      "004a5178",
      "DATA",
      [
        "storage",
        "00c661a8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5170",
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      "004a5178",
      "DATA",
      [
        "storage",
        "00c66278",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md#insn-004a5130) · [`004a5144`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md#insn-004a5144) · [`004a5158`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md#insn-004a5158)
- 新版 `004a5170`（命令位置の公開資料なし） · `004a5184`（命令位置の公開資料なし） · `004a5198`（命令位置の公開資料なし）

~~~diff
- 004a5130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
- 004a5130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5170 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
+ 004a5170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5130 bytes 089d46f9
+ 004a5170 bytes 080547f9
- 004a5144 ["INT_ADD", "register:40f0:8", ["const:4a5144:8", "const:4:8"]]
- 004a5144 ["CALL", null, ["callee:00c58750:8"]]
+ 004a5184 ["INT_ADD", "register:40f0:8", ["const:4a5184:8", "const:4:8"]]
+ 004a5184 ["CALL", null, ["callee:00c58750:8"]]
- 004a5144 bytes 4fcd1e94
+ 004a5184 bytes 73cd1e94
- 004a5158 ["INT_ADD", "register:40f0:8", ["const:4a5158:8", "const:4:8"]]
- 004a5158 ["CALL", null, ["callee:00c57f60:8"]]
+ 004a5198 ["INT_ADD", "register:40f0:8", ["const:4a5198:8", "const:4:8"]]
+ 004a5198 ["CALL", null, ["callee:00c57f60:8"]]
- 004a5158 bytes 4ecb1e94
+ 004a5198 bytes 72cb1e94
~~~


<a id="compare-2d4fe764862ebc721a9fd3f42d7f6ed1"></a>

### [`004a53d8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md) → [`004a5418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5418.md) _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) · 呼出先 6件 [`00542f88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542f88.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c586e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586e0.md)
- 新版 呼出元 1件 [`00c58780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) · 呼出先 6件 [`00542fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fc8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587b0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a5500",
      "incomplete_value": true,
      "site": "004a5500",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004a54c0",
      "incomplete_value": true,
      "site": "004a54c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a5540",
      "incomplete_value": true,
      "site": "004a5540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a5500",
      "incomplete_value": true,
      "site": "004a5500",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004a54f0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a5530",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a54f0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004a5530",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a54c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md#insn-004a54c0) · [`004a5500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md#insn-004a5500) · [`004a5404`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md#insn-004a5404)
- 新版 `004a5500`（命令位置の公開資料なし） · `004a5540`（命令位置の公開資料なし） · `004a5444`（命令位置の公開資料なし）

~~~diff
- 004a54c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a54c0 ["INT_ADD", "register:40f0:8", ["const:4a54c0:8", "const:4:8"]]
- 004a54c0 ["CALLIND", null, ["register:0:8"]]
+ 004a5500 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a5500 ["INT_ADD", "register:40f0:8", ["const:4a5500:8", "const:4:8"]]
+ 004a5500 ["CALLIND", null, ["register:0:8"]]
- 004a54c0 bytes 20013fd6
+ 004a5500 bytes 20013fd6
- 004a5500 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a5500 ["INT_ADD", "register:40f0:8", ["const:4a5500:8", "const:4:8"]]
- 004a5500 ["CALLIND", null, ["register:0:8"]]
+ 004a5540 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a5540 ["INT_ADD", "register:40f0:8", ["const:4a5540:8", "const:4:8"]]
+ 004a5540 ["CALLIND", null, ["register:0:8"]]
- 004a5500 bytes 20013fd6
+ 004a5540 bytes 20013fd6
- 004a5404 ["INT_ADD", "register:40f0:8", ["const:4a5404:8", "const:4:8"]]
- 004a5404 ["CALL", null, ["callee:00c587b0:8"]]
+ 004a5444 ["INT_ADD", "register:40f0:8", ["const:4a5444:8", "const:4:8"]]
+ 004a5444 ["CALL", null, ["callee:00c587b0:8"]]
- 004a5404 bytes b7cc1e94
+ 004a5444 bytes dbcc1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aadb52a89e20e2f604634ee02b2f8b91"></a>

### [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) → [`004a55dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) _ZN5Botan11DER_Encoder8end_consEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 1件 [`00c587a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md) · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.94% / 新版 97.94%

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
      "definition_site": "004a56cc",
      "incomplete_value": true,
      "site": "004a56cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a568c",
      "incomplete_value": true,
      "site": "004a568c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004a5714",
      "incomplete_value": false,
      "site": "004a571c",
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
            "const:f18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a56d4",
      "incomplete_value": false,
      "site": "004a56dc",
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
            "const:ed8:8"
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
      "definition_site": "004a574c",
      "incomplete_value": true,
      "site": "004a5758",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a570c",
      "incomplete_value": true,
      "site": "004a5718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "004a56bc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a5714",
      "PARAM",
      [
        "storage",
        "002b5ed8",
        null,
        "string"
      ]
    ],
    [
      "004a5748",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a56bc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004a5714",
      "PARAM",
      [
        "storage",
        "002b5f18",
        null,
        "string"
      ]
    ],
    [
      "004a5748",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a568c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md#insn-004a568c) · [`004a56dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md#insn-004a56dc) · [`004a5718`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md#insn-004a5718)
- 新版 `004a56cc`（命令位置の公開資料なし） · `004a571c`（命令位置の公開資料なし） · `004a5758`（命令位置の公開資料なし）

~~~diff
- 004a568c ["COPY", "register:0:8", ["register:4048:8"]]
- 004a568c ["INT_ADD", "register:40f0:8", ["const:4a568c:8", "const:4:8"]]
- 004a568c ["CALLIND", null, ["register:0:8"]]
+ 004a56cc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a56cc ["INT_ADD", "register:40f0:8", ["const:4a56cc:8", "const:4:8"]]
+ 004a56cc ["CALLIND", null, ["register:0:8"]]
- 004a568c bytes 20013fd6
+ 004a56cc bytes 20013fd6
- 004a56dc ["INT_ADD", "register:40f0:8", ["const:4a56dc:8", "const:4:8"]]
- 004a56dc ["CALL", null, ["callee:0043de18:8"]]
+ 004a571c ["INT_ADD", "register:40f0:8", ["const:4a571c:8", "const:4:8"]]
+ 004a571c ["CALL", null, ["callee:0043de18:8"]]
- 004a56dc bytes bf61fe97
+ 004a571c bytes bf61fe97
- 004a5718 ["INT_ADD", "register:40f0:8", ["const:4a5718:8", "const:4:8"]]
- 004a5718 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a5758 ["INT_ADD", "register:40f0:8", ["const:4a5758:8", "const:4:8"]]
+ 004a5758 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a5718 bytes fec91e94
+ 004a5758 bytes 22ca1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beeae495f223e2594eda2e8354e3f56d"></a>

### [`004a5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) → [`004a5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5b20.md) _ZN5Botan11BER_Decoder8end_consEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.67% / 新版 94.67%

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
      "definition_site": "004a5b9c",
      "incomplete_value": false,
      "site": "004a5ba4",
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
            "const:b1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a5b5c",
      "incomplete_value": false,
      "site": "004a5b64",
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
            "const:b72:8"
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
      "definition_site": "004a5bd8",
      "incomplete_value": true,
      "site": "004a5be4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a5b98",
      "incomplete_value": true,
      "site": "004a5ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "definition_site": "004a5bd4",
      "incomplete_value": false,
      "site": "004a5be4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a5b94",
      "incomplete_value": false,
      "site": "004a5ba4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a5b9c",
      "PARAM",
      [
        "storage",
        "002beb72",
        null,
        "string"
      ]
    ],
    [
      "004a5bd4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a5bd8",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a5b9c",
      "PARAM",
      [
        "storage",
        "002beb1e",
        null,
        "string"
      ]
    ],
    [
      "004a5bd4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a5bd8",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5b64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md#insn-004a5b64) · [`004a5ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md#insn-004a5ba4) · [`004a5bc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md#insn-004a5bc8)
- 新版 `004a5ba4`（命令位置の公開資料なし） · `004a5be4`（命令位置の公開資料なし） · `004a5c08`（命令位置の公開資料なし）

~~~diff
- 004a5b64 ["INT_ADD", "register:40f0:8", ["const:4a5b64:8", "const:4:8"]]
- 004a5b64 ["CALL", null, ["callee:0043de18:8"]]
+ 004a5ba4 ["INT_ADD", "register:40f0:8", ["const:4a5ba4:8", "const:4:8"]]
+ 004a5ba4 ["CALL", null, ["callee:0043de18:8"]]
- 004a5b64 bytes 9d60fe97
+ 004a5ba4 bytes 9d60fe97
- 004a5ba4 ["INT_ADD", "register:40f0:8", ["const:4a5ba4:8", "const:4:8"]]
- 004a5ba4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a5be4 ["INT_ADD", "register:40f0:8", ["const:4a5be4:8", "const:4:8"]]
+ 004a5be4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a5ba4 bytes dbc81e94
+ 004a5be4 bytes ffc81e94
- 004a5bc8 ["INT_ADD", "register:40f0:8", ["const:4a5bc8:8", "const:4:8"]]
- 004a5bc8 ["CALL", null, ["callee:0043de18:8"]]
+ 004a5c08 ["INT_ADD", "register:40f0:8", ["const:4a5c08:8", "const:4:8"]]
+ 004a5c08 ["CALL", null, ["callee:0043de18:8"]]
- 004a5bc8 bytes 8460fe97
+ 004a5c08 bytes 8460fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aeefafb5624a0c22b6f943410860f2b3"></a>

### [`004a5ccc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md) → [`004a5d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5d0c.md) _ZN5Botan9AttributeC2ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5d54",
      "incomplete_value": true,
      "site": "004a5d54",
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
      "definition_site": "004a5d14",
      "incomplete_value": true,
      "site": "004a5d14",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5d54",
      "incomplete_value": true,
      "site": "004a5d54",
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
      "definition_site": "004a5d14",
      "incomplete_value": true,
      "site": "004a5d14",
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
      "004a5d34",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d40",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d54",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5d34",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d40",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "004a5d54",
      "DATA",
      [
        "storage",
        "00c662a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md#insn-004a5cf4) · [`004a5cfc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md#insn-004a5cfc) · [`004a5d00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md#insn-004a5d00)
- 新版 `004a5d34`（命令位置の公開資料なし） · `004a5d40`（命令位置の公開資料なし）

~~~diff
- 004a5cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 004a5cf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
+ 004a5d34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5cf4 bytes 08ad46f9
+ 004a5d34 bytes 081547f9
- 004a5cfc ["COPY", "register:4098:8", ["register:4000:8"]]
- 004a5cfc bytes f30300aa
- 004a5d00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
- 004a5d00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5d40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
+ 004a5d40 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5d00 bytes 29a146f9
+ 004a5d40 bytes 290947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-941908b1b2e0177abd77a7e44b4ab47b"></a>

### [`004a5df0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md) → [`004a5e30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5e30.md) _ZN5Botan9AttributeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c59f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f60.md) · 呼出先 4件 [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c5a030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a030.md) · 呼出先 4件 [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a5e5c",
      "incomplete_value": true,
      "site": "004a5e5c",
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
      "definition_site": "004a5e1c",
      "incomplete_value": true,
      "site": "004a5e1c",
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
      "004a5e4c",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a5e5c",
      "DATA",
      [
        "storage",
        "00c661d8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a5e4c",
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      "004a5e5c",
      "DATA",
      [
        "storage",
        "00c662a8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a5e5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md#insn-004a5e5c) · [`004a5e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md#insn-004a5e0c) · [`004a5e14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md#insn-004a5e14)
- 新版 `004a5e9c`（命令位置の公開資料なし） · `004a5e4c`（命令位置の公開資料なし）

~~~diff
- 004a5e5c ["INT_ADD", "register:40f0:8", ["const:4a5e5c:8", "const:4:8"]]
- 004a5e5c ["CALL", null, ["callee:00c580d0:8"]]
+ 004a5e9c ["INT_ADD", "register:40f0:8", ["const:4a5e9c:8", "const:4:8"]]
+ 004a5e9c ["CALL", null, ["callee:00c580d0:8"]]
- 004a5e5c bytes 69c81e94
+ 004a5e9c bytes 8dc81e94
- 004a5e0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
- 004a5e0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a5e4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
+ 004a5e4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a5e0c bytes 08ad46f9
+ 004a5e4c bytes 081547f9
- 004a5e14 ["COPY", "register:4040:8", ["register:4000:8"]]
- 004a5e14 bytes e80300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4365f8da7681e14d86cafecba384937c"></a>

### [`004a5fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) → [`004a5fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) _ZN5Botan9Attribute11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0050e044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) · 呼出先 6件 [`004a5980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md)
- 新版 呼出元 1件 [`0050e084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) · 呼出先 6件 [`004a59c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a6090",
      "incomplete_value": true,
      "site": "004a6090",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004a6050",
      "incomplete_value": true,
      "site": "004a6050",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a60d4",
      "incomplete_value": true,
      "site": "004a60d4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004a6094",
      "incomplete_value": true,
      "site": "004a6094",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "004a6080",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a60c4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6080",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004a60c4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6010`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md#insn-004a6010) · [`004a6050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md#insn-004a6050) · [`004a6094`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md#insn-004a6094)
- 新版 `004a6050`（命令位置の公開資料なし） · `004a6090`（命令位置の公開資料なし） · `004a60d4`（命令位置の公開資料なし）

~~~diff
- 004a6010 ["INT_ADD", "register:40f0:8", ["const:4a6010:8", "const:4:8"]]
- 004a6010 ["CALL", null, ["callee:00c587e0:8"]]
+ 004a6050 ["INT_ADD", "register:40f0:8", ["const:4a6050:8", "const:4:8"]]
+ 004a6050 ["CALL", null, ["callee:00c587e0:8"]]
- 004a6010 bytes c0c91e94
+ 004a6050 bytes e4c91e94
- 004a6050 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6050 ["INT_ADD", "register:40f0:8", ["const:4a6050:8", "const:4:8"]]
- 004a6050 ["CALLIND", null, ["register:0:8"]]
+ 004a6090 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a6090 ["INT_ADD", "register:40f0:8", ["const:4a6090:8", "const:4:8"]]
+ 004a6090 ["CALLIND", null, ["register:0:8"]]
- 004a6050 bytes 20013fd6
+ 004a6090 bytes 20013fd6
- 004a6094 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a6094 ["INT_ADD", "register:40f0:8", ["const:4a6094:8", "const:4:8"]]
- 004a6094 ["CALLIND", null, ["register:0:8"]]
+ 004a60d4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a60d4 ["INT_ADD", "register:40f0:8", ["const:4a60d4:8", "const:4:8"]]
+ 004a60d4 ["CALLIND", null, ["register:0:8"]]
- 004a6094 bytes 20013fd6
+ 004a60d4 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f097595cb655378a6ee54f6cb674751"></a>

### [`004a6104`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md) → [`004a6144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6144.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58760`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58760.md) · 呼出先 5件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c58160`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c58830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58830.md) · 呼出先 5件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58230`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.65% / 新版 88.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6260",
      "incomplete_value": true,
      "site": "004a6260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:403:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6220",
      "incomplete_value": true,
      "site": "004a6220",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45f:8"
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
      "definition_site": "004a6338",
      "incomplete_value": true,
      "site": "004a6338",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:995:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a62f8",
      "incomplete_value": true,
      "site": "004a62f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:964:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6280",
      "incomplete_value": false,
      "site": "004a628c",
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
            "const:de4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6240",
      "incomplete_value": false,
      "site": "004a624c",
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
            "const:e38:8"
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
      "004a6178",
      "DATA",
      [
        "storage",
        "002ca758",
        "switchD_004a6140::switchdataD_002ca758",
        "byte"
      ]
    ],
    [
      "004a624c",
      "READ",
      [
        "storage",
        "002a645f",
        null,
        "string"
      ]
    ],
    [
      "004a6280",
      "PARAM",
      [
        "storage",
        "002b8e38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a6178",
      "DATA",
      [
        "storage",
        "002ca798",
        "switchD_004a6180::switchdataD_002ca798",
        "byte"
      ]
    ],
    [
      "004a624c",
      "READ",
      [
        "storage",
        "002a6403",
        null,
        "string"
      ]
    ],
    [
      "004a6280",
      "PARAM",
      [
        "storage",
        "002b8de4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a624c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md#insn-004a624c) · [`004a6274`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md#insn-004a6274) · [`004a6130`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md#insn-004a6130)
- 新版 `004a628c`（命令位置の公開資料なし） · `004a62b4`（命令位置の公開資料なし） · `004a6170`（命令位置の公開資料なし）

~~~diff
- 004a624c ["INT_ADD", "register:40f0:8", ["const:4a624c:8", "const:4:8"]]
- 004a624c ["CALL", null, ["callee:00c58030:8"]]
+ 004a628c ["INT_ADD", "register:40f0:8", ["const:4a628c:8", "const:4:8"]]
+ 004a628c ["CALL", null, ["callee:00c58030:8"]]
- 004a624c bytes 45c71e94
+ 004a628c bytes 69c71e94
- 004a6274 ["INT_ADD", "register:40f0:8", ["const:4a6274:8", "const:4:8"]]
- 004a6274 ["CALL", null, ["callee:00c58040:8"]]
+ 004a62b4 ["INT_ADD", "register:40f0:8", ["const:4a62b4:8", "const:4:8"]]
+ 004a62b4 ["CALL", null, ["callee:00c58040:8"]]
- 004a6274 bytes 3fc71e94
+ 004a62b4 bytes 63c71e94
- 004a6130 ["COPY", "tmp:0:8", ["const:758:8"]]
- 004a6130 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004a6130 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004a6130 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004a6170 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 004a6170 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004a6170 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004a6170 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004a6130 bytes 4a611d91
+ 004a6170 bytes 4a611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5ba47765cf0dea1624a07893ed57705"></a>

### [`004a642c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md) → [`004a646c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a646c.md) _ZN5Botan18BER_Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58770`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58770.md) [`00c58850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58850.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)
- 新版 呼出元 2件 [`00c58840`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58840.md) [`00c58920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58920.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a64d0",
      "incomplete_value": true,
      "site": "004a64d4",
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
      "definition_site": "004a6490",
      "incomplete_value": true,
      "site": "004a6494",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a64f0",
      "incomplete_value": true,
      "site": "004a64f4",
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
      "definition_site": "004a64b0",
      "incomplete_value": true,
      "site": "004a64b4",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a650c",
      "incomplete_value": true,
      "site": "004a6510",
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
      "definition_site": "004a64cc",
      "incomplete_value": true,
      "site": "004a64d0",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a6488",
      "PARAM",
      [
        "storage",
        "002a3028",
        null,
        "string"
      ]
    ],
    [
      "004a64a0",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004a64b4",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a6488",
      "PARAM",
      [
        "storage",
        "002a2fdb",
        null,
        "string"
      ]
    ],
    [
      "004a64a0",
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      "004a64b4",
      "PARAM",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6458`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md#insn-004a6458) · [`004a646c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md#insn-004a646c) · [`004a6474`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md#insn-004a6474)
- 新版 `004a6498`（命令位置の公開資料なし） · `004a64ac`（命令位置の公開資料なし） · `004a64b4`（命令位置の公開資料なし）

~~~diff
- 004a6458 ["INT_ADD", "register:40f0:8", ["const:4a6458:8", "const:4:8"]]
- 004a6458 ["CALL", null, ["callee:00c58180:8"]]
+ 004a6498 ["INT_ADD", "register:40f0:8", ["const:4a6498:8", "const:4:8"]]
+ 004a6498 ["CALL", null, ["callee:00c58180:8"]]
- 004a6458 bytes 16c71e94
+ 004a6498 bytes 3ac71e94
- 004a646c ["INT_ADD", "register:40f0:8", ["const:4a646c:8", "const:4:8"]]
- 004a646c ["CALL", null, ["callee:00c58180:8"]]
+ 004a64ac ["INT_ADD", "register:40f0:8", ["const:4a64ac:8", "const:4:8"]]
+ 004a64ac ["CALL", null, ["callee:00c58180:8"]]
- 004a646c bytes 11c71e94
+ 004a64ac bytes 35c71e94
- 004a6474 ["COPY", "tmp:0:8", ["const:44e:8"]]
- 004a6474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a6474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a6474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a64b4 ["COPY", "tmp:0:8", ["const:3f2:8"]]
+ 004a64b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a64b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a64b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a6474 bytes 21381191
+ 004a64b4 bytes 21c80f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e65bc218d98bab3f120e71c753cacc56"></a>

### [`004a653c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md) → [`004a657c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a657c.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58750`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58750.md) · 呼出先 4件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)
- 新版 呼出元 1件 [`00c58820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58820.md) · 呼出先 4件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a65cc",
      "incomplete_value": true,
      "site": "004a65d0",
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
      "definition_site": "004a658c",
      "incomplete_value": true,
      "site": "004a6590",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a65e8",
      "incomplete_value": true,
      "site": "004a65ec",
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
      "definition_site": "004a65a8",
      "incomplete_value": true,
      "site": "004a65ac",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6598",
      "incomplete_value": false,
      "site": "004a65a8",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a6558",
      "incomplete_value": false,
      "site": "004a6568",
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
            "const:e24:8"
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
      "004a6598",
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      "004a65b0",
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      "004a65c4",
      "READ",
      [
        "storage",
        "00c9ad60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a6598",
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      "004a65b0",
      "PARAM",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ],
    [
      "004a65c4",
      "READ",
      [
        "storage",
        "00c9ae30",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a6568`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md#insn-004a6568) · [`004a657c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md#insn-004a657c) · [`004a6558`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md#insn-004a6558)
- 新版 `004a65a8`（命令位置の公開資料なし） · `004a65bc`（命令位置の公開資料なし） · `004a6598`（命令位置の公開資料なし）

~~~diff
- 004a6568 ["INT_ADD", "register:40f0:8", ["const:4a6568:8", "const:4:8"]]
- 004a6568 ["CALL", null, ["callee:00c58180:8"]]
+ 004a65a8 ["INT_ADD", "register:40f0:8", ["const:4a65a8:8", "const:4:8"]]
+ 004a65a8 ["CALL", null, ["callee:00c58180:8"]]
- 004a6568 bytes d2c61e94
+ 004a65a8 bytes f6c61e94
- 004a657c ["INT_ADD", "register:40f0:8", ["const:4a657c:8", "const:4:8"]]
- 004a657c ["CALL", null, ["callee:00c58850:8"]]
+ 004a65bc ["INT_ADD", "register:40f0:8", ["const:4a65bc:8", "const:4:8"]]
+ 004a65bc ["CALL", null, ["callee:00c58850:8"]]
- 004a657c bytes 81c81e94
+ 004a65bc bytes a5c81e94
- 004a6558 ["COPY", "tmp:0:8", ["const:e24:8"]]
- 004a6558 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004a6558 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004a6558 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004a6598 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 004a6598 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004a6598 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004a6598 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004a6558 bytes 00903891
+ 004a6598 bytes 00403791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-174f40101e847e3b7febfa8c3f69a8cf"></a>

### [`004a689c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md) → [`004a68dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a68dc.md) _ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagESA_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58840`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58840.md) · 呼出先 9件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c58910`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58910.md) · 呼出先 9件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a6abc",
      "incomplete_value": true,
      "site": "004a6ac0",
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
      "definition_site": "004a6a7c",
      "incomplete_value": true,
      "site": "004a6a80",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a6a04",
      "incomplete_value": false,
      "site": "004a6a0c",
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
            "const:2f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a69c4",
      "incomplete_value": false,
      "site": "004a69cc",
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
            "const:352:8"
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
      "004a6a04",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      "004a6ab8",
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004a6ac0",
      "DATA",
      [
        "storage",
        "00c66230",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "004a6a04",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ],
    [
      "004a6ab8",
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004a6ac0",
      "DATA",
      [
        "storage",
        "00c66300",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a69cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md#insn-004a69cc) · [`004a693c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md#insn-004a693c) · [`004a6964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md#insn-004a6964)
- 新版 `004a6a0c`（命令位置の公開資料なし） · `004a697c`（命令位置の公開資料なし） · `004a69a4`（命令位置の公開資料なし）

~~~diff
- 004a69cc ["INT_ADD", "register:40f0:8", ["const:4a69cc:8", "const:4:8"]]
- 004a69cc ["CALL", null, ["callee:00c58040:8"]]
+ 004a6a0c ["INT_ADD", "register:40f0:8", ["const:4a6a0c:8", "const:4:8"]]
+ 004a6a0c ["CALL", null, ["callee:00c58040:8"]]
- 004a69cc bytes 69c51e94
+ 004a6a0c bytes 8dc51e94
- 004a693c ["INT_ADD", "register:40f0:8", ["const:4a693c:8", "const:4:8"]]
- 004a693c ["CALL", null, ["callee:00c57f60:8"]]
+ 004a697c ["INT_ADD", "register:40f0:8", ["const:4a697c:8", "const:4:8"]]
+ 004a697c ["CALL", null, ["callee:00c57f60:8"]]
- 004a693c bytes 55c51e94
+ 004a697c bytes 79c51e94
- 004a6964 ["INT_ADD", "register:40f0:8", ["const:4a6964:8", "const:4:8"]]
- 004a6964 ["CALL", null, ["callee:00c58010:8"]]
+ 004a69a4 ["INT_ADD", "register:40f0:8", ["const:4a69a4:8", "const:4:8"]]
+ 004a69a4 ["CALL", null, ["callee:00c58010:8"]]
- 004a6964 bytes 77c51e94
+ 004a69a4 bytes 9bc51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5737e4b4047a20413a7fa2e6e9a43df9"></a>

### [`004a6f9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) → [`004a6fdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6fdc.md) FUN_004a6fdc

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004ecd10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`004f0edc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md) [`0050d538`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 3件 [`004ecd50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`004f0f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0f1c.md) [`0050d578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a707c",
      "incomplete_value": false,
      "site": "004a7084",
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
            "const:bef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a703c",
      "incomplete_value": false,
      "site": "004a7044",
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
            "const:bbe:8"
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
      "definition_site": "004a70b8",
      "incomplete_value": true,
      "site": "004a70c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7078",
      "incomplete_value": true,
      "site": "004a7084",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d80:8"
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
      "definition_site": "004a70b4",
      "incomplete_value": false,
      "site": "004a70c4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a7074",
      "incomplete_value": false,
      "site": "004a7084",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a707c",
      "PARAM",
      [
        "storage",
        "002b4bbe",
        null,
        "string"
      ]
    ],
    [
      "004a70b4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a70b8",
      "READ",
      [
        "storage",
        "00c9ad80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a707c",
      "PARAM",
      [
        "storage",
        "002b4bef",
        null,
        "string"
      ]
    ],
    [
      "004a70b4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a70b8",
      "READ",
      [
        "storage",
        "00c9ae50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7044`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md#insn-004a7044) · [`004a7084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md#insn-004a7084) · [`004a70c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md#insn-004a70c0)
- 新版 `004a7084`（命令位置の公開資料なし） · `004a70c4`（命令位置の公開資料なし） · `004a7100`（命令位置の公開資料なし）

~~~diff
- 004a7044 ["INT_ADD", "register:40f0:8", ["const:4a7044:8", "const:4:8"]]
- 004a7044 ["CALL", null, ["callee:0043de18:8"]]
+ 004a7084 ["INT_ADD", "register:40f0:8", ["const:4a7084:8", "const:4:8"]]
+ 004a7084 ["CALL", null, ["callee:0043de18:8"]]
- 004a7044 bytes 655bfe97
+ 004a7084 bytes 655bfe97
- 004a7084 ["INT_ADD", "register:40f0:8", ["const:4a7084:8", "const:4:8"]]
- 004a7084 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a70c4 ["INT_ADD", "register:40f0:8", ["const:4a70c4:8", "const:4:8"]]
+ 004a70c4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a7084 bytes a3c31e94
+ 004a70c4 bytes c7c31e94
- 004a70c0 ["INT_ADD", "register:40f0:8", ["const:4a70c0:8", "const:4:8"]]
- 004a70c0 ["CALL", null, ["callee:00c58720:8"]]
+ 004a7100 ["INT_ADD", "register:40f0:8", ["const:4a7100:8", "const:4:8"]]
+ 004a7100 ["CALL", null, ["callee:00c58720:8"]]
- 004a70c0 bytes 64c51e94
+ 004a7100 bytes 88c51e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bdc30f3dd0bd232f95c73bffba40553"></a>

### [`004a7138`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md) → [`004a7178`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7178.md) _ZN5Botan17assertion_failureEPKcS1_S1_S1_i

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md) · 呼出先 11件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md) · 呼出先 11件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.27% / 新版 86.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a71c0",
      "incomplete_value": true,
      "site": "004a71d0",
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
      "definition_site": "004a7180",
      "incomplete_value": true,
      "site": "004a7190",
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
      "definition_site": "004a71c8",
      "incomplete_value": true,
      "site": "004a71dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a7188",
      "incomplete_value": true,
      "site": "004a719c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004a71e4",
      "incomplete_value": true,
      "site": "004a71e4",
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
      "definition_site": "004a71a4",
      "incomplete_value": true,
      "site": "004a71a4",
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
      "unmatched:004a7170",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a71c8",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004a71c8",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "004a71ac",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a71c8",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004a71c8",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a71dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md#insn-004a71dc) · [`004a7210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md#insn-004a7210) · [`004a7250`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md#insn-004a7250)
- 新版 `004a721c`（命令位置の公開資料なし） · `004a7250`（命令位置の公開資料なし） · `004a7290`（命令位置の公開資料なし）

~~~diff
- 004a71dc ["INT_ADD", "register:40f0:8", ["const:4a71dc:8", "const:4:8"]]
- 004a71dc ["CALL", null, ["callee:00c582c0:8"]]
+ 004a721c ["INT_ADD", "register:40f0:8", ["const:4a721c:8", "const:4:8"]]
+ 004a721c ["CALL", null, ["callee:00c582c0:8"]]
- 004a71dc bytes 05c41e94
+ 004a721c bytes 29c41e94
- 004a7210 ["INT_ADD", "register:40f0:8", ["const:4a7210:8", "const:4:8"]]
- 004a7210 ["CALL", null, ["callee:00459510:8"]]
+ 004a7250 ["INT_ADD", "register:40f0:8", ["const:4a7250:8", "const:4:8"]]
+ 004a7250 ["CALL", null, ["callee:00459510:8"]]
- 004a7210 bytes b0c8fe97
+ 004a7250 bytes b0c8fe97
- 004a7250 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 004a7250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a7250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a7250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a7290 ["COPY", "tmp:0:8", ["const:874:8"]]
+ 004a7290 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a7290 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a7290 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004a7250 bytes 21402391
+ 004a7290 bytes 21d02191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc6c55e40f1f36f922adfb5c7a56e310"></a>

### [`004a7448`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md) → [`004a7488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7488.md) _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58760`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

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
      "definition_site": "004a74b4",
      "incomplete_value": true,
      "site": "004a74bc",
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
      "definition_site": "004a7474",
      "incomplete_value": true,
      "site": "004a747c",
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
      "definition_site": "004a75a4",
      "incomplete_value": true,
      "site": "004a75ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a7564",
      "incomplete_value": true,
      "site": "004a756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
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
      "definition_site": "004a75a0",
      "incomplete_value": false,
      "site": "004a75ac",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a7560",
      "incomplete_value": false,
      "site": "004a756c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004a74ac",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a74bc",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a75a0",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a74ac",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "004a74bc",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004a75a0",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a756c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md#insn-004a756c) · [`004a746c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md#insn-004a746c) · [`004a74b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md#insn-004a74b0)
- 新版 `004a75ac`（命令位置の公開資料なし） · `004a74ac`（命令位置の公開資料なし） · `004a74f0`（命令位置の公開資料なし）

~~~diff
- 004a756c ["INT_ADD", "register:40f0:8", ["const:4a756c:8", "const:4:8"]]
- 004a756c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a75ac ["INT_ADD", "register:40f0:8", ["const:4a75ac:8", "const:4:8"]]
+ 004a75ac ["CALL", null, ["callee:00c57fe0:8"]]
- 004a756c bytes 69c21e94
+ 004a75ac bytes 8dc21e94
- 004a746c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 004a746c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a74ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 004a74ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a746c bytes 08a146f9
+ 004a74ac bytes 080947f9
- 004a74b0 ["INT_ADD", "register:40f0:8", ["const:4a74b0:8", "const:4:8"]]
- 004a74b0 ["CALL", null, ["callee:00c588a0:8"]]
+ 004a74f0 ["INT_ADD", "register:40f0:8", ["const:4a74f0:8", "const:4:8"]]
+ 004a74f0 ["CALL", null, ["callee:00c588a0:8"]]
- 004a74b0 bytes c8c41e94
+ 004a74f0 bytes ecc41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-246a6c9cf64688ec5fb01cbbfd908300"></a>

### [`004a762c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md) → [`004a766c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a766c.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587d0.md) · 呼出先 12件 [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c588a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588a0.md) · 呼出先 12件 [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a795c",
      "incomplete_value": true,
      "site": "004a7964",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a791c",
      "incomplete_value": true,
      "site": "004a7924",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
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
      "definition_site": "004a7958",
      "incomplete_value": false,
      "site": "004a7964",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a7918",
      "incomplete_value": false,
      "site": "004a7924",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 12,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a79e8",
      "incomplete_value": true,
      "site": "004a79f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a79a8",
      "incomplete_value": true,
      "site": "004a79b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
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
      "004a7958",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a795c",
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      "004a795c",
      "PARAM",
      [
        "storage",
        "00c662d8",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004a7958",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a795c",
      "READ",
      [
        "storage",
        "00c9ae60",
        null,
        "pointer"
      ]
    ],
    [
      "004a795c",
      "PARAM",
      [
        "storage",
        "00c663a8",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md#insn-004a7924) · [`004a79b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md#insn-004a79b0) · [`004a76a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md#insn-004a76a4)
- 新版 `004a7964`（命令位置の公開資料なし） · `004a79f0`（命令位置の公開資料なし） · `004a76e4`（命令位置の公開資料なし）

~~~diff
- 004a7924 ["INT_ADD", "register:40f0:8", ["const:4a7924:8", "const:4:8"]]
- 004a7924 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a7964 ["INT_ADD", "register:40f0:8", ["const:4a7964:8", "const:4:8"]]
+ 004a7964 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a7924 bytes 7bc11e94
+ 004a7964 bytes 9fc11e94
- 004a79b0 ["INT_ADD", "register:40f0:8", ["const:4a79b0:8", "const:4:8"]]
- 004a79b0 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a79f0 ["INT_ADD", "register:40f0:8", ["const:4a79f0:8", "const:4:8"]]
+ 004a79f0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a79b0 bytes 58c11e94
+ 004a79f0 bytes 7cc11e94
- 004a76a4 ["INT_ADD", "register:40f0:8", ["const:4a76a4:8", "const:4:8"]]
- 004a76a4 ["CALL", null, ["callee:00c586d0:8"]]
+ 004a76e4 ["INT_ADD", "register:40f0:8", ["const:4a76e4:8", "const:4:8"]]
+ 004a76e4 ["CALL", null, ["callee:00c586d0:8"]]
- 004a76a4 bytes d7c31e94
+ 004a76e4 bytes fbc31e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a753db0acf6a131666b679036fe3e63"></a>

### [`004a7cf4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md) → [`004a7d34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7d34.md) _ZN5BotanplERKNS_3OIDEj

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a7d64",
      "incomplete_value": true,
      "site": "004a7d70",
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
      "definition_site": "004a7d24",
      "incomplete_value": true,
      "site": "004a7d30",
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
      "004a7d54",
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      "004a7d70",
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004a7d54",
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      "004a7d70",
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a7d14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md#insn-004a7d14) · [`004a7d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md#insn-004a7d40) · [`004a7d58`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md#insn-004a7d58)
- 新版 `004a7d54`（命令位置の公開資料なし） · `004a7d80`（命令位置の公開資料なし） · `004a7d98`（命令位置の公開資料なし）

~~~diff
- 004a7d14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
- 004a7d14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a7d54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
+ 004a7d54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004a7d14 bytes 08a146f9
+ 004a7d54 bytes 080947f9
- 004a7d40 ["INT_ADD", "register:40f0:8", ["const:4a7d40:8", "const:4:8"]]
- 004a7d40 ["CALL", null, ["callee:00c57f60:8"]]
+ 004a7d80 ["INT_ADD", "register:40f0:8", ["const:4a7d80:8", "const:4:8"]]
+ 004a7d80 ["CALL", null, ["callee:00c57f60:8"]]
- 004a7d40 bytes 54c01e94
+ 004a7d80 bytes 78c01e94
- 004a7d58 ["INT_ADD", "register:40f0:8", ["const:4a7d58:8", "const:4:8"]]
- 004a7d58 ["CALL", null, ["callee:00c580d0:8"]]
+ 004a7d98 ["INT_ADD", "register:40f0:8", ["const:4a7d98:8", "const:4:8"]]
+ 004a7d98 ["CALL", null, ["callee:00c580d0:8"]]
- 004a7d58 bytes aac01e94
+ 004a7d98 bytes cec01e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5805ed99a4f44d9bdefab2215fe1fed"></a>

### [`004a7e28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md) → [`004a7e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7e68.md) _ZNK5Botan3OID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.26% / 新版 97.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a81c4",
      "incomplete_value": false,
      "site": "004a81e4",
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
            "const:21a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8184",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:26e:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004a81cc",
      "incomplete_value": false,
      "site": "004a81e4",
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
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a818c",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:ed0:8"
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
      "definition_site": "004a81d4",
      "incomplete_value": false,
      "site": "004a81e4",
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
            "const:3f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8194",
      "incomplete_value": false,
      "site": "004a81a4",
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
            "const:93:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a81c4",
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      "004a81cc",
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      "004a81d4",
      "PARAM",
      [
        "storage",
        "002ba093",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004a81c4",
      "PARAM",
      [
        "storage",
        "002bb21a",
        null,
        "string"
      ]
    ],
    [
      "004a81cc",
      "PARAM",
      [
        "storage",
        "002a1e83",
        null,
        "string"
      ]
    ],
    [
      "004a81d4",
      "PARAM",
      [
        "storage",
        "002ba03f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a81a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md#insn-004a81a4) · [`004a8214`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md#insn-004a8214) · [`004a8254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md#insn-004a8254)
- 新版 `004a81e4`（命令位置の公開資料なし） · `004a8254`（命令位置の公開資料なし） · `004a8294`（命令位置の公開資料なし）

~~~diff
- 004a81a4 ["INT_ADD", "register:40f0:8", ["const:4a81a4:8", "const:4:8"]]
- 004a81a4 ["CALL", null, ["callee:00c58720:8"]]
+ 004a81e4 ["INT_ADD", "register:40f0:8", ["const:4a81e4:8", "const:4:8"]]
+ 004a81e4 ["CALL", null, ["callee:00c58720:8"]]
- 004a81a4 bytes 2bc11e94
+ 004a81e4 bytes 4fc11e94
- 004a8214 ["INT_ADD", "register:40f0:8", ["const:4a8214:8", "const:4:8"]]
- 004a8214 ["CALL", null, ["callee:0043de18:8"]]
+ 004a8254 ["INT_ADD", "register:40f0:8", ["const:4a8254:8", "const:4:8"]]
+ 004a8254 ["CALL", null, ["callee:0043de18:8"]]
- 004a8214 bytes f156fe97
+ 004a8254 bytes f156fe97
- 004a8254 ["INT_ADD", "register:40f0:8", ["const:4a8254:8", "const:4:8"]]
- 004a8254 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a8294 ["INT_ADD", "register:40f0:8", ["const:4a8294:8", "const:4:8"]]
+ 004a8294 ["CALL", null, ["callee:00c57fe0:8"]]
- 004a8254 bytes 2fbf1e94
+ 004a8294 bytes 53bf1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7336c8322e351d6e5e936ba73b11c34a"></a>

### [`004a83a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md) → [`004a83e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a83e0.md) _ZN5Botan3OID11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004a86d0",
      "incomplete_value": true,
      "site": "004a86d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a8690",
      "incomplete_value": true,
      "site": "004a8690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004a871c",
      "incomplete_value": false,
      "site": "004a8724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:e0b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a86dc",
      "incomplete_value": false,
      "site": "004a86e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "definition_site": "004a8758",
      "incomplete_value": true,
      "site": "004a8764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004a8718",
      "incomplete_value": true,
      "site": "004a8724",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "004a86c0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a871c",
      "PARAM",
      [
        "storage",
        "0029ee58",
        null,
        "string"
      ]
    ],
    [
      "004a8754",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004a86c0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004a871c",
      "PARAM",
      [
        "storage",
        "0029ee0b",
        null,
        "string"
      ]
    ],
    [
      "004a8754",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8690`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md#insn-004a8690) · [`004a86d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md#insn-004a86d0) · [`004a86e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md#insn-004a86e4)
- 新版 `004a86d0`（命令位置の公開資料なし） · `004a8710`（命令位置の公開資料なし） · `004a8724`（命令位置の公開資料なし）

~~~diff
- 004a8690 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a8690 ["INT_ADD", "register:40f0:8", ["const:4a8690:8", "const:4:8"]]
- 004a8690 ["CALLIND", null, ["register:0:8"]]
+ 004a86d0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a86d0 ["INT_ADD", "register:40f0:8", ["const:4a86d0:8", "const:4:8"]]
+ 004a86d0 ["CALLIND", null, ["register:0:8"]]
- 004a8690 bytes 20013fd6
+ 004a86d0 bytes 20013fd6
- 004a86d0 ["INT_ADD", "register:40f0:8", ["const:4a86d0:8", "const:4:8"]]
- 004a86d0 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004a8710 ["INT_ADD", "register:40f0:8", ["const:4a8710:8", "const:4:8"]]
+ 004a8710 ["CALL", null, ["callee:00c57fc0:8"]]
- 004a86d0 bytes 08be1e94
+ 004a8710 bytes 2cbe1e94
- 004a86e4 ["INT_ADD", "register:40f0:8", ["const:4a86e4:8", "const:4:8"]]
- 004a86e4 ["CALL", null, ["callee:0043de18:8"]]
+ 004a8724 ["INT_ADD", "register:40f0:8", ["const:4a8724:8", "const:4:8"]]
+ 004a8724 ["CALL", null, ["callee:0043de18:8"]]
- 004a86e4 bytes bd55fe97
+ 004a8724 bytes bd55fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f798fcc0cbdb7cfca37ad39cdf0d0ab1"></a>

### [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) → [`004a8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) _ZN5Botan11BER_Decoder15get_next_objectEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 1件 [`00c587f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587f0.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004afa58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.80% / 新版 96.80%

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
      "definition_site": "004a8a78",
      "incomplete_value": false,
      "site": "004a8a80",
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
            "const:a41:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8a38",
      "incomplete_value": false,
      "site": "004a8a40",
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
            "const:a10:8"
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
      "definition_site": "004a8ab0",
      "incomplete_value": true,
      "site": "004a8abc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004a8a70",
      "incomplete_value": true,
      "site": "004a8a7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "definition_site": "004a8aac",
      "incomplete_value": false,
      "site": "004a8abc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004a8a6c",
      "incomplete_value": false,
      "site": "004a8a7c",
      "value": [
        "leaf",
        "const:535868:8"
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004a8a78",
      "PARAM",
      [
        "storage",
        "002b1a10",
        null,
        "string"
      ]
    ],
    [
      "004a8aac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004a8ab0",
      "READ",
      [
        "storage",
        "00c9ada8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004a8a78",
      "PARAM",
      [
        "storage",
        "002b1a41",
        null,
        "string"
      ]
    ],
    [
      "004a8aac",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004a8ab0",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md#insn-004a8a40) · [`004a8a7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md#insn-004a8a7c) · [`004a8a9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md#insn-004a8a9c)
- 新版 `004a8a80`（命令位置の公開資料なし） · `004a8abc`（命令位置の公開資料なし） · `004a8adc`（命令位置の公開資料なし）

~~~diff
- 004a8a40 ["INT_ADD", "register:40f0:8", ["const:4a8a40:8", "const:4:8"]]
- 004a8a40 ["CALL", null, ["callee:0043de18:8"]]
+ 004a8a80 ["INT_ADD", "register:40f0:8", ["const:4a8a80:8", "const:4:8"]]
+ 004a8a80 ["CALL", null, ["callee:0043de18:8"]]
- 004a8a40 bytes e654fe97
+ 004a8a80 bytes e654fe97
- 004a8a7c ["INT_ADD", "register:40f0:8", ["const:4a8a7c:8", "const:4:8"]]
- 004a8a7c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004a8abc ["INT_ADD", "register:40f0:8", ["const:4a8abc:8", "const:4:8"]]
+ 004a8abc ["CALL", null, ["callee:00c57fe0:8"]]
- 004a8a7c bytes 25bd1e94
+ 004a8abc bytes 49bd1e94
- 004a8a9c ["INT_ADD", "register:40f0:8", ["const:4a8a9c:8", "const:4:8"]]
- 004a8a9c ["CALL", null, ["callee:0043de18:8"]]
+ 004a8adc ["INT_ADD", "register:40f0:8", ["const:4a8adc:8", "const:4:8"]]
+ 004a8adc ["CALL", null, ["callee:0043de18:8"]]
- 004a8a9c bytes cf54fe97
+ 004a8adc bytes cf54fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c751fbffa7126a4284a5d73dd93b51be"></a>

### [`004a8b9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md) → [`004a8bdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8bdc.md) _ZNK5Botan14ASN1_Formatter5printEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

変更の種類 constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.76% / 新版 88.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8c24",
      "incomplete_value": true,
      "site": "004a8c34",
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
      "definition_site": "004a8be4",
      "incomplete_value": true,
      "site": "004a8bf4",
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
      "definition_site": "004a8c2c",
      "incomplete_value": true,
      "site": "004a8c3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8bec",
      "incomplete_value": true,
      "site": "004a8bfc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8c44",
      "incomplete_value": true,
      "site": "004a8c44",
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
                "const:8:8"
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
      "definition_site": "004a8c04",
      "incomplete_value": true,
      "site": "004a8c04",
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
                "const:8:8"
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
      "unmatched:004a8bd4",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8c2c",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004a8c2c",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "004a8c10",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004a8c2c",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004a8c2c",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8c3c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md#insn-004a8c3c) · [`004a8bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md#insn-004a8bd0) · [`004a8bd4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md#insn-004a8bd4)
- 新版 `004a8c7c`（命令位置の公開資料なし） · `004a8c14`（命令位置の公開資料なし）

~~~diff
- 004a8c3c ["INT_ADD", "register:40f0:8", ["const:4a8c3c:8", "const:4:8"]]
- 004a8c3c ["CALL", null, ["callee:00c582c0:8"]]
+ 004a8c7c ["INT_ADD", "register:40f0:8", ["const:4a8c7c:8", "const:4:8"]]
+ 004a8c7c ["CALL", null, ["callee:00c582c0:8"]]
- 004a8c3c bytes 6dbd1e94
+ 004a8c7c bytes 91bd1e94
- 004a8bd0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c88:8"]]
- 004a8bd0 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 004a8c14 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
+ 004a8c14 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8bd0 bytes 7b4746f9
+ 004a8c14 bytes 5a4746f9
- 004a8bd4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:bb8:8"]]
- 004a8bd4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 004a8bd4 bytes 5adf45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b7f1357e3fbd5df7b0798b1dffada8f"></a>

### [`004a8e2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md) → [`004a8e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8e6c.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58870`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58870.md) · 呼出先 36件 [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004a6db0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c58940`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58940.md) · 呼出先 36件 [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004a6df0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.82% / 新版 93.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `call_target` 8件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f4c",
      "incomplete_value": true,
      "site": "004a8f60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8f0c",
      "incomplete_value": true,
      "site": "004a8f20",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f70",
      "incomplete_value": true,
      "site": "004a8f70",
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
      "definition_site": "004a8f30",
      "incomplete_value": true,
      "site": "004a8f30",
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
    "kind": "store_value",
    "new": {
      "definition_site": "004a8f70",
      "incomplete_value": true,
      "site": "004a8f70",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004a8f30",
      "incomplete_value": true,
      "site": "004a8f30",
      "value": [
        "LOAD",
        "8",
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
      "004a8ed8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f34",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f4c",
      "READ",
      [
        "storage",
        "00c93200",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004a8ed8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f34",
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      "004a8f4c",
      "READ",
      [
        "storage",
        "00c932d0",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004a8ea8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md#insn-004a8ea8) · [`004a90e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md#insn-004a90e8) · [`004a92a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md#insn-004a92a4)
- 新版 `004a8ee8`（命令位置の公開資料なし） · `004a9128`（命令位置の公開資料なし） · `004a92e4`（命令位置の公開資料なし）

~~~diff
- 004a8ea8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a8ea8 ["INT_ADD", "register:40f0:8", ["const:4a8ea8:8", "const:4:8"]]
- 004a8ea8 ["CALLIND", null, ["register:0:8"]]
+ 004a8ee8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a8ee8 ["INT_ADD", "register:40f0:8", ["const:4a8ee8:8", "const:4:8"]]
+ 004a8ee8 ["CALLIND", null, ["register:0:8"]]
- 004a8ea8 bytes 20013fd6
+ 004a8ee8 bytes 20013fd6
- 004a90e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004a90e8 ["INT_ADD", "register:40f0:8", ["const:4a90e8:8", "const:4:8"]]
- 004a90e8 ["CALLIND", null, ["register:0:8"]]
+ 004a9128 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004a9128 ["INT_ADD", "register:40f0:8", ["const:4a9128:8", "const:4:8"]]
+ 004a9128 ["CALLIND", null, ["register:0:8"]]
- 004a90e8 bytes 20013fd6
+ 004a9128 bytes 20013fd6
- 004a92a4 ["INT_ADD", "register:40f0:8", ["const:4a92a4:8", "const:4:8"]]
- 004a92a4 ["CALL", null, ["callee:00c58080:8"]]
+ 004a92e4 ["INT_ADD", "register:40f0:8", ["const:4a92e4:8", "const:4:8"]]
+ 004a92e4 ["CALL", null, ["callee:00c58080:8"]]
- 004a92a4 bytes 43bb1e94
+ 004a92e4 bytes 67bb1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea1036f6698c7b3c68b6a800e8f17f92"></a>

### [`004aa27c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004aa/004aa27c.md) → [`004aa2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004aa/004aa2bc.md) _ZN5Botan4OIDS6lookupERKNS_3OIDE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c588b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md) · 呼出先 5件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)
- 新版 呼出元 1件 [`00c58980`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58980.md) · 呼出先 5件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 37.72% / 新版 37.72%

CFGの説明率　旧版 32.90% / 新版 32.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 74件, `store_value` 1件, `unresolved_branch_alignment` 110件, `unresolved_call_alignment` 108件

アドレスに依存する影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004aa524",
      "incomplete_value": true,
      "site": "004aa524",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:45d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa4e4",
      "incomplete_value": true,
      "site": "004aa4e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b9:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004aa498"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "004aa4b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004aa3fc",
      "PARAM",
      [
        "storage",
        "002a64c3",
        null,
        null
      ]
    ],
    [
      "004aa4ac",
      "PARAM",
      [
        "storage",
        "002ac651",
        null,
        "string"
      ]
    ],
    [
      "004aa4b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:004aa488"
      ]
    ]
  ],
  "added": [
    [
      "004aa3fc",
      "PARAM",
      [
        "storage",
        "002a6467",
        null,
        null
      ]
    ],
    [
      "004aa4ac",
      "PARAM",
      [
        "storage",
        "002ac5f5",
        null,
        "string"
      ]
    ],
    [
      "004aa4b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "004aa4c8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aa498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004aa/004aa27c.md#insn-004aa498) · [`004aa4b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004aa/004aa27c.md#insn-004aa4b8)
- 新版 `004aa4e4`（命令位置の公開資料なし）

~~~diff
- 004aa498 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004aa498 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004aa498 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004aa498 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004aa498 bytes 80000036
- 004aa4b8 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 004aa4b8 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 004aa4b8 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 004aa4b8 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 004aa4b8 bytes c0020036
+ 004aa4e4 ["BRANCH", null, ["local:b37:8"]]
+ 004aa4e4 bytes 62000014
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fecc1390038861cee3e455c8c439aaac"></a>

### [`004abd6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md) → [`004abdac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ab/004abdac.md) _ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588c0.md) · 呼出先 7件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58720`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) [`00c58730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)
- 新版 呼出元 1件 [`00c58990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58990.md) · 呼出先 7件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587f0.md) [`00c58800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58800.md) [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.27% / 新版 96.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abedc",
      "incomplete_value": true,
      "site": "004abedc",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004abe9c",
      "incomplete_value": true,
      "site": "004abe9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abf64",
      "incomplete_value": true,
      "site": "004abf64",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004abf24",
      "incomplete_value": true,
      "site": "004abf24",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004abf94",
      "incomplete_value": true,
      "site": "004abf94",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004abf54",
      "incomplete_value": true,
      "site": "004abf54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004abecc",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004abf54",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004abf84",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004abecc",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004abf54",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004abf84",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004abe9c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md#insn-004abe9c) · [`004abf14`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md#insn-004abf14) · [`004abf24`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md#insn-004abf24)
- 新版 `004abedc`（命令位置の公開資料なし） · `004abf54`（命令位置の公開資料なし） · `004abf64`（命令位置の公開資料なし）

~~~diff
- 004abe9c ["COPY", "register:0:8", ["register:4048:8"]]
- 004abe9c ["INT_ADD", "register:40f0:8", ["const:4abe9c:8", "const:4:8"]]
- 004abe9c ["CALLIND", null, ["register:0:8"]]
+ 004abedc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abedc ["INT_ADD", "register:40f0:8", ["const:4abedc:8", "const:4:8"]]
+ 004abedc ["CALLIND", null, ["register:0:8"]]
- 004abe9c bytes 20013fd6
+ 004abedc bytes 20013fd6
- 004abf14 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:738:8"]]
- 004abf14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004abf54 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:808:8"]]
+ 004abf54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004abf14 bytes c99e43f9
+ 004abf54 bytes c90644f9
- 004abf24 ["COPY", "register:0:8", ["register:4048:8"]]
- 004abf24 ["INT_ADD", "register:40f0:8", ["const:4abf24:8", "const:4:8"]]
- 004abf24 ["CALLIND", null, ["register:0:8"]]
+ 004abf64 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004abf64 ["INT_ADD", "register:40f0:8", ["const:4abf64:8", "const:4:8"]]
+ 004abf64 ["CALLIND", null, ["register:0:8"]]
- 004abf24 bytes 20013fd6
+ 004abf64 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff4fcdf7fa98d480a784e3decc5a33f"></a>

### [`004ac1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) → [`004ac224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac224.md) _ZNK5Botan9X509_Time15readable_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58910`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58910.md) · 呼出先 17件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 1件 [`00c589e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589e0.md) · 呼出先 17件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac3e0",
      "incomplete_value": true,
      "site": "004ac3e8",
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
      "definition_site": "004ac3a0",
      "incomplete_value": true,
      "site": "004ac3a8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004ac3f0",
      "incomplete_value": true,
      "site": "004ac3f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "004ac3b0",
      "incomplete_value": true,
      "site": "004ac3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac3f0",
      "incomplete_value": true,
      "site": "004ac3f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ac3b0",
      "incomplete_value": true,
      "site": "004ac3b0",
      "value": [
        "LOAD",
        "8",
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
      "004ac294",
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      "004ac294",
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac2e0",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ac294",
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      "004ac294",
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004ac2e0",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac258`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md#insn-004ac258) · [`004ac268`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md#insn-004ac268) · [`004ac298`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md#insn-004ac298)
- 新版 `004ac298`（命令位置の公開資料なし） · `004ac2a8`（命令位置の公開資料なし） · `004ac2d8`（命令位置の公開資料なし）

~~~diff
- 004ac258 ["INT_ADD", "register:40f0:8", ["const:4ac258:8", "const:4:8"]]
- 004ac258 ["CALL", null, ["callee:00c58350:8"]]
+ 004ac298 ["INT_ADD", "register:40f0:8", ["const:4ac298:8", "const:4:8"]]
+ 004ac298 ["CALL", null, ["callee:00c58350:8"]]
- 004ac258 bytes 0ab01e94
+ 004ac298 bytes 2eb01e94
- 004ac268 ["COPY", "register:0:8", ["register:4040:8"]]
- 004ac268 ["INT_ADD", "register:40f0:8", ["const:4ac268:8", "const:4:8"]]
- 004ac268 ["CALLIND", null, ["register:0:8"]]
+ 004ac2a8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004ac2a8 ["INT_ADD", "register:40f0:8", ["const:4ac2a8:8", "const:4:8"]]
+ 004ac2a8 ["CALLIND", null, ["register:0:8"]]
- 004ac268 bytes 00013fd6
+ 004ac2a8 bytes 00013fd6
- 004ac298 ["INT_ADD", "register:40f0:8", ["const:4ac298:8", "const:4:8"]]
- 004ac298 ["CALL", null, ["callee:00c58a30:8"]]
+ 004ac2d8 ["INT_ADD", "register:40f0:8", ["const:4ac2d8:8", "const:4:8"]]
+ 004ac2d8 ["CALL", null, ["callee:00c58a30:8"]]
- 004ac298 bytes b2b11e94
+ 004ac2d8 bytes d6b11e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed486f29428da9a6bfe7327a06efb2af"></a>

### [`004ac500`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md) → [`004ac540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac540.md) _ZNK5Botan19ASN1_Pretty_Printer6formatENS_8ASN1_TagES1_mmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`004594d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00459510`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.39% / 新版 93.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac5f4",
      "incomplete_value": true,
      "site": "004ac5f8",
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
      "definition_site": "004ac5b4",
      "incomplete_value": true,
      "site": "004ac5b8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ac5f0",
      "incomplete_value": true,
      "site": "004ac5fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004ac5b0",
      "incomplete_value": true,
      "site": "004ac5bc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004ac604",
      "incomplete_value": true,
      "site": "004ac604",
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
      "definition_site": "004ac5c4",
      "incomplete_value": true,
      "site": "004ac5c4",
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
    "ordinal": 21,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:004ac5a0",
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5f0",
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ac5f0",
      "READ",
      [
        "storage",
        "00c93210",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "004ac5dc",
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      "004ac5f0",
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "004ac5f0",
      "READ",
      [
        "storage",
        "00c932e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ac638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md#insn-004ac638) · [`004ac668`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md#insn-004ac668) · [`004ac694`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md#insn-004ac694)
- 新版 `004ac678`（命令位置の公開資料なし） · `004ac6a8`（命令位置の公開資料なし） · `004ac6d4`（命令位置の公開資料なし）

~~~diff
- 004ac638 ["INT_ADD", "register:40f0:8", ["const:4ac638:8", "const:4:8"]]
- 004ac638 ["CALL", null, ["callee:00459510:8"]]
+ 004ac678 ["INT_ADD", "register:40f0:8", ["const:4ac678:8", "const:4:8"]]
+ 004ac678 ["CALL", null, ["callee:00459510:8"]]
- 004ac638 bytes a6b3fe97
+ 004ac678 bytes a6b3fe97
- 004ac668 ["INT_ADD", "register:40f0:8", ["const:4ac668:8", "const:4:8"]]
- 004ac668 ["CALL", null, ["callee:00459510:8"]]
+ 004ac6a8 ["INT_ADD", "register:40f0:8", ["const:4ac6a8:8", "const:4:8"]]
+ 004ac6a8 ["CALL", null, ["callee:00459510:8"]]
- 004ac668 bytes 9ab3fe97
+ 004ac6a8 bytes 9ab3fe97
- 004ac694 ["INT_ADD", "register:40f0:8", ["const:4ac694:8", "const:4:8"]]
- 004ac694 ["CALL", null, ["callee:00459510:8"]]
+ 004ac6d4 ["INT_ADD", "register:40f0:8", ["const:4ac6d4:8", "const:4:8"]]
+ 004ac6d4 ["CALL", null, ["callee:00459510:8"]]
- 004ac694 bytes 8fb3fe97
+ 004ac6d4 bytes 8fb3fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dc57d3abb47cd72979438b92bb81619"></a>

### [`004ace50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) → [`004ace90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ace90.md) _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59960.md) · 呼出先 2件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004acf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md)
- 新版 呼出元 1件 [`00c59a30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a30.md) · 呼出先 2件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004acfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acfb8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004acebc",
      "incomplete_value": true,
      "site": "004acec0",
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
      "definition_site": "004ace7c",
      "incomplete_value": true,
      "site": "004ace80",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004aceac",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "004acec0",
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004acf34",
      "DATA",
      [
        "storage",
        "002cf568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004aceac",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "004acec0",
      "DATA",
      [
        "storage",
        "00c66418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004acf34",
      "DATA",
      [
        "storage",
        "002cf5a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ace6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md#insn-004ace6c) · [`004aceac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md#insn-004aceac) · [`004aceec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md#insn-004aceec)
- 新版 `004aceac`（命令位置の公開資料なし） · `004aceec`（命令位置の公開資料なし） · `004acf2c`（命令位置の公開資料なし）

~~~diff
- 004ace6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 004ace6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aceac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 004aceac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ace6c bytes 08dd46f9
+ 004aceac bytes 084547f9
- 004aceac ["INT_ADD", "register:40f0:8", ["const:4aceac:8", "const:4:8"]]
- 004aceac ["CALL", null, ["callee:0043bb60:8"]]
+ 004aceec ["INT_ADD", "register:40f0:8", ["const:4aceec:8", "const:4:8"]]
+ 004aceec ["CALL", null, ["callee:0043bb60:8"]]
- 004aceac bytes 1d3bfe97
+ 004aceec bytes 1d3bfe97
- 004aceec ["COPY", "tmp:0:8", ["const:568:8"]]
- 004aceec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004aceec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004aceec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004acf2c ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 004acf2c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004acf2c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004acf2c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004aceec bytes 4aa11591
+ 004acf2c bytes 4aa11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f63f5451121e93b5b2fb1b2aec384c01"></a>

### [`004acf78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md) → [`004acfb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acfb8.md) FUN_004acfb8

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ace50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) [`004ad774`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad774.md) · 呼出先 7件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`004ace90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ace90.md) [`004ad7b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad7b4.md) · 呼出先 7件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

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
      "definition_site": "004ad040",
      "incomplete_value": false,
      "site": "004ad04c",
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
            "const:973:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad000",
      "incomplete_value": false,
      "site": "004ad00c",
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
            "const:9cf:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad098",
      "incomplete_value": true,
      "site": "004ad0a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ad058",
      "incomplete_value": true,
      "site": "004ad064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004ad094",
      "incomplete_value": false,
      "site": "004ad0a4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004ad054",
      "incomplete_value": false,
      "site": "004ad064",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004ad040",
      "PARAM",
      [
        "storage",
        "002ae9cf",
        null,
        "string"
      ]
    ],
    [
      "004ad094",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ad098",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad040",
      "PARAM",
      [
        "storage",
        "002ae973",
        null,
        "string"
      ]
    ],
    [
      "004ad094",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004ad098",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad00c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md#insn-004ad00c) · [`004ad064`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md#insn-004ad064) · [`004acfe8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md#insn-004acfe8)
- 新版 `004ad04c`（命令位置の公開資料なし） · `004ad0a4`（命令位置の公開資料なし） · `004ad028`（命令位置の公開資料なし）

~~~diff
- 004ad00c ["INT_ADD", "register:40f0:8", ["const:4ad00c:8", "const:4:8"]]
- 004ad00c ["CALL", null, ["callee:00c58030:8"]]
+ 004ad04c ["INT_ADD", "register:40f0:8", ["const:4ad04c:8", "const:4:8"]]
+ 004ad04c ["CALL", null, ["callee:00c58030:8"]]
- 004ad00c bytes d5ab1e94
+ 004ad04c bytes f9ab1e94
- 004ad064 ["INT_ADD", "register:40f0:8", ["const:4ad064:8", "const:4:8"]]
- 004ad064 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004ad0a4 ["INT_ADD", "register:40f0:8", ["const:4ad0a4:8", "const:4:8"]]
+ 004ad0a4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004ad064 bytes abab1e94
+ 004ad0a4 bytes cfab1e94
- 004acfe8 ["INT_ADD", "register:40f0:8", ["const:4acfe8:8", "const:4:8"]]
- 004acfe8 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004ad028 ["INT_ADD", "register:40f0:8", ["const:4ad028:8", "const:4:8"]]
+ 004ad028 ["CALL", null, ["callee:00c57fc0:8"]]
- 004acfe8 bytes c2ab1e94
+ 004ad028 bytes e6ab1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0209a3975f1dc7b0a64aac578c5c4bd5"></a>

### [`004ad0e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md) → [`004ad120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad120.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588f0.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00c589c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589c0.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ad144",
      "incomplete_value": true,
      "site": "004ad148",
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
      "definition_site": "004ad104",
      "incomplete_value": true,
      "site": "004ad108",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ad138",
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      "004ad148",
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad1ac",
      "DATA",
      [
        "storage",
        "002cf568",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ad138",
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      "004ad148",
      "DATA",
      [
        "storage",
        "00c66418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "004ad1ac",
      "DATA",
      [
        "storage",
        "002cf5a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad0f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md#insn-004ad0f8) · [`004ad134`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md#insn-004ad134) · [`004ad164`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md#insn-004ad164)
- 新版 `004ad138`（命令位置の公開資料なし） · `004ad174`（命令位置の公開資料なし） · `004ad1a4`（命令位置の公開資料なし）

~~~diff
- 004ad0f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
- 004ad0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004ad138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 004ad138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004ad0f8 bytes 08dd46f9
+ 004ad138 bytes 084547f9
- 004ad134 ["INT_ADD", "register:40f0:8", ["const:4ad134:8", "const:4:8"]]
- 004ad134 ["CALL", null, ["callee:0043bb60:8"]]
+ 004ad174 ["INT_ADD", "register:40f0:8", ["const:4ad174:8", "const:4:8"]]
+ 004ad174 ["CALL", null, ["callee:0043bb60:8"]]
- 004ad134 bytes 7b3afe97
+ 004ad174 bytes 7b3afe97
- 004ad164 ["COPY", "tmp:0:8", ["const:568:8"]]
- 004ad164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004ad164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004ad164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004ad1a4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 004ad1a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004ad1a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004ad1a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004ad164 bytes 4aa11591
+ 004ad1a4 bytes 4aa11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c672c3c8033a8959104a818c82be753"></a>

### [`004ad1c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md) → [`004ad200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad200.md) _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58970`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58970.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a40.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ad314",
      "incomplete_value": false,
      "site": "004ad31c",
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
            "const:fbb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ad2d4",
      "incomplete_value": false,
      "site": "004ad2dc",
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
            "const:8:8"
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
      "definition_site": "004ad34c",
      "incomplete_value": true,
      "site": "004ad358",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ad30c",
      "incomplete_value": true,
      "site": "004ad318",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "definition_site": "004ad348",
      "incomplete_value": false,
      "site": "004ad358",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004ad308",
      "incomplete_value": false,
      "site": "004ad318",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004ad314",
      "PARAM",
      [
        "storage",
        "002a2008",
        null,
        "string"
      ]
    ],
    [
      "004ad348",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ad34c",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad314",
      "PARAM",
      [
        "storage",
        "002a1fbb",
        null,
        "string"
      ]
    ],
    [
      "004ad348",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004ad34c",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad2dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md#insn-004ad2dc) · [`004ad318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md#insn-004ad318) · [`004ad338`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md#insn-004ad338)
- 新版 `004ad31c`（命令位置の公開資料なし） · `004ad358`（命令位置の公開資料なし） · `004ad378`（命令位置の公開資料なし）

~~~diff
- 004ad2dc ["INT_ADD", "register:40f0:8", ["const:4ad2dc:8", "const:4:8"]]
- 004ad2dc ["CALL", null, ["callee:0043de18:8"]]
+ 004ad31c ["INT_ADD", "register:40f0:8", ["const:4ad31c:8", "const:4:8"]]
+ 004ad31c ["CALL", null, ["callee:0043de18:8"]]
- 004ad2dc bytes bf42fe97
+ 004ad31c bytes bf42fe97
- 004ad318 ["INT_ADD", "register:40f0:8", ["const:4ad318:8", "const:4:8"]]
- 004ad318 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004ad358 ["INT_ADD", "register:40f0:8", ["const:4ad358:8", "const:4:8"]]
+ 004ad358 ["CALL", null, ["callee:00c57fe0:8"]]
- 004ad318 bytes feaa1e94
+ 004ad358 bytes 22ab1e94
- 004ad338 ["INT_ADD", "register:40f0:8", ["const:4ad338:8", "const:4:8"]]
- 004ad338 ["CALL", null, ["callee:0043de18:8"]]
+ 004ad378 ["INT_ADD", "register:40f0:8", ["const:4ad378:8", "const:4:8"]]
+ 004ad378 ["CALL", null, ["callee:0043de18:8"]]
- 004ad338 bytes a842fe97
+ 004ad378 bytes a842fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37462a5d64e00ca2622ad9ae9a72f232"></a>

### [`004ad4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) → [`004ad4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) · 呼出先 8件 [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) · 呼出先 8件 [`004b2294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) [`004b2600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad5b0",
      "incomplete_value": true,
      "site": "004ad5b0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
    "old": {
      "definition_site": "004ad570",
      "incomplete_value": true,
      "site": "004ad570",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad638",
      "incomplete_value": true,
      "site": "004ad638",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
    "old": {
      "definition_site": "004ad5f8",
      "incomplete_value": true,
      "site": "004ad5f8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004ad724",
      "incomplete_value": true,
      "site": "004ad724",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
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
    "old": {
      "definition_site": "004ad6e4",
      "incomplete_value": true,
      "site": "004ad6e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40c0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004ad5a0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ad628",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004ad714",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ad5a0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004ad628",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004ad714",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ad570`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md#insn-004ad570) · [`004ad5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md#insn-004ad5f8) · [`004ad6e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md#insn-004ad6e4)
- 新版 `004ad5b0`（命令位置の公開資料なし） · `004ad638`（命令位置の公開資料なし） · `004ad724`（命令位置の公開資料なし）

~~~diff
- 004ad570 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad570 ["INT_ADD", "register:40f0:8", ["const:4ad570:8", "const:4:8"]]
- 004ad570 ["CALLIND", null, ["register:0:8"]]
+ 004ad5b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad5b0 ["INT_ADD", "register:40f0:8", ["const:4ad5b0:8", "const:4:8"]]
+ 004ad5b0 ["CALLIND", null, ["register:0:8"]]
- 004ad570 bytes 20013fd6
+ 004ad5b0 bytes 20013fd6
- 004ad5f8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad5f8 ["INT_ADD", "register:40f0:8", ["const:4ad5f8:8", "const:4:8"]]
- 004ad5f8 ["CALLIND", null, ["register:0:8"]]
+ 004ad638 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad638 ["INT_ADD", "register:40f0:8", ["const:4ad638:8", "const:4:8"]]
+ 004ad638 ["CALLIND", null, ["register:0:8"]]
- 004ad5f8 bytes 20013fd6
+ 004ad638 bytes 20013fd6
- 004ad6e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004ad6e4 ["INT_ADD", "register:40f0:8", ["const:4ad6e4:8", "const:4:8"]]
- 004ad6e4 ["CALLIND", null, ["register:0:8"]]
+ 004ad724 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004ad724 ["INT_ADD", "register:40f0:8", ["const:4ad724:8", "const:4:8"]]
+ 004ad724 ["CALLIND", null, ["register:0:8"]]
- 004ad6e4 bytes 20013fd6
+ 004ad724 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90e128fcecc4f2433fc18788dea98932"></a>

### [`004ad9ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md) → [`004ad9ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad9ec.md) _ZN5Botan12ucs2_to_utf8EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58980.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a50.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004f9250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9250.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "definition_site": "004ada78",
      "incomplete_value": false,
      "site": "004ada80",
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
            "const:26e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ada38",
      "incomplete_value": false,
      "site": "004ada40",
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
            "const:2c2:8"
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
      "definition_site": "004adab0",
      "incomplete_value": true,
      "site": "004adabc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ada70",
      "incomplete_value": true,
      "site": "004ada7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "definition_site": "004adaac",
      "incomplete_value": false,
      "site": "004adabc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004ada6c",
      "incomplete_value": false,
      "site": "004ada7c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004ada78",
      "PARAM",
      [
        "storage",
        "002ba2c2",
        null,
        "string"
      ]
    ],
    [
      "004adaac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004adab0",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ada78",
      "PARAM",
      [
        "storage",
        "002ba26e",
        null,
        "string"
      ]
    ],
    [
      "004adaac",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004adab0",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ada40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md#insn-004ada40) · [`004ada7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md#insn-004ada7c) · [`004ad9f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md#insn-004ad9f8)
- 新版 `004ada80`（命令位置の公開資料なし） · `004adabc`（命令位置の公開資料なし） · `004ada38`（命令位置の公開資料なし）

~~~diff
- 004ada40 ["INT_ADD", "register:40f0:8", ["const:4ada40:8", "const:4:8"]]
- 004ada40 ["CALL", null, ["callee:0043de18:8"]]
+ 004ada80 ["INT_ADD", "register:40f0:8", ["const:4ada80:8", "const:4:8"]]
+ 004ada80 ["CALL", null, ["callee:0043de18:8"]]
- 004ada40 bytes e640fe97
+ 004ada80 bytes e640fe97
- 004ada7c ["INT_ADD", "register:40f0:8", ["const:4ada7c:8", "const:4:8"]]
- 004ada7c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004adabc ["INT_ADD", "register:40f0:8", ["const:4adabc:8", "const:4:8"]]
+ 004adabc ["CALL", null, ["callee:00c57fe0:8"]]
- 004ada7c bytes 25a91e94
+ 004adabc bytes 49a91e94
- 004ad9f8 ["INT_ADD", "register:40f0:8", ["const:4ad9f8:8", "const:4:8"]]
- 004ad9f8 ["CALL", null, ["callee:004f9250:8"]]
+ 004ada38 ["INT_ADD", "register:40f0:8", ["const:4ada38:8", "const:4:8"]]
+ 004ada38 ["CALL", null, ["callee:004f9250:8"]]
- 004ad9f8 bytes 062e0194
+ 004ada38 bytes 062e0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c142d0efb3b95e1a486f8eb3521a1fb"></a>

### [`004adae4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md) → [`004adb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adb24.md) _ZN5Botan12ucs4_to_utf8EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58990`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58990.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a60.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004f9250`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9250.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

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
      "definition_site": "004adbb0",
      "incomplete_value": false,
      "site": "004adbb8",
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
            "const:165:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004adb70",
      "incomplete_value": false,
      "site": "004adb78",
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
            "const:1b2:8"
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
      "definition_site": "004adbe8",
      "incomplete_value": true,
      "site": "004adbf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004adba8",
      "incomplete_value": true,
      "site": "004adbb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "definition_site": "004adbe4",
      "incomplete_value": false,
      "site": "004adbf4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004adba4",
      "incomplete_value": false,
      "site": "004adbb4",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004adbb0",
      "PARAM",
      [
        "storage",
        "002a41b2",
        null,
        "string"
      ]
    ],
    [
      "004adbe4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004adbe8",
      "READ",
      [
        "storage",
        "00c9ad50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004adbb0",
      "PARAM",
      [
        "storage",
        "002a4165",
        null,
        "string"
      ]
    ],
    [
      "004adbe4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004adbe8",
      "READ",
      [
        "storage",
        "00c9ae20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adb78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md#insn-004adb78) · [`004adbb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md#insn-004adbb4) · [`004adb30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md#insn-004adb30)
- 新版 `004adbb8`（命令位置の公開資料なし） · `004adbf4`（命令位置の公開資料なし） · `004adb70`（命令位置の公開資料なし）

~~~diff
- 004adb78 ["INT_ADD", "register:40f0:8", ["const:4adb78:8", "const:4:8"]]
- 004adb78 ["CALL", null, ["callee:0043de18:8"]]
+ 004adbb8 ["INT_ADD", "register:40f0:8", ["const:4adbb8:8", "const:4:8"]]
+ 004adbb8 ["CALL", null, ["callee:0043de18:8"]]
- 004adb78 bytes 9840fe97
+ 004adbb8 bytes 9840fe97
- 004adbb4 ["INT_ADD", "register:40f0:8", ["const:4adbb4:8", "const:4:8"]]
- 004adbb4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004adbf4 ["INT_ADD", "register:40f0:8", ["const:4adbf4:8", "const:4:8"]]
+ 004adbf4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004adbb4 bytes d7a81e94
+ 004adbf4 bytes fba81e94
- 004adb30 ["INT_ADD", "register:40f0:8", ["const:4adb30:8", "const:4:8"]]
- 004adb30 ["CALL", null, ["callee:004f9250:8"]]
+ 004adb70 ["INT_ADD", "register:40f0:8", ["const:4adb70:8", "const:4:8"]]
+ 004adb70 ["CALL", null, ["callee:004f9250:8"]]
- 004adb30 bytes b82d0194
+ 004adb70 bytes b82d0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da68786fc795ca38fc3ed4f928abc858"></a>

### [`004adc1c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md) → [`004adc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adc5c.md) _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a70.md) · 呼出先 3件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589a0.md) [`00c589b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589b0.md)
- 新版 呼出元 1件 [`00c59b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b40.md) · 呼出先 3件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58a70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a70.md) [`00c58a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004adc88",
      "incomplete_value": true,
      "site": "004adc88",
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
      "definition_site": "004adc48",
      "incomplete_value": true,
      "site": "004adc48",
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
      "004adc78",
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      "004adc88",
      "DATA",
      [
        "storage",
        "00c66378",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "004adc78",
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      "004adc88",
      "DATA",
      [
        "storage",
        "00c66448",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004adc38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md#insn-004adc38) · [`004adc5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md#insn-004adc5c) · [`004adc6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md#insn-004adc6c)
- 新版 `004adc78`（命令位置の公開資料なし） · `004adc9c`（命令位置の公開資料なし） · `004adcac`（命令位置の公開資料なし）

~~~diff
- 004adc38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
- 004adc38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004adc78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
+ 004adc78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004adc38 bytes 08d946f9
+ 004adc78 bytes 084147f9
- 004adc5c ["INT_ADD", "register:40f0:8", ["const:4adc5c:8", "const:4:8"]]
- 004adc5c ["CALL", null, ["callee:00c58a70:8"]]
+ 004adc9c ["INT_ADD", "register:40f0:8", ["const:4adc9c:8", "const:4:8"]]
+ 004adc9c ["CALL", null, ["callee:00c58a70:8"]]
- 004adc5c bytes 51ab1e94
+ 004adc9c bytes 75ab1e94
- 004adc6c ["INT_ADD", "register:40f0:8", ["const:4adc6c:8", "const:4:8"]]
- 004adc6c ["CALL", null, ["callee:00c58a80:8"]]
+ 004adcac ["INT_ADD", "register:40f0:8", ["const:4adcac:8", "const:4:8"]]
+ 004adcac ["CALL", null, ["callee:00c58a80:8"]]
- 004adc6c bytes 51ab1e94
+ 004adcac bytes 75ab1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dbffb4f10e85d5f02ab0738035ec491"></a>

### [`004add64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md) → [`004adda4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adda4.md) _ZN5Botan9X509_Time6set_toERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589c0.md) · 呼出先 16件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540d7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c58a90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a90.md) · 呼出先 16件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540dbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件

アドレスに依存する影響 `call_argument_candidate` 5件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004ae324",
      "incomplete_value": true,
      "site": "004ae328",
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
      "definition_site": "004ae2e4",
      "incomplete_value": true,
      "site": "004ae2e8",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ade54",
      "incomplete_value": false,
      "site": "004ade60",
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
            "const:ab9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ade14",
      "incomplete_value": false,
      "site": "004ade20",
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
            "const:b15:8"
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
      "definition_site": "004ade68",
      "incomplete_value": false,
      "site": "004ade70",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ade28",
      "incomplete_value": false,
      "site": "004ade30",
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
            "const:48c:8"
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
      "004ade54",
      "PARAM",
      [
        "storage",
        "002a8b15",
        null,
        "string"
      ]
    ],
    [
      "004ade68",
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ],
    [
      "004adeb4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004ade54",
      "PARAM",
      [
        "storage",
        "002a8ab9",
        null,
        "string"
      ]
    ],
    [
      "004ade68",
      "PARAM",
      [
        "storage",
        "002a6430",
        null,
        null
      ]
    ],
    [
      "004adeb4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ade20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md#insn-004ade20) · [`004ade30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md#insn-004ade30) · [`004ade84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md#insn-004ade84)
- 新版 `004ade60`（命令位置の公開資料なし） · `004ade70`（命令位置の公開資料なし） · `004adec4`（命令位置の公開資料なし）

~~~diff
- 004ade20 ["INT_ADD", "register:40f0:8", ["const:4ade20:8", "const:4:8"]]
- 004ade20 ["CALL", null, ["callee:00c58180:8"]]
+ 004ade60 ["INT_ADD", "register:40f0:8", ["const:4ade60:8", "const:4:8"]]
+ 004ade60 ["CALL", null, ["callee:00c58180:8"]]
- 004ade20 bytes a4a81e94
+ 004ade60 bytes c8a81e94
- 004ade30 ["INT_ADD", "register:40f0:8", ["const:4ade30:8", "const:4:8"]]
- 004ade30 ["CALL", null, ["callee:00c58040:8"]]
+ 004ade70 ["INT_ADD", "register:40f0:8", ["const:4ade70:8", "const:4:8"]]
+ 004ade70 ["CALL", null, ["callee:00c58040:8"]]
- 004ade30 bytes 50a81e94
+ 004ade70 bytes 74a81e94
- 004ade84 ["INT_ADD", "register:40f0:8", ["const:4ade84:8", "const:4:8"]]
- 004ade84 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004adec4 ["INT_ADD", "register:40f0:8", ["const:4adec4:8", "const:4:8"]]
+ 004adec4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004ade84 bytes 23a81e94
+ 004adec4 bytes 47a81e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f876e0bab8594f6fb391ada70261a11f"></a>

### [`004ae584`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md) → [`004ae5c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae5c4.md) _ZNK5Botan9X509_Time11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

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
      "definition_site": "004ae670",
      "incomplete_value": false,
      "site": "004ae678",
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
            "const:fe1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae630",
      "incomplete_value": false,
      "site": "004ae638",
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
            "const:2e:8"
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
      "definition_site": "004ae6a8",
      "incomplete_value": true,
      "site": "004ae6b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ae668",
      "incomplete_value": true,
      "site": "004ae674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004ae6a4",
      "incomplete_value": false,
      "site": "004ae6b4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004ae664",
      "incomplete_value": false,
      "site": "004ae674",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004ae670",
      "PARAM",
      [
        "storage",
        "002a302e",
        null,
        "string"
      ]
    ],
    [
      "004ae6a4",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004ae6a8",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004ae670",
      "PARAM",
      [
        "storage",
        "002a2fe1",
        null,
        "string"
      ]
    ],
    [
      "004ae6a4",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004ae6a8",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae5f8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md#insn-004ae5f8) · [`004ae638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md#insn-004ae638) · [`004ae674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md#insn-004ae674)
- 新版 `004ae638`（命令位置の公開資料なし） · `004ae678`（命令位置の公開資料なし） · `004ae6b4`（命令位置の公開資料なし）

~~~diff
- 004ae5f8 ["INT_ADD", "register:40f0:8", ["const:4ae5f8:8", "const:4:8"]]
- 004ae5f8 ["CALL", null, ["callee:00c57f80:8"]]
+ 004ae638 ["INT_ADD", "register:40f0:8", ["const:4ae638:8", "const:4:8"]]
+ 004ae638 ["CALL", null, ["callee:00c57f80:8"]]
- 004ae5f8 bytes 2ea61e94
+ 004ae638 bytes 52a61e94
- 004ae638 ["INT_ADD", "register:40f0:8", ["const:4ae638:8", "const:4:8"]]
- 004ae638 ["CALL", null, ["callee:0043de18:8"]]
+ 004ae678 ["INT_ADD", "register:40f0:8", ["const:4ae678:8", "const:4:8"]]
+ 004ae678 ["CALL", null, ["callee:0043de18:8"]]
- 004ae638 bytes e83dfe97
+ 004ae678 bytes e83dfe97
- 004ae674 ["INT_ADD", "register:40f0:8", ["const:4ae674:8", "const:4:8"]]
- 004ae674 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004ae6b4 ["INT_ADD", "register:40f0:8", ["const:4ae6b4:8", "const:4:8"]]
+ 004ae6b4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004ae674 bytes 27a61e94
+ 004ae6b4 bytes 4ba61e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dde38124e013c666c7183ab738a14ff9"></a>

### [`004ae6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) → [`004ae71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae71c.md) _ZNK5Botan9X509_Time9to_stringEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589d0.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58aa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58aa0.md) · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004ae7dc",
      "incomplete_value": false,
      "site": "004ae7e4",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae79c",
      "incomplete_value": false,
      "site": "004ae7a4",
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
            "const:9cf:8"
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
      "definition_site": "004ae8d0",
      "incomplete_value": false,
      "site": "004ae8d8",
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
            "const:809:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004ae890",
      "incomplete_value": false,
      "site": "004ae898",
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
            "const:865:8"
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
      "definition_site": "004ae908",
      "incomplete_value": true,
      "site": "004ae914",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004ae8c8",
      "incomplete_value": true,
      "site": "004ae8d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "004ae7dc",
      "PARAM",
      [
        "storage",
        "002b19cf",
        null,
        null
      ]
    ],
    [
      "004ae87c",
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ],
    [
      "004ae8d0",
      "PARAM",
      [
        "storage",
        "002af865",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004ae7dc",
      "PARAM",
      [
        "storage",
        "002b1a00",
        null,
        null
      ]
    ],
    [
      "004ae87c",
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ],
    [
      "004ae8d0",
      "PARAM",
      [
        "storage",
        "002af809",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004ae7a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md#insn-004ae7a4) · [`004ae898`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md#insn-004ae898) · [`004ae8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md#insn-004ae8c4)
- 新版 `004ae7e4`（命令位置の公開資料なし） · `004ae8d8`（命令位置の公開資料なし） · `004ae904`（命令位置の公開資料なし）

~~~diff
- 004ae7a4 ["INT_ADD", "register:40f0:8", ["const:4ae7a4:8", "const:4:8"]]
- 004ae7a4 ["CALL", null, ["callee:00c58040:8"]]
+ 004ae7e4 ["INT_ADD", "register:40f0:8", ["const:4ae7e4:8", "const:4:8"]]
+ 004ae7e4 ["CALL", null, ["callee:00c58040:8"]]
- 004ae7a4 bytes f3a51e94
+ 004ae7e4 bytes 17a61e94
- 004ae898 ["INT_ADD", "register:40f0:8", ["const:4ae898:8", "const:4:8"]]
- 004ae898 ["CALL", null, ["callee:0043de18:8"]]
+ 004ae8d8 ["INT_ADD", "register:40f0:8", ["const:4ae8d8:8", "const:4:8"]]
+ 004ae8d8 ["CALL", null, ["callee:0043de18:8"]]
- 004ae898 bytes 503dfe97
+ 004ae8d8 bytes 503dfe97
- 004ae8c4 ["COPY", "register:4010:8", ["const:535868:8"]]
+ 004ae904 ["COPY", "register:4010:8", ["const:5358a8:8"]]
- 004ae8c4 bytes 227d4310
+ 004ae904 bytes 227d4310
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcba1f44be185dbb91ee22fea7fb14fb"></a>

### [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) → [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) FUN_004aeca4

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 29件 [`004a559c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) [`004a5ae0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) [`004ac1e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) [`004ae6dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) [`004aecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) · 呼出先 1件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 29件 [`004a55dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) [`004a5b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5b20.md) [`004ac224`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac224.md) [`004ae71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae71c.md) [`004aed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aed1c.md) · 呼出先 1件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "definition_site": "004aecc0",
      "incomplete_value": true,
      "site": "004aecc0",
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
      "definition_site": "004aec80",
      "incomplete_value": true,
      "site": "004aec80",
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
      "definition_site": "004aecf4",
      "incomplete_value": true,
      "site": "004aecf8",
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
      "definition_site": "004aecb4",
      "incomplete_value": true,
      "site": "004aecb8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004aecb8",
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      "004aecc0",
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aecf0",
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aecb8",
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      "004aecc0",
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004aecf0",
      "READ",
      [
        "storage",
        "00c9aea8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aec78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md#insn-004aec78) · [`004aeca8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md#insn-004aeca8) · [`004aecb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md#insn-004aecb0)
- 新版 `004aecb8`（命令位置の公開資料なし） · `004aece8`（命令位置の公開資料なし） · `004aecf0`（命令位置の公開資料なし）

~~~diff
- 004aec78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 004aec78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aecb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
+ 004aecb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004aec78 bytes 08e946f9
+ 004aecb8 bytes 085147f9
- 004aeca8 ["INT_ADD", "register:40f0:8", ["const:4aeca8:8", "const:4:8"]]
- 004aeca8 ["CALL", null, ["callee:0043bb60:8"]]
+ 004aece8 ["INT_ADD", "register:40f0:8", ["const:4aece8:8", "const:4:8"]]
+ 004aece8 ["CALL", null, ["callee:0043bb60:8"]]
- 004aeca8 bytes 9e33fe97
+ 004aece8 bytes 9e33fe97
- 004aecb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 004aecb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004aecf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
+ 004aecf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004aecb0 bytes 08ed46f9
+ 004aecf0 bytes 085547f9
~~~


<a id="compare-894bc2977b0cbb3ef69d24b35e93032a"></a>

### [`004aecdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) → [`004aed1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aed1c.md) _ZNK5Botan9X509_Time3cmpERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58ab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

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
      "definition_site": "004aee00",
      "incomplete_value": false,
      "site": "004aee08",
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
            "const:dee:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aedc0",
      "incomplete_value": false,
      "site": "004aedc8",
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
            "const:e42:8"
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
      "definition_site": "004aee3c",
      "incomplete_value": true,
      "site": "004aee48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004aedfc",
      "incomplete_value": true,
      "site": "004aee08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "definition_site": "004aee38",
      "incomplete_value": false,
      "site": "004aee48",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004aedf8",
      "incomplete_value": false,
      "site": "004aee08",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004aee00",
      "PARAM",
      [
        "storage",
        "002b8e42",
        null,
        "string"
      ]
    ],
    [
      "004aee38",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004aee3c",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aee00",
      "PARAM",
      [
        "storage",
        "002b8dee",
        null,
        "string"
      ]
    ],
    [
      "004aee38",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004aee3c",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aedc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md#insn-004aedc8) · [`004aee08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md#insn-004aee08) · [`004aedb4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md#insn-004aedb4)
- 新版 `004aee08`（命令位置の公開資料なし） · `004aee48`（命令位置の公開資料なし） · `004aedf4`（命令位置の公開資料なし）

~~~diff
- 004aedc8 ["INT_ADD", "register:40f0:8", ["const:4aedc8:8", "const:4:8"]]
- 004aedc8 ["CALL", null, ["callee:0043de18:8"]]
+ 004aee08 ["INT_ADD", "register:40f0:8", ["const:4aee08:8", "const:4:8"]]
+ 004aee08 ["CALL", null, ["callee:0043de18:8"]]
- 004aedc8 bytes 043cfe97
+ 004aee08 bytes 043cfe97
- 004aee08 ["INT_ADD", "register:40f0:8", ["const:4aee08:8", "const:4:8"]]
- 004aee08 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004aee48 ["INT_ADD", "register:40f0:8", ["const:4aee48:8", "const:4:8"]]
+ 004aee48 ["CALL", null, ["callee:00c57fe0:8"]]
- 004aee08 bytes 42a41e94
+ 004aee48 bytes 66a41e94
- 004aedb4 ["INT_ADD", "register:40f0:8", ["const:4aedb4:8", "const:4:8"]]
- 004aedb4 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004aedf4 ["INT_ADD", "register:40f0:8", ["const:4aedf4:8", "const:4:8"]]
+ 004aedf4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004aedb4 bytes 4fa41e94
+ 004aedf4 bytes 73a41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60100c566080c06e4bc459b51ff08cd0"></a>

### [`004aee5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md) → [`004aee9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aee9c.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md) · 呼出先 8件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00c588c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588c0.md) · 呼出先 8件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aef5c",
      "incomplete_value": false,
      "site": "004aef68",
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
            "const:2b5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aef1c",
      "incomplete_value": false,
      "site": "004aef28",
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
            "const:309:8"
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
      "definition_site": "004aef9c",
      "incomplete_value": true,
      "site": "004aefa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004aef5c",
      "incomplete_value": true,
      "site": "004aef68",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004aef98",
      "incomplete_value": false,
      "site": "004aefa8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004aef58",
      "incomplete_value": false,
      "site": "004aef68",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004aef5c",
      "PARAM",
      [
        "storage",
        "002ba309",
        null,
        "string"
      ]
    ],
    [
      "004aef98",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004aef9c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004aef5c",
      "PARAM",
      [
        "storage",
        "002ba2b5",
        null,
        "string"
      ]
    ],
    [
      "004aef98",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004aef9c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004aef28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md#insn-004aef28) · [`004aef68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md#insn-004aef68) · [`004aef90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md#insn-004aef90)
- 新版 `004aef68`（命令位置の公開資料なし） · `004aefa8`（命令位置の公開資料なし） · `004aefd0`（命令位置の公開資料なし）

~~~diff
- 004aef28 ["INT_ADD", "register:40f0:8", ["const:4aef28:8", "const:4:8"]]
- 004aef28 ["CALL", null, ["callee:00c58180:8"]]
+ 004aef68 ["INT_ADD", "register:40f0:8", ["const:4aef68:8", "const:4:8"]]
+ 004aef68 ["CALL", null, ["callee:00c58180:8"]]
- 004aef28 bytes 62a41e94
+ 004aef68 bytes 86a41e94
- 004aef68 ["INT_ADD", "register:40f0:8", ["const:4aef68:8", "const:4:8"]]
- 004aef68 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004aefa8 ["INT_ADD", "register:40f0:8", ["const:4aefa8:8", "const:4:8"]]
+ 004aefa8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004aef68 bytes eaa31e94
+ 004aefa8 bytes 0ea41e94
- 004aef90 ["INT_ADD", "register:40f0:8", ["const:4aef90:8", "const:4:8"]]
- 004aef90 ["CALL", null, ["callee:00c58180:8"]]
+ 004aefd0 ["INT_ADD", "register:40f0:8", ["const:4aefd0:8", "const:4:8"]]
+ 004aefd0 ["CALL", null, ["callee:00c58180:8"]]
- 004aef90 bytes 48a41e94
+ 004aefd0 bytes 6ca41e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c50328d7a6c87d55b97fbcc79f72f7a3"></a>

### [`004af1b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md) → [`004af1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1f8.md) _ZNK5Botan14calendar_point16to_std_timepointEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a00`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a00.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58ad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ad0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

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
      "definition_site": "004af320",
      "incomplete_value": false,
      "site": "004af328",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af2e0",
      "incomplete_value": false,
      "site": "004af2e8",
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
            "const:bec:8"
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
      "definition_site": "004af35c",
      "incomplete_value": true,
      "site": "004af368",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004af31c",
      "incomplete_value": true,
      "site": "004af328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004af358",
      "incomplete_value": false,
      "site": "004af368",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004af318",
      "incomplete_value": false,
      "site": "004af328",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004af320",
      "PARAM",
      [
        "storage",
        "002b0bec",
        null,
        "string"
      ]
    ],
    [
      "004af358",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004af35c",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004af320",
      "PARAM",
      [
        "storage",
        "002b0b90",
        null,
        "string"
      ]
    ],
    [
      "004af358",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004af35c",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af2e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md#insn-004af2e8) · [`004af328`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md#insn-004af328) · [`004af34c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md#insn-004af34c)
- 新版 `004af328`（命令位置の公開資料なし） · `004af368`（命令位置の公開資料なし） · `004af38c`（命令位置の公開資料なし）

~~~diff
- 004af2e8 ["INT_ADD", "register:40f0:8", ["const:4af2e8:8", "const:4:8"]]
- 004af2e8 ["CALL", null, ["callee:0043de18:8"]]
+ 004af328 ["INT_ADD", "register:40f0:8", ["const:4af328:8", "const:4:8"]]
+ 004af328 ["CALL", null, ["callee:0043de18:8"]]
- 004af2e8 bytes bc3afe97
+ 004af328 bytes bc3afe97
- 004af328 ["INT_ADD", "register:40f0:8", ["const:4af328:8", "const:4:8"]]
- 004af328 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004af368 ["INT_ADD", "register:40f0:8", ["const:4af368:8", "const:4:8"]]
+ 004af368 ["CALL", null, ["callee:00c57fe0:8"]]
- 004af328 bytes faa21e94
+ 004af368 bytes 1ea31e94
- 004af34c ["INT_ADD", "register:40f0:8", ["const:4af34c:8", "const:4:8"]]
- 004af34c ["CALL", null, ["callee:0043de18:8"]]
+ 004af38c ["INT_ADD", "register:40f0:8", ["const:4af38c:8", "const:4:8"]]
+ 004af38c ["CALL", null, ["callee:0043de18:8"]]
- 004af34c bytes a33afe97
+ 004af38c bytes a33afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-985dab958df227ae40f92e9cc29b4606"></a>

### [`004af484`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md) → [`004af4c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4c4.md) _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58730`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) · 呼出先 9件 [`004a684c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58800.md) · 呼出先 9件 [`004a688c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.61% / 新版 95.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af558",
      "incomplete_value": false,
      "site": "004af564",
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
            "const:a21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af518",
      "incomplete_value": false,
      "site": "004af524",
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
            "const:9f0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004af584",
      "incomplete_value": false,
      "site": "004af58c",
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
            "const:2f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af544",
      "incomplete_value": false,
      "site": "004af54c",
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
            "const:352:8"
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
      "definition_site": "004af5c8",
      "incomplete_value": false,
      "site": "004af5d0",
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
            "const:225:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af588",
      "incomplete_value": false,
      "site": "004af590",
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
            "const:279:8"
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
      "004af558",
      "PARAM",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      "004af584",
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      "004af5c8",
      "PARAM",
      [
        "storage",
        "002bb279",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004af558",
      "PARAM",
      [
        "storage",
        "002b1a21",
        null,
        "string"
      ]
    ],
    [
      "004af584",
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ],
    [
      "004af5c8",
      "PARAM",
      [
        "storage",
        "002bb225",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af524`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md#insn-004af524) · [`004af54c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md#insn-004af54c) · [`004af590`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md#insn-004af590)
- 新版 `004af564`（命令位置の公開資料なし） · `004af58c`（命令位置の公開資料なし） · `004af5d0`（命令位置の公開資料なし）

~~~diff
- 004af524 ["INT_ADD", "register:40f0:8", ["const:4af524:8", "const:4:8"]]
- 004af524 ["CALL", null, ["callee:00c58030:8"]]
+ 004af564 ["INT_ADD", "register:40f0:8", ["const:4af564:8", "const:4:8"]]
+ 004af564 ["CALL", null, ["callee:00c58030:8"]]
- 004af524 bytes 8fa21e94
+ 004af564 bytes b3a21e94
- 004af54c ["INT_ADD", "register:40f0:8", ["const:4af54c:8", "const:4:8"]]
- 004af54c ["CALL", null, ["callee:00c58040:8"]]
+ 004af58c ["INT_ADD", "register:40f0:8", ["const:4af58c:8", "const:4:8"]]
+ 004af58c ["CALL", null, ["callee:00c58040:8"]]
- 004af54c bytes 89a21e94
+ 004af58c bytes ada21e94
- 004af590 ["INT_ADD", "register:40f0:8", ["const:4af590:8", "const:4:8"]]
- 004af590 ["CALL", null, ["callee:00c58040:8"]]
+ 004af5d0 ["INT_ADD", "register:40f0:8", ["const:4af5d0:8", "const:4:8"]]
+ 004af5d0 ["CALL", null, ["callee:00c58040:8"]]
- 004af590 bytes 78a21e94
+ 004af5d0 bytes 9ca21e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5f660da4af46de69ffb5dce56692550"></a>

### [`004af894`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md) → [`004af8d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af8d4.md) _ZN5Botan11BER_Decoder10verify_endEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a20.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58af0.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

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
      "definition_site": "004af958",
      "incomplete_value": false,
      "site": "004af960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:e29:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004af918",
      "incomplete_value": false,
      "site": "004af920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:e76:8"
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
      "definition_site": "004af994",
      "incomplete_value": true,
      "site": "004af9a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004af954",
      "incomplete_value": true,
      "site": "004af960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "definition_site": "004af990",
      "incomplete_value": false,
      "site": "004af9a0",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004af950",
      "incomplete_value": false,
      "site": "004af960",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004af958",
      "PARAM",
      [
        "storage",
        "0029ee76",
        null,
        "string"
      ]
    ],
    [
      "004af990",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004af994",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004af958",
      "PARAM",
      [
        "storage",
        "0029ee29",
        null,
        "string"
      ]
    ],
    [
      "004af990",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004af994",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004af920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md#insn-004af920) · [`004af960`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md#insn-004af960) · [`004af8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md#insn-004af8c4)
- 新版 `004af960`（命令位置の公開資料なし） · `004af9a0`（命令位置の公開資料なし） · `004af904`（命令位置の公開資料なし）

~~~diff
- 004af920 ["INT_ADD", "register:40f0:8", ["const:4af920:8", "const:4:8"]]
- 004af920 ["CALL", null, ["callee:0043de18:8"]]
+ 004af960 ["INT_ADD", "register:40f0:8", ["const:4af960:8", "const:4:8"]]
+ 004af960 ["CALL", null, ["callee:0043de18:8"]]
- 004af920 bytes 2e39fe97
+ 004af960 bytes 2e39fe97
- 004af960 ["INT_ADD", "register:40f0:8", ["const:4af960:8", "const:4:8"]]
- 004af960 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004af9a0 ["INT_ADD", "register:40f0:8", ["const:4af9a0:8", "const:4:8"]]
+ 004af9a0 ["CALL", null, ["callee:00c57fe0:8"]]
- 004af960 bytes 6ca11e94
+ 004af9a0 bytes 90a11e94
- 004af8c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 004af8c4 ["INT_ADD", "register:40f0:8", ["const:4af8c4:8", "const:4:8"]]
- 004af8c4 ["CALLIND", null, ["register:0:8"]]
+ 004af904 ["COPY", "register:0:8", ["register:4040:8"]]
+ 004af904 ["INT_ADD", "register:40f0:8", ["const:4af904:8", "const:4:8"]]
+ 004af904 ["CALLIND", null, ["register:0:8"]]
- 004af8c4 bytes 00013fd6
+ 004af904 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f05f27832ec54569d23eccba97b261"></a>

### [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) → [`004afa58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) FUN_004afa58

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`004a8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

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
      "definition_site": "004afb60",
      "incomplete_value": false,
      "site": "004afb68",
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
            "const:1f6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afb20",
      "incomplete_value": false,
      "site": "004afb28",
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
            "const:243:8"
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
      "definition_site": "004afb98",
      "incomplete_value": true,
      "site": "004afba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004afb58",
      "incomplete_value": true,
      "site": "004afb64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "definition_site": "004afb94",
      "incomplete_value": false,
      "site": "004afba4",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004afb54",
      "incomplete_value": false,
      "site": "004afb64",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004afb60",
      "PARAM",
      [
        "storage",
        "002a1243",
        null,
        "string"
      ]
    ],
    [
      "004afb94",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004afb98",
      "READ",
      [
        "storage",
        "00c9ada8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004afb60",
      "PARAM",
      [
        "storage",
        "002a11f6",
        null,
        "string"
      ]
    ],
    [
      "004afb94",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004afb98",
      "READ",
      [
        "storage",
        "00c9ae78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004afb28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md#insn-004afb28) · [`004afb64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md#insn-004afb64) · [`004afb84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md#insn-004afb84)
- 新版 `004afb68`（命令位置の公開資料なし） · `004afba4`（命令位置の公開資料なし） · `004afbc4`（命令位置の公開資料なし）

~~~diff
- 004afb28 ["INT_ADD", "register:40f0:8", ["const:4afb28:8", "const:4:8"]]
- 004afb28 ["CALL", null, ["callee:0043de18:8"]]
+ 004afb68 ["INT_ADD", "register:40f0:8", ["const:4afb68:8", "const:4:8"]]
+ 004afb68 ["CALL", null, ["callee:0043de18:8"]]
- 004afb28 bytes ac38fe97
+ 004afb68 bytes ac38fe97
- 004afb64 ["INT_ADD", "register:40f0:8", ["const:4afb64:8", "const:4:8"]]
- 004afb64 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004afba4 ["INT_ADD", "register:40f0:8", ["const:4afba4:8", "const:4:8"]]
+ 004afba4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004afb64 bytes eba01e94
+ 004afba4 bytes 0fa11e94
- 004afb84 ["INT_ADD", "register:40f0:8", ["const:4afb84:8", "const:4:8"]]
- 004afb84 ["CALL", null, ["callee:0043de18:8"]]
+ 004afbc4 ["INT_ADD", "register:40f0:8", ["const:4afbc4:8", "const:4:8"]]
+ 004afbc4 ["CALL", null, ["callee:0043de18:8"]]
- 004afb84 bytes 9538fe97
+ 004afbc4 bytes 9538fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23d4782ca9a7d1929a116b88a940c5e4"></a>

### [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) → [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) FUN_004afc50

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`004f9a20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 2件 [`004a8928`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 18件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004afa58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) [`004afc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) [`004f9a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9a60.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 18件, `call_target` 3件

アドレスに依存する影響 `call_argument_candidate` 8件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004afdf0",
      "incomplete_value": true,
      "site": "004afdf0",
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
      "definition_site": "004afdb0",
      "incomplete_value": true,
      "site": "004afdb0",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004afed8",
      "incomplete_value": true,
      "site": "004afed8",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004afe98",
      "incomplete_value": true,
      "site": "004afe98",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004aff04",
      "incomplete_value": true,
      "site": "004aff04",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004afec4",
      "incomplete_value": true,
      "site": "004afec4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004afde0",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004afdf0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afe74",
      "READ",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004afde0",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "004afdf0",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "004afe74",
      "READ",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004afe98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md#insn-004afe98) · [`004afec4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md#insn-004afec4) · [`004afef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md#insn-004afef0)
- 新版 `004afed8`（命令位置の公開資料なし） · `004aff04`（命令位置の公開資料なし） · `004aff30`（命令位置の公開資料なし）

~~~diff
- 004afe98 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afe98 ["INT_ADD", "register:40f0:8", ["const:4afe98:8", "const:4:8"]]
- 004afe98 ["CALLIND", null, ["register:0:8"]]
+ 004afed8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004afed8 ["INT_ADD", "register:40f0:8", ["const:4afed8:8", "const:4:8"]]
+ 004afed8 ["CALLIND", null, ["register:0:8"]]
- 004afe98 bytes 20013fd6
+ 004afed8 bytes 20013fd6
- 004afec4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afec4 ["INT_ADD", "register:40f0:8", ["const:4afec4:8", "const:4:8"]]
- 004afec4 ["CALLIND", null, ["register:0:8"]]
+ 004aff04 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004aff04 ["INT_ADD", "register:40f0:8", ["const:4aff04:8", "const:4:8"]]
+ 004aff04 ["CALLIND", null, ["register:0:8"]]
- 004afec4 bytes 20013fd6
+ 004aff04 bytes 20013fd6
- 004afef0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004afef0 ["INT_ADD", "register:40f0:8", ["const:4afef0:8", "const:4:8"]]
- 004afef0 ["CALLIND", null, ["register:0:8"]]
+ 004aff30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004aff30 ["INT_ADD", "register:40f0:8", ["const:4aff30:8", "const:4:8"]]
+ 004aff30 ["CALLIND", null, ["register:0:8"]]
- 004afef0 bytes 20013fd6
+ 004aff30 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cddf53558624aab70f8e5b1691aad6d"></a>

### [`004b03f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md) → [`004b0430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0430.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a60.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543858`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58b30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b30.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543898`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

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
      "definition_site": "004b04e4",
      "incomplete_value": false,
      "site": "004b04ec",
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
            "const:aba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b04a4",
      "incomplete_value": false,
      "site": "004b04ac",
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
      "definition_site": "004b0520",
      "incomplete_value": true,
      "site": "004b052c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b04e0",
      "incomplete_value": true,
      "site": "004b04ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "definition_site": "004b051c",
      "incomplete_value": false,
      "site": "004b052c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b04dc",
      "incomplete_value": false,
      "site": "004b04ec",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b04e4",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        "string"
      ]
    ],
    [
      "004b051c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b0520",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b04e4",
      "PARAM",
      [
        "storage",
        "002a9aba",
        null,
        "string"
      ]
    ],
    [
      "004b051c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b0520",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b04ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md#insn-004b04ac) · [`004b04ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md#insn-004b04ec) · [`004b0498`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md#insn-004b0498)
- 新版 `004b04ec`（命令位置の公開資料なし） · `004b052c`（命令位置の公開資料なし） · `004b04d8`（命令位置の公開資料なし）

~~~diff
- 004b04ac ["INT_ADD", "register:40f0:8", ["const:4b04ac:8", "const:4:8"]]
- 004b04ac ["CALL", null, ["callee:0043de18:8"]]
+ 004b04ec ["INT_ADD", "register:40f0:8", ["const:4b04ec:8", "const:4:8"]]
+ 004b04ec ["CALL", null, ["callee:0043de18:8"]]
- 004b04ac bytes 4b36fe97
+ 004b04ec bytes 4b36fe97
- 004b04ec ["INT_ADD", "register:40f0:8", ["const:4b04ec:8", "const:4:8"]]
- 004b04ec ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b052c ["INT_ADD", "register:40f0:8", ["const:4b052c:8", "const:4:8"]]
+ 004b052c ["CALL", null, ["callee:00c57fe0:8"]]
- 004b04ec bytes 899e1e94
+ 004b052c bytes ad9e1e94
- 004b0498 ["INT_ADD", "register:40f0:8", ["const:4b0498:8", "const:4:8"]]
- 004b0498 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b04d8 ["INT_ADD", "register:40f0:8", ["const:4b04d8:8", "const:4:8"]]
+ 004b04d8 ["CALL", null, ["callee:00c57fc0:8"]]
- 004b0498 bytes 969e1e94
+ 004b04d8 bytes ba9e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151e3c7c0d87ee96348216c46a4663bc"></a>

### [`004b055c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b055c.md) → [`004b059c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b059c.md) _ZN5Botan11BER_DecoderC1EPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58740`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58740.md) · 呼出先 2件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58810.md) · 呼出先 2件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0598"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0598"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b05dc",
      "incomplete_value": true,
      "site": "004b05e0",
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
      "definition_site": "004b059c",
      "incomplete_value": true,
      "site": "004b05a0",
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
      "004b05d4",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b05e0",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b05d4",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "004b05e0",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0598`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b055c.md#insn-004b0598) · [`004b0588`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b055c.md#insn-004b0588)
- 新版 `004b05d8`（命令位置の公開資料なし） · `004b05c8`（命令位置の公開資料なし）

~~~diff
- 004b0598 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0598 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0598 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0598 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0598 bytes 1f7c01a9
+ 004b05d8 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b05d8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b05d8 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b05d8 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b05d8 bytes 1f7c01a9
- 004b0588 ["INT_ADD", "register:40f0:8", ["const:4b0588:8", "const:4:8"]]
- 004b0588 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b05c8 ["INT_ADD", "register:40f0:8", ["const:4b05c8:8", "const:4:8"]]
+ 004b05c8 ["CALL", null, ["callee:00c57f60:8"]]
- 004b0588 bytes 429e1e94
+ 004b05c8 bytes 669e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36052953d11a21a5d18a2d9b7c7475b2"></a>

### [`004b0638`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0638.md) → [`004b0678`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0678.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58890`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58890.md) · 呼出先 2件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58960.md) · 呼出先 2件 [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0674"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b06b8",
      "incomplete_value": true,
      "site": "004b06bc",
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
      "definition_site": "004b0678",
      "incomplete_value": true,
      "site": "004b067c",
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
      "004b06ac",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b06bc",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b06ac",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "004b06bc",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0674`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0638.md#insn-004b0674) · [`004b0660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0638.md#insn-004b0660)
- 新版 `004b06b4`（命令位置の公開資料なし） · `004b06a0`（命令位置の公開資料なし）

~~~diff
- 004b0674 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0674 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0674 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0674 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0674 bytes 1f7c01a9
+ 004b06b4 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b06b4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b06b4 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b06b4 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b06b4 bytes 1f7c01a9
- 004b0660 ["INT_ADD", "register:40f0:8", ["const:4b0660:8", "const:4:8"]]
- 004b0660 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b06a0 ["INT_ADD", "register:40f0:8", ["const:4b06a0:8", "const:4:8"]]
+ 004b06a0 ["CALL", null, ["callee:00c57f60:8"]]
- 004b0660 bytes 0c9e1e94
+ 004b06a0 bytes 309e1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a7efbd40869e01347ad9bd257497d742"></a>

### [`004b070c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b070c.md) → [`004b074c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b074c.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58880`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md) · 呼出先 2件 [`005403c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md) · 呼出先 2件 [`00540408`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "004b0748"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b078c",
      "incomplete_value": true,
      "site": "004b0790",
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
      "definition_site": "004b074c",
      "incomplete_value": true,
      "site": "004b0750",
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
      "004b0780",
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0790",
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "004b0780",
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "004b0790",
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0748`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b070c.md#insn-004b0748) · [`004b0734`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b070c.md#insn-004b0734)
- 新版 `004b0788`（命令位置の公開資料なし） · `004b0774`（命令位置の公開資料なし）

~~~diff
- 004b0748 ["COPY", "tmp:0:8", ["const:0:8"]]
- 004b0748 ["COPY", "tmp:1:8", ["const:0:8"]]
- 004b0748 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 004b0748 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 004b0748 bytes 1f7c01a9
+ 004b0788 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 004b0788 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 004b0788 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 004b0788 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 004b0788 bytes 1f7c01a9
- 004b0734 ["INT_ADD", "register:40f0:8", ["const:4b0734:8", "const:4:8"]]
- 004b0734 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b0774 ["INT_ADD", "register:40f0:8", ["const:4b0774:8", "const:4:8"]]
+ 004b0774 ["CALL", null, ["callee:00c57f60:8"]]
- 004b0734 bytes d79d1e94
+ 004b0774 bytes fb9d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d99405a04f43bf996a9f021520be04d"></a>

### [`004b0818`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md) → [`004b0858`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0858.md) _ZN5Botan11BER_Decoder11decode_nullEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

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
      "definition_site": "004b08bc",
      "incomplete_value": true,
      "site": "004b08bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b087c",
      "incomplete_value": true,
      "site": "004b087c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b0900",
      "incomplete_value": false,
      "site": "004b0908",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b08c0",
      "incomplete_value": false,
      "site": "004b08c8",
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
            "const:c29:8"
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
      "definition_site": "004b0938",
      "incomplete_value": true,
      "site": "004b0944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b08f8",
      "incomplete_value": true,
      "site": "004b0904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "004b08ac",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0900",
      "PARAM",
      [
        "storage",
        "002bfc29",
        null,
        "string"
      ]
    ],
    [
      "004b0934",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b08ac",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b0900",
      "PARAM",
      [
        "storage",
        "002bfbd5",
        null,
        "string"
      ]
    ],
    [
      "004b0934",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b087c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md#insn-004b087c) · [`004b08c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md#insn-004b08c8) · [`004b0904`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md#insn-004b0904)
- 新版 `004b08bc`（命令位置の公開資料なし） · `004b0908`（命令位置の公開資料なし） · `004b0944`（命令位置の公開資料なし）

~~~diff
- 004b087c ["COPY", "register:0:8", ["register:4050:8"]]
- 004b087c ["INT_ADD", "register:40f0:8", ["const:4b087c:8", "const:4:8"]]
- 004b087c ["CALLIND", null, ["register:0:8"]]
+ 004b08bc ["COPY", "register:0:8", ["register:4050:8"]]
+ 004b08bc ["INT_ADD", "register:40f0:8", ["const:4b08bc:8", "const:4:8"]]
+ 004b08bc ["CALLIND", null, ["register:0:8"]]
- 004b087c bytes 40013fd6
+ 004b08bc bytes 40013fd6
- 004b08c8 ["INT_ADD", "register:40f0:8", ["const:4b08c8:8", "const:4:8"]]
- 004b08c8 ["CALL", null, ["callee:0043de18:8"]]
+ 004b0908 ["INT_ADD", "register:40f0:8", ["const:4b0908:8", "const:4:8"]]
+ 004b0908 ["CALL", null, ["callee:0043de18:8"]]
- 004b08c8 bytes 4435fe97
+ 004b0908 bytes 4435fe97
- 004b0904 ["INT_ADD", "register:40f0:8", ["const:4b0904:8", "const:4:8"]]
- 004b0904 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b0944 ["INT_ADD", "register:40f0:8", ["const:4b0944:8", "const:4:8"]]
+ 004b0944 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b0904 bytes 839d1e94
+ 004b0944 bytes a79d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c65f4125b43db47446deb3291e6ebd5"></a>

### [`004b0968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md) → [`004b09a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b09a8.md) _ZN5Botan11BER_Decoder6decodeERbNS_8ASN1_TagES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588e0.md) · 呼出先 10件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c589b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589b0.md) · 呼出先 10件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.37% / 新版 94.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0a30",
      "incomplete_value": true,
      "site": "004b0a30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b09f0",
      "incomplete_value": true,
      "site": "004b09f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b0a78",
      "incomplete_value": false,
      "site": "004b0a80",
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
            "const:bf2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0a38",
      "incomplete_value": false,
      "site": "004b0a40",
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
            "const:c46:8"
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
      "definition_site": "004b0ab0",
      "incomplete_value": true,
      "site": "004b0abc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0a70",
      "incomplete_value": true,
      "site": "004b0a7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "004b0a20",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0a78",
      "PARAM",
      [
        "storage",
        "002bfc46",
        null,
        "string"
      ]
    ],
    [
      "004b0aac",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b0a20",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b0a78",
      "PARAM",
      [
        "storage",
        "002bfbf2",
        null,
        "string"
      ]
    ],
    [
      "004b0aac",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b09b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md#insn-004b09b0) · [`004b09f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md#insn-004b09f0) · [`004b0a40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md#insn-004b0a40)
- 新版 `004b09f0`（命令位置の公開資料なし） · `004b0a30`（命令位置の公開資料なし） · `004b0a80`（命令位置の公開資料なし）

~~~diff
- 004b09b0 ["INT_ADD", "register:40f0:8", ["const:4b09b0:8", "const:4:8"]]
- 004b09b0 ["CALL", null, ["callee:00c58800:8"]]
+ 004b09f0 ["INT_ADD", "register:40f0:8", ["const:4b09f0:8", "const:4:8"]]
+ 004b09f0 ["CALL", null, ["callee:00c58800:8"]]
- 004b09b0 bytes 609f1e94
+ 004b09f0 bytes 849f1e94
- 004b09f0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b09f0 ["INT_ADD", "register:40f0:8", ["const:4b09f0:8", "const:4:8"]]
- 004b09f0 ["CALLIND", null, ["register:0:8"]]
+ 004b0a30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0a30 ["INT_ADD", "register:40f0:8", ["const:4b0a30:8", "const:4:8"]]
+ 004b0a30 ["CALLIND", null, ["register:0:8"]]
- 004b09f0 bytes 20013fd6
+ 004b0a30 bytes 20013fd6
- 004b0a40 ["INT_ADD", "register:40f0:8", ["const:4b0a40:8", "const:4:8"]]
- 004b0a40 ["CALL", null, ["callee:0043de18:8"]]
+ 004b0a80 ["INT_ADD", "register:40f0:8", ["const:4b0a80:8", "const:4:8"]]
+ 004b0a80 ["CALL", null, ["callee:0043de18:8"]]
- 004b0a40 bytes e634fe97
+ 004b0a80 bytes e634fe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8abe8c0b717002522024e1919362b620"></a>

### [`004b0aec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md) → [`004b0b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0b2c.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a70.md) · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b40.md) · 呼出先 9件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

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
      "definition_site": "004b0c1c",
      "incomplete_value": true,
      "site": "004b0c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b0bdc",
      "incomplete_value": true,
      "site": "004b0bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004b0c60",
      "incomplete_value": false,
      "site": "004b0c68",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0c20",
      "incomplete_value": false,
      "site": "004b0c28",
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
            "const:48e:8"
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
      "definition_site": "004b0c98",
      "incomplete_value": true,
      "site": "004b0ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b0c58",
      "incomplete_value": true,
      "site": "004b0c64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "004b0c0c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0c60",
      "PARAM",
      [
        "storage",
        "002a648e",
        null,
        "string"
      ]
    ],
    [
      "004b0c94",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b0c0c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b0c60",
      "PARAM",
      [
        "storage",
        "002a6432",
        null,
        "string"
      ]
    ],
    [
      "004b0c94",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0bdc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md#insn-004b0bdc) · [`004b0c28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md#insn-004b0c28) · [`004b0c64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md#insn-004b0c64)
- 新版 `004b0c1c`（命令位置の公開資料なし） · `004b0c68`（命令位置の公開資料なし） · `004b0ca4`（命令位置の公開資料なし）

~~~diff
- 004b0bdc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0bdc ["INT_ADD", "register:40f0:8", ["const:4b0bdc:8", "const:4:8"]]
- 004b0bdc ["CALLIND", null, ["register:0:8"]]
+ 004b0c1c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0c1c ["INT_ADD", "register:40f0:8", ["const:4b0c1c:8", "const:4:8"]]
+ 004b0c1c ["CALLIND", null, ["register:0:8"]]
- 004b0bdc bytes 20013fd6
+ 004b0c1c bytes 20013fd6
- 004b0c28 ["INT_ADD", "register:40f0:8", ["const:4b0c28:8", "const:4:8"]]
- 004b0c28 ["CALL", null, ["callee:0043de18:8"]]
+ 004b0c68 ["INT_ADD", "register:40f0:8", ["const:4b0c68:8", "const:4:8"]]
+ 004b0c68 ["CALL", null, ["callee:0043de18:8"]]
- 004b0c28 bytes 6c34fe97
+ 004b0c68 bytes 6c34fe97
- 004b0c64 ["INT_ADD", "register:40f0:8", ["const:4b0c64:8", "const:4:8"]]
- 004b0c64 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b0ca4 ["INT_ADD", "register:40f0:8", ["const:4b0ca4:8", "const:4:8"]]
+ 004b0ca4 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b0c64 bytes ab9c1e94
+ 004b0ca4 bytes cf9c1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d751cd6630d95d1c71c708bcd2607b34"></a>

### [`004b0cc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md) → [`004b0d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0d08.md) _ZN5Botan11BER_Decoder26decode_octet_string_bigintERNS_6BigIntE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) [`00c58a90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a90.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md) [`00c58b60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b60.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0dd0",
      "incomplete_value": true,
      "site": "004b0dd0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b0d90",
      "incomplete_value": true,
      "site": "004b0d90",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0dfc",
      "incomplete_value": true,
      "site": "004b0dfc",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b0dbc",
      "incomplete_value": true,
      "site": "004b0dbc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "004b0dc0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0dec",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b0dc0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b0dec",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0d90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md#insn-004b0d90) · [`004b0dbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md#insn-004b0dbc) · [`004b0d0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md#insn-004b0d0c)
- 新版 `004b0dd0`（命令位置の公開資料なし） · `004b0dfc`（命令位置の公開資料なし） · `004b0d4c`（命令位置の公開資料なし）

~~~diff
- 004b0d90 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0d90 ["INT_ADD", "register:40f0:8", ["const:4b0d90:8", "const:4:8"]]
- 004b0d90 ["CALLIND", null, ["register:0:8"]]
+ 004b0dd0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0dd0 ["INT_ADD", "register:40f0:8", ["const:4b0dd0:8", "const:4:8"]]
+ 004b0dd0 ["CALLIND", null, ["register:0:8"]]
- 004b0d90 bytes 20013fd6
+ 004b0dd0 bytes 20013fd6
- 004b0dbc ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0dbc ["INT_ADD", "register:40f0:8", ["const:4b0dbc:8", "const:4:8"]]
- 004b0dbc ["CALLIND", null, ["register:0:8"]]
+ 004b0dfc ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0dfc ["INT_ADD", "register:40f0:8", ["const:4b0dfc:8", "const:4:8"]]
+ 004b0dfc ["CALLIND", null, ["register:0:8"]]
- 004b0dbc bytes 20013fd6
+ 004b0dfc bytes 20013fd6
- 004b0d0c ["INT_ADD", "register:40f0:8", ["const:4b0d0c:8", "const:4:8"]]
- 004b0d0c ["CALL", null, ["callee:00c58b50:8"]]
+ 004b0d4c ["INT_ADD", "register:40f0:8", ["const:4b0d4c:8", "const:4:8"]]
+ 004b0d4c ["CALL", null, ["callee:00c58b50:8"]]
- 004b0d0c bytes 5d9f1e94
+ 004b0d4c bytes 819f1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80125b62caf8ca7dfd424f2909307ae5"></a>

### [`004b0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) → [`004b0e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0e74.md) _ZN5Botan6BigInt6decodeEPKhmNS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58aa0.md) · 呼出先 20件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md)
- 新版 呼出元 1件 [`00c58b70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b70.md) · 呼出先 20件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b0f6c",
      "incomplete_value": true,
      "site": "004b0f6c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b0f2c",
      "incomplete_value": true,
      "site": "004b0f2c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "definition_site": "004b0fb0",
      "incomplete_value": true,
      "site": "004b0fb0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b0f70",
      "incomplete_value": true,
      "site": "004b0f70",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b10b4",
      "incomplete_value": true,
      "site": "004b10b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b1074",
      "incomplete_value": true,
      "site": "004b1074",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b0f5c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b0fa0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b10a4",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b0f5c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b0fa0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b10a4",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b0eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md#insn-004b0eec) · [`004b0f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md#insn-004b0f2c) · [`004b0f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md#insn-004b0f70)
- 新版 `004b0f2c`（命令位置の公開資料なし） · `004b0f6c`（命令位置の公開資料なし） · `004b0fb0`（命令位置の公開資料なし）

~~~diff
- 004b0eec ["INT_ADD", "register:40f0:8", ["const:4b0eec:8", "const:4:8"]]
- 004b0eec ["CALL", null, ["callee:00c58b80:8"]]
+ 004b0f2c ["INT_ADD", "register:40f0:8", ["const:4b0f2c:8", "const:4:8"]]
+ 004b0f2c ["CALL", null, ["callee:00c58b80:8"]]
- 004b0eec bytes f19e1e94
+ 004b0f2c bytes 159f1e94
- 004b0f2c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0f2c ["INT_ADD", "register:40f0:8", ["const:4b0f2c:8", "const:4:8"]]
- 004b0f2c ["CALLIND", null, ["register:0:8"]]
+ 004b0f6c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0f6c ["INT_ADD", "register:40f0:8", ["const:4b0f6c:8", "const:4:8"]]
+ 004b0f6c ["CALLIND", null, ["register:0:8"]]
- 004b0f2c bytes 20013fd6
+ 004b0f6c bytes 20013fd6
- 004b0f70 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b0f70 ["INT_ADD", "register:40f0:8", ["const:4b0f70:8", "const:4:8"]]
- 004b0f70 ["CALLIND", null, ["register:0:8"]]
+ 004b0fb0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b0fb0 ["INT_ADD", "register:40f0:8", ["const:4b0fb0:8", "const:4:8"]]
+ 004b0fb0 ["CALLIND", null, ["register:0:8"]]
- 004b0f70 bytes 20013fd6
+ 004b0fb0 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03266e0c2eff04a86fd2e4b12e10576c"></a>

### [`004b1518`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md) → [`004b1558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1558.md) _ZN5Botan11BER_Decoder26decode_constrained_integerENS_8ASN1_TagES1_m

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b16b0",
      "incomplete_value": true,
      "site": "004b16b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b1670",
      "incomplete_value": true,
      "site": "004b1670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004b1718",
      "incomplete_value": false,
      "site": "004b1720",
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
            "const:681:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b16d8",
      "incomplete_value": false,
      "site": "004b16e0",
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
            "const:6dd:8"
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
      "definition_site": "004b1750",
      "incomplete_value": true,
      "site": "004b175c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1710",
      "incomplete_value": true,
      "site": "004b171c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
      "004b16a0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b1718",
      "PARAM",
      [
        "storage",
        "002a76dd",
        null,
        "string"
      ]
    ],
    [
      "004b174c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b16a0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b1718",
      "PARAM",
      [
        "storage",
        "002a7681",
        null,
        "string"
      ]
    ],
    [
      "004b174c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1670`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md#insn-004b1670) · [`004b16e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md#insn-004b16e0) · [`004b171c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md#insn-004b171c)
- 新版 `004b16b0`（命令位置の公開資料なし） · `004b1720`（命令位置の公開資料なし） · `004b175c`（命令位置の公開資料なし）

~~~diff
- 004b1670 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1670 ["INT_ADD", "register:40f0:8", ["const:4b1670:8", "const:4:8"]]
- 004b1670 ["CALLIND", null, ["register:0:8"]]
+ 004b16b0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b16b0 ["INT_ADD", "register:40f0:8", ["const:4b16b0:8", "const:4:8"]]
+ 004b16b0 ["CALLIND", null, ["register:0:8"]]
- 004b1670 bytes 20013fd6
+ 004b16b0 bytes 20013fd6
- 004b16e0 ["INT_ADD", "register:40f0:8", ["const:4b16e0:8", "const:4:8"]]
- 004b16e0 ["CALL", null, ["callee:0043de18:8"]]
+ 004b1720 ["INT_ADD", "register:40f0:8", ["const:4b1720:8", "const:4:8"]]
+ 004b1720 ["CALL", null, ["callee:0043de18:8"]]
- 004b16e0 bytes be31fe97
+ 004b1720 bytes be31fe97
- 004b171c ["INT_ADD", "register:40f0:8", ["const:4b171c:8", "const:4:8"]]
- 004b171c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b175c ["INT_ADD", "register:40f0:8", ["const:4b175c:8", "const:4:8"]]
+ 004b175c ["CALL", null, ["callee:00c57fe0:8"]]
- 004b171c bytes fd991e94
+ 004b175c bytes 219a1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81516d3b030227d987472fcff8e8d1c3"></a>

### [`004b186c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md) → [`004b18ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b18ac.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) · 呼出先 14件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00540f2c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540f2c.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md) · 呼出先 14件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00540f6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.97% / 新版 95.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b19b8",
      "incomplete_value": true,
      "site": "004b19b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b1978",
      "incomplete_value": true,
      "site": "004b1978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004b1a00",
      "incomplete_value": false,
      "site": "004b1a08",
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
            "const:362:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b19c0",
      "incomplete_value": false,
      "site": "004b19c8",
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
            "const:3be:8"
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
      "definition_site": "004b1a3c",
      "incomplete_value": true,
      "site": "004b1a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b19fc",
      "incomplete_value": true,
      "site": "004b1a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
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
      "004b19a8",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b1a00",
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      "004b1a38",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b19a8",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b1a00",
      "PARAM",
      [
        "storage",
        "002a5362",
        null,
        "string"
      ]
    ],
    [
      "004b1a38",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1978`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md#insn-004b1978) · [`004b19c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md#insn-004b19c8) · [`004b1a08`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md#insn-004b1a08)
- 新版 `004b19b8`（命令位置の公開資料なし） · `004b1a08`（命令位置の公開資料なし） · `004b1a48`（命令位置の公開資料なし）

~~~diff
- 004b1978 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1978 ["INT_ADD", "register:40f0:8", ["const:4b1978:8", "const:4:8"]]
- 004b1978 ["CALLIND", null, ["register:0:8"]]
+ 004b19b8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b19b8 ["INT_ADD", "register:40f0:8", ["const:4b19b8:8", "const:4:8"]]
+ 004b19b8 ["CALLIND", null, ["register:0:8"]]
- 004b1978 bytes 20013fd6
+ 004b19b8 bytes 20013fd6
- 004b19c8 ["INT_ADD", "register:40f0:8", ["const:4b19c8:8", "const:4:8"]]
- 004b19c8 ["CALL", null, ["callee:0043de18:8"]]
+ 004b1a08 ["INT_ADD", "register:40f0:8", ["const:4b1a08:8", "const:4:8"]]
+ 004b1a08 ["CALL", null, ["callee:0043de18:8"]]
- 004b19c8 bytes 0431fe97
+ 004b1a08 bytes 0431fe97
- 004b1a08 ["INT_ADD", "register:40f0:8", ["const:4b1a08:8", "const:4:8"]]
- 004b1a08 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b1a48 ["INT_ADD", "register:40f0:8", ["const:4b1a48:8", "const:4:8"]]
+ 004b1a48 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b1a08 bytes 42991e94
+ 004b1a48 bytes 66991e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bc8977d61dc6e0ebb894d9bb20a9549"></a>

### [`004b1b54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md) → [`004b1b94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1b94.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS1_9allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588a0.md) · 呼出先 18件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0054108c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/0054108c.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58970.md) · 呼出先 18件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005410cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005410cc.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.89% / 新版 96.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b1d30",
      "incomplete_value": true,
      "site": "004b1d30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b1cf0",
      "incomplete_value": true,
      "site": "004b1cf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004b1d80",
      "incomplete_value": false,
      "site": "004b1d88",
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
            "const:362:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1d40",
      "incomplete_value": false,
      "site": "004b1d48",
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
            "const:3be:8"
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
      "definition_site": "004b1dbc",
      "incomplete_value": true,
      "site": "004b1dc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b1d7c",
      "incomplete_value": true,
      "site": "004b1d88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
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
      "004b1d20",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d80",
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      "004b1db8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b1d20",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b1d80",
      "PARAM",
      [
        "storage",
        "002a5362",
        null,
        "string"
      ]
    ],
    [
      "004b1db8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b1cf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md#insn-004b1cf0) · [`004b1d48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md#insn-004b1d48) · [`004b1d88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md#insn-004b1d88)
- 新版 `004b1d30`（命令位置の公開資料なし） · `004b1d88`（命令位置の公開資料なし） · `004b1dc8`（命令位置の公開資料なし）

~~~diff
- 004b1cf0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b1cf0 ["INT_ADD", "register:40f0:8", ["const:4b1cf0:8", "const:4:8"]]
- 004b1cf0 ["CALLIND", null, ["register:0:8"]]
+ 004b1d30 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b1d30 ["INT_ADD", "register:40f0:8", ["const:4b1d30:8", "const:4:8"]]
+ 004b1d30 ["CALLIND", null, ["register:0:8"]]
- 004b1cf0 bytes 20013fd6
+ 004b1d30 bytes 20013fd6
- 004b1d48 ["INT_ADD", "register:40f0:8", ["const:4b1d48:8", "const:4:8"]]
- 004b1d48 ["CALL", null, ["callee:0043de18:8"]]
+ 004b1d88 ["INT_ADD", "register:40f0:8", ["const:4b1d88:8", "const:4:8"]]
+ 004b1d88 ["CALL", null, ["callee:0043de18:8"]]
- 004b1d48 bytes 2430fe97
+ 004b1d88 bytes 2430fe97
- 004b1d88 ["INT_ADD", "register:40f0:8", ["const:4b1d88:8", "const:4:8"]]
- 004b1d88 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b1dc8 ["INT_ADD", "register:40f0:8", ["const:4b1dc8:8", "const:4:8"]]
+ 004b1dc8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b1d88 bytes 62981e94
+ 004b1dc8 bytes 86981e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0466be6914fa723d416e83347e0d4502"></a>

### [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) → [`004b1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586f0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586f0.md) · 呼出先 8件 [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005412b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c587c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587c0.md) · 呼出先 8件 [`004b2294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) [`004b2600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005412f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005412f0.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.98% / 新版 96.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b208c",
      "incomplete_value": true,
      "site": "004b208c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b204c",
      "incomplete_value": true,
      "site": "004b204c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "definition_site": "004b2124",
      "incomplete_value": true,
      "site": "004b2124",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b20e4",
      "incomplete_value": true,
      "site": "004b20e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b21b0",
      "incomplete_value": true,
      "site": "004b21b0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b2170",
      "incomplete_value": true,
      "site": "004b2170",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
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
      "004b207c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b2114",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b21a0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b207c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b2114",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b21a0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b204c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md#insn-004b204c) · [`004b20e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md#insn-004b20e4) · [`004b2124`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md#insn-004b2124)
- 新版 `004b208c`（命令位置の公開資料なし） · `004b2124`（命令位置の公開資料なし） · `004b2164`（命令位置の公開資料なし）

~~~diff
- 004b204c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b204c ["INT_ADD", "register:40f0:8", ["const:4b204c:8", "const:4:8"]]
- 004b204c ["CALLIND", null, ["register:0:8"]]
+ 004b208c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b208c ["INT_ADD", "register:40f0:8", ["const:4b208c:8", "const:4:8"]]
+ 004b208c ["CALLIND", null, ["register:0:8"]]
- 004b204c bytes 20013fd6
+ 004b208c bytes 20013fd6
- 004b20e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b20e4 ["INT_ADD", "register:40f0:8", ["const:4b20e4:8", "const:4:8"]]
- 004b20e4 ["CALLIND", null, ["register:0:8"]]
+ 004b2124 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2124 ["INT_ADD", "register:40f0:8", ["const:4b2124:8", "const:4:8"]]
+ 004b2124 ["CALLIND", null, ["register:0:8"]]
- 004b20e4 bytes 20013fd6
+ 004b2124 bytes 20013fd6
- 004b2124 ["INT_ADD", "register:40f0:8", ["const:4b2124:8", "const:4:8"]]
- 004b2124 ["CALL", null, ["callee:0054052c:8"]]
+ 004b2164 ["INT_ADD", "register:40f0:8", ["const:4b2164:8", "const:4:8"]]
+ 004b2164 ["CALL", null, ["callee:0054052c:8"]]
- 004b2124 bytes f2380294
+ 004b2164 bytes f2380294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e7a9c9c34fbf65955db649f3f6a482"></a>

### [`004b2254`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) → [`004b2294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) FUN_004b2294

採用 · 移動量 `+0x40` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ad4b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) [`004b1eec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) · 呼出先 9件 [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`004ad4f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) [`004b1f2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) · 呼出先 9件 [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b2320",
      "incomplete_value": false,
      "site": "004b2340",
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
            "const:21a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22e0",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:26e:8"
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
      "definition_site": "004b2328",
      "incomplete_value": false,
      "site": "004b2340",
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
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22e8",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:ed0:8"
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
      "definition_site": "004b2330",
      "incomplete_value": false,
      "site": "004b2340",
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
            "const:cb7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b22f0",
      "incomplete_value": false,
      "site": "004b2300",
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
            "const:d13:8"
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
      "004b2320",
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      "004b2328",
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      "004b2330",
      "PARAM",
      [
        "storage",
        "002a8d13",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b2320",
      "PARAM",
      [
        "storage",
        "002bb21a",
        null,
        "string"
      ]
    ],
    [
      "004b2328",
      "PARAM",
      [
        "storage",
        "002a1e83",
        null,
        "string"
      ]
    ],
    [
      "004b2330",
      "PARAM",
      [
        "storage",
        "002a8cb7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2300`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md#insn-004b2300) · [`004b24d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md#insn-004b24d4) · [`004b2528`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md#insn-004b2528)
- 新版 `004b2340`（命令位置の公開資料なし） · `004b2514`（命令位置の公開資料なし） · `004b2568`（命令位置の公開資料なし）

~~~diff
- 004b2300 ["INT_ADD", "register:40f0:8", ["const:4b2300:8", "const:4:8"]]
- 004b2300 ["CALL", null, ["callee:00c58720:8"]]
+ 004b2340 ["INT_ADD", "register:40f0:8", ["const:4b2340:8", "const:4:8"]]
+ 004b2340 ["CALL", null, ["callee:00c58720:8"]]
- 004b2300 bytes d4981e94
+ 004b2340 bytes f8981e94
- 004b24d4 ["INT_ADD", "register:40f0:8", ["const:4b24d4:8", "const:4:8"]]
- 004b24d4 ["CALL", null, ["callee:00c58030:8"]]
+ 004b2514 ["INT_ADD", "register:40f0:8", ["const:4b2514:8", "const:4:8"]]
+ 004b2514 ["CALL", null, ["callee:00c58030:8"]]
- 004b24d4 bytes a3961e94
+ 004b2514 bytes c7961e94
- 004b2528 ["INT_ADD", "register:40f0:8", ["const:4b2528:8", "const:4:8"]]
- 004b2528 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b2568 ["INT_ADD", "register:40f0:8", ["const:4b2568:8", "const:4:8"]]
+ 004b2568 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b2528 bytes 7a961e94
+ 004b2568 bytes 9e961e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdb90e553bfc7d57b0a1ada51ef7c0c4"></a>

### [`004b28e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md) → [`004b2924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2924.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587a0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587a0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58870.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "004b29a0",
      "incomplete_value": false,
      "site": "004b29a8",
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
            "const:e0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2960",
      "incomplete_value": false,
      "site": "004b2968",
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
            "const:e5e:8"
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
      "definition_site": "004b29dc",
      "incomplete_value": true,
      "site": "004b29e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b299c",
      "incomplete_value": true,
      "site": "004b29a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
      "definition_site": "004b29d8",
      "incomplete_value": false,
      "site": "004b29e8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b2998",
      "incomplete_value": false,
      "site": "004b29a8",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b29a0",
      "PARAM",
      [
        "storage",
        "002b8e5e",
        null,
        "string"
      ]
    ],
    [
      "004b29d8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b29dc",
      "READ",
      [
        "storage",
        "00c9ad48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b29a0",
      "PARAM",
      [
        "storage",
        "002b8e0a",
        null,
        "string"
      ]
    ],
    [
      "004b29d8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b29dc",
      "READ",
      [
        "storage",
        "00c9ae18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2968`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md#insn-004b2968) · [`004b29a8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md#insn-004b29a8) · [`004b2954`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md#insn-004b2954)
- 新版 `004b29a8`（命令位置の公開資料なし） · `004b29e8`（命令位置の公開資料なし） · `004b2994`（命令位置の公開資料なし）

~~~diff
- 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
- 004b2968 ["CALL", null, ["callee:0043de18:8"]]
+ 004b29a8 ["INT_ADD", "register:40f0:8", ["const:4b29a8:8", "const:4:8"]]
+ 004b29a8 ["CALL", null, ["callee:0043de18:8"]]
- 004b2968 bytes 1c2dfe97
+ 004b29a8 bytes 1c2dfe97
- 004b29a8 ["INT_ADD", "register:40f0:8", ["const:4b29a8:8", "const:4:8"]]
- 004b29a8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b29e8 ["INT_ADD", "register:40f0:8", ["const:4b29e8:8", "const:4:8"]]
+ 004b29e8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b29a8 bytes 5a951e94
+ 004b29e8 bytes 7e951e94
- 004b2954 ["INT_ADD", "register:40f0:8", ["const:4b2954:8", "const:4:8"]]
- 004b2954 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b2994 ["INT_ADD", "register:40f0:8", ["const:4b2994:8", "const:4:8"]]
+ 004b2994 ["CALL", null, ["callee:00c57fc0:8"]]
- 004b2954 bytes 67951e94
+ 004b2994 bytes 8b951e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad38a4c988c511280fe71a49b0c67bf"></a>

### [`004b29fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md) → [`004b2a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2a3c.md) FUN_004b2a3c

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2aa4",
      "incomplete_value": true,
      "site": "004b2aa4",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b2a64",
      "incomplete_value": true,
      "site": "004b2a64",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2ae0",
      "incomplete_value": true,
      "site": "004b2ae0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b2aa0",
      "incomplete_value": true,
      "site": "004b2aa0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "004b2a94",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b2ad0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2a94",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b2ad0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2a64`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md#insn-004b2a64) · [`004b2aa0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md#insn-004b2aa0) · [`004b2a54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md#insn-004b2a54)
- 新版 `004b2aa4`（命令位置の公開資料なし） · `004b2ae0`（命令位置の公開資料なし） · `004b2a94`（命令位置の公開資料なし）

~~~diff
- 004b2a64 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2a64 ["INT_ADD", "register:40f0:8", ["const:4b2a64:8", "const:4:8"]]
- 004b2a64 ["CALLIND", null, ["register:0:8"]]
+ 004b2aa4 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2aa4 ["INT_ADD", "register:40f0:8", ["const:4b2aa4:8", "const:4:8"]]
+ 004b2aa4 ["CALLIND", null, ["register:0:8"]]
- 004b2a64 bytes 20013fd6
+ 004b2aa4 bytes 20013fd6
- 004b2aa0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2aa0 ["INT_ADD", "register:40f0:8", ["const:4b2aa0:8", "const:4:8"]]
- 004b2aa0 ["CALLIND", null, ["register:0:8"]]
+ 004b2ae0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2ae0 ["INT_ADD", "register:40f0:8", ["const:4b2ae0:8", "const:4:8"]]
+ 004b2ae0 ["CALLIND", null, ["register:0:8"]]
- 004b2aa0 bytes 20013fd6
+ 004b2ae0 bytes 20013fd6
- 004b2a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
- 004b2a54 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b2a94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
+ 004b2a94 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b2a54 bytes a99e43f9
+ 004b2a94 bytes a90644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b62df3175931d69e5ad75699d4876caf"></a>

### [`004b2ad8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md) → [`004b2b18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2b18.md) _ZN5Botan11DER_Encoder14start_explicitEt

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "004b2b80",
      "incomplete_value": false,
      "site": "004b2b88",
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
            "const:84b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2b40",
      "incomplete_value": false,
      "site": "004b2b48",
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
            "const:8a7:8"
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
      "definition_site": "004b2bbc",
      "incomplete_value": true,
      "site": "004b2bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b2b7c",
      "incomplete_value": true,
      "site": "004b2b88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
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
      "definition_site": "004b2bb8",
      "incomplete_value": false,
      "site": "004b2bc8",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b2b78",
      "incomplete_value": false,
      "site": "004b2b88",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b2b80",
      "PARAM",
      [
        "storage",
        "002af8a7",
        null,
        "string"
      ]
    ],
    [
      "004b2bb8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b2bbc",
      "READ",
      [
        "storage",
        "00c9adf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2b80",
      "PARAM",
      [
        "storage",
        "002af84b",
        null,
        "string"
      ]
    ],
    [
      "004b2bb8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b2bbc",
      "READ",
      [
        "storage",
        "00c9aec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2b48`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md#insn-004b2b48) · [`004b2b88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md#insn-004b2b88) · [`004b2b34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md#insn-004b2b34)
- 新版 `004b2b88`（命令位置の公開資料なし） · `004b2bc8`（命令位置の公開資料なし） · `004b2b74`（命令位置の公開資料なし）

~~~diff
- 004b2b48 ["INT_ADD", "register:40f0:8", ["const:4b2b48:8", "const:4:8"]]
- 004b2b48 ["CALL", null, ["callee:0043de18:8"]]
+ 004b2b88 ["INT_ADD", "register:40f0:8", ["const:4b2b88:8", "const:4:8"]]
+ 004b2b88 ["CALL", null, ["callee:0043de18:8"]]
- 004b2b48 bytes a42cfe97
+ 004b2b88 bytes a42cfe97
- 004b2b88 ["INT_ADD", "register:40f0:8", ["const:4b2b88:8", "const:4:8"]]
- 004b2b88 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b2bc8 ["INT_ADD", "register:40f0:8", ["const:4b2bc8:8", "const:4:8"]]
+ 004b2bc8 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b2b88 bytes e2941e94
+ 004b2bc8 bytes 06951e94
- 004b2b34 ["INT_ADD", "register:40f0:8", ["const:4b2b34:8", "const:4:8"]]
- 004b2b34 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b2b74 ["INT_ADD", "register:40f0:8", ["const:4b2b74:8", "const:4:8"]]
+ 004b2b74 ["CALL", null, ["callee:00c57fc0:8"]]
- 004b2b34 bytes ef941e94
+ 004b2b74 bytes 13951e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5595c40a5afafcc82798cdc24273077"></a>

### [`004b2e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) → [`004b2e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2e44.md) _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b10.md) · 呼出先 8件 [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58820`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) [`00c58920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)
- 新版 呼出元 1件 [`00c58be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58be0.md) · 呼出先 8件 [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c588f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) [`00c589f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.86% / 新版 96.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b2ec0",
      "incomplete_value": true,
      "site": "004b2ec0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "004b2e80",
      "incomplete_value": true,
      "site": "004b2e80",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b3054",
      "incomplete_value": true,
      "site": "004b3054",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "004b3014",
      "incomplete_value": true,
      "site": "004b3014",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004b3100",
      "incomplete_value": true,
      "site": "004b3100",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
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
    "old": {
      "definition_site": "004b30c0",
      "incomplete_value": true,
      "site": "004b30c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:40d0:8"
              ],
              [
                "leaf",
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004b2eb0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b3044",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b30f0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b2eb0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b3044",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b30f0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b2e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md#insn-004b2e80) · [`004b3014`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md#insn-004b3014) · [`004b30c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md#insn-004b30c0)
- 新版 `004b2ec0`（命令位置の公開資料なし） · `004b3054`（命令位置の公開資料なし） · `004b3100`（命令位置の公開資料なし）

~~~diff
- 004b2e80 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b2e80 ["INT_ADD", "register:40f0:8", ["const:4b2e80:8", "const:4:8"]]
- 004b2e80 ["CALLIND", null, ["register:0:8"]]
+ 004b2ec0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b2ec0 ["INT_ADD", "register:40f0:8", ["const:4b2ec0:8", "const:4:8"]]
+ 004b2ec0 ["CALLIND", null, ["register:0:8"]]
- 004b2e80 bytes 20013fd6
+ 004b2ec0 bytes 20013fd6
- 004b3014 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b3014 ["INT_ADD", "register:40f0:8", ["const:4b3014:8", "const:4:8"]]
- 004b3014 ["CALLIND", null, ["register:0:8"]]
+ 004b3054 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3054 ["INT_ADD", "register:40f0:8", ["const:4b3054:8", "const:4:8"]]
+ 004b3054 ["CALLIND", null, ["register:0:8"]]
- 004b3014 bytes 20013fd6
+ 004b3054 bytes 20013fd6
- 004b30c0 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b30c0 ["INT_ADD", "register:40f0:8", ["const:4b30c0:8", "const:4:8"]]
- 004b30c0 ["CALLIND", null, ["register:0:8"]]
+ 004b3100 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3100 ["INT_ADD", "register:40f0:8", ["const:4b3100:8", "const:4:8"]]
+ 004b3100 ["CALLIND", null, ["register:0:8"]]
- 004b30c0 bytes 20013fd6
+ 004b3100 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a9c78ab4cd0c16b48b417ffb4fbd880"></a>

### [`004b314c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md) → [`004b318c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b318c.md) _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b30`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b30.md) · 呼出先 12件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005411a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58c00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c00.md) · 呼出先 12件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005411e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "004b329c",
      "incomplete_value": true,
      "site": "004b329c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b325c",
      "incomplete_value": true,
      "site": "004b325c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
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
      "definition_site": "004b32e8",
      "incomplete_value": false,
      "site": "004b32f0",
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
            "const:f6d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b32a8",
      "incomplete_value": false,
      "site": "004b32b0",
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
            "const:fba:8"
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
      "definition_site": "004b3320",
      "incomplete_value": true,
      "site": "004b332c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b32e0",
      "incomplete_value": true,
      "site": "004b32ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "004b328c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b32e8",
      "PARAM",
      [
        "storage",
        "002a3fba",
        null,
        "string"
      ]
    ],
    [
      "004b331c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b328c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b32e8",
      "PARAM",
      [
        "storage",
        "002a3f6d",
        null,
        "string"
      ]
    ],
    [
      "004b331c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b325c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md#insn-004b325c) · [`004b329c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md#insn-004b329c) · [`004b32b0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md#insn-004b32b0)
- 新版 `004b329c`（命令位置の公開資料なし） · `004b32dc`（命令位置の公開資料なし） · `004b32f0`（命令位置の公開資料なし）

~~~diff
- 004b325c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b325c ["INT_ADD", "register:40f0:8", ["const:4b325c:8", "const:4:8"]]
- 004b325c ["CALLIND", null, ["register:0:8"]]
+ 004b329c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b329c ["INT_ADD", "register:40f0:8", ["const:4b329c:8", "const:4:8"]]
+ 004b329c ["CALLIND", null, ["register:0:8"]]
- 004b325c bytes 20013fd6
+ 004b329c bytes 20013fd6
- 004b329c ["INT_ADD", "register:40f0:8", ["const:4b329c:8", "const:4:8"]]
- 004b329c ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b32dc ["INT_ADD", "register:40f0:8", ["const:4b32dc:8", "const:4:8"]]
+ 004b32dc ["CALL", null, ["callee:00c57fc0:8"]]
- 004b329c bytes 15931e94
+ 004b32dc bytes 39931e94
- 004b32b0 ["INT_ADD", "register:40f0:8", ["const:4b32b0:8", "const:4:8"]]
- 004b32b0 ["CALL", null, ["callee:0043de18:8"]]
+ 004b32f0 ["INT_ADD", "register:40f0:8", ["const:4b32f0:8", "const:4:8"]]
+ 004b32f0 ["CALL", null, ["callee:0043de18:8"]]
- 004b32b0 bytes ca2afe97
+ 004b32f0 bytes ca2afe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1744eb64af1993c39b61289d853a73c5"></a>

### [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) → [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) FUN_004b3548

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 55件 [`004b0e34`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) [`004b2e04`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) [`004b3600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) [`004b4e0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4e0c.md) [`004b56dc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b56dc.md) · 呼出先 7件 [`00536e88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c37ba4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 55件 [`004b0e74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0e74.md) [`004b2e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2e44.md) [`004b3640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3640.md) [`004b4e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e4c.md) [`004b571c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b571c.md) · 呼出先 7件 [`00536ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b360c",
      "incomplete_value": true,
      "site": "004b3614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b35cc",
      "incomplete_value": true,
      "site": "004b35d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:de8:8"
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
      "definition_site": "004b3610",
      "incomplete_value": true,
      "site": "004b3614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b35d0",
      "incomplete_value": true,
      "site": "004b35d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
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
      "004b360c",
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      "004b360c",
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b3610",
      "READ",
      [
        "storage",
        "00c9adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b360c",
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      "004b360c",
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004b3610",
      "READ",
      [
        "storage",
        "00c9aec0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b35d4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md#insn-004b35d4) · [`004b3550`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md#insn-004b3550) · [`004b359c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md#insn-004b359c)
- 新版 `004b3614`（命令位置の公開資料なし） · `004b3590`（命令位置の公開資料なし） · `004b35dc`（命令位置の公開資料なし）

~~~diff
- 004b35d4 ["INT_ADD", "register:40f0:8", ["const:4b35d4:8", "const:4:8"]]
- 004b35d4 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b3614 ["INT_ADD", "register:40f0:8", ["const:4b3614:8", "const:4:8"]]
+ 004b3614 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b35d4 bytes 4f921e94
+ 004b3614 bytes 73921e94
- 004b3550 ["INT_ADD", "register:40f0:8", ["const:4b3550:8", "const:4:8"]]
- 004b3550 ["CALL", null, ["callee:00c58b00:8"]]
+ 004b3590 ["INT_ADD", "register:40f0:8", ["const:4b3590:8", "const:4:8"]]
+ 004b3590 ["CALL", null, ["callee:00c58b00:8"]]
- 004b3550 bytes 38951e94
+ 004b3590 bytes 5c951e94
- 004b359c ["INT_ADD", "register:40f0:8", ["const:4b359c:8", "const:4:8"]]
- 004b359c ["CALL", null, ["callee:00536ec8:8"]]
+ 004b35dc ["INT_ADD", "register:40f0:8", ["const:4b35dc:8", "const:4:8"]]
+ 004b35dc ["CALL", null, ["callee:00536ec8:8"]]
- 004b359c bytes 3b0e0294
+ 004b35dc bytes 3b0e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f53f052d6366e6eacf204df6735c3e30"></a>

### [`004b3600`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) → [`004b3640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3640.md) _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58950`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md) · 呼出先 13件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md) · 呼出先 13件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004b3980",
      "incomplete_value": true,
      "site": "004b3980",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "TRUNC",
            "8",
            [
              "FLOAT_ADD"
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
      "definition_site": "004b3940",
      "incomplete_value": true,
      "site": "004b3940",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "TRUNC",
            "8",
            [
              "FLOAT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b3934",
      "incomplete_value": true,
      "site": "004b3934",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b38f4",
      "incomplete_value": true,
      "site": "004b38f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b39d0",
      "incomplete_value": true,
      "site": "004b39d0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b3990",
      "incomplete_value": true,
      "site": "004b3990",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
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
      "004b38fc",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b3904",
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      "004b3924",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b38fc",
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      "004b3904",
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      "004b3924",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b38f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md#insn-004b38f4) · [`004b3934`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md#insn-004b3934) · [`004b3980`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md#insn-004b3980)
- 新版 `004b3934`（命令位置の公開資料なし） · `004b3974`（命令位置の公開資料なし） · `004b39c0`（命令位置の公開資料なし）

~~~diff
- 004b38f4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b38f4 ["INT_ADD", "register:40f0:8", ["const:4b38f4:8", "const:4:8"]]
- 004b38f4 ["CALLIND", null, ["register:0:8"]]
+ 004b3934 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b3934 ["INT_ADD", "register:40f0:8", ["const:4b3934:8", "const:4:8"]]
+ 004b3934 ["CALLIND", null, ["register:0:8"]]
- 004b38f4 bytes 20013fd6
+ 004b3934 bytes 20013fd6
- 004b3934 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
- 004b3934 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 004b3934 ["COPY", "register:5048:8", ["const:0:8"]]
- 004b3934 ["COPY", "register:5050:8", ["const:0:8"]]
+ 004b3974 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2c8:8"]]
+ 004b3974 ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b3974 ["COPY", "register:5048:8", ["const:0:8"]]
+ 004b3974 ["COPY", "register:5050:8", ["const:0:8"]]
- 004b3934 bytes 024541fd
+ 004b3974 bytes 026541fd
- 004b3980 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:738:8"]]
- 004b3980 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b39c0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:808:8"]]
+ 004b39c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004b3980 bytes 299f43f9
+ 004b39c0 bytes 290744f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d676caca79356332e5ba241f3c8a96f"></a>

### [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) → [`004b3f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58b80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b80.md) [`00c58d40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md) · 呼出先 19件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00481e80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`004b47ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md)
- 新版 呼出元 2件 [`00c58c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c50.md) [`00c58e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e10.md) · 呼出先 19件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00481ec0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`004b47ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b47ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.15% / 新版 98.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b3fb8",
      "incomplete_value": false,
      "site": "004b3fc4",
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
            "const:45b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3f78",
      "incomplete_value": false,
      "site": "004b3f84",
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
            "const:4b7:8"
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
      "definition_site": "004b3fcc",
      "incomplete_value": false,
      "site": "004b3fd4",
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
            "const:845:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b3f8c",
      "incomplete_value": false,
      "site": "004b3f94",
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
            "const:899:8"
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
      "definition_site": "004b453c",
      "incomplete_value": false,
      "site": "004b4548",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b44fc",
      "incomplete_value": false,
      "site": "004b4508",
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
            "const:337:8"
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
      "004b3fb8",
      "PARAM",
      [
        "storage",
        "002a54b7",
        null,
        "string"
      ]
    ],
    [
      "004b3fcc",
      "PARAM",
      [
        "storage",
        "002bd899",
        null,
        null
      ]
    ],
    [
      "004b4050",
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
      "004b3fb8",
      "PARAM",
      [
        "storage",
        "002a545b",
        null,
        "string"
      ]
    ],
    [
      "004b3fcc",
      "PARAM",
      [
        "storage",
        "002bd845",
        null,
        null
      ]
    ],
    [
      "004b4050",
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

- 旧版 [`004b3f84`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md#insn-004b3f84) · [`004b3f94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md#insn-004b3f94) · [`004b4508`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md#insn-004b4508)
- 新版 `004b3fc4`（命令位置の公開資料なし） · `004b3fd4`（命令位置の公開資料なし） · `004b4548`（命令位置の公開資料なし）

~~~diff
- 004b3f84 ["INT_ADD", "register:40f0:8", ["const:4b3f84:8", "const:4:8"]]
- 004b3f84 ["CALL", null, ["callee:00c58180:8"]]
+ 004b3fc4 ["INT_ADD", "register:40f0:8", ["const:4b3fc4:8", "const:4:8"]]
+ 004b3fc4 ["CALL", null, ["callee:00c58180:8"]]
- 004b3f84 bytes 4b901e94
+ 004b3fc4 bytes 6f901e94
- 004b3f94 ["INT_ADD", "register:40f0:8", ["const:4b3f94:8", "const:4:8"]]
- 004b3f94 ["CALL", null, ["callee:00c58040:8"]]
+ 004b3fd4 ["INT_ADD", "register:40f0:8", ["const:4b3fd4:8", "const:4:8"]]
+ 004b3fd4 ["CALL", null, ["callee:00c58040:8"]]
- 004b3f94 bytes f78f1e94
+ 004b3fd4 bytes 1b901e94
- 004b4508 ["INT_ADD", "register:40f0:8", ["const:4b4508:8", "const:4:8"]]
- 004b4508 ["CALL", null, ["callee:00481ec0:8"]]
+ 004b4548 ["INT_ADD", "register:40f0:8", ["const:4b4548:8", "const:4:8"]]
+ 004b4548 ["CALL", null, ["callee:00481ec0:8"]]
- 004b4508 bytes 5e36ff97
+ 004b4548 bytes 5e36ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe4e62e86d045f5b08c244549ab3923f"></a>

### [`004b47ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md) → [`004b47ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b47ec.md) FUN_004b47ec

採用 · 移動量 `+0x40` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b3ee4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) · 呼出先 6件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004b3f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) · 呼出先 6件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b4930",
      "incomplete_value": false,
      "site": "004b4934",
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
            "const:cfb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b48f0",
      "incomplete_value": false,
      "site": "004b48f4",
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
            "const:cca:8"
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
      "definition_site": "004b49a0",
      "incomplete_value": false,
      "site": "004b49a4",
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
    "old": {
      "definition_site": "004b4960",
      "incomplete_value": false,
      "site": "004b4964",
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
            "const:a5c:8"
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
      "004b48e0",
      "PARAM",
      [
        "storage",
        "002afa22",
        null,
        null
      ]
    ],
    [
      "004b4930",
      "PARAM",
      [
        "storage",
        "002b2cca",
        null,
        null
      ]
    ],
    [
      "004b49a0",
      "PARAM",
      [
        "storage",
        "002a9a5c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b48e0",
      "PARAM",
      [
        "storage",
        "002af9c6",
        null,
        null
      ]
    ],
    [
      "004b4930",
      "PARAM",
      [
        "storage",
        "002b2cfb",
        null,
        null
      ]
    ],
    [
      "004b49a0",
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b48f4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md#insn-004b48f4) · [`004b4924`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md#insn-004b4924) · [`004b4964`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md#insn-004b4964)
- 新版 `004b4934`（命令位置の公開資料なし） · `004b4964`（命令位置の公開資料なし） · `004b49a4`（命令位置の公開資料なし）

~~~diff
- 004b48f4 ["INT_ADD", "register:40f0:8", ["const:4b48f4:8", "const:4:8"]]
- 004b48f4 ["CALL", null, ["callee:00c58180:8"]]
+ 004b4934 ["INT_ADD", "register:40f0:8", ["const:4b4934:8", "const:4:8"]]
+ 004b4934 ["CALL", null, ["callee:00c58180:8"]]
- 004b48f4 bytes ef8d1e94
+ 004b4934 bytes 138e1e94
- 004b4924 ["INT_ADD", "register:40f0:8", ["const:4b4924:8", "const:4:8"]]
- 004b4924 ["CALL", null, ["callee:00c57f80:8"]]
+ 004b4964 ["INT_ADD", "register:40f0:8", ["const:4b4964:8", "const:4:8"]]
+ 004b4964 ["CALL", null, ["callee:00c57f80:8"]]
- 004b4924 bytes 638d1e94
+ 004b4964 bytes 878d1e94
- 004b4964 ["INT_ADD", "register:40f0:8", ["const:4b4964:8", "const:4:8"]]
- 004b4964 ["CALL", null, ["callee:00c58040:8"]]
+ 004b49a4 ["INT_ADD", "register:40f0:8", ["const:4b49a4:8", "const:4:8"]]
+ 004b49a4 ["CALL", null, ["callee:00c58040:8"]]
- 004b4964 bytes 838d1e94
+ 004b49a4 bytes a78d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c05854e9dca0fe815848db5841c3cf2"></a>

### [`004b4ab8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md) → [`004b4af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4af8.md) _ZNK5Botan9SCAN_Name3argEm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md) · 呼出先 10件 [`0043bb20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58c60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c60.md) · 呼出先 10件 [`0043bb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.12% / 新版 96.12%

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
      "definition_site": "004b4bcc",
      "incomplete_value": false,
      "site": "004b4bd8",
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
            "const:4b1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4b8c",
      "incomplete_value": false,
      "site": "004b4b98",
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
            "const:505:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b4bf8",
      "incomplete_value": false,
      "site": "004b4c00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:a82:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4bb8",
      "incomplete_value": false,
      "site": "004b4bc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b3000:8"
          ],
          [
            "leaf",
            "const:a51:8"
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
      "definition_site": "004b4c30",
      "incomplete_value": false,
      "site": "004b4c38",
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
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b4bf0",
      "incomplete_value": false,
      "site": "004b4bf8",
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
            "const:48c:8"
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
      "004b4bcc",
      "PARAM",
      [
        "storage",
        "002bc505",
        null,
        "string"
      ]
    ],
    [
      "004b4bf8",
      "PARAM",
      [
        "storage",
        "002b3a51",
        null,
        "string"
      ]
    ],
    [
      "004b4c30",
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b4bcc",
      "PARAM",
      [
        "storage",
        "002bc4b1",
        null,
        "string"
      ]
    ],
    [
      "004b4bf8",
      "PARAM",
      [
        "storage",
        "002b3a82",
        null,
        "string"
      ]
    ],
    [
      "004b4c30",
      "PARAM",
      [
        "storage",
        "002a6430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b4b98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md#insn-004b4b98) · [`004b4bb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md#insn-004b4bb8) · [`004b4bc0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md#insn-004b4bc0)
- 新版 `004b4bd8`（命令位置の公開資料なし） · `004b4bf8`（命令位置の公開資料なし） · `004b4c00`（命令位置の公開資料なし）

~~~diff
- 004b4b98 ["INT_ADD", "register:40f0:8", ["const:4b4b98:8", "const:4:8"]]
- 004b4b98 ["CALL", null, ["callee:00c58030:8"]]
+ 004b4bd8 ["INT_ADD", "register:40f0:8", ["const:4b4bd8:8", "const:4:8"]]
+ 004b4bd8 ["CALL", null, ["callee:00c58030:8"]]
- 004b4b98 bytes f28c1e94
+ 004b4bd8 bytes 168d1e94
- 004b4bb8 ["COPY", "tmp:0:8", ["const:a51:8"]]
- 004b4bb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004b4bb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004b4bb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004b4bf8 ["COPY", "tmp:0:8", ["const:a82:8"]]
+ 004b4bf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4bf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004b4bf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004b4bb8 bytes 21442991
+ 004b4bf8 bytes 21082a91
- 004b4bc0 ["INT_ADD", "register:40f0:8", ["const:4b4bc0:8", "const:4:8"]]
- 004b4bc0 ["CALL", null, ["callee:00c58040:8"]]
+ 004b4c00 ["INT_ADD", "register:40f0:8", ["const:4b4c00:8", "const:4:8"]]
+ 004b4c00 ["CALL", null, ["callee:00c58040:8"]]
- 004b4bc0 bytes ec8c1e94
+ 004b4c00 bytes 108d1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af65d39e7a5126a75efe4774083dbf83"></a>

### [`004b5358`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md) → [`004b5398`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5398.md) _ZN5BotaneqERKNS_11OctetStringES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bb0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bb0.md) · 呼出先 5件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c58c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c80.md) · 呼出先 5件 [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5450",
      "incomplete_value": true,
      "site": "004b5450",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b5410",
      "incomplete_value": true,
      "site": "004b5410",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b547c",
      "incomplete_value": true,
      "site": "004b547c",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b543c",
      "incomplete_value": true,
      "site": "004b543c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004b5440",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b546c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b5440",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b546c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b53d0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md#insn-004b53d0) · [`004b5410`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md#insn-004b5410) · [`004b543c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md#insn-004b543c)
- 新版 `004b5410`（命令位置の公開資料なし） · `004b5450`（命令位置の公開資料なし） · `004b547c`（命令位置の公開資料なし）

~~~diff
- 004b53d0 ["INT_ADD", "register:40f0:8", ["const:4b53d0:8", "const:4:8"]]
- 004b53d0 ["CALL", null, ["callee:00c58120:8"]]
+ 004b5410 ["INT_ADD", "register:40f0:8", ["const:4b5410:8", "const:4:8"]]
+ 004b5410 ["CALL", null, ["callee:00c58120:8"]]
- 004b53d0 bytes 208b1e94
+ 004b5410 bytes 448b1e94
- 004b5410 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5410 ["INT_ADD", "register:40f0:8", ["const:4b5410:8", "const:4:8"]]
- 004b5410 ["CALLIND", null, ["register:0:8"]]
+ 004b5450 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5450 ["INT_ADD", "register:40f0:8", ["const:4b5450:8", "const:4:8"]]
+ 004b5450 ["CALLIND", null, ["register:0:8"]]
- 004b5410 bytes 20013fd6
+ 004b5450 bytes 20013fd6
- 004b543c ["COPY", "register:0:8", ["register:4048:8"]]
- 004b543c ["INT_ADD", "register:40f0:8", ["const:4b543c:8", "const:4:8"]]
- 004b543c ["CALLIND", null, ["register:0:8"]]
+ 004b547c ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b547c ["INT_ADD", "register:40f0:8", ["const:4b547c:8", "const:4:8"]]
+ 004b547c ["CALLIND", null, ["register:0:8"]]
- 004b543c bytes 20013fd6
+ 004b547c bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b230d7937bc595c80ccf5a035570d68b"></a>

### [`004b54c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md) → [`004b5500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5500.md) _ZN5BotanplERKNS_11OctetStringES2_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`005402a4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005402e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b55c0",
      "incomplete_value": true,
      "site": "004b55c0",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b5580",
      "incomplete_value": true,
      "site": "004b5580",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5654",
      "incomplete_value": true,
      "site": "004b5654",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b5614",
      "incomplete_value": true,
      "site": "004b5614",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b5698",
      "incomplete_value": true,
      "site": "004b5698",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b5658",
      "incomplete_value": true,
      "site": "004b5658",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
      "004b55b0",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b5644",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b5688",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b55b0",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b5644",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b5688",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5580`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md#insn-004b5580) · [`004b5614`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md#insn-004b5614) · [`004b5658`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md#insn-004b5658)
- 新版 `004b55c0`（命令位置の公開資料なし） · `004b5654`（命令位置の公開資料なし） · `004b5698`（命令位置の公開資料なし）

~~~diff
- 004b5580 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5580 ["INT_ADD", "register:40f0:8", ["const:4b5580:8", "const:4:8"]]
- 004b5580 ["CALLIND", null, ["register:0:8"]]
+ 004b55c0 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b55c0 ["INT_ADD", "register:40f0:8", ["const:4b55c0:8", "const:4:8"]]
+ 004b55c0 ["CALLIND", null, ["register:0:8"]]
- 004b5580 bytes 20013fd6
+ 004b55c0 bytes 20013fd6
- 004b5614 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5614 ["INT_ADD", "register:40f0:8", ["const:4b5614:8", "const:4:8"]]
- 004b5614 ["CALLIND", null, ["register:0:8"]]
+ 004b5654 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5654 ["INT_ADD", "register:40f0:8", ["const:4b5654:8", "const:4:8"]]
+ 004b5654 ["CALLIND", null, ["register:0:8"]]
- 004b5614 bytes 20013fd6
+ 004b5654 bytes 20013fd6
- 004b5658 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b5658 ["INT_ADD", "register:40f0:8", ["const:4b5658:8", "const:4:8"]]
- 004b5658 ["CALLIND", null, ["register:0:8"]]
+ 004b5698 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b5698 ["INT_ADD", "register:40f0:8", ["const:4b5698:8", "const:4:8"]]
+ 004b5698 ["CALLIND", null, ["register:0:8"]]
- 004b5658 bytes 20013fd6
+ 004b5698 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eab86c351452f4648df25ae2f2d510e5"></a>

### [`004b5a68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md) → [`004b5aa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5aa8.md) _ZN5Botan13base64_encodeEPKhm

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bd0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md) · 呼出先 6件 [`0043b764`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c58ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md) · 呼出先 6件 [`0043b7a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.64% / 新版 94.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5c54",
      "incomplete_value": false,
      "site": "004b5c60",
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
            "const:53d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5c14",
      "incomplete_value": false,
      "site": "004b5c20",
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
            "const:599:8"
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
      "definition_site": "004b5c5c",
      "incomplete_value": false,
      "site": "004b5c60",
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
            "const:973:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5c1c",
      "incomplete_value": false,
      "site": "004b5c20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29e000:8"
          ],
          [
            "leaf",
            "const:dcb:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004b5c18",
      "PARAM",
      [
        "storage",
        "002b8171",
        null,
        "string"
      ]
    ],
    [
      "004b5c24",
      "PARAM",
      [
        "storage",
        "002a9b72",
        null,
        "string"
      ]
    ],
    [
      "004b5c30",
      "PARAM",
      [
        "storage",
        "002bb349",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004b5c18",
      "PARAM",
      [
        "storage",
        "002b81b1",
        null,
        "string"
      ]
    ],
    [
      "004b5c24",
      "PARAM",
      [
        "storage",
        "002a9ba1",
        null,
        "string"
      ]
    ],
    [
      "004b5c30",
      "PARAM",
      [
        "storage",
        "002bb2f5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5c20`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md#insn-004b5c20) · [`004b5b18`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md#insn-004b5b18) · [`004b5b38`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md#insn-004b5b38)
- 新版 `004b5c60`（命令位置の公開資料なし） · `004b5b58`（命令位置の公開資料なし） · `004b5b78`（命令位置の公開資料なし）

~~~diff
- 004b5c20 ["INT_ADD", "register:40f0:8", ["const:4b5c20:8", "const:4:8"]]
- 004b5c20 ["CALL", null, ["callee:00c58720:8"]]
+ 004b5c60 ["INT_ADD", "register:40f0:8", ["const:4b5c60:8", "const:4:8"]]
+ 004b5c60 ["CALL", null, ["callee:00c58720:8"]]
- 004b5c20 bytes 8c8a1e94
+ 004b5c60 bytes b08a1e94
- 004b5b18 ["INT_ADD", "register:40f0:8", ["const:4b5b18:8", "const:4:8"]]
- 004b5b18 ["CALL", null, ["callee:00c57f60:8"]]
+ 004b5b58 ["INT_ADD", "register:40f0:8", ["const:4b5b58:8", "const:4:8"]]
+ 004b5b58 ["CALL", null, ["callee:00c57f60:8"]]
- 004b5b18 bytes de881e94
+ 004b5b58 bytes 02891e94
- 004b5b38 ["INT_ADD", "register:40f0:8", ["const:4b5b38:8", "const:4:8"]]
- 004b5b38 ["CALL", null, ["callee:00c58160:8"]]
+ 004b5b78 ["INT_ADD", "register:40f0:8", ["const:4b5b78:8", "const:4:8"]]
+ 004b5b78 ["CALL", null, ["callee:00c58160:8"]]
- 004b5b38 bytes 56891e94
+ 004b5b78 bytes 7a891e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b333e1e8bc6097d8232bb8e53e7bdb6"></a>

### [`004b5c88`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md) → [`004b5cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5cc8.md) _ZN5Botan13base64_decodeEPhPKcmRmbb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58be0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58be0.md) · 呼出先 11件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`0044fcbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cb0.md) · 呼出先 11件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`0044fcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.02% / 新版 94.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5ea4",
      "incomplete_value": false,
      "site": "004b5eb8",
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
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5e64",
      "incomplete_value": false,
      "site": "004b5e78",
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
            "const:81c:8"
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
      "definition_site": "004b5ed0",
      "incomplete_value": false,
      "site": "004b5ed8",
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
      "definition_site": "004b5e90",
      "incomplete_value": false,
      "site": "004b5e98",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004b5ef0",
      "incomplete_value": false,
      "site": "004b5ef8",
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
            "const:1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b5eb0",
      "incomplete_value": false,
      "site": "004b5eb8",
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
            "const:6c:8"
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
      "004b5dc0",
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      "004b5e40",
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      "004b5ea4",
      "PARAM",
      [
        "storage",
        "002ae81c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b5dc0",
      "DATA",
      [
        "storage",
        "002cad5c",
        null,
        null
      ]
    ],
    [
      "004b5e40",
      "DATA",
      [
        "storage",
        "002cad5c",
        null,
        null
      ]
    ],
    [
      "004b5ea4",
      "PARAM",
      [
        "storage",
        "002ae7c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b5e78`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md#insn-004b5e78) · [`004b5e98`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md#insn-004b5e98) · [`004b5eb8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md#insn-004b5eb8)
- 新版 `004b5eb8`（命令位置の公開資料なし） · `004b5ed8`（命令位置の公開資料なし） · `004b5ef8`（命令位置の公開資料なし）

~~~diff
- 004b5e78 ["INT_ADD", "register:40f0:8", ["const:4b5e78:8", "const:4:8"]]
- 004b5e78 ["CALL", null, ["callee:00441ed4:8"]]
+ 004b5eb8 ["INT_ADD", "register:40f0:8", ["const:4b5eb8:8", "const:4:8"]]
+ 004b5eb8 ["CALL", null, ["callee:00441ed4:8"]]
- 004b5e78 bytes 0730fe97
+ 004b5eb8 bytes 0730fe97
- 004b5e98 ["INT_ADD", "register:40f0:8", ["const:4b5e98:8", "const:4:8"]]
- 004b5e98 ["CALL", null, ["callee:00441ed4:8"]]
+ 004b5ed8 ["INT_ADD", "register:40f0:8", ["const:4b5ed8:8", "const:4:8"]]
+ 004b5ed8 ["CALL", null, ["callee:00441ed4:8"]]
- 004b5e98 bytes ff2ffe97
+ 004b5ed8 bytes ff2ffe97
- 004b5eb8 ["INT_ADD", "register:40f0:8", ["const:4b5eb8:8", "const:4:8"]]
- 004b5eb8 ["CALL", null, ["callee:00441ed4:8"]]
+ 004b5ef8 ["INT_ADD", "register:40f0:8", ["const:4b5ef8:8", "const:4:8"]]
+ 004b5ef8 ["CALL", null, ["callee:00441ed4:8"]]
- 004b5eb8 bytes f72ffe97
+ 004b5ef8 bytes f72ffe97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fcb3e67d511528c91d7bd02455624e0"></a>

### [`004b6028`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md) → [`004b6068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6068.md) _ZN5Botan13base64_decodeEPhPKcmb

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bf0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bf0.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.08% / 新版 96.08%

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
      "definition_site": "004b60e4",
      "incomplete_value": false,
      "site": "004b60ec",
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
            "const:b97:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b60a4",
      "incomplete_value": false,
      "site": "004b60ac",
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
            "const:bf3:8"
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
      "definition_site": "004b6120",
      "incomplete_value": true,
      "site": "004b612c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b60e0",
      "incomplete_value": true,
      "site": "004b60ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004b611c",
      "incomplete_value": false,
      "site": "004b612c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b60dc",
      "incomplete_value": false,
      "site": "004b60ec",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b60e4",
      "PARAM",
      [
        "storage",
        "002a8bf3",
        null,
        "string"
      ]
    ],
    [
      "004b611c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b6120",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b60e4",
      "PARAM",
      [
        "storage",
        "002a8b97",
        null,
        "string"
      ]
    ],
    [
      "004b611c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b6120",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b60ac`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md#insn-004b60ac) · [`004b60ec`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md#insn-004b60ec) · [`004b605c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md#insn-004b605c)
- 新版 `004b60ec`（命令位置の公開資料なし） · `004b612c`（命令位置の公開資料なし） · `004b609c`（命令位置の公開資料なし）

~~~diff
- 004b60ac ["INT_ADD", "register:40f0:8", ["const:4b60ac:8", "const:4:8"]]
- 004b60ac ["CALL", null, ["callee:0043de18:8"]]
+ 004b60ec ["INT_ADD", "register:40f0:8", ["const:4b60ec:8", "const:4:8"]]
+ 004b60ec ["CALL", null, ["callee:0043de18:8"]]
- 004b60ac bytes 4b1ffe97
+ 004b60ec bytes 4b1ffe97
- 004b60ec ["INT_ADD", "register:40f0:8", ["const:4b60ec:8", "const:4:8"]]
- 004b60ec ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b612c ["INT_ADD", "register:40f0:8", ["const:4b612c:8", "const:4:8"]]
+ 004b612c ["CALL", null, ["callee:00c57fe0:8"]]
- 004b60ec bytes 89871e94
+ 004b612c bytes ad871e94
- 004b605c ["INT_ADD", "register:40f0:8", ["const:4b605c:8", "const:4:8"]]
- 004b605c ["CALL", null, ["callee:00c58cb0:8"]]
+ 004b609c ["INT_ADD", "register:40f0:8", ["const:4b609c:8", "const:4:8"]]
+ 004b609c ["CALL", null, ["callee:00c58cb0:8"]]
- 004b605c bytes e18a1e94
+ 004b609c bytes 058b1e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-001a81651f0b2d5c056362eadbfdd454"></a>

### [`004b63cc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md) → [`004b640c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b640c.md) _ZNK5Botan6BigInt12encoded_sizeENS0_4BaseE

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58940`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.84% / 新版 96.84%

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
      "definition_site": "004b6634",
      "incomplete_value": false,
      "site": "004b663c",
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
            "const:fe3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b65f4",
      "incomplete_value": false,
      "site": "004b65fc",
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
            "const:fa3:8"
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
      "definition_site": "004b6670",
      "incomplete_value": true,
      "site": "004b667c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b6630",
      "incomplete_value": true,
      "site": "004b663c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004b666c",
      "incomplete_value": false,
      "site": "004b667c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b662c",
      "incomplete_value": false,
      "site": "004b663c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b65ac",
      "READ",
      [
        "storage",
        "002c4288",
        null,
        "undefined8"
      ]
    ],
    [
      "004b6634",
      "PARAM",
      [
        "storage",
        "002b5fa3",
        null,
        "string"
      ]
    ],
    [
      "004b666c",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b65ac",
      "READ",
      [
        "storage",
        "002c42c8",
        null,
        "undefined8"
      ]
    ],
    [
      "004b6634",
      "PARAM",
      [
        "storage",
        "002b5fe3",
        null,
        "string"
      ]
    ],
    [
      "004b666c",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b65fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md#insn-004b65fc) · [`004b663c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md#insn-004b663c) · [`004b656c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md#insn-004b656c)
- 新版 `004b663c`（命令位置の公開資料なし） · `004b667c`（命令位置の公開資料なし） · `004b65ac`（命令位置の公開資料なし）

~~~diff
- 004b65fc ["INT_ADD", "register:40f0:8", ["const:4b65fc:8", "const:4:8"]]
- 004b65fc ["CALL", null, ["callee:0043de18:8"]]
+ 004b663c ["INT_ADD", "register:40f0:8", ["const:4b663c:8", "const:4:8"]]
+ 004b663c ["CALL", null, ["callee:0043de18:8"]]
- 004b65fc bytes f71dfe97
+ 004b663c bytes f71dfe97
- 004b663c ["INT_ADD", "register:40f0:8", ["const:4b663c:8", "const:4:8"]]
- 004b663c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b667c ["INT_ADD", "register:40f0:8", ["const:4b667c:8", "const:4:8"]]
+ 004b667c ["CALL", null, ["callee:00c57fe0:8"]]
- 004b663c bytes 35861e94
+ 004b667c bytes 59861e94
- 004b656c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
- 004b656c ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
- 004b656c ["COPY", "register:5048:8", ["const:0:8"]]
- 004b656c ["COPY", "register:5050:8", ["const:0:8"]]
+ 004b65ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c8:8"]]
+ 004b65ac ["LOAD", "register:5040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004b65ac ["COPY", "register:5048:8", ["const:0:8"]]
+ 004b65ac ["COPY", "register:5050:8", ["const:0:8"]]
- 004b656c bytes 224541fd
+ 004b65ac bytes 226541fd
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df471692fbd4b2dbb627fb9d7949ed7"></a>

### [`004b6728`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) → [`004b6768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) _ZN5Botan6divideERKNS_6BigIntES2_RS0_S3_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b50`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b50.md) · 呼出先 21件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bb8c4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md) [`004bbb6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c20.md) · 呼出先 21件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004bb904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md) [`004bbbac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件, `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004b6834",
      "incomplete_value": true,
      "site": "004b6838",
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
      "definition_site": "004b67f4",
      "incomplete_value": true,
      "site": "004b67f8",
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
      "definition_site": "004b6858",
      "incomplete_value": true,
      "site": "004b685c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b6818",
      "incomplete_value": true,
      "site": "004b681c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "definition_site": "004b6854",
      "incomplete_value": false,
      "site": "004b685c",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b6814",
      "incomplete_value": false,
      "site": "004b681c",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b6820",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      "004b6838",
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b6854",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004b6820",
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      "004b6838",
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "004b6854",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b681c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md#insn-004b681c) · [`004b68e4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md#insn-004b68e4) · [`004b69b8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md#insn-004b69b8)
- 新版 `004b685c`（命令位置の公開資料なし） · `004b6924`（命令位置の公開資料なし） · `004b69f8`（命令位置の公開資料なし）

~~~diff
- 004b681c ["INT_ADD", "register:40f0:8", ["const:4b681c:8", "const:4:8"]]
- 004b681c ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b685c ["INT_ADD", "register:40f0:8", ["const:4b685c:8", "const:4:8"]]
+ 004b685c ["CALL", null, ["callee:00c57fe0:8"]]
- 004b681c bytes bd851e94
+ 004b685c bytes e1851e94
- 004b68e4 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b68e4 ["INT_ADD", "register:40f0:8", ["const:4b68e4:8", "const:4:8"]]
- 004b68e4 ["CALLIND", null, ["register:0:8"]]
+ 004b6924 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b6924 ["INT_ADD", "register:40f0:8", ["const:4b6924:8", "const:4:8"]]
+ 004b6924 ["CALLIND", null, ["register:0:8"]]
- 004b68e4 bytes 20013fd6
+ 004b6924 bytes 20013fd6
- 004b69b8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b69b8 ["INT_ADD", "register:40f0:8", ["const:4b69b8:8", "const:4:8"]]
- 004b69b8 ["CALLIND", null, ["register:0:8"]]
+ 004b69f8 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b69f8 ["INT_ADD", "register:40f0:8", ["const:4b69f8:8", "const:4:8"]]
+ 004b69f8 ["CALLIND", null, ["register:0:8"]]
- 004b69b8 bytes 20013fd6
+ 004b69f8 bytes 20013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36ef6456874b7f03be6bf7c51f3e1da2"></a>

### [`004b7318`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md) → [`004b7358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7358.md) _ZN5Botan7Charset10digit2charEh

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b60.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58c30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c30.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "004b73c0",
      "incomplete_value": false,
      "site": "004b73c8",
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
            "const:185:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7380",
      "incomplete_value": false,
      "site": "004b7388",
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
            "const:1d2:8"
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
      "definition_site": "004b73fc",
      "incomplete_value": true,
      "site": "004b7408",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b73bc",
      "incomplete_value": true,
      "site": "004b73c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004b73f8",
      "incomplete_value": false,
      "site": "004b7408",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b73b8",
      "incomplete_value": false,
      "site": "004b73c8",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b73c0",
      "PARAM",
      [
        "storage",
        "002a41d2",
        null,
        "string"
      ]
    ],
    [
      "004b73f8",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b73fc",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b73c0",
      "PARAM",
      [
        "storage",
        "002a4185",
        null,
        "string"
      ]
    ],
    [
      "004b73f8",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b73fc",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7388`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md#insn-004b7388) · [`004b73c8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md#insn-004b73c8) · [`004b7374`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md#insn-004b7374)
- 新版 `004b73c8`（命令位置の公開資料なし） · `004b7408`（命令位置の公開資料なし） · `004b73b4`（命令位置の公開資料なし）

~~~diff
- 004b7388 ["INT_ADD", "register:40f0:8", ["const:4b7388:8", "const:4:8"]]
- 004b7388 ["CALL", null, ["callee:0043de18:8"]]
+ 004b73c8 ["INT_ADD", "register:40f0:8", ["const:4b73c8:8", "const:4:8"]]
+ 004b73c8 ["CALL", null, ["callee:0043de18:8"]]
- 004b7388 bytes 941afe97
+ 004b73c8 bytes 941afe97
- 004b73c8 ["INT_ADD", "register:40f0:8", ["const:4b73c8:8", "const:4:8"]]
- 004b73c8 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b7408 ["INT_ADD", "register:40f0:8", ["const:4b7408:8", "const:4:8"]]
+ 004b7408 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b73c8 bytes d2821e94
+ 004b7408 bytes f6821e94
- 004b7374 ["INT_ADD", "register:40f0:8", ["const:4b7374:8", "const:4:8"]]
- 004b7374 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b73b4 ["INT_ADD", "register:40f0:8", ["const:4b73b4:8", "const:4:8"]]
+ 004b73b4 ["CALL", null, ["callee:00c57fc0:8"]]
- 004b7374 bytes df821e94
+ 004b73b4 bytes 03831e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f38c44f8c3622ab9294b3db65cb28d6"></a>

### [`004b750c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md) → [`004b754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b754c.md) _ZN5Botan6BigInt11encode_1363EPhmRKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58c60`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c60.md) · 呼出先 7件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58d30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md) · 呼出先 7件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.59% / 新版 97.59%

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
      "definition_site": "004b7648",
      "incomplete_value": false,
      "site": "004b7650",
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
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7608",
      "incomplete_value": false,
      "site": "004b7610",
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
            "const:f74:8"
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
      "definition_site": "004b7684",
      "incomplete_value": true,
      "site": "004b7690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b7644",
      "incomplete_value": true,
      "site": "004b7650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
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
      "definition_site": "004b7680",
      "incomplete_value": false,
      "site": "004b7690",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b7640",
      "incomplete_value": false,
      "site": "004b7650",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b7648",
      "PARAM",
      [
        "storage",
        "002b5f74",
        null,
        "string"
      ]
    ],
    [
      "004b7680",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b7684",
      "READ",
      [
        "storage",
        "00c9ad98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7648",
      "PARAM",
      [
        "storage",
        "002b5fb4",
        null,
        "string"
      ]
    ],
    [
      "004b7680",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b7684",
      "READ",
      [
        "storage",
        "00c9ae68",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7610`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md#insn-004b7610) · [`004b7650`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md#insn-004b7650) · [`004b75fc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md#insn-004b75fc)
- 新版 `004b7650`（命令位置の公開資料なし） · `004b7690`（命令位置の公開資料なし） · `004b763c`（命令位置の公開資料なし）

~~~diff
- 004b7610 ["INT_ADD", "register:40f0:8", ["const:4b7610:8", "const:4:8"]]
- 004b7610 ["CALL", null, ["callee:0043de18:8"]]
+ 004b7650 ["INT_ADD", "register:40f0:8", ["const:4b7650:8", "const:4:8"]]
+ 004b7650 ["CALL", null, ["callee:0043de18:8"]]
- 004b7610 bytes f219fe97
+ 004b7650 bytes f219fe97
- 004b7650 ["INT_ADD", "register:40f0:8", ["const:4b7650:8", "const:4:8"]]
- 004b7650 ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b7690 ["INT_ADD", "register:40f0:8", ["const:4b7690:8", "const:4:8"]]
+ 004b7690 ["CALL", null, ["callee:00c57fe0:8"]]
- 004b7650 bytes 30821e94
+ 004b7690 bytes 54821e94
- 004b75fc ["INT_ADD", "register:40f0:8", ["const:4b75fc:8", "const:4:8"]]
- 004b75fc ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b763c ["INT_ADD", "register:40f0:8", ["const:4b763c:8", "const:4:8"]]
+ 004b763c ["CALL", null, ["callee:00c57fc0:8"]]
- 004b75fc bytes 3d821e94
+ 004b763c bytes 61821e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4803ef5962d13e167ea8dce3c64c702"></a>

### [`004b7b0c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md) → [`004b7b4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7b4c.md) _ZN5Botan7Charset10char2digitEc

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ab0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ab0.md) · 呼出先 6件 [`0043ddd8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58b80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b80.md) · 呼出先 6件 [`0043de18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.65% / 新版 95.65%

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
      "definition_site": "004b7bb4",
      "incomplete_value": false,
      "site": "004b7bbc",
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
            "const:3b3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004b7b74",
      "incomplete_value": false,
      "site": "004b7b7c",
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
            "const:407:8"
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
      "definition_site": "004b7bf0",
      "incomplete_value": true,
      "site": "004b7bfc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b7bb0",
      "incomplete_value": true,
      "site": "004b7bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d30:8"
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
      "definition_site": "004b7bec",
      "incomplete_value": false,
      "site": "004b7bfc",
      "value": [
        "leaf",
        "const:5358a8:8"
      ]
    },
    "old": {
      "definition_site": "004b7bac",
      "incomplete_value": false,
      "site": "004b7bbc",
      "value": [
        "leaf",
        "const:535868:8"
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
      "004b7bb4",
      "PARAM",
      [
        "storage",
        "002bb407",
        null,
        "string"
      ]
    ],
    [
      "004b7bec",
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      "004b7bf0",
      "READ",
      [
        "storage",
        "00c9ad30",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7bb4",
      "PARAM",
      [
        "storage",
        "002bb3b3",
        null,
        "string"
      ]
    ],
    [
      "004b7bec",
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      "004b7bf0",
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7b7c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md#insn-004b7b7c) · [`004b7bbc`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md#insn-004b7bbc) · [`004b7b68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md#insn-004b7b68)
- 新版 `004b7bbc`（命令位置の公開資料なし） · `004b7bfc`（命令位置の公開資料なし） · `004b7ba8`（命令位置の公開資料なし）

~~~diff
- 004b7b7c ["INT_ADD", "register:40f0:8", ["const:4b7b7c:8", "const:4:8"]]
- 004b7b7c ["CALL", null, ["callee:0043de18:8"]]
+ 004b7bbc ["INT_ADD", "register:40f0:8", ["const:4b7bbc:8", "const:4:8"]]
+ 004b7bbc ["CALL", null, ["callee:0043de18:8"]]
- 004b7b7c bytes 9718fe97
+ 004b7bbc bytes 9718fe97
- 004b7bbc ["INT_ADD", "register:40f0:8", ["const:4b7bbc:8", "const:4:8"]]
- 004b7bbc ["CALL", null, ["callee:00c57fe0:8"]]
+ 004b7bfc ["INT_ADD", "register:40f0:8", ["const:4b7bfc:8", "const:4:8"]]
+ 004b7bfc ["CALL", null, ["callee:00c57fe0:8"]]
- 004b7bbc bytes d5801e94
+ 004b7bfc bytes f9801e94
- 004b7b68 ["INT_ADD", "register:40f0:8", ["const:4b7b68:8", "const:4:8"]]
- 004b7b68 ["CALL", null, ["callee:00c57fc0:8"]]
+ 004b7ba8 ["INT_ADD", "register:40f0:8", ["const:4b7ba8:8", "const:4:8"]]
+ 004b7ba8 ["CALL", null, ["callee:00c57fc0:8"]]
- 004b7b68 bytes e2801e94
+ 004b7ba8 bytes 06811e94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f3ba8569135273233c64db1a875de1c"></a>

### [`004b7c10`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) → [`004b7c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7c50.md) _ZN5Botan6BigIntmLERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ac0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ac0.md) · 呼出先 10件 [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b90e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b90e0.md) [`004b91e0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b91e0.md) [`004d6e68`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`00540920`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58b90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b90.md) · 呼出先 10件 [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`004b9120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9120.md) [`004b9220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9220.md) [`004d6ea8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md) [`00540960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b7f68",
      "incomplete_value": true,
      "site": "004b7f68",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b7f28",
      "incomplete_value": true,
      "site": "004b7f28",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "004b7f94",
      "incomplete_value": true,
      "site": "004b7f94",
      "value": [
        "LOAD",
        "8",
        [
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
    "old": {
      "definition_site": "004b7f54",
      "incomplete_value": true,
      "site": "004b7f54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004b7f58",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f84",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b7f58",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      "004b7f84",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b7f28`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md#insn-004b7f28) · [`004b7f54`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md#insn-004b7f54) · [`004b7d44`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md#insn-004b7d44)
- 新版 `004b7f68`（命令位置の公開資料なし） · `004b7f94`（命令位置の公開資料なし） · `004b7d84`（命令位置の公開資料なし）

~~~diff
- 004b7f28 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7f28 ["INT_ADD", "register:40f0:8", ["const:4b7f28:8", "const:4:8"]]
- 004b7f28 ["CALLIND", null, ["register:0:8"]]
+ 004b7f68 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7f68 ["INT_ADD", "register:40f0:8", ["const:4b7f68:8", "const:4:8"]]
+ 004b7f68 ["CALLIND", null, ["register:0:8"]]
- 004b7f28 bytes 20013fd6
+ 004b7f68 bytes 20013fd6
- 004b7f54 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b7f54 ["INT_ADD", "register:40f0:8", ["const:4b7f54:8", "const:4:8"]]
- 004b7f54 ["CALLIND", null, ["register:0:8"]]
+ 004b7f94 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b7f94 ["INT_ADD", "register:40f0:8", ["const:4b7f94:8", "const:4:8"]]
+ 004b7f94 ["CALLIND", null, ["register:0:8"]]
- 004b7f54 bytes 20013fd6
+ 004b7f94 bytes 20013fd6
- 004b7d44 ["INT_ADD", "register:40f0:8", ["const:4b7d44:8", "const:4:8"]]
- 004b7d44 ["CALL", null, ["callee:00540960:8"]]
+ 004b7d84 ["INT_ADD", "register:40f0:8", ["const:4b7d84:8", "const:4:8"]]
+ 004b7d84 ["CALL", null, ["callee:00540960:8"]]
- 004b7d44 bytes f7220294
+ 004b7d84 bytes f7220294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b74b1fdb4c93a25c82f4fa7602d33d9"></a>

### [`004b7fc8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) → [`004b8008`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) _ZN5Botan6BigIntpLERKS0_

採用 · 移動量 `+0x40` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00c58ad0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md) · 呼出先 10件 [`004b87b4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8850`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b894c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d6bc4`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md)
- 新版 呼出元 1件 [`00c58ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ba0.md) · 呼出先 10件 [`004b87f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`004b898c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004b8bac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004d6c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6c04.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004b8228",
      "incomplete_value": true,
      "site": "004b8228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004b81e8",
      "incomplete_value": true,
      "site": "004b81e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:738:8"
              ]
            ]
          ]
        ]
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
      "004b821c",
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004b821c",
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004b81e8`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md#insn-004b81e8) · [`004b8084`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md#insn-004b8084) · [`004b80c0`](../../../../reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md#insn-004b80c0)
- 新版 `004b8228`（命令位置の公開資料なし） · `004b80c4`（命令位置の公開資料なし） · `004b8100`（命令位置の公開資料なし）

~~~diff
- 004b81e8 ["COPY", "register:0:8", ["register:4048:8"]]
- 004b81e8 ["INT_ADD", "register:40f0:8", ["const:4b81e8:8", "const:4:8"]]
- 004b81e8 ["CALLIND", null, ["register:0:8"]]
+ 004b8228 ["COPY", "register:0:8", ["register:4048:8"]]
+ 004b8228 ["INT_ADD", "register:40f0:8", ["const:4b8228:8", "const:4:8"]]
+ 004b8228 ["CALLIND", null, ["register:0:8"]]
- 004b81e8 bytes 20013fd6
+ 004b8228 bytes 20013fd6
- 004b8084 ["INT_ADD", "register:40f0:8", ["const:4b8084:8", "const:4:8"]]
- 004b8084 ["CALL", null, ["callee:00540960:8"]]
+ 004b80c4 ["INT_ADD", "register:40f0:8", ["const:4b80c4:8", "const:4:8"]]
+ 004b80c4 ["CALL", null, ["callee:00540960:8"]]
- 004b8084 bytes 27220294
+ 004b80c4 bytes 27220294
- 004b80c0 ["INT_ADD", "register:40f0:8", ["const:4b80c0:8", "const:4:8"]]
- 004b80c0 ["CALL", null, ["callee:004d6c04:8"]]
+ 004b8100 ["INT_ADD", "register:40f0:8", ["const:4b8100:8", "const:4:8"]]
+ 004b8100 ["CALL", null, ["callee:004d6c04:8"]]
- 004b80c0 bytes c17a0094
+ 004b8100 bytes c17a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

