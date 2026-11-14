# v16.0.1 → v16.0.2 · 最優先の変更候補 (7)

[一覧の目次](README.md)

### [`0049f8e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f8e0.md) → [`0049f920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f920.md) FUN_0049f920

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0049c378`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049c378.md) [`0049cadc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049c/0049cadc.md) [`0049da20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049d/0049da20.md) [`0049e904`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049e/0049e904.md) · 呼出先 1件 [`00442930`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00442/00442930.md)
- 新版 呼出元 4件 [`0049c3b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049c3b8.md) [`0049cb1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049c/0049cb1c.md) [`0049da60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049d/0049da60.md) [`0049e944`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049e/0049e944.md) · 呼出先 1件 [`00442970`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00442/00442970.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
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
      12,
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


~~~diff
- 0049f8ec ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 0049f92c ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 0049f8f0 ["INT_ADD", "register:40f0:8", ["const:49f8f0:8", "const:4:8"]]
+ 0049f930 ["INT_ADD", "register:40f0:8", ["const:49f930:8", "const:4:8"]]
~~~


### [`0049fa7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fa7c.md) → [`0049fabc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fabc.md) FUN_0049fabc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b68c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049b6cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      100,
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      108,
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
      100,
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      108,
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


~~~diff
- 0049fad0 ["INT_ADD", "register:40f0:8", ["const:49fad0:8", "const:4:8"]]
+ 0049fb10 ["INT_ADD", "register:40f0:8", ["const:49fb10:8", "const:4:8"]]
- 0049fad8 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 0049fb18 ["COPY", "tmp:0:8", ["const:9ae:8"]]
- 0049fae8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d08:8"]]
+ 0049fb28 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:dd8:8"]]
~~~


### [`0049faf0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049faf0.md) → [`0049fb30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fb30.md) FUN_0049fb30

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      132,
      "READ",
      [
        "storage",
        "002c2cd0",
        null,
        null
      ]
    ],
    [
      244,
      "DATA",
      [
        "storage",
        "002b806d",
        null,
        "string"
      ]
    ],
    [
      252,
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
      132,
      "READ",
      [
        "storage",
        "002c2d10",
        null,
        null
      ]
    ],
    [
      244,
      "DATA",
      [
        "storage",
        "002b80ad",
        null,
        "string"
      ]
    ],
    [
      252,
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


~~~diff
- 0049fb30 ["INT_ADD", "register:40f0:8", ["const:49fb30:8", "const:4:8"]]
+ 0049fb70 ["INT_ADD", "register:40f0:8", ["const:49fb70:8", "const:4:8"]]
- 0049fb4c ["INT_ADD", "register:40f0:8", ["const:49fb4c:8", "const:4:8"]]
+ 0049fb8c ["INT_ADD", "register:40f0:8", ["const:49fb8c:8", "const:4:8"]]
- 0049fb74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cd0:8"]]
+ 0049fbb4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d10:8"]]
~~~


### [`0049fc68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fc68.md) → [`0049fca8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fca8.md) FUN_0049fca8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 5件 [`0049b3c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 5件 [`0049b408`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      196,
      "READ",
      [
        "storage",
        "002c24d0",
        null,
        null
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b393d",
        null,
        "string"
      ]
    ],
    [
      300,
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
      196,
      "READ",
      [
        "storage",
        "002c2510",
        null,
        null
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b396e",
        null,
        "string"
      ]
    ],
    [
      300,
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


~~~diff
- 0049fc98 ["INT_ADD", "register:40f0:8", ["const:49fc98:8", "const:4:8"]]
+ 0049fcd8 ["INT_ADD", "register:40f0:8", ["const:49fcd8:8", "const:4:8"]]
- 0049fcf0 ["INT_ADD", "register:40f0:8", ["const:49fcf0:8", "const:4:8"]]
+ 0049fd30 ["INT_ADD", "register:40f0:8", ["const:49fd30:8", "const:4:8"]]
- 0049fd14 ["INT_ADD", "register:40f0:8", ["const:49fd14:8", "const:4:8"]]
+ 0049fd54 ["INT_ADD", "register:40f0:8", ["const:49fd54:8", "const:4:8"]]
~~~


### [`0049fdd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049fdd0.md) → [`0049fe10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049fe10.md) FUN_0049fe10

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049ff50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049ff50.md) · 呼出先 6件 [`0049b3c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b3c8.md) [`0049b4a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b4a0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049ff90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049ff90.md) · 呼出先 6件 [`0049b408`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b408.md) [`0049b4e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b4e0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      108,
      "READ",
      [
        "storage",
        "00ca3790",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "002bc414",
        null,
        "string"
      ]
    ],
    [
      124,
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
      108,
      "READ",
      [
        "storage",
        "00ca3860",
        null,
        "pointer"
      ]
    ],
    [
      108,
      "PARAM",
      [
        "storage",
        "002bc3c0",
        null,
        "string"
      ]
    ],
    [
      124,
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


~~~diff
- 0049fe04 ["INT_ADD", "register:40f0:8", ["const:49fe04:8", "const:4:8"]]
+ 0049fe44 ["INT_ADD", "register:40f0:8", ["const:49fe44:8", "const:4:8"]]
- 0049fe3c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:790:8"]]
+ 0049fe7c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:860:8"]]
- 0049fe44 ["INT_ADD", "register:40f0:8", ["const:49fe44:8", "const:4:8"]]
+ 0049fe84 ["INT_ADD", "register:40f0:8", ["const:49fe84:8", "const:4:8"]]
~~~


### [`004a0278`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0278.md) → [`004a02b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a02b8.md) FUN_004a02b8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049b68c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049b/0049b68c.md) · 呼出先 2件 [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`0049b6cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049b/0049b6cc.md) · 呼出先 2件 [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      196,
      "DATA",
      [
        "storage",
        "002b297d",
        null,
        "string"
      ]
    ],
    [
      204,
      "READ",
      [
        "storage",
        "00c9ad08",
        null,
        "pointer"
      ]
    ],
    [
      204,
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
      196,
      "DATA",
      [
        "storage",
        "002b29ae",
        null,
        "string"
      ]
    ],
    [
      204,
      "READ",
      [
        "storage",
        "00c9add8",
        null,
        "pointer"
      ]
    ],
    [
      204,
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


~~~diff
- 004a032c ["INT_ADD", "register:40f0:8", ["const:4a032c:8", "const:4:8"]]
+ 004a036c ["INT_ADD", "register:40f0:8", ["const:4a036c:8", "const:4:8"]]
- 004a0334 ["COPY", "tmp:0:8", ["const:97d:8"]]
+ 004a0374 ["COPY", "tmp:0:8", ["const:9ae:8"]]
- 004a0344 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d08:8"]]
+ 004a0384 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:dd8:8"]]
~~~


### [`004a04e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a04e8.md) → [`004a0528`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0528.md) FUN_004a0528

根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004a0368`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0368.md) · 呼出先 1件 [`0043b778`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b778.md)
- 新版 呼出元 1件 [`004a03a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a03a8.md) · 呼出先 1件 [`0043b7b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7b8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      12,
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
      12,
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


~~~diff
- 004a04f4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 004a0534 ["COPY", "tmp:0:8", ["const:f8c:8"]]
- 004a04f8 ["INT_ADD", "register:40f0:8", ["const:4a04f8:8", "const:4:8"]]
+ 004a0538 ["INT_ADD", "register:40f0:8", ["const:4a0538:8", "const:4:8"]]
~~~


### [`004a0568`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) → [`004a05a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a05a8.md) _ZNK5Botan7AES_1289encrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a05dc ["INT_ADD", "register:40f0:8", ["const:4a05dc:8", "const:4:8"]]
+ 004a061c ["INT_ADD", "register:40f0:8", ["const:4a061c:8", "const:4:8"]]
- 004a05f4 ["INT_ADD", "register:40f0:8", ["const:4a05f4:8", "const:4:8"]]
+ 004a0634 ["INT_ADD", "register:40f0:8", ["const:4a0634:8", "const:4:8"]]
- 004a0604 ["INT_ADD", "register:40f0:8", ["const:4a0604:8", "const:4:8"]]
+ 004a0644 ["INT_ADD", "register:40f0:8", ["const:4a0644:8", "const:4:8"]]
~~~


### [`004a0688`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) → [`004a06c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) FUN_004a06c8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a0568`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0568.md) [`004a1b70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) [`004a1e8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) · 呼出先 4件 [`0053593c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/0053593c.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 3件 [`004a05a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a05a8.md) [`004a1bb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1bb0.md) [`004a1ecc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1ecc.md) · 呼出先 4件 [`0053597c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/0053597c.md) [`00c57f20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      72,
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
      56,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      72,
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


~~~diff
- 004a06c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d18:8"]]
+ 004a0700 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de8:8"]]
- 004a06d8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 004a0718 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df0:8"]]
- 004a06e4 ["COPY", "tmp:0:8", ["const:7c0:8"]]
+ 004a0724 ["COPY", "tmp:0:8", ["const:8c0:8"]]
~~~


### [`004a0c48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) → [`004a0c88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0c88.md) _ZNK5Botan7AES_1289decrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a0cbc ["INT_ADD", "register:40f0:8", ["const:4a0cbc:8", "const:4:8"]]
+ 004a0cfc ["INT_ADD", "register:40f0:8", ["const:4a0cfc:8", "const:4:8"]]
- 004a0cd4 ["INT_ADD", "register:40f0:8", ["const:4a0cd4:8", "const:4:8"]]
+ 004a0d14 ["INT_ADD", "register:40f0:8", ["const:4a0d14:8", "const:4:8"]]
- 004a0ce4 ["INT_ADD", "register:40f0:8", ["const:4a0ce4:8", "const:4:8"]]
+ 004a0d24 ["INT_ADD", "register:40f0:8", ["const:4a0d24:8", "const:4:8"]]
~~~


### [`004a0d68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) → [`004a0da8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) FUN_004a0da8

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a0c48`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0c48.md) [`004a1c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) [`004a1fac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) · 呼出先 4件 [`00535a34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`00c57e50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e50.md) [`00c57e70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e70.md) [`00c58650`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 3件 [`004a0c88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0c88.md) [`004a1cd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1cd0.md) [`004a1fec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1fec.md) · 呼出先 4件 [`00535a74`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535a74.md) [`00c57f20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f20.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f40.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 branch_value, call, call_argument_candidate, call_target, constant, operands_and_dependencies, store_condition

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "00c9ad18",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca5238",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      72,
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
      56,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      60,
      "READ",
      [
        "storage",
        "00ca5338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      72,
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


~~~diff
- 004a0da0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d18:8"]]
+ 004a0de0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de8:8"]]
- 004a0db8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 004a0df8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:df0:8"]]
- 004a0dc4 ["COPY", "tmp:0:8", ["const:c00:8"]]
+ 004a0e04 ["COPY", "tmp:0:8", ["const:d00:8"]]
~~~


### [`004a1354`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1354.md) → [`004a1394`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1394.md) FUN_004a1394

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004a1334`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1334.md) [`004a1db0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1db0.md) [`004a20cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a20cc.md) · 呼出先 15件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b8850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535a34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535a34.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 3件 [`004a1374`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1374.md) [`004a1df0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1df0.md) [`004a210c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a210c.md) · 呼出先 15件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b8890`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535a74`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535a74.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      372,
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "002cf340",
        null,
        null
      ]
    ],
    [
      380,
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
      372,
      "DATA",
      [
        "storage",
        "002cf380",
        null,
        null
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "002cf380",
        null,
        null
      ]
    ],
    [
      380,
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


~~~diff
- 004a13a4 ["INT_ADD", "register:40f0:8", ["const:4a13a4:8", "const:4:8"]]
+ 004a13e4 ["INT_ADD", "register:40f0:8", ["const:4a13e4:8", "const:4:8"]]
- 004a13b0 ["INT_ADD", "register:40f0:8", ["const:4a13b0:8", "const:4:8"]]
+ 004a13f0 ["INT_ADD", "register:40f0:8", ["const:4a13f0:8", "const:4:8"]]
- 004a1458 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 004a1498 ["COPY", "tmp:0:8", ["const:380:8"]]
~~~


### [`004a1b70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1b70.md) → [`004a1bb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1bb0.md) _ZNK5Botan7AES_1929encrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a1be4 ["INT_ADD", "register:40f0:8", ["const:4a1be4:8", "const:4:8"]]
+ 004a1c24 ["INT_ADD", "register:40f0:8", ["const:4a1c24:8", "const:4:8"]]
- 004a1bfc ["INT_ADD", "register:40f0:8", ["const:4a1bfc:8", "const:4:8"]]
+ 004a1c3c ["INT_ADD", "register:40f0:8", ["const:4a1c3c:8", "const:4:8"]]
- 004a1c0c ["INT_ADD", "register:40f0:8", ["const:4a1c0c:8", "const:4:8"]]
+ 004a1c4c ["INT_ADD", "register:40f0:8", ["const:4a1c4c:8", "const:4:8"]]
~~~


### [`004a1c90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1c90.md) → [`004a1cd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1cd0.md) _ZNK5Botan7AES_1929decrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a1d04 ["INT_ADD", "register:40f0:8", ["const:4a1d04:8", "const:4:8"]]
+ 004a1d44 ["INT_ADD", "register:40f0:8", ["const:4a1d44:8", "const:4:8"]]
- 004a1d1c ["INT_ADD", "register:40f0:8", ["const:4a1d1c:8", "const:4:8"]]
+ 004a1d5c ["INT_ADD", "register:40f0:8", ["const:4a1d5c:8", "const:4:8"]]
- 004a1d2c ["INT_ADD", "register:40f0:8", ["const:4a1d2c:8", "const:4:8"]]
+ 004a1d6c ["INT_ADD", "register:40f0:8", ["const:4a1d6c:8", "const:4:8"]]
~~~


### [`004a1e8c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1e8c.md) → [`004a1ecc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1ecc.md) _ZNK5Botan7AES_2569encrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0688`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0688.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a06c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a06c8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a1f00 ["INT_ADD", "register:40f0:8", ["const:4a1f00:8", "const:4:8"]]
+ 004a1f40 ["INT_ADD", "register:40f0:8", ["const:4a1f40:8", "const:4:8"]]
- 004a1f18 ["INT_ADD", "register:40f0:8", ["const:4a1f18:8", "const:4:8"]]
+ 004a1f58 ["INT_ADD", "register:40f0:8", ["const:4a1f58:8", "const:4:8"]]
- 004a1f28 ["INT_ADD", "register:40f0:8", ["const:4a1f28:8", "const:4:8"]]
+ 004a1f68 ["INT_ADD", "register:40f0:8", ["const:4a1f68:8", "const:4:8"]]
~~~


### [`004a1fac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a1/004a1fac.md) → [`004a1fec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a1/004a1fec.md) _ZNK5Botan7AES_2569decrypt_nEPKhPhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`004a0d68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a0/004a0d68.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`004a0da8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a0/004a0da8.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ad10",
        null,
        "pointer"
      ]
    ],
    [
      192,
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
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      192,
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


~~~diff
- 004a2020 ["INT_ADD", "register:40f0:8", ["const:4a2020:8", "const:4:8"]]
+ 004a2060 ["INT_ADD", "register:40f0:8", ["const:4a2060:8", "const:4:8"]]
- 004a2038 ["INT_ADD", "register:40f0:8", ["const:4a2038:8", "const:4:8"]]
+ 004a2078 ["INT_ADD", "register:40f0:8", ["const:4a2078:8", "const:4:8"]]
- 004a2048 ["INT_ADD", "register:40f0:8", ["const:4a2048:8", "const:4:8"]]
+ 004a2088 ["INT_ADD", "register:40f0:8", ["const:4a2088:8", "const:4:8"]]
~~~


### [`004a21a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a21a8.md) → [`004a21e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a21e8.md) _ZN5Botan19AlgorithmIdentifierC1ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59440`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59440.md) · 呼出先 4件 [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c59510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59510.md) · 呼出先 4件 [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      40,
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004a21d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a2210 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 004a21dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a221c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 004a2204 ["INT_ADD", "register:40f0:8", ["const:4a2204:8", "const:4:8"]]
+ 004a2244 ["INT_ADD", "register:40f0:8", ["const:4a2244:8", "const:4:8"]]
~~~


### [`004a22e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a22e4.md) → [`004a2324`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a2324.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e20.md) · 呼出先 4件 [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c58ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ef0.md) · 呼出先 4件 [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      44,
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
      28,
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      44,
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


~~~diff
- 004a2300 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a2340 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 004a2314 ["INT_ADD", "register:40f0:8", ["const:4a2314:8", "const:4:8"]]
+ 004a2354 ["INT_ADD", "register:40f0:8", ["const:4a2354:8", "const:4:8"]]
- 004a2338 ["INT_ADD", "register:40f0:8", ["const:4a2338:8", "const:4:8"]]
+ 004a2378 ["INT_ADD", "register:40f0:8", ["const:4a2378:8", "const:4:8"]]
~~~


### [`004a23b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a2/004a23b0.md) → [`004a23f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a2/004a23f0.md) _ZN5Botan4OIDS6lookupERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58680`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 380件, `store_value` 12件

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      332,
      "PARAM",
      [
        "storage",
        "002a8b70",
        null,
        "string"
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "002bb2d1",
        null,
        "string"
      ]
    ],
    [
      384,
      "PARAM",
      [
        "storage",
        "0029ef33",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      332,
      "PARAM",
      [
        "storage",
        "002a8b14",
        null,
        "string"
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "002bb27d",
        null,
        "string"
      ]
    ],
    [
      384,
      "PARAM",
      [
        "storage",
        "0029eee6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004a24fc ["COPY", "tmp:0:8", ["const:b70:8"]]
- 004a24fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004a24fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004a24fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["COPY", "tmp:0:8", ["const:b14:8"]]
+ 004a253c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004a253c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
~~~


### [`004a502c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a502c.md) → [`004a506c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a506c.md) _ZN5Botan19AlgorithmIdentifierC2ERKNS_3OIDENS0_15Encoding_OptionE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59720.md) · 呼出先 5件 [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c597f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c597f0.md) · 呼出先 5件 [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      40,
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004a5054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a5094 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 004a5060 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a50a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 004a5088 ["INT_ADD", "register:40f0:8", ["const:4a5088:8", "const:4:8"]]
+ 004a50c8 ["INT_ADD", "register:40f0:8", ["const:4a50c8:8", "const:4:8"]]
~~~


### [`004a5118`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5118.md) → [`004a5158`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5158.md) _ZN5Botan19AlgorithmIdentifierC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58e10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58e10.md) · 呼出先 2件 [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58680`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c58ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ee0.md) · 呼出先 2件 [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c58750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "READ",
      [
        "storage",
        "00c9ad38",
        null,
        "pointer"
      ]
    ],
    [
      32,
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
      24,
      "READ",
      [
        "storage",
        "00c9ae08",
        null,
        "pointer"
      ]
    ],
    [
      32,
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


~~~diff
- 004a5130 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d38:8"]]
+ 004a5170 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e08:8"]]
- 004a5144 ["INT_ADD", "register:40f0:8", ["const:4a5144:8", "const:4:8"]]
+ 004a5184 ["INT_ADD", "register:40f0:8", ["const:4a5184:8", "const:4:8"]]
- 004a5158 ["INT_ADD", "register:40f0:8", ["const:4a5158:8", "const:4:8"]]
+ 004a5198 ["INT_ADD", "register:40f0:8", ["const:4a5198:8", "const:4:8"]]
~~~


### [`004a53d8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a53d8.md) → [`004a5418`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5418.md) _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586b0.md) · 呼出先 6件 [`00542f88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00542/00542f88.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c586e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586e0.md)
- 新版 呼出元 1件 [`00c58780`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58780.md) · 呼出先 6件 [`00542fc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00542/00542fc8.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587b0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      216,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      280,
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
      216,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      280,
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


~~~diff
- 004a5404 ["INT_ADD", "register:40f0:8", ["const:4a5404:8", "const:4:8"]]
+ 004a5444 ["INT_ADD", "register:40f0:8", ["const:4a5444:8", "const:4:8"]]
- 004a5468 ["INT_ADD", "register:40f0:8", ["const:4a5468:8", "const:4:8"]]
+ 004a54a8 ["INT_ADD", "register:40f0:8", ["const:4a54a8:8", "const:4:8"]]
- 004a54b0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:738:8"]]
+ 004a54f0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:808:8"]]
~~~


### [`004a559c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) → [`004a55dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) _ZN5Botan11DER_Encoder8end_consEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586d0.md) · 呼出先 13件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 1件 [`00c587a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587a0.md) · 呼出先 13件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      224,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      312,
      "PARAM",
      [
        "storage",
        "002b5ed8",
        null,
        "string"
      ]
    ],
    [
      364,
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
      224,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      312,
      "PARAM",
      [
        "storage",
        "002b5f18",
        null,
        "string"
      ]
    ],
    [
      364,
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


~~~diff
- 004a55d8 ["INT_ADD", "register:40f0:8", ["const:4a55d8:8", "const:4:8"]]
+ 004a5618 ["INT_ADD", "register:40f0:8", ["const:4a5618:8", "const:4:8"]]
- 004a55ec ["INT_ADD", "register:40f0:8", ["const:4a55ec:8", "const:4:8"]]
+ 004a562c ["INT_ADD", "register:40f0:8", ["const:4a562c:8", "const:4:8"]]
- 004a5610 ["INT_ADD", "register:40f0:8", ["const:4a5610:8", "const:4:8"]]
+ 004a5650 ["INT_ADD", "register:40f0:8", ["const:4a5650:8", "const:4:8"]]
~~~


### [`004a5ae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) → [`004a5b20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5b20.md) _ZN5Botan11BER_Decoder8end_consEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58710`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c587e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "PARAM",
      [
        "storage",
        "002beb72",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      184,
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
      124,
      "PARAM",
      [
        "storage",
        "002beb1e",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      184,
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


~~~diff
- 004a5b18 ["INT_ADD", "register:40f0:8", ["const:4a5b18:8", "const:4:8"]]
+ 004a5b58 ["INT_ADD", "register:40f0:8", ["const:4a5b58:8", "const:4:8"]]
- 004a5b50 ["INT_ADD", "register:40f0:8", ["const:4a5b50:8", "const:4:8"]]
+ 004a5b90 ["INT_ADD", "register:40f0:8", ["const:4a5b90:8", "const:4:8"]]
- 004a5b5c ["COPY", "tmp:0:8", ["const:b72:8"]]
+ 004a5b9c ["COPY", "tmp:0:8", ["const:b1e:8"]]
~~~


### [`004a5ccc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ccc.md) → [`004a5d0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5d0c.md) _ZN5Botan9AttributeC2ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      40,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      72,
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
      40,
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      72,
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


~~~diff
- 004a5cf4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 004a5d34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
- 004a5d00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 004a5d40 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e10:8"]]
- 004a5d28 ["INT_ADD", "register:40f0:8", ["const:4a5d28:8", "const:4:8"]]
+ 004a5d68 ["INT_ADD", "register:40f0:8", ["const:4a5d68:8", "const:4:8"]]
~~~


### [`004a5df0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5df0.md) → [`004a5e30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5e30.md) _ZN5Botan9AttributeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59f60.md) · 呼出先 4件 [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58680`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58680.md)
- 新版 呼出元 1件 [`00c5a030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a030.md) · 呼出先 4件 [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c58750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58750.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      44,
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
      28,
      "READ",
      [
        "storage",
        "00c9ae28",
        null,
        "pointer"
      ]
    ],
    [
      44,
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


~~~diff
- 004a5e0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d58:8"]]
+ 004a5e4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
- 004a5e20 ["INT_ADD", "register:40f0:8", ["const:4a5e20:8", "const:4:8"]]
+ 004a5e60 ["INT_ADD", "register:40f0:8", ["const:4a5e60:8", "const:4:8"]]
- 004a5e44 ["INT_ADD", "register:40f0:8", ["const:4a5e44:8", "const:4:8"]]
+ 004a5e84 ["INT_ADD", "register:40f0:8", ["const:4a5e84:8", "const:4:8"]]
~~~


### [`004a5fa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5fa0.md) → [`004a5fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5fe0.md) _ZN5Botan9Attribute11decode_fromERNS_11BER_DecoderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0050e044`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050e/0050e044.md) · 呼出先 6件 [`004a5980`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5980.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58700`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58700.md) [`00c58710`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58710.md)
- 新版 呼出元 1件 [`0050e084`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050e/0050e084.md) · 呼出先 6件 [`004a59c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a59c0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587d0.md) [`00c587e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587e0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      160,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      228,
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
      160,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      228,
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


~~~diff
- 004a5fd4 ["INT_ADD", "register:40f0:8", ["const:4a5fd4:8", "const:4:8"]]
+ 004a6014 ["INT_ADD", "register:40f0:8", ["const:4a6014:8", "const:4:8"]]
- 004a5fe8 ["INT_ADD", "register:40f0:8", ["const:4a5fe8:8", "const:4:8"]]
+ 004a6028 ["INT_ADD", "register:40f0:8", ["const:4a6028:8", "const:4:8"]]
- 004a5ffc ["INT_ADD", "register:40f0:8", ["const:4a5ffc:8", "const:4:8"]]
+ 004a603c ["INT_ADD", "register:40f0:8", ["const:4a603c:8", "const:4:8"]]
~~~


### [`004a6104`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6104.md) → [`004a6144`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6144.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58760`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58760.md) · 呼出先 5件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md) [`00c57f70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c58160`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58160.md)
- 新版 呼出元 1件 [`00c58830`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58830.md) · 呼出先 5件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md) [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58230`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "DATA",
      [
        "storage",
        "002ca758",
        "switchD_004a6140::switchdataD_002ca758",
        "byte"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "002a645f",
        null,
        "string"
      ]
    ],
    [
      316,
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
      52,
      "DATA",
      [
        "storage",
        "002ca798",
        "switchD_004a6180::switchdataD_002ca798",
        "byte"
      ]
    ],
    [
      264,
      "READ",
      [
        "storage",
        "002a6403",
        null,
        "string"
      ]
    ],
    [
      316,
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


~~~diff
- 004a6130 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 004a6170 ["COPY", "tmp:0:8", ["const:798:8"]]
- 004a6134 ["COPY", "register:4058:8", ["const:4a6144:8"]]
+ 004a6174 ["COPY", "register:4058:8", ["const:4a6184:8"]]
- 004a6168 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 004a61a8 ["COPY", "tmp:0:8", ["const:34:8"]]
~~~


### [`004a642c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a642c.md) → [`004a646c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a646c.md) _ZN5Botan18BER_Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58770`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58770.md) [`00c58850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58850.md) · 呼出先 4件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)
- 新版 呼出元 2件 [`00c58840`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58840.md) [`00c58920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58920.md) · 呼出先 4件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002a3028",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      72,
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
      28,
      "PARAM",
      [
        "storage",
        "002a2fdb",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      72,
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


~~~diff
- 004a6444 ["COPY", "register:4000:8", ["const:2a3000:8"]]
- 004a6448 ["COPY", "tmp:0:8", ["const:28:8"]]
+ 004a6484 ["COPY", "register:4000:8", ["const:2a2000:8"]]
+ 004a6488 ["COPY", "tmp:0:8", ["const:fdb:8"]]
- 004a6458 ["INT_ADD", "register:40f0:8", ["const:4a6458:8", "const:4:8"]]
+ 004a6498 ["INT_ADD", "register:40f0:8", ["const:4a6498:8", "const:4:8"]]
- 004a6460 ["COPY", "tmp:0:8", ["const:e24:8"]]
+ 004a64a0 ["COPY", "tmp:0:8", ["const:dd0:8"]]
~~~


### [`004a653c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a653c.md) → [`004a657c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a657c.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58750`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58750.md) · 呼出先 4件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c580b0.md) [`00c58780`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58780.md)
- 新版 呼出元 1件 [`00c58820`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58820.md) · 呼出先 4件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58180`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58180.md) [`00c58850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58850.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "PARAM",
      [
        "storage",
        "002bfe24",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002a644e",
        null,
        "string"
      ]
    ],
    [
      72,
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
      28,
      "PARAM",
      [
        "storage",
        "002bfdd0",
        null,
        "string"
      ]
    ],
    [
      52,
      "PARAM",
      [
        "storage",
        "002a63f2",
        null,
        "string"
      ]
    ],
    [
      72,
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


~~~diff
- 004a6558 ["COPY", "tmp:0:8", ["const:e24:8"]]
+ 004a6598 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 004a6568 ["INT_ADD", "register:40f0:8", ["const:4a6568:8", "const:4:8"]]
+ 004a65a8 ["INT_ADD", "register:40f0:8", ["const:4a65a8:8", "const:4:8"]]
- 004a6570 ["COPY", "tmp:0:8", ["const:44e:8"]]
+ 004a65b0 ["COPY", "tmp:0:8", ["const:3f2:8"]]
~~~


### [`004a689c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a689c.md) → [`004a68dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a68dc.md) _ZN5Botan11BER_Bad_TagC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagESA_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58840`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58840.md) · 呼出先 9件 [`0043b764`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c58910`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58910.md) · 呼出先 9件 [`0043b7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      296,
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      476,
      "READ",
      [
        "storage",
        "00c9ad78",
        null,
        "pointer"
      ]
    ],
    [
      484,
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
      296,
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ],
    [
      476,
      "READ",
      [
        "storage",
        "00c9ae48",
        null,
        "pointer"
      ]
    ],
    [
      484,
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


~~~diff
- 004a693c ["INT_ADD", "register:40f0:8", ["const:4a693c:8", "const:4:8"]]
+ 004a697c ["INT_ADD", "register:40f0:8", ["const:4a697c:8", "const:4:8"]]
- 004a6964 ["INT_ADD", "register:40f0:8", ["const:4a6964:8", "const:4:8"]]
+ 004a69a4 ["INT_ADD", "register:40f0:8", ["const:4a69a4:8", "const:4:8"]]
- 004a6984 ["INT_ADD", "register:40f0:8", ["const:4a6984:8", "const:4:8"]]
+ 004a69c4 ["INT_ADD", "register:40f0:8", ["const:4a69c4:8", "const:4:8"]]
~~~


### [`004a6f9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6f9c.md) → [`004a6fdc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6fdc.md) FUN_004a6fdc

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004ecd10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ec/004ecd10.md) [`004f0edc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f0/004f0edc.md) [`0050d538`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0050d/0050d538.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 3件 [`004ecd50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ec/004ecd50.md) [`004f0f1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f0/004f0f1c.md) [`0050d578`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0050d/0050d578.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      160,
      "PARAM",
      [
        "storage",
        "002b4bbe",
        null,
        "string"
      ]
    ],
    [
      216,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      220,
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
      160,
      "PARAM",
      [
        "storage",
        "002b4bef",
        null,
        "string"
      ]
    ],
    [
      216,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      220,
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


~~~diff
- 004a6fd4 ["INT_ADD", "register:40f0:8", ["const:4a6fd4:8", "const:4:8"]]
+ 004a7014 ["INT_ADD", "register:40f0:8", ["const:4a7014:8", "const:4:8"]]
- 004a7024 ["INT_ADD", "register:40f0:8", ["const:4a7024:8", "const:4:8"]]
+ 004a7064 ["INT_ADD", "register:40f0:8", ["const:4a7064:8", "const:4:8"]]
- 004a7030 ["INT_ADD", "register:40f0:8", ["const:4a7030:8", "const:4:8"]]
+ 004a7070 ["INT_ADD", "register:40f0:8", ["const:4a7070:8", "const:4:8"]]
~~~


### [`004a7138`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7138.md) → [`004a7178`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7178.md) _ZN5Botan17assertion_failureEPKcS1_S1_S1_i

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58650`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md) · 呼出先 11件 [`004594d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md) · 呼出先 11件 [`00459510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 004a716c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:c88:8"]]
+ 004a71ac ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:d58:8"]]
- 004a7170 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:bb8:8"]]
+ 004a71b0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c88:8"]]
- 004a71bc ["INT_ADD", "register:40f0:8", ["const:4a71bc:8", "const:4:8"]]
+ 004a71fc ["INT_ADD", "register:40f0:8", ["const:4a71fc:8", "const:4:8"]]
~~~


### [`004a7448`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7448.md) → [`004a7488`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7488.md) _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58690`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58690.md) · 呼出先 7件 [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58760`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58760.md) · 呼出先 7件 [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      36,
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c66288",
        null,
        "undefined1[48]"
      ]
    ],
    [
      280,
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
      36,
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      52,
      "DATA",
      [
        "storage",
        "00c66358",
        null,
        "undefined1[48]"
      ]
    ],
    [
      280,
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


~~~diff
- 004a746c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 004a74ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 004a74b0 ["INT_ADD", "register:40f0:8", ["const:4a74b0:8", "const:4:8"]]
+ 004a74f0 ["INT_ADD", "register:40f0:8", ["const:4a74f0:8", "const:4:8"]]
- 004a74c0 ["INT_ADD", "register:40f0:8", ["const:4a74c0:8", "const:4:8"]]
+ 004a7500 ["INT_ADD", "register:40f0:8", ["const:4a7500:8", "const:4:8"]]
~~~


### [`004a762c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a762c.md) → [`004a766c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a766c.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587d0.md) · 呼出先 12件 [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c588a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588a0.md) · 呼出先 12件 [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      748,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      752,
      "READ",
      [
        "storage",
        "00c9ad90",
        null,
        "pointer"
      ]
    ],
    [
      752,
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
      748,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      752,
      "READ",
      [
        "storage",
        "00c9ae60",
        null,
        "pointer"
      ]
    ],
    [
      752,
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


~~~diff
- 004a76a4 ["INT_ADD", "register:40f0:8", ["const:4a76a4:8", "const:4:8"]]
+ 004a76e4 ["INT_ADD", "register:40f0:8", ["const:4a76e4:8", "const:4:8"]]
- 004a76f8 ["INT_ADD", "register:40f0:8", ["const:4a76f8:8", "const:4:8"]]
+ 004a7738 ["INT_ADD", "register:40f0:8", ["const:4a7738:8", "const:4:8"]]
- 004a775c ["INT_ADD", "register:40f0:8", ["const:4a775c:8", "const:4:8"]]
+ 004a779c ["INT_ADD", "register:40f0:8", ["const:4a779c:8", "const:4:8"]]
~~~


### [`004a7cf4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7cf4.md) → [`004a7d34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7d34.md) _ZN5BotanplERKNS_3OIDEj

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c53f5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c53/00c53f5c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c53ffc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c53/00c53ffc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "READ",
      [
        "storage",
        "00c9ad40",
        null,
        "pointer"
      ]
    ],
    [
      60,
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
      32,
      "READ",
      [
        "storage",
        "00c9ae10",
        null,
        "pointer"
      ]
    ],
    [
      60,
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


~~~diff
- 004a7d14 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d40:8"]]
+ 004a7d54 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 004a7d40 ["INT_ADD", "register:40f0:8", ["const:4a7d40:8", "const:4:8"]]
+ 004a7d80 ["INT_ADD", "register:40f0:8", ["const:4a7d80:8", "const:4:8"]]
- 004a7d58 ["INT_ADD", "register:40f0:8", ["const:4a7d58:8", "const:4:8"]]
+ 004a7d98 ["INT_ADD", "register:40f0:8", ["const:4a7d98:8", "const:4:8"]]
~~~


### [`004a7e28`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a7/004a7e28.md) → [`004a7e68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a7/004a7e68.md) _ZNK5Botan3OID11encode_intoERNS_11DER_EncoderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      860,
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      868,
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      876,
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
      860,
      "PARAM",
      [
        "storage",
        "002bb21a",
        null,
        "string"
      ]
    ],
    [
      868,
      "PARAM",
      [
        "storage",
        "002a1e83",
        null,
        "string"
      ]
    ],
    [
      876,
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


~~~diff
- 004a7e90 ["INT_ADD", "register:40f0:8", ["const:4a7e90:8", "const:4:8"]]
+ 004a7ed0 ["INT_ADD", "register:40f0:8", ["const:4a7ed0:8", "const:4:8"]]
- 004a7fac ["INT_ADD", "register:40f0:8", ["const:4a7fac:8", "const:4:8"]]
+ 004a7fec ["INT_ADD", "register:40f0:8", ["const:4a7fec:8", "const:4:8"]]
- 004a7fd4 ["INT_ADD", "register:40f0:8", ["const:4a7fd4:8", "const:4:8"]]
+ 004a8014 ["INT_ADD", "register:40f0:8", ["const:4a8014:8", "const:4:8"]]
~~~


### [`004a83a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a83a0.md) → [`004a83e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a83e0.md) _ZN5Botan3OID11decode_fromERNS_11BER_DecoderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 16件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00535b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b6c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00535bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bac.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      736,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      828,
      "PARAM",
      [
        "storage",
        "0029ee58",
        null,
        "string"
      ]
    ],
    [
      884,
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
      736,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      828,
      "PARAM",
      [
        "storage",
        "0029ee0b",
        null,
        "string"
      ]
    ],
    [
      884,
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


~~~diff
- 004a83d8 ["INT_ADD", "register:40f0:8", ["const:4a83d8:8", "const:4:8"]]
+ 004a8418 ["INT_ADD", "register:40f0:8", ["const:4a8418:8", "const:4:8"]]
- 004a8464 ["INT_ADD", "register:40f0:8", ["const:4a8464:8", "const:4:8"]]
+ 004a84a4 ["INT_ADD", "register:40f0:8", ["const:4a84a4:8", "const:4:8"]]
- 004a8484 ["INT_ADD", "register:40f0:8", ["const:4a8484:8", "const:4:8"]]
+ 004a84c4 ["INT_ADD", "register:40f0:8", ["const:4a84c4:8", "const:4:8"]]
~~~


### [`004a88e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) → [`004a8928`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) _ZN5Botan11BER_Decoder15get_next_objectEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) · 呼出先 10件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md)
- 新版 呼出元 1件 [`00c587f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587f0.md) · 呼出先 10件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004afa58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) [`004afc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      336,
      "PARAM",
      [
        "storage",
        "002b1a10",
        null,
        "string"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      392,
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
      336,
      "PARAM",
      [
        "storage",
        "002b1a41",
        null,
        "string"
      ]
    ],
    [
      388,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      392,
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


~~~diff
- 004a8940 ["INT_ADD", "register:40f0:8", ["const:4a8940:8", "const:4:8"]]
+ 004a8980 ["INT_ADD", "register:40f0:8", ["const:4a8980:8", "const:4:8"]]
- 004a895c ["INT_ADD", "register:40f0:8", ["const:4a895c:8", "const:4:8"]]
+ 004a899c ["INT_ADD", "register:40f0:8", ["const:4a899c:8", "const:4:8"]]
- 004a8974 ["INT_ADD", "register:40f0:8", ["const:4a8974:8", "const:4:8"]]
+ 004a89b4 ["INT_ADD", "register:40f0:8", ["const:4a89b4:8", "const:4:8"]]
~~~


### [`004a8b9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8b9c.md) → [`004a8bdc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8bdc.md) _ZNK5Botan14ASN1_Formatter5printEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57fa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fa0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fc0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58070`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58070.md) [`00c58080`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58080.md) [`00c58090`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58090.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      56,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      80,
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 004a8bd0 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:c88:8"]]
+ 004a8c10 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d58:8"]]
- 004a8bd4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:bb8:8"]]
+ 004a8c14 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:c88:8"]]
- 004a8c1c ["INT_ADD", "register:40f0:8", ["const:4a8c1c:8", "const:4:8"]]
+ 004a8c5c ["INT_ADD", "register:40f0:8", ["const:4a8c5c:8", "const:4:8"]]
~~~


### [`004a8e2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a8e2c.md) → [`004a8e6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8e6c.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58870`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58870.md) · 呼出先 36件 [`004594d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004a6db0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a6db0.md) [`00535b80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535b80.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c58940`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58940.md) · 呼出先 36件 [`00459510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004a6df0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a6df0.md) [`00535bc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/00535bc0.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      108,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      224,
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
      108,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      200,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      224,
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


~~~diff
- 004a8e70 ["INT_ADD", "register:40f0:8", ["const:4a8e70:8", "const:4:8"]]
+ 004a8eb0 ["INT_ADD", "register:40f0:8", ["const:4a8eb0:8", "const:4:8"]]
- 004a8e98 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:738:8"]]
+ 004a8ed8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:808:8"]]
- 004a8ea8 ["INT_ADD", "register:40f0:8", ["const:4a8ea8:8", "const:4:8"]]
+ 004a8ee8 ["INT_ADD", "register:40f0:8", ["const:4a8ee8:8", "const:4:8"]]
~~~


### [`004aa27c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004aa/004aa27c.md) → [`004aa2bc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004aa/004aa2bc.md) _ZN5Botan4OIDS6lookupERKNS_3OIDE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588b0.md) · 呼出先 5件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58800`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58800.md)
- 新版 呼出元 1件 [`00c58980`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58980.md) · 呼出先 5件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c588d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 192件, `store_value` 1件

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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004aa4ac",
      "incomplete_value": false,
      "site": "004aa4b4",
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
            "const:5f5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa46c",
      "incomplete_value": false,
      "site": "004aa474",
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
            "const:651:8"
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
      "definition_site": "004aa4cc",
      "incomplete_value": false,
      "site": "004aa4d4",
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
            "const:77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004aa48c",
      "incomplete_value": false,
      "site": "004aa494",
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
            "const:cb:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      320,
      "PARAM",
      [
        "storage",
        "002a64c3",
        null,
        null
      ]
    ],
    [
      496,
      "PARAM",
      [
        "storage",
        "002ac651",
        null,
        "string"
      ]
    ],
    [
      516,
      "PARAM",
      [
        "storage",
        "002a7705",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      320,
      "PARAM",
      [
        "storage",
        "002a6467",
        null,
        null
      ]
    ],
    [
      496,
      "PARAM",
      [
        "storage",
        "002ac5f5",
        null,
        "string"
      ]
    ],
    [
      516,
      "PARAM",
      [
        "storage",
        "002a76a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 004aa2a8 ["INT_ADD", "register:40f0:8", ["const:4aa2a8:8", "const:4:8"]]
- 004aa2a8 ["CALL", null, ["callee:00c588d0:8"]]
- 004aa2ac ["COPY", "tmp:0:8", ["register:8:8"]]
- 004aa2ac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 004aa2e8 ["INT_ADD", "register:40f0:8", ["const:4aa2e8:8", "const:4:8"]]
+ 004aa2e8 ["CALL", null, ["callee:00c588d0:8"]]
+ 004aa2ec ["COPY", "tmp:0:8", ["register:8:8"]]
+ 004aa2ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
~~~


### [`004abd6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ab/004abd6c.md) → [`004abdac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ab/004abdac.md) _ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588c0.md) · 呼出先 7件 [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58720.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) [`00c58920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)
- 新版 呼出元 1件 [`00c58990`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58990.md) · 呼出先 7件 [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c587f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587f0.md) [`00c58800`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58800.md) [`00c589f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      288,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      424,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      472,
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
      288,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      424,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      472,
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


~~~diff
- 004abda8 ["INT_ADD", "register:40f0:8", ["const:4abda8:8", "const:4:8"]]
+ 004abde8 ["INT_ADD", "register:40f0:8", ["const:4abde8:8", "const:4:8"]]
- 004abdb8 ["INT_ADD", "register:40f0:8", ["const:4abdb8:8", "const:4:8"]]
+ 004abdf8 ["INT_ADD", "register:40f0:8", ["const:4abdf8:8", "const:4:8"]]
- 004abe40 ["INT_ADD", "register:40f0:8", ["const:4abe40:8", "const:4:8"]]
+ 004abe80 ["INT_ADD", "register:40f0:8", ["const:4abe80:8", "const:4:8"]]
~~~


### [`004ac1e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) → [`004ac224`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac224.md) _ZNK5Botan9X509_Time15readable_stringEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58910`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58910.md) · 呼出先 17件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004518b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00451/004518b0.md) [`004594d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 1件 [`00c589e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589e0.md) · 呼出先 17件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004518f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00451/004518f0.md) [`00459510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      112,
      "READ",
      [
        "storage",
        "00c9ac30",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "01127e18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      188,
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
      112,
      "READ",
      [
        "storage",
        "00c9ad00",
        null,
        "pointer"
      ]
    ],
    [
      112,
      "PARAM",
      [
        "storage",
        "01127f18",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      188,
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


~~~diff
- 004ac220 ["INT_ADD", "register:40f0:8", ["const:4ac220:8", "const:4:8"]]
+ 004ac260 ["INT_ADD", "register:40f0:8", ["const:4ac260:8", "const:4:8"]]
- 004ac248 ["INT_ADD", "register:40f0:8", ["const:4ac248:8", "const:4:8"]]
+ 004ac288 ["INT_ADD", "register:40f0:8", ["const:4ac288:8", "const:4:8"]]
- 004ac254 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:c30:8"]]
+ 004ac294 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d00:8"]]
~~~


### [`004ac500`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac500.md) → [`004ac540`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac540.md) _ZNK5Botan19ASN1_Pretty_Printer6formatENS_8ASN1_TagES1_mmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`0043b764`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`004594d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00459/004594d0.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`0043b7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00459510`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00459/00459510.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      156,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00c9abb8",
        null,
        "pointer"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00c93208",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      156,
      "READ",
      [
        "storage",
        "00c9ad58",
        null,
        "pointer"
      ]
    ],
    [
      160,
      "READ",
      [
        "storage",
        "00c9ac88",
        null,
        "pointer"
      ]
    ],
    [
      176,
      "READ",
      [
        "storage",
        "00c932d8",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


~~~diff
- 004ac59c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:c88:8"]]
+ 004ac5dc ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:d58:8"]]
- 004ac5a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bb8:8"]]
+ 004ac5e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c88:8"]]
- 004ac5dc ["INT_ADD", "register:40f0:8", ["const:4ac5dc:8", "const:4:8"]]
+ 004ac61c ["INT_ADD", "register:40f0:8", ["const:4ac61c:8", "const:4:8"]]
~~~


### [`004ace50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) → [`004ace90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ace90.md) _ZN5Botan11ASN1_StringC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59960.md) · 呼出先 2件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`004acf78`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md)
- 新版 呼出元 1件 [`00c59a30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59a30.md) · 呼出先 2件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`004acfb8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acfb8.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      164,
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
      28,
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      48,
      "DATA",
      [
        "storage",
        "00c66418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      164,
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


~~~diff
- 004ace6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 004aceac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 004aceac ["INT_ADD", "register:40f0:8", ["const:4aceac:8", "const:4:8"]]
+ 004aceec ["INT_ADD", "register:40f0:8", ["const:4aceec:8", "const:4:8"]]
- 004aceec ["COPY", "tmp:0:8", ["const:568:8"]]
+ 004acf2c ["COPY", "tmp:0:8", ["const:5a8:8"]]
~~~


### [`004acf78`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004acf78.md) → [`004acfb8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004acfb8.md) FUN_004acfb8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ace50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ace50.md) [`004ad774`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad774.md) · 呼出先 7件 [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f60.md)
- 新版 呼出元 2件 [`004ace90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ace90.md) [`004ad7b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad7b4.md) · 呼出先 7件 [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58030`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      136,
      "PARAM",
      [
        "storage",
        "002ae9cf",
        null,
        "string"
      ]
    ],
    [
      220,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      224,
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
      136,
      "PARAM",
      [
        "storage",
        "002ae973",
        null,
        "string"
      ]
    ],
    [
      220,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      224,
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


~~~diff
- 004acfe8 ["INT_ADD", "register:40f0:8", ["const:4acfe8:8", "const:4:8"]]
+ 004ad028 ["INT_ADD", "register:40f0:8", ["const:4ad028:8", "const:4:8"]]
- 004acff8 ["INT_ADD", "register:40f0:8", ["const:4acff8:8", "const:4:8"]]
+ 004ad038 ["INT_ADD", "register:40f0:8", ["const:4ad038:8", "const:4:8"]]
- 004ad000 ["COPY", "tmp:0:8", ["const:9cf:8"]]
+ 004ad040 ["COPY", "tmp:0:8", ["const:973:8"]]
~~~


### [`004ad0e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad0e0.md) → [`004ad120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad120.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588f0.md) · 呼出先 1件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 1件 [`00c589c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589c0.md) · 呼出先 1件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      24,
      "READ",
      [
        "storage",
        "00c9adb8",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c66348",
        null,
        "undefined1[48]"
      ]
    ],
    [
      140,
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
      24,
      "READ",
      [
        "storage",
        "00c9ae88",
        null,
        "pointer"
      ]
    ],
    [
      40,
      "DATA",
      [
        "storage",
        "00c66418",
        null,
        "undefined1[48]"
      ]
    ],
    [
      140,
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


~~~diff
- 004ad0f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db8:8"]]
+ 004ad138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
- 004ad134 ["INT_ADD", "register:40f0:8", ["const:4ad134:8", "const:4:8"]]
+ 004ad174 ["INT_ADD", "register:40f0:8", ["const:4ad174:8", "const:4:8"]]
- 004ad164 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 004ad1a4 ["COPY", "tmp:0:8", ["const:5a8:8"]]
~~~


### [`004ad1c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad1c0.md) → [`004ad200`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad200.md) _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58970`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58970.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58a40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a40.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      276,
      "PARAM",
      [
        "storage",
        "002a2008",
        null,
        "string"
      ]
    ],
    [
      328,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      332,
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
      276,
      "PARAM",
      [
        "storage",
        "002a1fbb",
        null,
        "string"
      ]
    ],
    [
      328,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      332,
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


~~~diff
- 004ad220 ["INT_ADD", "register:40f0:8", ["const:4ad220:8", "const:4:8"]]
+ 004ad260 ["INT_ADD", "register:40f0:8", ["const:4ad260:8", "const:4:8"]]
- 004ad290 ["INT_ADD", "register:40f0:8", ["const:4ad290:8", "const:4:8"]]
+ 004ad2d0 ["INT_ADD", "register:40f0:8", ["const:4ad2d0:8", "const:4:8"]]
- 004ad2c8 ["INT_ADD", "register:40f0:8", ["const:4ad2c8:8", "const:4:8"]]
+ 004ad308 ["INT_ADD", "register:40f0:8", ["const:4ad308:8", "const:4:8"]]
~~~


### [`004ad4b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) → [`004ad4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58820`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) · 呼出先 8件 [`004b2254`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md)
- 新版 呼出元 1件 [`00c588f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) · 呼出先 8件 [`004b2294`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) [`004b2600`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      176,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      312,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      548,
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
      176,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      312,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      548,
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


~~~diff
- 004ad4f8 ["INT_ADD", "register:40f0:8", ["const:4ad4f8:8", "const:4:8"]]
+ 004ad538 ["INT_ADD", "register:40f0:8", ["const:4ad538:8", "const:4:8"]]
- 004ad520 ["INT_ADD", "register:40f0:8", ["const:4ad520:8", "const:4:8"]]
+ 004ad560 ["INT_ADD", "register:40f0:8", ["const:4ad560:8", "const:4:8"]]
- 004ad548 ["INT_ADD", "register:40f0:8", ["const:4ad548:8", "const:4:8"]]
+ 004ad588 ["INT_ADD", "register:40f0:8", ["const:4ad588:8", "const:4:8"]]
~~~


### [`004ad9ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad9ac.md) → [`004ad9ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad9ec.md) _ZN5Botan12ucs2_to_utf8EPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58980`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58980.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a50.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004f9250`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9250.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "PARAM",
      [
        "storage",
        "002ba2c2",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      196,
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
      140,
      "PARAM",
      [
        "storage",
        "002ba26e",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      196,
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


~~~diff
- 004ad9f8 ["INT_ADD", "register:40f0:8", ["const:4ad9f8:8", "const:4:8"]]
+ 004ada38 ["INT_ADD", "register:40f0:8", ["const:4ada38:8", "const:4:8"]]
- 004ada2c ["INT_ADD", "register:40f0:8", ["const:4ada2c:8", "const:4:8"]]
+ 004ada6c ["INT_ADD", "register:40f0:8", ["const:4ada6c:8", "const:4:8"]]
- 004ada38 ["COPY", "tmp:0:8", ["const:2c2:8"]]
+ 004ada78 ["COPY", "tmp:0:8", ["const:26e:8"]]
~~~


### [`004adae4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adae4.md) → [`004adb24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adb24.md) _ZN5Botan12ucs4_to_utf8EPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58990`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58990.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004f9210`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9210.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a60.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004f9250`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9250.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "PARAM",
      [
        "storage",
        "002a41b2",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      196,
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
      140,
      "PARAM",
      [
        "storage",
        "002a4165",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      196,
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


~~~diff
- 004adb30 ["INT_ADD", "register:40f0:8", ["const:4adb30:8", "const:4:8"]]
+ 004adb70 ["INT_ADD", "register:40f0:8", ["const:4adb70:8", "const:4:8"]]
- 004adb64 ["INT_ADD", "register:40f0:8", ["const:4adb64:8", "const:4:8"]]
+ 004adba4 ["INT_ADD", "register:40f0:8", ["const:4adba4:8", "const:4:8"]]
- 004adb70 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 004adbb0 ["COPY", "tmp:0:8", ["const:165:8"]]
~~~


### [`004adc1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004adc1c.md) → [`004adc5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adc5c.md) _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c59a70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c59/00c59a70.md) · 呼出先 3件 [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c589a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589a0.md) [`00c589b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589b0.md)
- 新版 呼出元 1件 [`00c59b40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c59/00c59b40.md) · 呼出先 3件 [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58a70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a70.md) [`00c58a80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a80.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      28,
      "READ",
      [
        "storage",
        "00c9adb0",
        null,
        "pointer"
      ]
    ],
    [
      44,
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
      28,
      "READ",
      [
        "storage",
        "00c9ae80",
        null,
        "pointer"
      ]
    ],
    [
      44,
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


~~~diff
- 004adc38 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:db0:8"]]
+ 004adc78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
- 004adc5c ["INT_ADD", "register:40f0:8", ["const:4adc5c:8", "const:4:8"]]
+ 004adc9c ["INT_ADD", "register:40f0:8", ["const:4adc9c:8", "const:4:8"]]
- 004adc6c ["INT_ADD", "register:40f0:8", ["const:4adc6c:8", "const:4:8"]]
+ 004adcac ["INT_ADD", "register:40f0:8", ["const:4adcac:8", "const:4:8"]]
~~~


### [`004add64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004add64.md) → [`004adda4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004adda4.md) _ZN5Botan9X509_Time6set_toERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589c0.md) · 呼出先 16件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540d7c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540d7c.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md)
- 新版 呼出元 1件 [`00c58a90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a90.md) · 呼出先 16件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540dbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540dbc.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      176,
      "PARAM",
      [
        "storage",
        "002a8b15",
        null,
        "string"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "002a648c",
        null,
        null
      ]
    ],
    [
      272,
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
      176,
      "PARAM",
      [
        "storage",
        "002a8ab9",
        null,
        "string"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "002a6430",
        null,
        null
      ]
    ],
    [
      272,
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


~~~diff
- 004adda8 ["INT_ADD", "register:40f0:8", ["const:4adda8:8", "const:4:8"]]
+ 004adde8 ["INT_ADD", "register:40f0:8", ["const:4adde8:8", "const:4:8"]]
- 004ade08 ["INT_ADD", "register:40f0:8", ["const:4ade08:8", "const:4:8"]]
+ 004ade48 ["INT_ADD", "register:40f0:8", ["const:4ade48:8", "const:4:8"]]
- 004ade14 ["COPY", "tmp:0:8", ["const:b15:8"]]
+ 004ade54 ["COPY", "tmp:0:8", ["const:ab9:8"]]
~~~


### [`004ae584`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae584.md) → [`004ae5c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae5c4.md) _ZNK5Botan9X509_Time11encode_intoERNS_11DER_EncoderE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      172,
      "PARAM",
      [
        "storage",
        "002a302e",
        null,
        "string"
      ]
    ],
    [
      224,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      228,
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
      172,
      "PARAM",
      [
        "storage",
        "002a2fe1",
        null,
        "string"
      ]
    ],
    [
      224,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      228,
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


~~~diff
- 004ae5c0 ["INT_ADD", "register:40f0:8", ["const:4ae5c0:8", "const:4:8"]]
+ 004ae600 ["INT_ADD", "register:40f0:8", ["const:4ae600:8", "const:4:8"]]
- 004ae5e8 ["INT_ADD", "register:40f0:8", ["const:4ae5e8:8", "const:4:8"]]
+ 004ae628 ["INT_ADD", "register:40f0:8", ["const:4ae628:8", "const:4:8"]]
- 004ae5f8 ["INT_ADD", "register:40f0:8", ["const:4ae5f8:8", "const:4:8"]]
+ 004ae638 ["INT_ADD", "register:40f0:8", ["const:4ae638:8", "const:4:8"]]
~~~


### [`004ae6dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) → [`004ae71c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae71c.md) _ZNK5Botan9X509_Time9to_stringEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589d0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589d0.md) · 呼出先 13件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58aa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58aa0.md) · 呼出先 13件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      192,
      "PARAM",
      [
        "storage",
        "002b19cf",
        null,
        null
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "002b807b",
        null,
        null
      ]
    ],
    [
      436,
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
      192,
      "PARAM",
      [
        "storage",
        "002b1a00",
        null,
        null
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "002b80bb",
        null,
        null
      ]
    ],
    [
      436,
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


~~~diff
- 004ae794 ["INT_ADD", "register:40f0:8", ["const:4ae794:8", "const:4:8"]]
+ 004ae7d4 ["INT_ADD", "register:40f0:8", ["const:4ae7d4:8", "const:4:8"]]
- 004ae79c ["COPY", "tmp:0:8", ["const:9cf:8"]]
+ 004ae7dc ["COPY", "tmp:0:8", ["const:a00:8"]]
- 004ae7a4 ["INT_ADD", "register:40f0:8", ["const:4ae7a4:8", "const:4:8"]]
+ 004ae7e4 ["INT_ADD", "register:40f0:8", ["const:4ae7e4:8", "const:4:8"]]
~~~


### [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) → [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) FUN_004aeca4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 29件 [`004a559c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a559c.md) [`004a5ae0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a5/004a5ae0.md) [`004ac1e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ac/004ac1e4.md) [`004ae6dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004ae6dc.md) [`004aecdc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) · 呼出先 1件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md)
- 新版 呼出元 29件 [`004a55dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a55dc.md) [`004a5b20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a5/004a5b20.md) [`004ac224`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ac/004ac224.md) [`004ae71c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004ae71c.md) [`004aed1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aed1c.md) · 呼出先 1件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md)

変更の種類 constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      20,
      "READ",
      [
        "storage",
        "00c9add0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c67428",
        null,
        "undefined1[40]"
      ]
    ],
    [
      76,
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
      20,
      "READ",
      [
        "storage",
        "00c9aea0",
        null,
        "pointer"
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00c674f8",
        null,
        "undefined1[40]"
      ]
    ],
    [
      76,
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


~~~diff
- 004aec78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 004aecb8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 004aeca8 ["INT_ADD", "register:40f0:8", ["const:4aeca8:8", "const:4:8"]]
+ 004aece8 ["INT_ADD", "register:40f0:8", ["const:4aece8:8", "const:4:8"]]
- 004aecb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
+ 004aecf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
~~~


### [`004aecdc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aecdc.md) → [`004aed1c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aed1c.md) _ZNK5Botan9X509_Time3cmpERKS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c589e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c589e0.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58ab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ab0.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      228,
      "PARAM",
      [
        "storage",
        "002b8e42",
        null,
        "string"
      ]
    ],
    [
      284,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      288,
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
      228,
      "PARAM",
      [
        "storage",
        "002b8dee",
        null,
        "string"
      ]
    ],
    [
      284,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      288,
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


~~~diff
- 004aedb4 ["INT_ADD", "register:40f0:8", ["const:4aedb4:8", "const:4:8"]]
+ 004aedf4 ["INT_ADD", "register:40f0:8", ["const:4aedf4:8", "const:4:8"]]
- 004aedc0 ["COPY", "tmp:0:8", ["const:e42:8"]]
+ 004aee00 ["COPY", "tmp:0:8", ["const:dee:8"]]
- 004aedc8 ["INT_ADD", "register:40f0:8", ["const:4aedc8:8", "const:4:8"]]
+ 004aee08 ["INT_ADD", "register:40f0:8", ["const:4aee08:8", "const:4:8"]]
~~~


### [`004aee5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aee5c.md) → [`004aee9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aee9c.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587f0.md) · 呼出先 8件 [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md) [`00c57f70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md)
- 新版 呼出元 1件 [`00c588c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588c0.md) · 呼出先 8件 [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md) [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      192,
      "PARAM",
      [
        "storage",
        "002ba309",
        null,
        "string"
      ]
    ],
    [
      252,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      256,
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
      192,
      "PARAM",
      [
        "storage",
        "002ba2b5",
        null,
        "string"
      ]
    ],
    [
      252,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      256,
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


~~~diff
- 004aeec8 ["INT_ADD", "register:40f0:8", ["const:4aeec8:8", "const:4:8"]]
+ 004aef08 ["INT_ADD", "register:40f0:8", ["const:4aef08:8", "const:4:8"]]
- 004aef10 ["INT_ADD", "register:40f0:8", ["const:4aef10:8", "const:4:8"]]
+ 004aef50 ["INT_ADD", "register:40f0:8", ["const:4aef50:8", "const:4:8"]]
- 004aef1c ["COPY", "tmp:0:8", ["const:309:8"]]
+ 004aef5c ["COPY", "tmp:0:8", ["const:2b5:8"]]
~~~


### [`004af1b8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af1b8.md) → [`004af1f8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af1f8.md) _ZNK5Botan14calendar_point16to_std_timepointEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a00.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58ad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ad0.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      296,
      "PARAM",
      [
        "storage",
        "002b0bec",
        null,
        "string"
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      356,
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
      296,
      "PARAM",
      [
        "storage",
        "002b0b90",
        null,
        "string"
      ]
    ],
    [
      352,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      356,
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


~~~diff
- 004af2d4 ["INT_ADD", "register:40f0:8", ["const:4af2d4:8", "const:4:8"]]
+ 004af314 ["INT_ADD", "register:40f0:8", ["const:4af314:8", "const:4:8"]]
- 004af2e0 ["COPY", "tmp:0:8", ["const:bec:8"]]
+ 004af320 ["COPY", "tmp:0:8", ["const:b90:8"]]
- 004af2e8 ["INT_ADD", "register:40f0:8", ["const:4af2e8:8", "const:4:8"]]
+ 004af328 ["INT_ADD", "register:40f0:8", ["const:4af328:8", "const:4:8"]]
~~~


### [`004af484`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af484.md) → [`004af4c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af4c4.md) _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58730.md) · 呼出先 9件 [`004a684c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a6/004a684c.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58800`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58800.md) · 呼出先 9件 [`004a688c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a6/004a688c.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "PARAM",
      [
        "storage",
        "002b19f0",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "002a5352",
        null,
        null
      ]
    ],
    [
      260,
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
      148,
      "PARAM",
      [
        "storage",
        "002b1a21",
        null,
        "string"
      ]
    ],
    [
      192,
      "PARAM",
      [
        "storage",
        "002a52f6",
        null,
        null
      ]
    ],
    [
      260,
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


~~~diff
- 004af4f8 ["INT_ADD", "register:40f0:8", ["const:4af4f8:8", "const:4:8"]]
+ 004af538 ["INT_ADD", "register:40f0:8", ["const:4af538:8", "const:4:8"]]
- 004af510 ["INT_ADD", "register:40f0:8", ["const:4af510:8", "const:4:8"]]
+ 004af550 ["INT_ADD", "register:40f0:8", ["const:4af550:8", "const:4:8"]]
- 004af518 ["COPY", "tmp:0:8", ["const:9f0:8"]]
+ 004af558 ["COPY", "tmp:0:8", ["const:a21:8"]]
~~~


### [`004af894`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004af894.md) → [`004af8d4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004af8d4.md) _ZN5Botan11BER_Decoder10verify_endEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58a20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a20.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58af0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58af0.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      132,
      "PARAM",
      [
        "storage",
        "0029ee76",
        null,
        "string"
      ]
    ],
    [
      188,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      192,
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
      132,
      "PARAM",
      [
        "storage",
        "0029ee29",
        null,
        "string"
      ]
    ],
    [
      188,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      192,
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


~~~diff
- 004af8c4 ["INT_ADD", "register:40f0:8", ["const:4af8c4:8", "const:4:8"]]
+ 004af904 ["INT_ADD", "register:40f0:8", ["const:4af904:8", "const:4:8"]]
- 004af90c ["INT_ADD", "register:40f0:8", ["const:4af90c:8", "const:4:8"]]
+ 004af94c ["INT_ADD", "register:40f0:8", ["const:4af94c:8", "const:4:8"]]
- 004af918 ["COPY", "tmp:0:8", ["const:e76:8"]]
+ 004af958 ["COPY", "tmp:0:8", ["const:e29:8"]]
~~~


### [`004afa18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) → [`004afa58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) FUN_004afa58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`004a8928`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) [`004afc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      264,
      "PARAM",
      [
        "storage",
        "002a1243",
        null,
        "string"
      ]
    ],
    [
      316,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      320,
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
      264,
      "PARAM",
      [
        "storage",
        "002a11f6",
        null,
        "string"
      ]
    ],
    [
      316,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      320,
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


~~~diff
- 004afa58 ["INT_ADD", "register:40f0:8", ["const:4afa58:8", "const:4:8"]]
+ 004afa98 ["INT_ADD", "register:40f0:8", ["const:4afa98:8", "const:4:8"]]
- 004afa94 ["INT_ADD", "register:40f0:8", ["const:4afa94:8", "const:4:8"]]
+ 004afad4 ["INT_ADD", "register:40f0:8", ["const:4afad4:8", "const:4:8"]]
- 004afb14 ["INT_ADD", "register:40f0:8", ["const:4afb14:8", "const:4:8"]]
+ 004afb54 ["INT_ADD", "register:40f0:8", ["const:4afb54:8", "const:4:8"]]
~~~


### [`004afc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) → [`004afc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) FUN_004afc50

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004a88e8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004a8/004a88e8.md) [`004afc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) · 呼出先 18件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004afa18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afa18.md) [`004afc10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004af/004afc10.md) [`004f9a20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004f9/004f9a20.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md)
- 新版 呼出元 2件 [`004a8928`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004a8/004a8928.md) [`004afc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) · 呼出先 18件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004afa58`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afa58.md) [`004afc50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004af/004afc50.md) [`004f9a60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004f9/004f9a60.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      400,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      416,
      "DATA",
      [
        "storage",
        "00c67388",
        null,
        "undefined1[80]"
      ]
    ],
    [
      548,
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
      400,
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      416,
      "DATA",
      [
        "storage",
        "00c67458",
        null,
        "undefined1[80]"
      ]
    ],
    [
      548,
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


~~~diff
- 004afc58 ["INT_ADD", "register:40f0:8", ["const:4afc58:8", "const:4:8"]]
+ 004afc98 ["INT_ADD", "register:40f0:8", ["const:4afc98:8", "const:4:8"]]
- 004afcb0 ["INT_ADD", "register:40f0:8", ["const:4afcb0:8", "const:4:8"]]
+ 004afcf0 ["INT_ADD", "register:40f0:8", ["const:4afcf0:8", "const:4:8"]]
- 004afcf8 ["INT_ADD", "register:40f0:8", ["const:4afcf8:8", "const:4:8"]]
+ 004afd38 ["INT_ADD", "register:40f0:8", ["const:4afd38:8", "const:4:8"]]
~~~


### [`004b03f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b03f0.md) → [`004b0430`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0430.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a60.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00543858`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00543/00543858.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58b30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b30.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00543898`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00543/00543898.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      180,
      "PARAM",
      [
        "storage",
        "002a9a8b",
        null,
        "string"
      ]
    ],
    [
      236,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      240,
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
      180,
      "PARAM",
      [
        "storage",
        "002a9aba",
        null,
        "string"
      ]
    ],
    [
      236,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      240,
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


~~~diff
- 004b0498 ["INT_ADD", "register:40f0:8", ["const:4b0498:8", "const:4:8"]]
+ 004b04d8 ["INT_ADD", "register:40f0:8", ["const:4b04d8:8", "const:4:8"]]
- 004b04a4 ["COPY", "tmp:0:8", ["const:a8b:8"]]
+ 004b04e4 ["COPY", "tmp:0:8", ["const:aba:8"]]
- 004b04ac ["INT_ADD", "register:40f0:8", ["const:4b04ac:8", "const:4:8"]]
+ 004b04ec ["INT_ADD", "register:40f0:8", ["const:4b04ec:8", "const:4:8"]]
~~~


### [`004b055c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b055c.md) → [`004b059c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b059c.md) _ZN5Botan11BER_DecoderC1EPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58740`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58740.md) · 呼出先 2件 [`005403c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58810`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58810.md) · 呼出先 2件 [`00540408`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      56,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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
      56,
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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


~~~diff
- 004b0588 ["INT_ADD", "register:40f0:8", ["const:4b0588:8", "const:4:8"]]
+ 004b05c8 ["INT_ADD", "register:40f0:8", ["const:4b05c8:8", "const:4:8"]]
- 004b0594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004b05d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
- 004b05b4 ["INT_ADD", "register:40f0:8", ["const:4b05b4:8", "const:4:8"]]
+ 004b05f4 ["INT_ADD", "register:40f0:8", ["const:4b05f4:8", "const:4:8"]]
~~~


### [`004b0638`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0638.md) → [`004b0678`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0678.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58890`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58890.md) · 呼出先 2件 [`005402a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58960.md) · 呼出先 2件 [`005402e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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
      52,
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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


~~~diff
- 004b0660 ["INT_ADD", "register:40f0:8", ["const:4b0660:8", "const:4:8"]]
+ 004b06a0 ["INT_ADD", "register:40f0:8", ["const:4b06a0:8", "const:4:8"]]
- 004b066c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004b06ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
- 004b0688 ["INT_ADD", "register:40f0:8", ["const:4b0688:8", "const:4:8"]]
+ 004b06c8 ["INT_ADD", "register:40f0:8", ["const:4b06c8:8", "const:4:8"]]
~~~


### [`004b070c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b070c.md) → [`004b074c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b074c.md) _ZN5Botan11BER_DecoderC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00c58880`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58880.md) · 呼出先 2件 [`005403c8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005403c8.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58950`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58950.md) · 呼出先 2件 [`00540408`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540408.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      52,
      "READ",
      [
        "storage",
        "00c9ade0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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
      52,
      "READ",
      [
        "storage",
        "00c9aeb0",
        null,
        "pointer"
      ]
    ],
    [
      68,
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


~~~diff
- 004b0734 ["INT_ADD", "register:40f0:8", ["const:4b0734:8", "const:4:8"]]
+ 004b0774 ["INT_ADD", "register:40f0:8", ["const:4b0774:8", "const:4:8"]]
- 004b0740 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:de0:8"]]
+ 004b0780 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
- 004b075c ["INT_ADD", "register:40f0:8", ["const:4b075c:8", "const:4:8"]]
+ 004b079c ["INT_ADD", "register:40f0:8", ["const:4b079c:8", "const:4:8"]]
~~~


### [`004b0818`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0818.md) → [`004b0858`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0858.md) _ZN5Botan11BER_Decoder11decode_nullEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      84,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "002bfc29",
        null,
        "string"
      ]
    ],
    [
      220,
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
      84,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "002bfbd5",
        null,
        "string"
      ]
    ],
    [
      220,
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


~~~diff
- 004b0840 ["INT_ADD", "register:40f0:8", ["const:4b0840:8", "const:4:8"]]
+ 004b0880 ["INT_ADD", "register:40f0:8", ["const:4b0880:8", "const:4:8"]]
- 004b0850 ["INT_ADD", "register:40f0:8", ["const:4b0850:8", "const:4:8"]]
+ 004b0890 ["INT_ADD", "register:40f0:8", ["const:4b0890:8", "const:4:8"]]
- 004b086c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:738:8"]]
+ 004b08ac ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:808:8"]]
~~~


### [`004b0968`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0968.md) → [`004b09a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b09a8.md) _ZN5Botan11BER_Decoder6decodeERbNS_8ASN1_TagES2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588e0.md) · 呼出先 10件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c589b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589b0.md) · 呼出先 10件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      120,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      208,
      "PARAM",
      [
        "storage",
        "002bfc46",
        null,
        "string"
      ]
    ],
    [
      260,
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
      120,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      208,
      "PARAM",
      [
        "storage",
        "002bfbf2",
        null,
        "string"
      ]
    ],
    [
      260,
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


~~~diff
- 004b09a0 ["INT_ADD", "register:40f0:8", ["const:4b09a0:8", "const:4:8"]]
+ 004b09e0 ["INT_ADD", "register:40f0:8", ["const:4b09e0:8", "const:4:8"]]
- 004b09b0 ["INT_ADD", "register:40f0:8", ["const:4b09b0:8", "const:4:8"]]
+ 004b09f0 ["INT_ADD", "register:40f0:8", ["const:4b09f0:8", "const:4:8"]]
- 004b09e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 004b0a20 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
~~~


### [`004b0aec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0aec.md) → [`004b0b2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0b2c.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a70.md) · 呼出先 9件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58b40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b40.md) · 呼出先 9件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      224,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "002a648e",
        null,
        "string"
      ]
    ],
    [
      360,
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
      224,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "002a6432",
        null,
        "string"
      ]
    ],
    [
      360,
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


~~~diff
- 004b0b28 ["INT_ADD", "register:40f0:8", ["const:4b0b28:8", "const:4:8"]]
+ 004b0b68 ["INT_ADD", "register:40f0:8", ["const:4b0b68:8", "const:4:8"]]
- 004b0bcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 004b0c0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
- 004b0bdc ["INT_ADD", "register:40f0:8", ["const:4b0bdc:8", "const:4:8"]]
+ 004b0c1c ["INT_ADD", "register:40f0:8", ["const:4b0c1c:8", "const:4:8"]]
~~~


### [`004b0cc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0cc8.md) → [`004b0d08`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0d08.md) _ZN5Botan11BER_Decoder26decode_octet_string_bigintERNS_6BigIntE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58a80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) [`00c58a90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a90.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c58b50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md) [`00c58b60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b60.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      184,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      228,
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
      184,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      228,
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


~~~diff
- 004b0d0c ["INT_ADD", "register:40f0:8", ["const:4b0d0c:8", "const:4:8"]]
+ 004b0d4c ["INT_ADD", "register:40f0:8", ["const:4b0d4c:8", "const:4:8"]]
- 004b0d30 ["INT_ADD", "register:40f0:8", ["const:4b0d30:8", "const:4:8"]]
+ 004b0d70 ["INT_ADD", "register:40f0:8", ["const:4b0d70:8", "const:4:8"]]
- 004b0d80 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:738:8"]]
+ 004b0dc0 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:808:8"]]
~~~


### [`004b0e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) → [`004b0e74`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0e74.md) _ZN5Botan6BigInt6decodeEPKhmNS0_4BaseE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58aa0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58aa0.md) · 呼出先 20件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c37ba4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md)
- 新版 呼出元 1件 [`00c58b70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b70.md) · 呼出先 20件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c37c40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      232,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      300,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      560,
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
      232,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      300,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      560,
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


~~~diff
- 004b0eb0 ["INT_ADD", "register:40f0:8", ["const:4b0eb0:8", "const:4:8"]]
+ 004b0ef0 ["INT_ADD", "register:40f0:8", ["const:4b0ef0:8", "const:4:8"]]
- 004b0eec ["INT_ADD", "register:40f0:8", ["const:4b0eec:8", "const:4:8"]]
+ 004b0f2c ["INT_ADD", "register:40f0:8", ["const:4b0f2c:8", "const:4:8"]]
- 004b0efc ["INT_ADD", "register:40f0:8", ["const:4b0efc:8", "const:4:8"]]
+ 004b0f3c ["INT_ADD", "register:40f0:8", ["const:4b0f3c:8", "const:4:8"]]
~~~


### [`004b1518`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1518.md) → [`004b1558`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1558.md) _ZN5Botan11BER_Decoder26decode_constrained_integerENS_8ASN1_TagES1_m

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      328,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "002a76dd",
        null,
        "string"
      ]
    ],
    [
      500,
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
      328,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      448,
      "PARAM",
      [
        "storage",
        "002a7681",
        null,
        "string"
      ]
    ],
    [
      500,
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


~~~diff
- 004b156c ["INT_ADD", "register:40f0:8", ["const:4b156c:8", "const:4:8"]]
+ 004b15ac ["INT_ADD", "register:40f0:8", ["const:4b15ac:8", "const:4:8"]]
- 004b1660 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:738:8"]]
+ 004b16a0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:808:8"]]
- 004b1670 ["INT_ADD", "register:40f0:8", ["const:4b1670:8", "const:4:8"]]
+ 004b16b0 ["INT_ADD", "register:40f0:8", ["const:4b16b0:8", "const:4:8"]]
~~~


### [`004b186c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b186c.md) → [`004b18ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b18ac.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58a80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58a80.md) · 呼出先 14件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00540f2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540f2c.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58b50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b50.md) · 呼出先 14件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00540f6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540f6c.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      252,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      340,
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      396,
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
      252,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      340,
      "PARAM",
      [
        "storage",
        "002a5362",
        null,
        "string"
      ]
    ],
    [
      396,
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


~~~diff
- 004b18b4 ["INT_ADD", "register:40f0:8", ["const:4b18b4:8", "const:4:8"]]
+ 004b18f4 ["INT_ADD", "register:40f0:8", ["const:4b18f4:8", "const:4:8"]]
- 004b18c4 ["INT_ADD", "register:40f0:8", ["const:4b18c4:8", "const:4:8"]]
+ 004b1904 ["INT_ADD", "register:40f0:8", ["const:4b1904:8", "const:4:8"]]
- 004b18e0 ["INT_ADD", "register:40f0:8", ["const:4b18e0:8", "const:4:8"]]
+ 004b1920 ["INT_ADD", "register:40f0:8", ["const:4b1920:8", "const:4:8"]]
~~~


### [`004b1b54`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1b54.md) → [`004b1b94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1b94.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS1_9allocatorIhEEEENS_8ASN1_TagES7_S7_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c588a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c588a0.md) · 呼出先 18件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`0049f42c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0049f/0049f42c.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`0054108c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/0054108c.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md)
- 新版 呼出元 1件 [`00c58970`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58970.md) · 呼出先 18件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`0049f46c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0049f/0049f46c.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005410cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005410cc.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      396,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      492,
      "PARAM",
      [
        "storage",
        "002a53be",
        null,
        "string"
      ]
    ],
    [
      548,
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
      396,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      492,
      "PARAM",
      [
        "storage",
        "002a5362",
        null,
        "string"
      ]
    ],
    [
      548,
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


~~~diff
- 004b1ba4 ["INT_ADD", "register:40f0:8", ["const:4b1ba4:8", "const:4:8"]]
+ 004b1be4 ["INT_ADD", "register:40f0:8", ["const:4b1be4:8", "const:4:8"]]
- 004b1bb4 ["INT_ADD", "register:40f0:8", ["const:4b1bb4:8", "const:4:8"]]
+ 004b1bf4 ["INT_ADD", "register:40f0:8", ["const:4b1bf4:8", "const:4:8"]]
- 004b1bd0 ["INT_ADD", "register:40f0:8", ["const:4b1bd0:8", "const:4:8"]]
+ 004b1c10 ["INT_ADD", "register:40f0:8", ["const:4b1c10:8", "const:4:8"]]
~~~


### [`004b1eec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) → [`004b1f2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c586f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c586f0.md) · 呼出先 8件 [`004b2254`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) [`004b25c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b25c0.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005412b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005412b0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c587c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c587c0.md) · 呼出先 8件 [`004b2294`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) [`004b2600`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2600.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005412f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005412f0.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      336,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      488,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      628,
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
      336,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      488,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      628,
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


~~~diff
- 004b1f68 ["INT_ADD", "register:40f0:8", ["const:4b1f68:8", "const:4:8"]]
+ 004b1fa8 ["INT_ADD", "register:40f0:8", ["const:4b1fa8:8", "const:4:8"]]
- 004b1fd4 ["INT_ADD", "register:40f0:8", ["const:4b1fd4:8", "const:4:8"]]
+ 004b2014 ["INT_ADD", "register:40f0:8", ["const:4b2014:8", "const:4:8"]]
- 004b2000 ["INT_ADD", "register:40f0:8", ["const:4b2000:8", "const:4:8"]]
+ 004b2040 ["INT_ADD", "register:40f0:8", ["const:4b2040:8", "const:4:8"]]
~~~


### [`004b2254`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2254.md) → [`004b2294`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2294.md) FUN_004b2294

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004ad4b0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ad/004ad4b0.md) [`004b1eec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b1/004b1eec.md) · 呼出先 9件 [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005411a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 2件 [`004ad4f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ad/004ad4f0.md) [`004b1f2c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b1/004b1f2c.md) · 呼出先 9件 [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`005411e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      140,
      "PARAM",
      [
        "storage",
        "002bb26e",
        null,
        "string"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "002a1ed0",
        null,
        "string"
      ]
    ],
    [
      156,
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
      140,
      "PARAM",
      [
        "storage",
        "002bb21a",
        null,
        "string"
      ]
    ],
    [
      148,
      "PARAM",
      [
        "storage",
        "002a1e83",
        null,
        "string"
      ]
    ],
    [
      156,
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


~~~diff
- 004b22a8 ["INT_ADD", "register:40f0:8", ["const:4b22a8:8", "const:4:8"]]
+ 004b22e8 ["INT_ADD", "register:40f0:8", ["const:4b22e8:8", "const:4:8"]]
- 004b22e0 ["COPY", "tmp:0:8", ["const:26e:8"]]
+ 004b2320 ["COPY", "tmp:0:8", ["const:21a:8"]]
- 004b22e8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 004b2328 ["COPY", "tmp:0:8", ["const:e83:8"]]
~~~


### [`004b28e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b28e4.md) → [`004b2924`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2924.md) _ZN5Botan11DER_Encoder12get_contentsEv

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c587a0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c587a0.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004aec64`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004ae/004aec64.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58870`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58870.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004aeca4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aeca4.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "PARAM",
      [
        "storage",
        "002b8e5e",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      184,
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
      124,
      "PARAM",
      [
        "storage",
        "002b8e0a",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      184,
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


~~~diff
- 004b2954 ["INT_ADD", "register:40f0:8", ["const:4b2954:8", "const:4:8"]]
+ 004b2994 ["INT_ADD", "register:40f0:8", ["const:4b2994:8", "const:4:8"]]
- 004b2960 ["COPY", "tmp:0:8", ["const:e5e:8"]]
+ 004b29a0 ["COPY", "tmp:0:8", ["const:e0a:8"]]
- 004b2968 ["INT_ADD", "register:40f0:8", ["const:4b2968:8", "const:4:8"]]
+ 004b29a8 ["INT_ADD", "register:40f0:8", ["const:4b29a8:8", "const:4:8"]]
~~~


### [`004b29fc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b29fc.md) → [`004b2a3c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2a3c.md) FUN_004b2a3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      88,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      148,
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
      88,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      148,
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


~~~diff
- 004b2a54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:738:8"]]
+ 004b2a94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:808:8"]]
- 004b2a64 ["INT_ADD", "register:40f0:8", ["const:4b2a64:8", "const:4:8"]]
+ 004b2aa4 ["INT_ADD", "register:40f0:8", ["const:4b2aa4:8", "const:4:8"]]
- 004b2a6c ["INT_ADD", "register:40f0:8", ["const:4b2a6c:8", "const:4:8"]]
+ 004b2aac ["INT_ADD", "register:40f0:8", ["const:4b2aac:8", "const:4:8"]]
~~~


### [`004b2ad8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2ad8.md) → [`004b2b18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2b18.md) _ZN5Botan11DER_Encoder14start_explicitEt

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002af8a7",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      164,
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
      104,
      "PARAM",
      [
        "storage",
        "002af84b",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      164,
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


~~~diff
- 004b2b34 ["INT_ADD", "register:40f0:8", ["const:4b2b34:8", "const:4:8"]]
+ 004b2b74 ["INT_ADD", "register:40f0:8", ["const:4b2b74:8", "const:4:8"]]
- 004b2b40 ["COPY", "tmp:0:8", ["const:8a7:8"]]
+ 004b2b80 ["COPY", "tmp:0:8", ["const:84b:8"]]
- 004b2b48 ["INT_ADD", "register:40f0:8", ["const:4b2b48:8", "const:4:8"]]
+ 004b2b88 ["INT_ADD", "register:40f0:8", ["const:4b2b88:8", "const:4:8"]]
~~~


### [`004b2e04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) → [`004b2e44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2e44.md) _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b10.md) · 呼出先 8件 [`004b3508`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`00c58820`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58820.md) [`00c58920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58920.md)
- 新版 呼出元 1件 [`00c58be0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58be0.md) · 呼出先 8件 [`004b3548`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`00c588f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c588f0.md) [`00c589f0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c589f0.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      108,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      684,
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
      108,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      684,
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


~~~diff
- 004b2e44 ["INT_ADD", "register:40f0:8", ["const:4b2e44:8", "const:4:8"]]
+ 004b2e84 ["INT_ADD", "register:40f0:8", ["const:4b2e84:8", "const:4:8"]]
- 004b2e54 ["INT_ADD", "register:40f0:8", ["const:4b2e54:8", "const:4:8"]]
+ 004b2e94 ["INT_ADD", "register:40f0:8", ["const:4b2e94:8", "const:4:8"]]
- 004b2e70 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:738:8"]]
+ 004b2eb0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:808:8"]]
~~~


### [`004b314c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b314c.md) → [`004b318c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b318c.md) _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b30.md) · 呼出先 12件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`005411a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00541/005411a4.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58c00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c00.md) · 呼出先 12件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`005411e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00541/005411e4.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      256,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      348,
      "PARAM",
      [
        "storage",
        "002a3fba",
        null,
        "string"
      ]
    ],
    [
      400,
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
      256,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      348,
      "PARAM",
      [
        "storage",
        "002a3f6d",
        null,
        "string"
      ]
    ],
    [
      400,
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


~~~diff
- 004b31b0 ["INT_ADD", "register:40f0:8", ["const:4b31b0:8", "const:4:8"]]
+ 004b31f0 ["INT_ADD", "register:40f0:8", ["const:4b31f0:8", "const:4:8"]]
- 004b31d4 ["INT_ADD", "register:40f0:8", ["const:4b31d4:8", "const:4:8"]]
+ 004b3214 ["INT_ADD", "register:40f0:8", ["const:4b3214:8", "const:4:8"]]
- 004b31f4 ["INT_ADD", "register:40f0:8", ["const:4b31f4:8", "const:4:8"]]
+ 004b3234 ["INT_ADD", "register:40f0:8", ["const:4b3234:8", "const:4:8"]]
~~~


### [`004b3508`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) → [`004b3548`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) FUN_004b3548

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 55件 [`004b0e34`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b0/004b0e34.md) [`004b2e04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b2/004b2e04.md) [`004b3600`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) [`004b4e0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4e0c.md) [`004b56dc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b56dc.md) · 呼出先 7件 [`00536e88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00536/00536e88.md) [`00c37ba4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c37/00c37ba4.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 55件 [`004b0e74`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b0/004b0e74.md) [`004b2e44`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b2/004b2e44.md) [`004b3640`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3640.md) [`004b4e4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4e4c.md) [`004b571c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b571c.md) · 呼出先 7件 [`00536ec8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00536/00536ec8.md) [`00c37c40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c37/00c37c40.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      196,
      "READ",
      [
        "storage",
        "00c9ade8",
        null,
        "pointer"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "00c96698",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      200,
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
      196,
      "READ",
      [
        "storage",
        "00c9aeb8",
        null,
        "pointer"
      ]
    ],
    [
      196,
      "PARAM",
      [
        "storage",
        "00c96768",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      200,
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


~~~diff
- 004b3550 ["INT_ADD", "register:40f0:8", ["const:4b3550:8", "const:4:8"]]
+ 004b3590 ["INT_ADD", "register:40f0:8", ["const:4b3590:8", "const:4:8"]]
- 004b359c ["INT_ADD", "register:40f0:8", ["const:4b359c:8", "const:4:8"]]
+ 004b35dc ["INT_ADD", "register:40f0:8", ["const:4b35dc:8", "const:4:8"]]
- 004b35a4 ["INT_ADD", "register:40f0:8", ["const:4b35a4:8", "const:4:8"]]
+ 004b35e4 ["INT_ADD", "register:40f0:8", ["const:4b35e4:8", "const:4:8"]]
~~~


### [`004b3600`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3600.md) → [`004b3640`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3640.md) _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58950`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58950.md) · 呼出先 13件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004b3508`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3508.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58a20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a20.md) · 呼出先 13件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004b3548`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3548.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      700,
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      708,
      "DATA",
      [
        "storage",
        "002c21f0",
        null,
        null
      ]
    ],
    [
      740,
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
      700,
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      708,
      "DATA",
      [
        "storage",
        "002c2230",
        null,
        null
      ]
    ],
    [
      740,
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


~~~diff
- 004b36a8 ["INT_ADD", "register:40f0:8", ["const:4b36a8:8", "const:4:8"]]
+ 004b36e8 ["INT_ADD", "register:40f0:8", ["const:4b36e8:8", "const:4:8"]]
- 004b37a0 ["INT_ADD", "register:40f0:8", ["const:4b37a0:8", "const:4:8"]]
+ 004b37e0 ["INT_ADD", "register:40f0:8", ["const:4b37e0:8", "const:4:8"]]
- 004b38a4 ["COPY", "tmp:0:8", ["const:1f0:8"]]
+ 004b38e4 ["COPY", "tmp:0:8", ["const:230:8"]]
~~~


### [`004b3ee4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) → [`004b3f24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c58b80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b80.md) [`00c58d40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58d40.md) · 呼出先 19件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00440ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440ec0.md) [`00440f5c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00440/00440f5c.md) [`00481e80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00481/00481e80.md) [`004b47ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md)
- 新版 呼出元 2件 [`00c58c50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c50.md) [`00c58e10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58e10.md) · 呼出先 19件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00440f00`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f00.md) [`00440f9c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00440/00440f9c.md) [`00481ec0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00481/00481ec0.md) [`004b47ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b47ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      148,
      "PARAM",
      [
        "storage",
        "002a54b7",
        null,
        "string"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "002bd899",
        null,
        null
      ]
    ],
    [
      300,
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
      148,
      "PARAM",
      [
        "storage",
        "002a545b",
        null,
        "string"
      ]
    ],
    [
      168,
      "PARAM",
      [
        "storage",
        "002bd845",
        null,
        null
      ]
    ],
    [
      300,
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


~~~diff
- 004b3f40 ["INT_ADD", "register:40f0:8", ["const:4b3f40:8", "const:4:8"]]
+ 004b3f80 ["INT_ADD", "register:40f0:8", ["const:4b3f80:8", "const:4:8"]]
- 004b3f78 ["COPY", "tmp:0:8", ["const:4b7:8"]]
+ 004b3fb8 ["COPY", "tmp:0:8", ["const:45b:8"]]
- 004b3f84 ["INT_ADD", "register:40f0:8", ["const:4b3f84:8", "const:4:8"]]
+ 004b3fc4 ["INT_ADD", "register:40f0:8", ["const:4b3fc4:8", "const:4:8"]]
~~~


### [`004b47ac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b47ac.md) → [`004b47ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b47ec.md) FUN_004b47ec

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004b3ee4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b3/004b3ee4.md) · 呼出先 6件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`00c57eb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57eb0.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f70`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f70.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f80.md)
- 新版 呼出元 1件 [`004b3f24`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b3/004b3f24.md) · 呼出先 6件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`00c57f80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f80.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58040`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58040.md) [`00c58050`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58050.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      244,
      "PARAM",
      [
        "storage",
        "002afa22",
        null,
        null
      ]
    ],
    [
      324,
      "PARAM",
      [
        "storage",
        "002b2cca",
        null,
        null
      ]
    ],
    [
      436,
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
      244,
      "PARAM",
      [
        "storage",
        "002af9c6",
        null,
        null
      ]
    ],
    [
      324,
      "PARAM",
      [
        "storage",
        "002b2cfb",
        null,
        null
      ]
    ],
    [
      436,
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


~~~diff
- 004b4810 ["INT_ADD", "register:40f0:8", ["const:4b4810:8", "const:4:8"]]
+ 004b4850 ["INT_ADD", "register:40f0:8", ["const:4b4850:8", "const:4:8"]]
- 004b4844 ["COPY", "tmp:0:8", ["const:a22:8"]]
+ 004b4884 ["COPY", "tmp:0:8", ["const:9c6:8"]]
- 004b48a4 ["INT_ADD", "register:40f0:8", ["const:4b48a4:8", "const:4:8"]]
+ 004b48e4 ["INT_ADD", "register:40f0:8", ["const:4b48e4:8", "const:4:8"]]
~~~


### [`004b4ab8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b4/004b4ab8.md) → [`004b4af8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b4/004b4af8.md) _ZNK5Botan9SCAN_Name3argEm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b90.md) · 呼出先 10件 [`0043bb20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043bb20.md) [`0044fcbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md)
- 新版 呼出元 1件 [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c60.md) · 呼出先 10件 [`0043bb60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043bb60.md) [`0044fcfc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      212,
      "PARAM",
      [
        "storage",
        "002bc505",
        null,
        "string"
      ]
    ],
    [
      256,
      "PARAM",
      [
        "storage",
        "002b3a51",
        null,
        "string"
      ]
    ],
    [
      312,
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
      212,
      "PARAM",
      [
        "storage",
        "002bc4b1",
        null,
        "string"
      ]
    ],
    [
      256,
      "PARAM",
      [
        "storage",
        "002b3a82",
        null,
        "string"
      ]
    ],
    [
      312,
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


~~~diff
- 004b4b74 ["INT_ADD", "register:40f0:8", ["const:4b4b74:8", "const:4:8"]]
+ 004b4bb4 ["INT_ADD", "register:40f0:8", ["const:4b4bb4:8", "const:4:8"]]
- 004b4b84 ["INT_ADD", "register:40f0:8", ["const:4b4b84:8", "const:4:8"]]
+ 004b4bc4 ["INT_ADD", "register:40f0:8", ["const:4b4bc4:8", "const:4:8"]]
- 004b4b8c ["COPY", "tmp:0:8", ["const:505:8"]]
+ 004b4bcc ["COPY", "tmp:0:8", ["const:4b1:8"]]
~~~


### [`004b5358`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5358.md) → [`004b5398`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5398.md) _ZN5BotaneqERKNS_11OctetStringES2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bb0.md) · 呼出先 5件 [`005402a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58050`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58050.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0112a/0112a058.md)
- 新版 呼出元 1件 [`00c58c80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c80.md) · 呼出先 5件 [`005402e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58120.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md) [`0112a058`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0112a/0112a058.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      168,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      212,
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
      168,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      212,
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


~~~diff
- 004b5394 ["INT_ADD", "register:40f0:8", ["const:4b5394:8", "const:4:8"]]
+ 004b53d4 ["INT_ADD", "register:40f0:8", ["const:4b53d4:8", "const:4:8"]]
- 004b53ac ["INT_ADD", "register:40f0:8", ["const:4b53ac:8", "const:4:8"]]
+ 004b53ec ["INT_ADD", "register:40f0:8", ["const:4b53ec:8", "const:4:8"]]
- 004b53d0 ["INT_ADD", "register:40f0:8", ["const:4b53d0:8", "const:4:8"]]
+ 004b5410 ["INT_ADD", "register:40f0:8", ["const:4b5410:8", "const:4:8"]]
~~~


### [`004b54c0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b54c0.md) → [`004b5500`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5500.md) _ZN5BotanplERKNS_11OctetStringES2_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`005402a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005402a4.md) [`005404ec`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/005404ec.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 6件 [`005402e4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/005402e4.md) [`0054052c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/0054052c.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      176,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      392,
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
      176,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      392,
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


~~~diff
- 004b5508 ["INT_ADD", "register:40f0:8", ["const:4b5508:8", "const:4:8"]]
+ 004b5548 ["INT_ADD", "register:40f0:8", ["const:4b5548:8", "const:4:8"]]
- 004b5530 ["INT_ADD", "register:40f0:8", ["const:4b5530:8", "const:4:8"]]
+ 004b5570 ["INT_ADD", "register:40f0:8", ["const:4b5570:8", "const:4:8"]]
- 004b5558 ["INT_ADD", "register:40f0:8", ["const:4b5558:8", "const:4:8"]]
+ 004b5598 ["INT_ADD", "register:40f0:8", ["const:4b5598:8", "const:4:8"]]
~~~


### [`004b5a68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5a68.md) → [`004b5aa8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5aa8.md) _ZN5Botan13base64_encodeEPKhm

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bd0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bd0.md) · 呼出先 6件 [`0043b764`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043b/0043b764.md) [`00c57e90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57e90.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c58090`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58090.md) [`00c58650`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58650.md)
- 新版 呼出元 1件 [`00c58ca0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ca0.md) · 呼出先 6件 [`0043b7a4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043b/0043b7a4.md) [`00c57f60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57f60.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c58160`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58160.md) [`00c58720`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58720.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      368,
      "PARAM",
      [
        "storage",
        "002b8171",
        null,
        "string"
      ]
    ],
    [
      380,
      "PARAM",
      [
        "storage",
        "002a9b72",
        null,
        "string"
      ]
    ],
    [
      392,
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
      368,
      "PARAM",
      [
        "storage",
        "002b81b1",
        null,
        "string"
      ]
    ],
    [
      380,
      "PARAM",
      [
        "storage",
        "002a9ba1",
        null,
        "string"
      ]
    ],
    [
      392,
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


~~~diff
- 004b5b18 ["INT_ADD", "register:40f0:8", ["const:4b5b18:8", "const:4:8"]]
+ 004b5b58 ["INT_ADD", "register:40f0:8", ["const:4b5b58:8", "const:4:8"]]
- 004b5b38 ["INT_ADD", "register:40f0:8", ["const:4b5b38:8", "const:4:8"]]
+ 004b5b78 ["INT_ADD", "register:40f0:8", ["const:4b5b78:8", "const:4:8"]]
- 004b5b64 ["INT_ADD", "register:40f0:8", ["const:4b5b64:8", "const:4:8"]]
+ 004b5ba4 ["INT_ADD", "register:40f0:8", ["const:4b5ba4:8", "const:4:8"]]
~~~


### [`004b5c88`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b5/004b5c88.md) → [`004b5cc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b5/004b5cc8.md) _ZN5Botan13base64_decodeEPhPKcmRmbb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58be0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58be0.md) · 呼出先 11件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00441e94`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00441/00441e94.md) [`0044fcbc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0044f/0044fcbc.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md)
- 新版 呼出元 1件 [`00c58cb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cb0.md) · 呼出先 11件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`00441ed4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00441/00441ed4.md) [`0044fcfc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0044f/0044fcfc.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      248,
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "002cad1c",
        null,
        null
      ]
    ],
    [
      476,
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
      248,
      "DATA",
      [
        "storage",
        "002cad5c",
        null,
        null
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "002cad5c",
        null,
        null
      ]
    ],
    [
      476,
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


~~~diff
- 004b5ce8 ["INT_ADD", "register:40f0:8", ["const:4b5ce8:8", "const:4:8"]]
+ 004b5d28 ["INT_ADD", "register:40f0:8", ["const:4b5d28:8", "const:4:8"]]
- 004b5d08 ["COPY", "tmp:0:8", ["const:d1c:8"]]
+ 004b5d48 ["COPY", "tmp:0:8", ["const:d5c:8"]]
- 004b5d28 ["INT_ADD", "register:40f0:8", ["const:4b5d28:8", "const:4:8"]]
+ 004b5d68 ["INT_ADD", "register:40f0:8", ["const:4b5d68:8", "const:4:8"]]
~~~


### [`004b6028`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6028.md) → [`004b6068`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6068.md) _ZN5Botan13base64_decodeEPhPKcmb

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58bf0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58bf0.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58cc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58cc0.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "PARAM",
      [
        "storage",
        "002a8bf3",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      184,
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
      124,
      "PARAM",
      [
        "storage",
        "002a8b97",
        null,
        "string"
      ]
    ],
    [
      180,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      184,
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


~~~diff
- 004b605c ["INT_ADD", "register:40f0:8", ["const:4b605c:8", "const:4:8"]]
+ 004b609c ["INT_ADD", "register:40f0:8", ["const:4b609c:8", "const:4:8"]]
- 004b6098 ["INT_ADD", "register:40f0:8", ["const:4b6098:8", "const:4:8"]]
+ 004b60d8 ["INT_ADD", "register:40f0:8", ["const:4b60d8:8", "const:4:8"]]
- 004b60a4 ["COPY", "tmp:0:8", ["const:bf3:8"]]
+ 004b60e4 ["COPY", "tmp:0:8", ["const:b97:8"]]
~~~


### [`004b63cc`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b63cc.md) → [`004b640c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b640c.md) _ZNK5Botan6BigInt12encoded_sizeENS0_4BaseE

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58940`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58940.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58a10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58a10.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      416,
      "READ",
      [
        "storage",
        "002c4288",
        null,
        "undefined8"
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002b5fa3",
        null,
        "string"
      ]
    ],
    [
      608,
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
      416,
      "READ",
      [
        "storage",
        "002c42c8",
        null,
        "undefined8"
      ]
    ],
    [
      552,
      "PARAM",
      [
        "storage",
        "002b5fe3",
        null,
        "string"
      ]
    ],
    [
      608,
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


~~~diff
- 004b656c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:288:8"]]
+ 004b65ac ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2c8:8"]]
- 004b65e8 ["INT_ADD", "register:40f0:8", ["const:4b65e8:8", "const:4:8"]]
+ 004b6628 ["INT_ADD", "register:40f0:8", ["const:4b6628:8", "const:4:8"]]
- 004b65f4 ["COPY", "tmp:0:8", ["const:fa3:8"]]
+ 004b6634 ["COPY", "tmp:0:8", ["const:fe3:8"]]
~~~


### [`004b6728`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b6/004b6728.md) → [`004b6768`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b6/004b6768.md) _ZN5Botan6divideERKNS_6BigIntES2_RS0_S3_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b50.md) · 呼出先 21件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`004bb8c4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bb8c4.md) [`004bbb6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004bb/004bbb6c.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00540920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58c20`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c20.md) · 呼出先 21件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`004bb904`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bb904.md) [`004bbbac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bb/004bbbac.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00540960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      184,
      "READ",
      [
        "storage",
        "00c9ae00",
        null,
        "pointer"
      ]
    ],
    [
      208,
      "DATA",
      [
        "storage",
        "00c69c60",
        null,
        "undefined1[40]"
      ]
    ],
    [
      236,
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
      184,
      "READ",
      [
        "storage",
        "00c9aed0",
        null,
        "pointer"
      ]
    ],
    [
      208,
      "DATA",
      [
        "storage",
        "00c69d30",
        null,
        "undefined1[40]"
      ]
    ],
    [
      236,
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


~~~diff
- 004b67a8 ["INT_ADD", "register:40f0:8", ["const:4b67a8:8", "const:4:8"]]
+ 004b67e8 ["INT_ADD", "register:40f0:8", ["const:4b67e8:8", "const:4:8"]]
- 004b67e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
+ 004b6820 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ed0:8"]]
- 004b6814 ["COPY", "register:4010:8", ["const:535868:8"]]
- 004b6818 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e08:8"]]
+ 004b6854 ["COPY", "register:4010:8", ["const:5358a8:8"]]
+ 004b6858 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed8:8"]]
~~~


### [`004b7318`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7318.md) → [`004b7358`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7358.md) _ZN5Botan7Charset10digit2charEh

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58b60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58b60.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58c30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58c30.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002a41d2",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      164,
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
      104,
      "PARAM",
      [
        "storage",
        "002a4185",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      164,
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


~~~diff
- 004b7374 ["INT_ADD", "register:40f0:8", ["const:4b7374:8", "const:4:8"]]
+ 004b73b4 ["INT_ADD", "register:40f0:8", ["const:4b73b4:8", "const:4:8"]]
- 004b7380 ["COPY", "tmp:0:8", ["const:1d2:8"]]
+ 004b73c0 ["COPY", "tmp:0:8", ["const:185:8"]]
- 004b7388 ["INT_ADD", "register:40f0:8", ["const:4b7388:8", "const:4:8"]]
+ 004b73c8 ["INT_ADD", "register:40f0:8", ["const:4b73c8:8", "const:4:8"]]
~~~


### [`004b750c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b750c.md) → [`004b754c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b754c.md) _ZN5Botan6BigInt11encode_1363EPhmRKS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58c60`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58c60.md) · 呼出先 7件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58d30`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58d30.md) · 呼出先 7件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      252,
      "PARAM",
      [
        "storage",
        "002b5f74",
        null,
        "string"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      312,
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
      252,
      "PARAM",
      [
        "storage",
        "002b5fb4",
        null,
        "string"
      ]
    ],
    [
      308,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      312,
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


~~~diff
- 004b75fc ["INT_ADD", "register:40f0:8", ["const:4b75fc:8", "const:4:8"]]
+ 004b763c ["INT_ADD", "register:40f0:8", ["const:4b763c:8", "const:4:8"]]
- 004b7608 ["COPY", "tmp:0:8", ["const:f74:8"]]
+ 004b7648 ["COPY", "tmp:0:8", ["const:fb4:8"]]
- 004b7610 ["INT_ADD", "register:40f0:8", ["const:4b7610:8", "const:4:8"]]
+ 004b7650 ["INT_ADD", "register:40f0:8", ["const:4b7650:8", "const:4:8"]]
~~~


### [`004b7b0c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7b0c.md) → [`004b7b4c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7b4c.md) _ZN5Botan7Charset10char2digitEc

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ab0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ab0.md) · 呼出先 6件 [`0043ddd8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/0043d/0043ddd8.md) [`00535868`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00535/00535868.md) [`00c57ee0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ee0.md) [`00c57ef0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57ef0.md) [`00c57f10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f10.md)
- 新版 呼出元 1件 [`00c58b80`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b80.md) · 呼出先 6件 [`0043de18`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/0043d/0043de18.md) [`005358a8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00535/005358a8.md) [`00c57fb0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fb0.md) [`00c57fc0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fc0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c57/00c57fe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "PARAM",
      [
        "storage",
        "002bb407",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "00535868",
        null,
        null
      ]
    ],
    [
      164,
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
      104,
      "PARAM",
      [
        "storage",
        "002bb3b3",
        null,
        "string"
      ]
    ],
    [
      160,
      "PARAM",
      [
        "storage",
        "005358a8",
        null,
        null
      ]
    ],
    [
      164,
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


~~~diff
- 004b7b68 ["INT_ADD", "register:40f0:8", ["const:4b7b68:8", "const:4:8"]]
+ 004b7ba8 ["INT_ADD", "register:40f0:8", ["const:4b7ba8:8", "const:4:8"]]
- 004b7b74 ["COPY", "tmp:0:8", ["const:407:8"]]
+ 004b7bb4 ["COPY", "tmp:0:8", ["const:3b3:8"]]
- 004b7b7c ["INT_ADD", "register:40f0:8", ["const:4b7b7c:8", "const:4:8"]]
+ 004b7bbc ["INT_ADD", "register:40f0:8", ["const:4b7bbc:8", "const:4:8"]]
~~~


### [`004b7c10`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7c10.md) → [`004b7c50`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b7/004b7c50.md) _ZN5Botan6BigIntmLERKS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ac0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ac0.md) · 呼出先 10件 [`004b8850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b90e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b90e0.md) [`004b91e0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b9/004b91e0.md) [`004d6e68`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6e68.md) [`00540920`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00540/00540920.md)
- 新版 呼出元 1件 [`00c58b90`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58b90.md) · 呼出先 10件 [`004b8890`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`004b9120`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9120.md) [`004b9220`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b9/004b9220.md) [`004d6ea8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6ea8.md) [`00540960`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00540/00540960.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      776,
      "READ",
      [
        "storage",
        "00c67738",
        null,
        "pointer"
      ]
    ],
    [
      820,
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
      776,
      "READ",
      [
        "storage",
        "00c67808",
        null,
        "pointer"
      ]
    ],
    [
      820,
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


~~~diff
- 004b7d44 ["INT_ADD", "register:40f0:8", ["const:4b7d44:8", "const:4:8"]]
+ 004b7d84 ["INT_ADD", "register:40f0:8", ["const:4b7d84:8", "const:4:8"]]
- 004b7d68 ["INT_ADD", "register:40f0:8", ["const:4b7d68:8", "const:4:8"]]
+ 004b7da8 ["INT_ADD", "register:40f0:8", ["const:4b7da8:8", "const:4:8"]]
- 004b7db8 ["INT_ADD", "register:40f0:8", ["const:4b7db8:8", "const:4:8"]]
+ 004b7df8 ["INT_ADD", "register:40f0:8", ["const:4b7df8:8", "const:4:8"]]
~~~


### [`004b7fc8`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b7/004b7fc8.md) → [`004b8008`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8008.md) _ZN5Botan6BigIntpLERKS0_

根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c58ad0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58ad0.md) · 呼出先 10件 [`004b87b4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b87b4.md) [`004b8850`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8850.md) [`004b894c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b894c.md) [`004b8b6c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004b8/004b8b6c.md) [`004d6bc4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004d6/004d6bc4.md)
- 新版 呼出元 1件 [`00c58ba0`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58ba0.md) · 呼出先 10件 [`004b87f4`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b87f4.md) [`004b8890`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8890.md) [`004b898c`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b898c.md) [`004b8bac`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004b8/004b8bac.md) [`004d6c04`](https://github.com/sinsuirakv0/KBCS/blob/191e2390e39dc910c4526a9fce126ed9f91e3a21/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004d6/004d6c04.md)

変更の種類 call_target, constant, operands_and_dependencies

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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      532,
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
      532,
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


~~~diff
- 004b8084 ["INT_ADD", "register:40f0:8", ["const:4b8084:8", "const:4:8"]]
+ 004b80c4 ["INT_ADD", "register:40f0:8", ["const:4b80c4:8", "const:4:8"]]
- 004b80c0 ["INT_ADD", "register:40f0:8", ["const:4b80c0:8", "const:4:8"]]
+ 004b8100 ["INT_ADD", "register:40f0:8", ["const:4b8100:8", "const:4:8"]]
- 004b80e8 ["INT_ADD", "register:40f0:8", ["const:4b80e8:8", "const:4:8"]]
+ 004b8128 ["INT_ADD", "register:40f0:8", ["const:4b8128:8", "const:4:8"]]
~~~


