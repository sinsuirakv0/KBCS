# v16.0.1 → v16.0.2 · 最優先の変更候補 (99)

[一覧の目次](README.md)

### [`00c3cd40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cd40.md) → [`00c3cddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cddc.md) FUN_00c3cddc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ce40",
      "incomplete_value": false,
      "site": "00c3ce40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cda4",
      "incomplete_value": false,
      "site": "00c3cda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99690",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99760",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3cd74 ["INT_ADD", "register:40f0:8", ["const:c3cd74:8", "const:4:8"]]
+ 00c3ce10 ["INT_ADD", "register:40f0:8", ["const:c3ce10:8", "const:4:8"]]
- 00c3cd98 ["COPY", "tmp:0:8", ["const:690:8"]]
+ 00c3ce34 ["COPY", "tmp:0:8", ["const:760:8"]]
- 00c3cddc ["INT_ADD", "register:40f0:8", ["const:c3cddc:8", "const:4:8"]]
+ 00c3ce78 ["INT_ADD", "register:40f0:8", ["const:c3ce78:8", "const:4:8"]]
~~~


### [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) → [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) FUN_00c3ce7c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 10件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c3cf98",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cefc",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:ee2:8"
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
      "definition_site": "00c3cfa0",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
            "const:8c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cf04",
      "incomplete_value": false,
      "site": "00c3cf14",
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
            "const:896:8"
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
      "definition_site": "00c3cfa8",
      "incomplete_value": false,
      "site": "00c3cfb0",
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
      "definition_site": "00c3cf0c",
      "incomplete_value": false,
      "site": "00c3cf14",
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
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      284,
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      292,
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
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
      284,
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      292,
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
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
- 00c3ce4c ["INT_ADD", "register:40f0:8", ["const:c3ce4c:8", "const:4:8"]]
+ 00c3cee8 ["INT_ADD", "register:40f0:8", ["const:c3cee8:8", "const:4:8"]]
- 00c3ce74 ["INT_ADD", "register:40f0:8", ["const:c3ce74:8", "const:4:8"]]
+ 00c3cf10 ["INT_ADD", "register:40f0:8", ["const:c3cf10:8", "const:4:8"]]
- 00c3ceb0 ["INT_ADD", "register:40f0:8", ["const:c3ceb0:8", "const:4:8"]]
+ 00c3cf4c ["INT_ADD", "register:40f0:8", ["const:c3cf4c:8", "const:4:8"]]
~~~


### [`00c3cf3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cf3c.md) → [`00c3cfd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cfd8.md) FUN_00c3cfd8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d060",
      "incomplete_value": false,
      "site": "00c3d060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3cfc4",
      "incomplete_value": false,
      "site": "00c3cfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:770:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      136,
      "DATA",
      [
        "storage",
        "00c99770",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      136,
      "DATA",
      [
        "storage",
        "00c99840",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3cf94 ["INT_ADD", "register:40f0:8", ["const:c3cf94:8", "const:4:8"]]
+ 00c3d030 ["INT_ADD", "register:40f0:8", ["const:c3d030:8", "const:4:8"]]
- 00c3cfb8 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00c3d054 ["COPY", "tmp:0:8", ["const:840:8"]]
- 00c3d02c ["INT_ADD", "register:40f0:8", ["const:c3d02c:8", "const:4:8"]]
+ 00c3d0c8 ["INT_ADD", "register:40f0:8", ["const:c3d0c8:8", "const:4:8"]]
~~~


### [`00c3d210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d210.md) → [`00c3d2ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d2ac.md) FUN_00c3d2ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d310",
      "incomplete_value": false,
      "site": "00c3d310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d274",
      "incomplete_value": false,
      "site": "00c3d274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d334",
      "incomplete_value": false,
      "site": "00c3d334",
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
            "const:e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d298",
      "incomplete_value": false,
      "site": "00c3d298",
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
            "const:13d:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002bb13d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002bb0e9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d244 ["INT_ADD", "register:40f0:8", ["const:c3d244:8", "const:4:8"]]
+ 00c3d2e0 ["INT_ADD", "register:40f0:8", ["const:c3d2e0:8", "const:4:8"]]
- 00c3d268 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d304 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d290 ["COPY", "tmp:0:8", ["const:13d:8"]]
+ 00c3d32c ["COPY", "tmp:0:8", ["const:e9:8"]]
~~~


### [`00c3d2c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d2c0.md) → [`00c3d35c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d35c.md) FUN_00c3d35c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d3c0",
      "incomplete_value": false,
      "site": "00c3d3c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d324",
      "incomplete_value": false,
      "site": "00c3d324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d3e4",
      "incomplete_value": false,
      "site": "00c3d3e4",
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
            "const:875:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d348",
      "incomplete_value": false,
      "site": "00c3d348",
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
            "const:8d1:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b18d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b1875",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d2f4 ["INT_ADD", "register:40f0:8", ["const:c3d2f4:8", "const:4:8"]]
+ 00c3d390 ["INT_ADD", "register:40f0:8", ["const:c3d390:8", "const:4:8"]]
- 00c3d318 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d3b4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d340 ["COPY", "tmp:0:8", ["const:8d1:8"]]
+ 00c3d3dc ["COPY", "tmp:0:8", ["const:875:8"]]
~~~


### [`00c3d370`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d370.md) → [`00c3d40c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d40c.md) FUN_00c3d40c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d470",
      "incomplete_value": false,
      "site": "00c3d470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3d4",
      "incomplete_value": false,
      "site": "00c3d3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d494",
      "incomplete_value": false,
      "site": "00c3d494",
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
            "const:e1e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d3f8",
      "incomplete_value": false,
      "site": "00c3d3f8",
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
            "const:e6b:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "0029fe6b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "0029fe1e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d3a4 ["INT_ADD", "register:40f0:8", ["const:c3d3a4:8", "const:4:8"]]
+ 00c3d440 ["INT_ADD", "register:40f0:8", ["const:c3d440:8", "const:4:8"]]
- 00c3d3c8 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d464 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d3f0 ["COPY", "tmp:0:8", ["const:e6b:8"]]
+ 00c3d48c ["COPY", "tmp:0:8", ["const:e1e:8"]]
~~~


### [`00c3d420`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d420.md) → [`00c3d4bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d4bc.md) FUN_00c3d4bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d520",
      "incomplete_value": false,
      "site": "00c3d520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d484",
      "incomplete_value": false,
      "site": "00c3d484",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d544",
      "incomplete_value": false,
      "site": "00c3d544",
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
            "const:8b9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d4a8",
      "incomplete_value": false,
      "site": "00c3d4a8",
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
            "const:888:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b2888",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b28b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d454 ["INT_ADD", "register:40f0:8", ["const:c3d454:8", "const:4:8"]]
+ 00c3d4f0 ["INT_ADD", "register:40f0:8", ["const:c3d4f0:8", "const:4:8"]]
- 00c3d478 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d514 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d4a0 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00c3d53c ["COPY", "tmp:0:8", ["const:8b9:8"]]
~~~


### [`00c3d4d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d4d0.md) → [`00c3d56c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d56c.md) FUN_00c3d56c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d5d0",
      "incomplete_value": false,
      "site": "00c3d5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d534",
      "incomplete_value": false,
      "site": "00c3d534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d5f4",
      "incomplete_value": false,
      "site": "00c3d5f4",
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
            "const:9db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d558",
      "incomplete_value": false,
      "site": "00c3d558",
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
            "const:9ac:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a99ac",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a99db",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d504 ["INT_ADD", "register:40f0:8", ["const:c3d504:8", "const:4:8"]]
+ 00c3d5a0 ["INT_ADD", "register:40f0:8", ["const:c3d5a0:8", "const:4:8"]]
- 00c3d528 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d5c4 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d550 ["COPY", "tmp:0:8", ["const:9ac:8"]]
+ 00c3d5ec ["COPY", "tmp:0:8", ["const:9db:8"]]
~~~


### [`00c3d730`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d730.md) → [`00c3d7cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d7cc.md) FUN_00c3d7cc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d830",
      "incomplete_value": false,
      "site": "00c3d830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d794",
      "incomplete_value": false,
      "site": "00c3d794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d854",
      "incomplete_value": false,
      "site": "00c3d854",
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
            "const:e21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d7b8",
      "incomplete_value": false,
      "site": "00c3d7b8",
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
            "const:e75:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b9e75",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b9e21",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d764 ["INT_ADD", "register:40f0:8", ["const:c3d764:8", "const:4:8"]]
+ 00c3d800 ["INT_ADD", "register:40f0:8", ["const:c3d800:8", "const:4:8"]]
- 00c3d788 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d824 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d7b0 ["COPY", "tmp:0:8", ["const:e75:8"]]
+ 00c3d84c ["COPY", "tmp:0:8", ["const:e21:8"]]
~~~


### [`00c3d7e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d7e0.md) → [`00c3d87c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d87c.md) FUN_00c3d87c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d8e4",
      "incomplete_value": false,
      "site": "00c3d8e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d848",
      "incomplete_value": false,
      "site": "00c3d848",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c975d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c976a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d818 ["INT_ADD", "register:40f0:8", ["const:c3d818:8", "const:4:8"]]
+ 00c3d8b4 ["INT_ADD", "register:40f0:8", ["const:c3d8b4:8", "const:4:8"]]
- 00c3d83c ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00c3d8d8 ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 00c3d884 ["INT_ADD", "register:40f0:8", ["const:c3d884:8", "const:4:8"]]
+ 00c3d920 ["INT_ADD", "register:40f0:8", ["const:c3d920:8", "const:4:8"]]
~~~


### [`00c3d888`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d888.md) → [`00c3d924`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d924.md) FUN_00c3d924

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d988",
      "incomplete_value": false,
      "site": "00c3d988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d8ec",
      "incomplete_value": false,
      "site": "00c3d8ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3d9ac",
      "incomplete_value": false,
      "site": "00c3d9ac",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d910",
      "incomplete_value": false,
      "site": "00c3d910",
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
            "const:8e5:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b08e5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002b0889",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d8bc ["INT_ADD", "register:40f0:8", ["const:c3d8bc:8", "const:4:8"]]
+ 00c3d958 ["INT_ADD", "register:40f0:8", ["const:c3d958:8", "const:4:8"]]
- 00c3d8e0 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3d97c ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d908 ["COPY", "tmp:0:8", ["const:8e5:8"]]
+ 00c3d9a4 ["COPY", "tmp:0:8", ["const:889:8"]]
~~~


### [`00c3d938`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d938.md) → [`00c3d9d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3d9d4.md) FUN_00c3d9d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3da38",
      "incomplete_value": false,
      "site": "00c3da38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d99c",
      "incomplete_value": false,
      "site": "00c3d99c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3da5c",
      "incomplete_value": false,
      "site": "00c3da5c",
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
            "const:e54:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3d9c0",
      "incomplete_value": false,
      "site": "00c3d9c0",
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
            "const:e14:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c0e14",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c0e54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3d96c ["INT_ADD", "register:40f0:8", ["const:c3d96c:8", "const:4:8"]]
+ 00c3da08 ["INT_ADD", "register:40f0:8", ["const:c3da08:8", "const:4:8"]]
- 00c3d990 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3da2c ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3d9b8 ["COPY", "tmp:0:8", ["const:e14:8"]]
+ 00c3da54 ["COPY", "tmp:0:8", ["const:e54:8"]]
~~~


### [`00c3d9e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3d9e8.md) → [`00c3da84`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3da84.md) FUN_00c3da84

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3dae8",
      "incomplete_value": false,
      "site": "00c3dae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da4c",
      "incomplete_value": false,
      "site": "00c3da4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3db0c",
      "incomplete_value": false,
      "site": "00c3db0c",
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
            "const:93f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3da70",
      "incomplete_value": false,
      "site": "00c3da70",
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
            "const:99b:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a899b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002a893f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3da1c ["INT_ADD", "register:40f0:8", ["const:c3da1c:8", "const:4:8"]]
+ 00c3dab8 ["INT_ADD", "register:40f0:8", ["const:c3dab8:8", "const:4:8"]]
- 00c3da40 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3dadc ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3da60 ["COPY", "tmp:0:8", ["const:99b:8"]]
+ 00c3dafc ["COPY", "tmp:0:8", ["const:93f:8"]]
~~~


### [`00c3da94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3da94.md) → [`00c3db30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3db30.md) FUN_00c3db30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3db94",
      "incomplete_value": false,
      "site": "00c3db94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:620:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3daf8",
      "incomplete_value": false,
      "site": "00c3daf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:550:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3dbb8",
      "incomplete_value": false,
      "site": "00c3dbb8",
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
            "const:fe6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3db1c",
      "incomplete_value": false,
      "site": "00c3db1c",
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
            "const:fa6:8"
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
      100,
      "DATA",
      [
        "storage",
        "00c97550",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c1fa6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97620",
        null,
        "undefined *"
      ]
    ],
    [
      136,
      "DATA",
      [
        "storage",
        "002c1fe6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3dac8 ["INT_ADD", "register:40f0:8", ["const:c3dac8:8", "const:4:8"]]
+ 00c3db64 ["INT_ADD", "register:40f0:8", ["const:c3db64:8", "const:4:8"]]
- 00c3daec ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00c3db88 ["COPY", "tmp:0:8", ["const:620:8"]]
- 00c3db14 ["COPY", "tmp:0:8", ["const:fa6:8"]]
+ 00c3dbb0 ["COPY", "tmp:0:8", ["const:fe6:8"]]
~~~


### [`00c3de30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3de30.md) → [`00c3decc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3decc.md) FUN_00c3decc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3df34",
      "incomplete_value": true,
      "site": "00c3df40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:108:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3de98",
      "incomplete_value": true,
      "site": "00c3dea4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:15c:8"
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
      "definition_site": "00c3df38",
      "incomplete_value": true,
      "site": "00c3df44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00c3de9c",
      "incomplete_value": true,
      "site": "00c3dea8",
      "value": [
        "LOAD",
        "8",
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
      104,
      "READ",
      [
        "storage",
        "002bb15c",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002bb16c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "READ",
      [
        "storage",
        "002bb108",
        null,
        "string"
      ]
    ],
    [
      108,
      "READ",
      [
        "storage",
        "002bb118",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3de78 ["INT_ADD", "register:40f0:8", ["const:c3de78:8", "const:4:8"]]
+ 00c3df14 ["INT_ADD", "register:40f0:8", ["const:c3df14:8", "const:4:8"]]
- 00c3de90 ["COPY", "tmp:0:8", ["const:15c:8"]]
+ 00c3df2c ["COPY", "tmp:0:8", ["const:108:8"]]
- 00c3dec8 ["INT_ADD", "register:40f0:8", ["const:c3dec8:8", "const:4:8"]]
+ 00c3df64 ["INT_ADD", "register:40f0:8", ["const:c3df64:8", "const:4:8"]]
~~~


### [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) → [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) FUN_00c3e04c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00c3db44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c4366c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 7件 [`00c3dbe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e16c",
      "incomplete_value": false,
      "site": "00c3e16c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e0d0",
      "incomplete_value": false,
      "site": "00c3e0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      288,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002af764",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      288,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002af708",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e0a0 ["INT_ADD", "register:40f0:8", ["const:c3e0a0:8", "const:4:8"]]
+ 00c3e13c ["INT_ADD", "register:40f0:8", ["const:c3e13c:8", "const:4:8"]]
- 00c3e0c4 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e160 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3e128 ["INT_ADD", "register:40f0:8", ["const:c3e128:8", "const:4:8"]]
+ 00c3e1c4 ["INT_ADD", "register:40f0:8", ["const:c3e1c4:8", "const:4:8"]]
~~~


### [`00c3e1dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e1dc.md) → [`00c3e278`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e278.md) FUN_00c3e278

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e2dc",
      "incomplete_value": false,
      "site": "00c3e2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e240",
      "incomplete_value": false,
      "site": "00c3e240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e210 ["INT_ADD", "register:40f0:8", ["const:c3e210:8", "const:4:8"]]
+ 00c3e2ac ["INT_ADD", "register:40f0:8", ["const:c3e2ac:8", "const:4:8"]]
- 00c3e234 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e2d0 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3e278 ["INT_ADD", "register:40f0:8", ["const:c3e278:8", "const:4:8"]]
+ 00c3e314 ["INT_ADD", "register:40f0:8", ["const:c3e314:8", "const:4:8"]]
~~~


### [`00c3e454`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) → [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) FUN_00c3e4f0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 4件 [`00c3f034`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 4件 [`00c3f0d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3e5f4",
      "incomplete_value": false,
      "site": "00c3e600",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3e558",
      "incomplete_value": false,
      "site": "00c3e564",
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
            "const:d84:8"
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
      232,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b8d84",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      232,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      272,
      "DATA",
      [
        "storage",
        "002b8d30",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e4ac ["INT_ADD", "register:40f0:8", ["const:c3e4ac:8", "const:4:8"]]
+ 00c3e548 ["INT_ADD", "register:40f0:8", ["const:c3e548:8", "const:4:8"]]
- 00c3e4fc ["INT_ADD", "register:40f0:8", ["const:c3e4fc:8", "const:4:8"]]
+ 00c3e598 ["INT_ADD", "register:40f0:8", ["const:c3e598:8", "const:4:8"]]
- 00c3e530 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3e5cc ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) → [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) FUN_00c3e660

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4366c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) [`00c4b7ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) [`00c4e5e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 8件 [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 8件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eae0",
      "incomplete_value": false,
      "site": "00c3eae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3ea44",
      "incomplete_value": false,
      "site": "00c3ea44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      532,
      "DATA",
      [
        "storage",
        "00c99460",
        null,
        "undefined *"
      ]
    ],
    [
      1152,
      "DATA",
      [
        "storage",
        "00c994d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      532,
      "DATA",
      [
        "storage",
        "00c99530",
        null,
        "undefined *"
      ]
    ],
    [
      1152,
      "DATA",
      [
        "storage",
        "00c995a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3e638 ["INT_ADD", "register:40f0:8", ["const:c3e638:8", "const:4:8"]]
+ 00c3e6d4 ["INT_ADD", "register:40f0:8", ["const:c3e6d4:8", "const:4:8"]]
- 00c3e644 ["INT_ADD", "register:40f0:8", ["const:c3e644:8", "const:4:8"]]
+ 00c3e6e0 ["INT_ADD", "register:40f0:8", ["const:c3e6e0:8", "const:4:8"]]
- 00c3e64c ["INT_ADD", "register:40f0:8", ["const:c3e64c:8", "const:4:8"]]
+ 00c3e6e8 ["INT_ADD", "register:40f0:8", ["const:c3e6e8:8", "const:4:8"]]
~~~


### [`00c3ea94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) → [`00c3eb30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) FUN_00c3eb30

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4366c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3eb98",
      "incomplete_value": false,
      "site": "00c3eb98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eafc",
      "incomplete_value": false,
      "site": "00c3eafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3eacc ["INT_ADD", "register:40f0:8", ["const:c3eacc:8", "const:4:8"]]
+ 00c3eb68 ["INT_ADD", "register:40f0:8", ["const:c3eb68:8", "const:4:8"]]
- 00c3eaf0 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00c3eb8c ["COPY", "tmp:0:8", ["const:610:8"]]
- 00c3eb38 ["INT_ADD", "register:40f0:8", ["const:c3eb38:8", "const:4:8"]]
+ 00c3ebd4 ["INT_ADD", "register:40f0:8", ["const:c3ebd4:8", "const:4:8"]]
~~~


### [`00c3eb3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) → [`00c3ebd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) FUN_00c3ebd8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4b628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 7件 [`00c3f970`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f970.md) [`00c3fa48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 4件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 7件 [`00c3fa0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fa0c.md) [`00c3fae4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3ee44",
      "incomplete_value": false,
      "site": "00c3ee44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3eda8",
      "incomplete_value": false,
      "site": "00c3eda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      340,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00c97720",
        null,
        "undefined *"
      ]
    ],
    [
      844,
      "PARAM",
      [
        "storage",
        "002a1d99",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      340,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      620,
      "DATA",
      [
        "storage",
        "00c977f0",
        null,
        "undefined *"
      ]
    ],
    [
      844,
      "PARAM",
      [
        "storage",
        "002a1d4c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3ec60 ["INT_ADD", "register:40f0:8", ["const:c3ec60:8", "const:4:8"]]
+ 00c3ecfc ["INT_ADD", "register:40f0:8", ["const:c3ecfc:8", "const:4:8"]]
- 00c3ec84 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3ed20 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3ed70 ["INT_ADD", "register:40f0:8", ["const:c3ed70:8", "const:4:8"]]
+ 00c3ee0c ["INT_ADD", "register:40f0:8", ["const:c3ee0c:8", "const:4:8"]]
~~~


### [`00c3ef00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) → [`00c3ef9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) FUN_00c3ef9c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c4b628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 3件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 3件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 3件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f078",
      "incomplete_value": false,
      "site": "00c3f078",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3efdc",
      "incomplete_value": false,
      "site": "00c3efdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f098",
      "incomplete_value": false,
      "site": "00c3f098",
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
            "const:530:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3effc",
      "incomplete_value": false,
      "site": "00c3effc",
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
            "const:58c:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      220,
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "002ae58c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      220,
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      252,
      "DATA",
      [
        "storage",
        "002ae530",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3ef60 ["INT_ADD", "register:40f0:8", ["const:c3ef60:8", "const:4:8"]]
+ 00c3effc ["INT_ADD", "register:40f0:8", ["const:c3effc:8", "const:4:8"]]
- 00c3efa8 ["INT_ADD", "register:40f0:8", ["const:c3efa8:8", "const:4:8"]]
+ 00c3f044 ["INT_ADD", "register:40f0:8", ["const:c3f044:8", "const:4:8"]]
- 00c3efd0 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00c3f06c ["COPY", "tmp:0:8", ["const:110:8"]]
~~~


### [`00c3f034`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f034.md) → [`00c3f0d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f0d0.md) FUN_00c3f0d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) [`00c4b628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) · 呼出先 6件 [`00c4c228`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c228.md) [`00c57f40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57f40.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md)
- 新版 呼出元 3件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) · 呼出先 6件 [`00c4c2c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c2c4.md) [`00c58010`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58010.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f2f4",
      "incomplete_value": false,
      "site": "00c3f2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f258",
      "incomplete_value": false,
      "site": "00c3f25c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:70:8"
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
      552,
      "DATA",
      [
        "storage",
        "00c99070",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      552,
      "DATA",
      [
        "storage",
        "00c99140",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f200 ["INT_ADD", "register:40f0:8", ["const:c3f200:8", "const:4:8"]]
+ 00c3f29c ["INT_ADD", "register:40f0:8", ["const:c3f29c:8", "const:4:8"]]
- 00c3f258 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00c3f2f4 ["COPY", "tmp:0:8", ["const:140:8"]]
- 00c3f260 ["INT_ADD", "register:40f0:8", ["const:c3f260:8", "const:4:8"]]
+ 00c3f2fc ["INT_ADD", "register:40f0:8", ["const:c3f2fc:8", "const:4:8"]]
~~~


### [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) → [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) FUN_00c3f3ac

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3e454`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e454.md) · 呼出先 13件 [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3db44`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3db44.md) [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c46520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md)
- 新版 呼出元 2件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3e4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e4f0.md) · 呼出先 13件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3dbe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3d/00c3dbe0.md) [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f5f4",
      "incomplete_value": false,
      "site": "00c3f5f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f558",
      "incomplete_value": false,
      "site": "00c3f558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:2a0:8"
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
      "definition_site": "00c3f85c",
      "incomplete_value": false,
      "site": "00c3f85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f7c0",
      "incomplete_value": false,
      "site": "00c3f7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 58,
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
      "DATA",
      [
        "storage",
        "00c990f8",
        null,
        "undefined *"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00c992a0",
        null,
        "undefined *"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c99380",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      396,
      "DATA",
      [
        "storage",
        "00c991c8",
        null,
        "undefined *"
      ]
    ],
    [
      584,
      "DATA",
      [
        "storage",
        "00c99370",
        null,
        "undefined *"
      ]
    ],
    [
      824,
      "DATA",
      [
        "storage",
        "00c99450",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f344 ["INT_ADD", "register:40f0:8", ["const:c3f344:8", "const:4:8"]]
+ 00c3f3e0 ["INT_ADD", "register:40f0:8", ["const:c3f3e0:8", "const:4:8"]]
- 00c3f3c8 ["INT_ADD", "register:40f0:8", ["const:c3f3c8:8", "const:4:8"]]
+ 00c3f464 ["INT_ADD", "register:40f0:8", ["const:c3f464:8", "const:4:8"]]
- 00c3f3e8 ["INT_ADD", "register:40f0:8", ["const:c3f3e8:8", "const:4:8"]]
+ 00c3f484 ["INT_ADD", "register:40f0:8", ["const:c3f484:8", "const:4:8"]]
~~~


### [`00c3f8d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f8d0.md) → [`00c3f96c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f96c.md) FUN_00c3f96c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3f9d0",
      "incomplete_value": false,
      "site": "00c3f9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3f934",
      "incomplete_value": false,
      "site": "00c3f934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3f904 ["INT_ADD", "register:40f0:8", ["const:c3f904:8", "const:4:8"]]
+ 00c3f9a0 ["INT_ADD", "register:40f0:8", ["const:c3f9a0:8", "const:4:8"]]
- 00c3f928 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3f9c4 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c3f96c ["INT_ADD", "register:40f0:8", ["const:c3f96c:8", "const:4:8"]]
+ 00c3fa08 ["INT_ADD", "register:40f0:8", ["const:c3fa08:8", "const:4:8"]]
~~~


### [`00c3fa48`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fa48.md) → [`00c3fae4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fae4.md) FUN_00c3fae4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3eb3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3eb3c.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ebd8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c3fb50",
      "incomplete_value": false,
      "site": "00c3fb50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c3fab4",
      "incomplete_value": false,
      "site": "00c3fab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3fa7c ["INT_ADD", "register:40f0:8", ["const:c3fa7c:8", "const:4:8"]]
+ 00c3fb18 ["INT_ADD", "register:40f0:8", ["const:c3fb18:8", "const:4:8"]]
- 00c3faa4 ["INT_ADD", "register:40f0:8", ["const:c3faa4:8", "const:4:8"]]
+ 00c3fb40 ["INT_ADD", "register:40f0:8", ["const:c3fb40:8", "const:4:8"]]
- 00c3faac ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c3fb48 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) → [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) FUN_00c3fe18

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 14件 [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ef00`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ef00.md) · 呼出先 42件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3a118`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3cc68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cc68.md)
- 新版 呼出元 14件 [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3ef9c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ef9c.md) · 呼出先 42件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3a1b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3cd04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3cd04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c405ac",
      "incomplete_value": false,
      "site": "00c405ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40510",
      "incomplete_value": false,
      "site": "00c40510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e10:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c409ec",
      "incomplete_value": false,
      "site": "00c409ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40950",
      "incomplete_value": false,
      "site": "00c40950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 105,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41098",
      "incomplete_value": false,
      "site": "00c41098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c40ffc",
      "incomplete_value": false,
      "site": "00c40ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "ordinal": 164,
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
      "READ",
      [
        "storage",
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      212,
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      228,
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      272,
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c3fe30 ["COPY", "register:4040:8", ["const:c97780:8"]]
- 00c3fe34 ["BRANCH", null, ["local:b10:8"]]
- 00c3fe38 ["COPY", "tmp:0:8", ["const:1:8"]]
- 00c3fe38 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
+ 00c3fecc ["COPY", "register:4040:8", ["const:c97850:8"]]
+ 00c3fed0 ["BRANCH", null, ["local:b10:8"]]
+ 00c3fed4 ["COPY", "tmp:0:8", ["const:1:8"]]
+ 00c3fed4 ["INT_CARRY", "register:105:1", ["register:4070:8", "tmp:0:8"]]
~~~


### [`00c4110c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c4110c.md) → [`00c411a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c411a8.md) FUN_00c411a8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41218",
      "incomplete_value": false,
      "site": "00c41218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4117c",
      "incomplete_value": false,
      "site": "00c4117c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c97c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4114c ["INT_ADD", "register:40f0:8", ["const:c4114c:8", "const:4:8"]]
+ 00c411e8 ["INT_ADD", "register:40f0:8", ["const:c411e8:8", "const:4:8"]]
- 00c41170 ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 00c4120c ["COPY", "tmp:0:8", ["const:d20:8"]]
- 00c411c8 ["INT_ADD", "register:40f0:8", ["const:c411c8:8", "const:4:8"]]
+ 00c41264 ["INT_ADD", "register:40f0:8", ["const:c41264:8", "const:4:8"]]
~~~


### [`00c411cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c411cc.md) → [`00c41268`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41268.md) FUN_00c41268

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c412d8",
      "incomplete_value": false,
      "site": "00c412d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4123c",
      "incomplete_value": false,
      "site": "00c4123c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c97cc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97d90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4120c ["INT_ADD", "register:40f0:8", ["const:c4120c:8", "const:4:8"]]
+ 00c412a8 ["INT_ADD", "register:40f0:8", ["const:c412a8:8", "const:4:8"]]
- 00c41230 ["COPY", "tmp:0:8", ["const:cc0:8"]]
+ 00c412cc ["COPY", "tmp:0:8", ["const:d90:8"]]
- 00c41284 ["INT_ADD", "register:40f0:8", ["const:c41284:8", "const:4:8"]]
+ 00c41320 ["INT_ADD", "register:40f0:8", ["const:c41320:8", "const:4:8"]]
~~~


### [`00c41288`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41288.md) → [`00c41324`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41324.md) FUN_00c41324

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41398",
      "incomplete_value": false,
      "site": "00c41398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c412fc",
      "incomplete_value": false,
      "site": "00c412fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:d30:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c97e00",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c412cc ["INT_ADD", "register:40f0:8", ["const:c412cc:8", "const:4:8"]]
+ 00c41368 ["INT_ADD", "register:40f0:8", ["const:c41368:8", "const:4:8"]]
- 00c412f0 ["COPY", "tmp:0:8", ["const:d30:8"]]
+ 00c4138c ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00c41350 ["INT_ADD", "register:40f0:8", ["const:c41350:8", "const:4:8"]]
+ 00c413ec ["INT_ADD", "register:40f0:8", ["const:c413ec:8", "const:4:8"]]
~~~


### [`00c41354`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41354.md) → [`00c413f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c413f0.md) FUN_00c413f0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41470",
      "incomplete_value": false,
      "site": "00c41470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c413d4",
      "incomplete_value": false,
      "site": "00c413d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:da0:8"
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
      128,
      "DATA",
      [
        "storage",
        "00c97da0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      128,
      "DATA",
      [
        "storage",
        "00c97e70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c413a4 ["INT_ADD", "register:40f0:8", ["const:c413a4:8", "const:4:8"]]
+ 00c41440 ["INT_ADD", "register:40f0:8", ["const:c41440:8", "const:4:8"]]
- 00c413c8 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00c41464 ["COPY", "tmp:0:8", ["const:e70:8"]]
- 00c4143c ["INT_ADD", "register:40f0:8", ["const:c4143c:8", "const:4:8"]]
+ 00c414d8 ["INT_ADD", "register:40f0:8", ["const:c414d8:8", "const:4:8"]]
~~~


### [`00c41440`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41440.md) → [`00c414dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c414dc.md) FUN_00c414dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4154c",
      "incomplete_value": false,
      "site": "00c4154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c414b0",
      "incomplete_value": false,
      "site": "00c414b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:e80:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c97e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97f50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41480 ["INT_ADD", "register:40f0:8", ["const:c41480:8", "const:4:8"]]
+ 00c4151c ["INT_ADD", "register:40f0:8", ["const:c4151c:8", "const:4:8"]]
- 00c414a4 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00c41540 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00c414fc ["INT_ADD", "register:40f0:8", ["const:c414fc:8", "const:4:8"]]
+ 00c41598 ["INT_ADD", "register:40f0:8", ["const:c41598:8", "const:4:8"]]
~~~


### [`00c41500`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41500.md) → [`00c4159c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4159c.md) FUN_00c4159c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4160c",
      "incomplete_value": false,
      "site": "00c4160c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41570",
      "incomplete_value": false,
      "site": "00c41570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c97ef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97fc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41540 ["INT_ADD", "register:40f0:8", ["const:c41540:8", "const:4:8"]]
+ 00c415dc ["INT_ADD", "register:40f0:8", ["const:c415dc:8", "const:4:8"]]
- 00c41564 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00c41600 ["COPY", "tmp:0:8", ["const:fc0:8"]]
- 00c415bc ["INT_ADD", "register:40f0:8", ["const:c415bc:8", "const:4:8"]]
+ 00c41658 ["INT_ADD", "register:40f0:8", ["const:c41658:8", "const:4:8"]]
~~~


### [`00c415c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c415c0.md) → [`00c4165c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c4165c.md) FUN_00c4165c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c416d0",
      "incomplete_value": false,
      "site": "00c416d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41634",
      "incomplete_value": false,
      "site": "00c41634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:f60:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97f60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c98030",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c41604 ["INT_ADD", "register:40f0:8", ["const:c41604:8", "const:4:8"]]
+ 00c416a0 ["INT_ADD", "register:40f0:8", ["const:c416a0:8", "const:4:8"]]
- 00c41624 ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c41628 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00c416c0 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c416c4 ["COPY", "tmp:0:8", ["const:30:8"]]
- 00c41684 ["INT_ADD", "register:40f0:8", ["const:c41684:8", "const:4:8"]]
+ 00c41720 ["INT_ADD", "register:40f0:8", ["const:c41720:8", "const:4:8"]]
~~~


### [`00c41688`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41688.md) → [`00c41724`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c41724.md) FUN_00c41724

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41798",
      "incomplete_value": false,
      "site": "00c41798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c416fc",
      "incomplete_value": false,
      "site": "00c416fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c980a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c416cc ["INT_ADD", "register:40f0:8", ["const:c416cc:8", "const:4:8"]]
+ 00c41768 ["INT_ADD", "register:40f0:8", ["const:c41768:8", "const:4:8"]]
- 00c416ec ["COPY", "register:4040:8", ["const:c97000:8"]]
- 00c416f0 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 00c41788 ["COPY", "register:4040:8", ["const:c98000:8"]]
+ 00c4178c ["COPY", "tmp:0:8", ["const:a0:8"]]
- 00c4174c ["INT_ADD", "register:40f0:8", ["const:c4174c:8", "const:4:8"]]
+ 00c417e8 ["INT_ADD", "register:40f0:8", ["const:c417e8:8", "const:4:8"]]
~~~


### [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) → [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) FUN_00c417ec

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 12件 [`00c3a118`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a118.md) [`00c3a178`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3a178.md) [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c46238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) [`00c4632c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md)
- 新版 呼出元 2件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 12件 [`00c3a1b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a1b4.md) [`00c3a214`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3a214.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c462d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) [`00c463c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c41b30",
      "incomplete_value": false,
      "site": "00c41b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41a94",
      "incomplete_value": false,
      "site": "00c41a94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:190:8"
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
      "definition_site": "00c41e4c",
      "incomplete_value": false,
      "site": "00c41e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:340:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c41db0",
      "incomplete_value": false,
      "site": "00c41db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:270:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c420c8",
      "incomplete_value": false,
      "site": "00c420c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4202c",
      "incomplete_value": false,
      "site": "00c4202c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:200:8"
          ]
        ]
      ]
    },
    "ordinal": 53,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      96,
      "DATA",
      [
        "storage",
        "00312adc",
        "switchD_00c417b8::switchdataD_00312adc",
        "ushort"
      ]
    ],
    [
      408,
      "PARAM",
      [
        "storage",
        "002ad1ed",
        null,
        "string"
      ]
    ],
    [
      432,
      "PARAM",
      [
        "storage",
        "002ac4c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      96,
      "DATA",
      [
        "storage",
        "00312b1c",
        "switchD_00c41854::switchdataD_00312b1c",
        "ushort"
      ]
    ],
    [
      408,
      "PARAM",
      [
        "storage",
        "002ad191",
        null,
        "string"
      ]
    ],
    [
      432,
      "PARAM",
      [
        "storage",
        "002ac46c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c417a4 ["COPY", "tmp:0:8", ["const:adc:8"]]
+ 00c41840 ["COPY", "tmp:0:8", ["const:b1c:8"]]
- 00c417ac ["COPY", "register:4078:8", ["const:c417bc:8"]]
+ 00c41848 ["COPY", "register:4078:8", ["const:c41858:8"]]
- 00c417c4 ["INT_ADD", "register:40f0:8", ["const:c417c4:8", "const:4:8"]]
+ 00c41860 ["INT_ADD", "register:40f0:8", ["const:c41860:8", "const:4:8"]]
~~~


### [`00c420d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) → [`00c4216c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) FUN_00c4216c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 3件 [`00c4955c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 3件 [`00c495f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42398",
      "incomplete_value": false,
      "site": "00c42398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c422fc",
      "incomplete_value": false,
      "site": "00c422fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00c423c0",
      "incomplete_value": false,
      "site": "00c423c0",
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
            "const:e9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42324",
      "incomplete_value": false,
      "site": "00c42324",
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
            "const:e5b:8"
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42470",
      "incomplete_value": false,
      "site": "00c42470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c423d4",
      "incomplete_value": false,
      "site": "00c423d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      556,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "DATA",
      [
        "storage",
        "002c0e5b",
        null,
        null
      ]
    ],
    [
      772,
      "DATA",
      [
        "storage",
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      556,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      596,
      "DATA",
      [
        "storage",
        "002c0e9b",
        null,
        null
      ]
    ],
    [
      772,
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c422cc ["INT_ADD", "register:40f0:8", ["const:c422cc:8", "const:4:8"]]
+ 00c42368 ["INT_ADD", "register:40f0:8", ["const:c42368:8", "const:4:8"]]
- 00c422f0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4238c ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c42314 ["COPY", "tmp:0:8", ["const:e5b:8"]]
+ 00c423b0 ["COPY", "tmp:0:8", ["const:e9b:8"]]
~~~


### [`00c4248c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) → [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) FUN_00c42528

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) · 呼出先 5件 [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c4248c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c4248c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) · 呼出先 5件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c42528`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42528.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c425f0",
      "incomplete_value": false,
      "site": "00c425f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42554",
      "incomplete_value": false,
      "site": "00c42554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:900:8"
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
      200,
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "00c98900",
        null,
        "undefined *"
      ]
    ],
    [
      552,
      "DATA",
      [
        "storage",
        "00c98970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      200,
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      376,
      "DATA",
      [
        "storage",
        "00c989d0",
        null,
        "undefined *"
      ]
    ],
    [
      552,
      "DATA",
      [
        "storage",
        "00c98a40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c424ec ["INT_ADD", "register:40f0:8", ["const:c424ec:8", "const:4:8"]]
+ 00c42588 ["INT_ADD", "register:40f0:8", ["const:c42588:8", "const:4:8"]]
- 00c424fc ["INT_ADD", "register:40f0:8", ["const:c424fc:8", "const:4:8"]]
+ 00c42598 ["INT_ADD", "register:40f0:8", ["const:c42598:8", "const:4:8"]]
- 00c42524 ["INT_ADD", "register:40f0:8", ["const:c42524:8", "const:4:8"]]
+ 00c425c0 ["INT_ADD", "register:40f0:8", ["const:c425c0:8", "const:4:8"]]
~~~


### [`00c426f4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c426f4.md) → [`00c42790`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42790.md) FUN_00c42790

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c427f4",
      "incomplete_value": true,
      "site": "00c427f4",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42758",
      "incomplete_value": true,
      "site": "00c42758",
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
            "const:9e0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42728 ["INT_ADD", "register:40f0:8", ["const:c42728:8", "const:4:8"]]
+ 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
- 00c4274c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00c427e8 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00c42794 ["INT_ADD", "register:40f0:8", ["const:c42794:8", "const:4:8"]]
+ 00c42830 ["INT_ADD", "register:40f0:8", ["const:c42830:8", "const:4:8"]]
~~~


### [`00c42798`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42798.md) → [`00c42834`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42834.md) FUN_00c42834

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 4件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 4件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42950",
      "incomplete_value": false,
      "site": "00c42950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c428b4",
      "incomplete_value": false,
      "site": "00c428b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c98a50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c98b20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c427b4 ["INT_ADD", "register:40f0:8", ["const:c427b4:8", "const:4:8"]]
+ 00c42850 ["INT_ADD", "register:40f0:8", ["const:c42850:8", "const:4:8"]]
- 00c427c4 ["INT_ADD", "register:40f0:8", ["const:c427c4:8", "const:4:8"]]
+ 00c42860 ["INT_ADD", "register:40f0:8", ["const:c42860:8", "const:4:8"]]
- 00c42880 ["INT_ADD", "register:40f0:8", ["const:c42880:8", "const:4:8"]]
+ 00c4291c ["INT_ADD", "register:40f0:8", ["const:c4291c:8", "const:4:8"]]
~~~


### [`00c42900`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42900.md) → [`00c4299c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4299c.md) FUN_00c4299c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42a04",
      "incomplete_value": false,
      "site": "00c42a04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42968",
      "incomplete_value": false,
      "site": "00c42968",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:40:8"
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
      "definition_site": "00c42a30",
      "incomplete_value": false,
      "site": "00c42a30",
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
            "const:eca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42994",
      "incomplete_value": false,
      "site": "00c42994",
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
            "const:e8a:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c98040",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "DATA",
      [
        "storage",
        "002b7e8a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c98110",
        null,
        "undefined *"
      ]
    ],
    [
      148,
      "DATA",
      [
        "storage",
        "002b7eca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42938 ["INT_ADD", "register:40f0:8", ["const:c42938:8", "const:4:8"]]
+ 00c429d4 ["INT_ADD", "register:40f0:8", ["const:c429d4:8", "const:4:8"]]
- 00c4295c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00c429f8 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00c4297c ["COPY", "tmp:0:8", ["const:e8a:8"]]
+ 00c42a18 ["COPY", "tmp:0:8", ["const:eca:8"]]
~~~


### [`00c429c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c429c0.md) → [`00c42a5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42a5c.md) FUN_00c42a5c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 9件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 9件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c42eec",
      "incomplete_value": false,
      "site": "00c42eec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c42e50",
      "incomplete_value": false,
      "site": "00c42e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
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
      "DATA",
      [
        "storage",
        "00c98ac0",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98b30",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98ba0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      748,
      "DATA",
      [
        "storage",
        "00c98b90",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98c00",
        null,
        "undefined *"
      ]
    ],
    [
      896,
      "DATA",
      [
        "storage",
        "00c98c70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42a5c ["INT_ADD", "register:40f0:8", ["const:c42a5c:8", "const:4:8"]]
+ 00c42af8 ["INT_ADD", "register:40f0:8", ["const:c42af8:8", "const:4:8"]]
- 00c42aa4 ["INT_ADD", "register:40f0:8", ["const:c42aa4:8", "const:4:8"]]
+ 00c42b40 ["INT_ADD", "register:40f0:8", ["const:c42b40:8", "const:4:8"]]
- 00c42ad4 ["INT_ADD", "register:40f0:8", ["const:c42ad4:8", "const:4:8"]]
+ 00c42b70 ["INT_ADD", "register:40f0:8", ["const:c42b70:8", "const:4:8"]]
~~~


### [`00c42e90`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c42e90.md) → [`00c42f2c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c42f2c.md) FUN_00c42f2c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 8件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 8件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43210",
      "incomplete_value": true,
      "site": "00c43210",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43174",
      "incomplete_value": true,
      "site": "00c43174",
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
            "const:c80:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      740,
      "DATA",
      [
        "storage",
        "00c98c80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      740,
      "DATA",
      [
        "storage",
        "00c98d50",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c42eb8 ["INT_ADD", "register:40f0:8", ["const:c42eb8:8", "const:4:8"]]
+ 00c42f54 ["INT_ADD", "register:40f0:8", ["const:c42f54:8", "const:4:8"]]
- 00c42ec8 ["INT_ADD", "register:40f0:8", ["const:c42ec8:8", "const:4:8"]]
+ 00c42f64 ["INT_ADD", "register:40f0:8", ["const:c42f64:8", "const:4:8"]]
- 00c42f60 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c42ffc ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c433d8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c433d8.md) → [`00c43474`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43474.md) FUN_00c43474

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c434d8",
      "incomplete_value": false,
      "site": "00c434d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4343c",
      "incomplete_value": false,
      "site": "00c4343c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:d60:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c98d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c98e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4340c ["INT_ADD", "register:40f0:8", ["const:c4340c:8", "const:4:8"]]
+ 00c434a8 ["INT_ADD", "register:40f0:8", ["const:c434a8:8", "const:4:8"]]
- 00c43430 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00c434cc ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00c43470 ["INT_ADD", "register:40f0:8", ["const:c43470:8", "const:4:8"]]
+ 00c4350c ["INT_ADD", "register:40f0:8", ["const:c4350c:8", "const:4:8"]]
~~~


### [`00c43474`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43474.md) → [`00c43510`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43510.md) FUN_00c43510

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43578",
      "incomplete_value": false,
      "site": "00c43578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c434dc",
      "incomplete_value": false,
      "site": "00c434dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c989e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c98ab0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c434ac ["INT_ADD", "register:40f0:8", ["const:c434ac:8", "const:4:8"]]
+ 00c43548 ["INT_ADD", "register:40f0:8", ["const:c43548:8", "const:4:8"]]
- 00c434d0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00c4356c ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00c4351c ["INT_ADD", "register:40f0:8", ["const:c4351c:8", "const:4:8"]]
+ 00c435b8 ["INT_ADD", "register:40f0:8", ["const:c435b8:8", "const:4:8"]]
~~~


### [`00c435cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c435cc.md) → [`00c43668`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43668.md) FUN_00c43668

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c436cc",
      "incomplete_value": true,
      "site": "00c436cc",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43630",
      "incomplete_value": true,
      "site": "00c43630",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c98dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c98ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c43600 ["INT_ADD", "register:40f0:8", ["const:c43600:8", "const:4:8"]]
+ 00c4369c ["INT_ADD", "register:40f0:8", ["const:c4369c:8", "const:4:8"]]
- 00c43624 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 00c436c0 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00c43668 ["INT_ADD", "register:40f0:8", ["const:c43668:8", "const:4:8"]]
+ 00c43704 ["INT_ADD", "register:40f0:8", ["const:c43704:8", "const:4:8"]]
~~~


### [`00c4366c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) → [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) FUN_00c43708

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 7件 [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c3ea94`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3ea94.md) [`00c4b628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4b7ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 7件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c3eb30`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3eb30.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c437dc",
      "incomplete_value": false,
      "site": "00c437dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43740",
      "incomplete_value": false,
      "site": "00c43740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00c43adc",
      "incomplete_value": false,
      "site": "00c43adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43a40",
      "incomplete_value": false,
      "site": "00c43a40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43bac",
      "incomplete_value": false,
      "site": "00c43bac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43b10",
      "incomplete_value": false,
      "site": "00c43b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
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
      "DATA",
      [
        "storage",
        "00c99000",
        null,
        "undefined *"
      ]
    ],
    [
      520,
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      588,
      "DATA",
      [
        "storage",
        "00c98e40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      212,
      "DATA",
      [
        "storage",
        "00c990d0",
        null,
        "undefined *"
      ]
    ],
    [
      520,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      588,
      "DATA",
      [
        "storage",
        "00c98f10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c436e4 ["INT_ADD", "register:40f0:8", ["const:c436e4:8", "const:4:8"]]
+ 00c43780 ["INT_ADD", "register:40f0:8", ["const:c43780:8", "const:4:8"]]
- 00c4370c ["INT_ADD", "register:40f0:8", ["const:c4370c:8", "const:4:8"]]
+ 00c437a8 ["INT_ADD", "register:40f0:8", ["const:c437a8:8", "const:4:8"]]
- 00c43734 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 00c437d0 ["COPY", "tmp:0:8", ["const:d0:8"]]
~~~


### [`00c43ce0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c43ce0.md) → [`00c43d7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43d7c.md) FUN_00c43d7c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c43df0",
      "incomplete_value": false,
      "site": "00c43df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c43d54",
      "incomplete_value": false,
      "site": "00c43d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c97b70",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c97c40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c43d24 ["INT_ADD", "register:40f0:8", ["const:c43d24:8", "const:4:8"]]
+ 00c43dc0 ["INT_ADD", "register:40f0:8", ["const:c43dc0:8", "const:4:8"]]
- 00c43d48 ["COPY", "tmp:0:8", ["const:b70:8"]]
+ 00c43de4 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 00c43da8 ["INT_ADD", "register:40f0:8", ["const:c43da8:8", "const:4:8"]]
+ 00c43e44 ["INT_ADD", "register:40f0:8", ["const:c43e44:8", "const:4:8"]]
~~~


### [`00c442c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c44/00c442c0.md) → [`00c4435c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c44/00c4435c.md) FUN_00c4435c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c443cc",
      "incomplete_value": false,
      "site": "00c443cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c44330",
      "incomplete_value": false,
      "site": "00c44330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c97be0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c97cb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c44300 ["INT_ADD", "register:40f0:8", ["const:c44300:8", "const:4:8"]]
+ 00c4439c ["INT_ADD", "register:40f0:8", ["const:c4439c:8", "const:4:8"]]
- 00c44324 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00c443c0 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00c4437c ["INT_ADD", "register:40f0:8", ["const:c4437c:8", "const:4:8"]]
+ 00c44418 ["INT_ADD", "register:40f0:8", ["const:c44418:8", "const:4:8"]]
~~~


### [`00c46238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46238.md) → [`00c462d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c462d4.md) FUN_00c462d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c3ab8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3ab8c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c3ac28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ac28.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4637c",
      "incomplete_value": false,
      "site": "00c4637c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c462e0",
      "incomplete_value": false,
      "site": "00c462e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      168,
      "DATA",
      [
        "storage",
        "00c980b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      168,
      "DATA",
      [
        "storage",
        "00c98180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46260 ["INT_ADD", "register:40f0:8", ["const:c46260:8", "const:4:8"]]
+ 00c462fc ["INT_ADD", "register:40f0:8", ["const:c462fc:8", "const:4:8"]]
- 00c462a8 ["INT_ADD", "register:40f0:8", ["const:c462a8:8", "const:4:8"]]
+ 00c46344 ["INT_ADD", "register:40f0:8", ["const:c46344:8", "const:4:8"]]
- 00c462dc ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 00c46378 ["COPY", "tmp:0:8", ["const:180:8"]]
~~~


### [`00c4632c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c4632c.md) → [`00c463c8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c463c8.md) FUN_00c463c8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46444",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:1f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4639c",
      "incomplete_value": false,
      "site": "00c463a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:120:8"
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
      124,
      "DATA",
      [
        "storage",
        "00c98120",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c981f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46360 ["INT_ADD", "register:40f0:8", ["const:c46360:8", "const:4:8"]]
+ 00c463fc ["INT_ADD", "register:40f0:8", ["const:c463fc:8", "const:4:8"]]
- 00c4639c ["COPY", "tmp:0:8", ["const:120:8"]]
+ 00c46438 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00c463d0 ["INT_ADD", "register:40f0:8", ["const:c463d0:8", "const:4:8"]]
+ 00c4646c ["INT_ADD", "register:40f0:8", ["const:c4646c:8", "const:4:8"]]
~~~


### [`00c463d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c463d4.md) → [`00c46470`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46470.md) FUN_00c46470

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c464d4",
      "incomplete_value": false,
      "site": "00c464d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46438",
      "incomplete_value": false,
      "site": "00c46438",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c982e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c983b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46408 ["INT_ADD", "register:40f0:8", ["const:c46408:8", "const:4:8"]]
+ 00c464a4 ["INT_ADD", "register:40f0:8", ["const:c464a4:8", "const:4:8"]]
- 00c4642c ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00c464c8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
- 00c46470 ["INT_ADD", "register:40f0:8", ["const:c46470:8", "const:4:8"]]
+ 00c4650c ["INT_ADD", "register:40f0:8", ["const:c4650c:8", "const:4:8"]]
~~~


### [`00c46474`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46474.md) → [`00c46510`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46510.md) FUN_00c46510

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4657c",
      "incomplete_value": false,
      "site": "00c4657c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c464e0",
      "incomplete_value": false,
      "site": "00c464e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c464a8 ["INT_ADD", "register:40f0:8", ["const:c464a8:8", "const:4:8"]]
+ 00c46544 ["INT_ADD", "register:40f0:8", ["const:c46544:8", "const:4:8"]]
- 00c464d0 ["INT_ADD", "register:40f0:8", ["const:c464d0:8", "const:4:8"]]
+ 00c4656c ["INT_ADD", "register:40f0:8", ["const:c4656c:8", "const:4:8"]]
- 00c464d8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c46574 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c46520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) → [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) FUN_00c465bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 14件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c47834`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md)
- 新版 呼出元 2件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 14件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c466dc",
      "incomplete_value": false,
      "site": "00c466dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46640",
      "incomplete_value": false,
      "site": "00c46640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00c46704",
      "incomplete_value": false,
      "site": "00c46704",
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
            "const:d34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46668",
      "incomplete_value": false,
      "site": "00c46668",
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
            "const:d88:8"
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
      "definition_site": "00c46890",
      "incomplete_value": false,
      "site": "00c46890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c467f4",
      "incomplete_value": false,
      "site": "00c467f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:350:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      288,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "002b8d88",
        null,
        "string"
      ]
    ],
    [
      724,
      "DATA",
      [
        "storage",
        "00c98350",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      288,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      328,
      "DATA",
      [
        "storage",
        "002b8d34",
        null,
        "string"
      ]
    ],
    [
      724,
      "DATA",
      [
        "storage",
        "00c98420",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46610 ["INT_ADD", "register:40f0:8", ["const:c46610:8", "const:4:8"]]
+ 00c466ac ["INT_ADD", "register:40f0:8", ["const:c466ac:8", "const:4:8"]]
- 00c46634 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c466d0 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c46658 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00c466f4 ["COPY", "tmp:0:8", ["const:d34:8"]]
~~~


### [`00c46ca0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46ca0.md) → [`00c46d3c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46d3c.md) FUN_00c46d3c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46da0",
      "incomplete_value": false,
      "site": "00c46da0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46d04",
      "incomplete_value": false,
      "site": "00c46d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c986d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c987a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46cd4 ["INT_ADD", "register:40f0:8", ["const:c46cd4:8", "const:4:8"]]
+ 00c46d70 ["INT_ADD", "register:40f0:8", ["const:c46d70:8", "const:4:8"]]
- 00c46cf8 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00c46d94 ["COPY", "tmp:0:8", ["const:7a0:8"]]
- 00c46d3c ["INT_ADD", "register:40f0:8", ["const:c46d3c:8", "const:4:8"]]
+ 00c46dd8 ["INT_ADD", "register:40f0:8", ["const:c46dd8:8", "const:4:8"]]
~~~


### [`00c46d40`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46d40.md) → [`00c46ddc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c46ddc.md) FUN_00c46ddc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c41750`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c41/00c41750.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c417ec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c41/00c417ec.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c46e44",
      "incomplete_value": false,
      "site": "00c46e44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c46da8",
      "incomplete_value": false,
      "site": "00c46da8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:740:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c98740",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c98810",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c46d78 ["INT_ADD", "register:40f0:8", ["const:c46d78:8", "const:4:8"]]
+ 00c46e14 ["INT_ADD", "register:40f0:8", ["const:c46e14:8", "const:4:8"]]
- 00c46d9c ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00c46e38 ["COPY", "tmp:0:8", ["const:810:8"]]
- 00c46de8 ["INT_ADD", "register:40f0:8", ["const:c46de8:8", "const:4:8"]]
+ 00c46e84 ["INT_ADD", "register:40f0:8", ["const:c46e84:8", "const:4:8"]]
~~~


### [`00c47190`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47190.md) → [`00c4722c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c4722c.md) FUN_00c4722c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47350",
      "incomplete_value": false,
      "site": "00c47368",
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
            "const:d2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c472b4",
      "incomplete_value": false,
      "site": "00c472cc",
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
            "const:d80:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      292,
      "PARAM",
      [
        "storage",
        "002b8d80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      292,
      "PARAM",
      [
        "storage",
        "002b8d2c",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c472b4 ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 00c47350 ["COPY", "tmp:0:8", ["const:d2c:8"]]
- 00c472cc ["INT_ADD", "register:40f0:8", ["const:c472cc:8", "const:4:8"]]
+ 00c47368 ["INT_ADD", "register:40f0:8", ["const:c47368:8", "const:4:8"]]
- 00c47300 ["INT_ADD", "register:40f0:8", ["const:c47300:8", "const:4:8"]]
+ 00c4739c ["INT_ADD", "register:40f0:8", ["const:c4739c:8", "const:4:8"]]
~~~


### [`00c4734c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c4734c.md) → [`00c473e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c473e8.md) FUN_00c473e8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47524",
      "incomplete_value": false,
      "site": "00c47534",
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
            "const:4c1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47488",
      "incomplete_value": false,
      "site": "00c47498",
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
            "const:51d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      316,
      "PARAM",
      [
        "storage",
        "002ac51d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      316,
      "PARAM",
      [
        "storage",
        "002ac4c1",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c47488 ["COPY", "tmp:0:8", ["const:51d:8"]]
+ 00c47524 ["COPY", "tmp:0:8", ["const:4c1:8"]]
- 00c47498 ["INT_ADD", "register:40f0:8", ["const:c47498:8", "const:4:8"]]
+ 00c47534 ["INT_ADD", "register:40f0:8", ["const:c47534:8", "const:4:8"]]
- 00c474cc ["INT_ADD", "register:40f0:8", ["const:c474cc:8", "const:4:8"]]
+ 00c47568 ["INT_ADD", "register:40f0:8", ["const:c47568:8", "const:4:8"]]
~~~


### [`00c47518`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47518.md) → [`00c475b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c475b4.md) FUN_00c475b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md) [`00c5e100`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5e/00c5e100.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md) [`00c5e1d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5e/00c5e1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c47728",
      "incomplete_value": false,
      "site": "00c4773c",
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
            "const:dfa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4768c",
      "incomplete_value": false,
      "site": "00c476a0",
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
            "const:e4e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      372,
      "PARAM",
      [
        "storage",
        "002b9e4e",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      372,
      "PARAM",
      [
        "storage",
        "002b9dfa",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4768c ["COPY", "tmp:0:8", ["const:e4e:8"]]
+ 00c47728 ["COPY", "tmp:0:8", ["const:dfa:8"]]
- 00c476a0 ["INT_ADD", "register:40f0:8", ["const:c476a0:8", "const:4:8"]]
+ 00c4773c ["INT_ADD", "register:40f0:8", ["const:c4773c:8", "const:4:8"]]
- 00c476d4 ["INT_ADD", "register:40f0:8", ["const:c476d4:8", "const:4:8"]]
+ 00c47770 ["INT_ADD", "register:40f0:8", ["const:c47770:8", "const:4:8"]]
~~~


### [`00c47834`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) → [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) FUN_00c478d0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00c3c940`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c940.md) [`00c46520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) [`00c47834`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 14件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md)
- 新版 呼出元 3件 [`00c3c9dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c9dc.md) [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 14件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 8件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c479ec",
      "incomplete_value": false,
      "site": "00c479ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47950",
      "incomplete_value": false,
      "site": "00c47950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
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
      "definition_site": "00c47ac4",
      "incomplete_value": false,
      "site": "00c47ac4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47a28",
      "incomplete_value": false,
      "site": "00c47a28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c47b84",
      "incomplete_value": false,
      "site": "00c47b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c47ae8",
      "incomplete_value": false,
      "site": "00c47ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:3c0:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      500,
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ],
    [
      692,
      "DATA",
      [
        "storage",
        "00c983c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      284,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      500,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ],
    [
      692,
      "DATA",
      [
        "storage",
        "00c98490",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c478d0 ["INT_ADD", "register:40f0:8", ["const:c478d0:8", "const:4:8"]]
+ 00c4796c ["INT_ADD", "register:40f0:8", ["const:c4796c:8", "const:4:8"]]
- 00c478e4 ["INT_ADD", "register:40f0:8", ["const:c478e4:8", "const:4:8"]]
+ 00c47980 ["INT_ADD", "register:40f0:8", ["const:c47980:8", "const:4:8"]]
- 00c4791c ["INT_ADD", "register:40f0:8", ["const:c4791c:8", "const:4:8"]]
+ 00c479b8 ["INT_ADD", "register:40f0:8", ["const:c479b8:8", "const:4:8"]]
~~~


### [`00c481a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c481a0.md) → [`00c4823c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4823c.md) FUN_00c4823c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c46520`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c46/00c46520.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c465bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c46/00c465bc.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c482b8",
      "incomplete_value": false,
      "site": "00c482b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:730:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4821c",
      "incomplete_value": false,
      "site": "00c4821c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c98660",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      124,
      "DATA",
      [
        "storage",
        "00c98730",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c481ec ["INT_ADD", "register:40f0:8", ["const:c481ec:8", "const:4:8"]]
+ 00c48288 ["INT_ADD", "register:40f0:8", ["const:c48288:8", "const:4:8"]]
- 00c48210 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 00c482ac ["COPY", "tmp:0:8", ["const:730:8"]]
- 00c4827c ["INT_ADD", "register:40f0:8", ["const:c4827c:8", "const:4:8"]]
+ 00c48318 ["INT_ADD", "register:40f0:8", ["const:c48318:8", "const:4:8"]]
~~~


### [`00c48280`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48280.md) → [`00c4831c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c4831c.md) FUN_00c4831c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58660.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c58730`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c58730.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c48378",
      "incomplete_value": false,
      "site": "00c48390",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c482dc",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:ee2:8"
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
      "definition_site": "00c48380",
      "incomplete_value": false,
      "site": "00c48390",
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
            "const:8c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c482e4",
      "incomplete_value": false,
      "site": "00c482f4",
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
            "const:896:8"
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
      "definition_site": "00c48388",
      "incomplete_value": false,
      "site": "00c48390",
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
      "definition_site": "00c482ec",
      "incomplete_value": false,
      "site": "00c482f4",
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
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      92,
      "PARAM",
      [
        "storage",
        "002a0ee2",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "002b2896",
        null,
        "string"
      ]
    ],
    [
      108,
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
      92,
      "PARAM",
      [
        "storage",
        "002a0e95",
        null,
        "string"
      ]
    ],
    [
      100,
      "PARAM",
      [
        "storage",
        "002b28c7",
        null,
        "string"
      ]
    ],
    [
      108,
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
- 00c482dc ["COPY", "tmp:0:8", ["const:ee2:8"]]
+ 00c48378 ["COPY", "tmp:0:8", ["const:e95:8"]]
- 00c482e4 ["COPY", "tmp:0:8", ["const:896:8"]]
+ 00c48380 ["COPY", "tmp:0:8", ["const:8c7:8"]]
- 00c482ec ["COPY", "tmp:0:8", ["const:3ea:8"]]
+ 00c48388 ["COPY", "tmp:0:8", ["const:38e:8"]]
~~~


### [`00c4844c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c4844c.md) → [`00c484e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c484e8.md) FUN_00c484e8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c47834`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c47/00c47834.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c478d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c47/00c478d0.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4854c",
      "incomplete_value": false,
      "site": "00c4854c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c484b0",
      "incomplete_value": false,
      "site": "00c484b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c985f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c986c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48480 ["INT_ADD", "register:40f0:8", ["const:c48480:8", "const:4:8"]]
+ 00c4851c ["INT_ADD", "register:40f0:8", ["const:c4851c:8", "const:4:8"]]
- 00c484a4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 00c48540 ["COPY", "tmp:0:8", ["const:6c0:8"]]
- 00c484e8 ["INT_ADD", "register:40f0:8", ["const:c484e8:8", "const:4:8"]]
+ 00c48584 ["INT_ADD", "register:40f0:8", ["const:c48584:8", "const:4:8"]]
~~~


### [`00c48720`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48720.md) → [`00c487bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c487bc.md) FUN_00c487bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48814",
      "incomplete_value": true,
      "site": "00c48820",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d51:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48778",
      "incomplete_value": true,
      "site": "00c48784",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d9e:8"
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
      88,
      "READ",
      [
        "storage",
        "002a1d9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "002a1d51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4875c ["INT_ADD", "register:40f0:8", ["const:c4875c:8", "const:4:8"]]
+ 00c487f8 ["INT_ADD", "register:40f0:8", ["const:c487f8:8", "const:4:8"]]
- 00c48770 ["COPY", "tmp:0:8", ["const:d9e:8"]]
+ 00c4880c ["COPY", "tmp:0:8", ["const:d51:8"]]
- 00c487a4 ["INT_ADD", "register:40f0:8", ["const:c487a4:8", "const:4:8"]]
+ 00c48840 ["INT_ADD", "register:40f0:8", ["const:c48840:8", "const:4:8"]]
~~~


### [`00c48a70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48a70.md) → [`00c48b0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48b0c.md) FUN_00c48b0c

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48b74",
      "incomplete_value": true,
      "site": "00c48b80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:afc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48ad8",
      "incomplete_value": true,
      "site": "00c48ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b50:8"
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
      "definition_site": "00c48be0",
      "incomplete_value": true,
      "site": "00c48bec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48b44",
      "incomplete_value": true,
      "site": "00c48b50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:943:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "READ",
      [
        "storage",
        "002bfb50",
        null,
        "string"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "002b0943",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      104,
      "READ",
      [
        "storage",
        "002bfafc",
        null,
        "string"
      ]
    ],
    [
      212,
      "READ",
      [
        "storage",
        "002b08e7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48abc ["INT_ADD", "register:40f0:8", ["const:c48abc:8", "const:4:8"]]
+ 00c48b58 ["INT_ADD", "register:40f0:8", ["const:c48b58:8", "const:4:8"]]
- 00c48ad0 ["COPY", "tmp:0:8", ["const:b50:8"]]
+ 00c48b6c ["COPY", "tmp:0:8", ["const:afc:8"]]
- 00c48afc ["INT_ADD", "register:40f0:8", ["const:c48afc:8", "const:4:8"]]
+ 00c48b98 ["INT_ADD", "register:40f0:8", ["const:c48b98:8", "const:4:8"]]
~~~


### [`00c48b8c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c48/00c48b8c.md) → [`00c48c28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c48/00c48c28.md) FUN_00c48c28

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c48cc8",
      "incomplete_value": true,
      "site": "00c48cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c48c2c",
      "incomplete_value": true,
      "site": "00c48c3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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
      160,
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      160,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c48bb8 ["INT_ADD", "register:40f0:8", ["const:c48bb8:8", "const:4:8"]]
+ 00c48c54 ["INT_ADD", "register:40f0:8", ["const:c48c54:8", "const:4:8"]]
- 00c48bdc ["INT_ADD", "register:40f0:8", ["const:c48bdc:8", "const:4:8"]]
+ 00c48c78 ["INT_ADD", "register:40f0:8", ["const:c48c78:8", "const:4:8"]]
- 00c48c10 ["INT_ADD", "register:40f0:8", ["const:c48c10:8", "const:4:8"]]
+ 00c48cac ["INT_ADD", "register:40f0:8", ["const:c48cac:8", "const:4:8"]]
~~~


### [`00c4955c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c4955c.md) → [`00c495f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c495f8.md) FUN_00c495f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c420d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c42/00c420d0.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c4216c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c42/00c4216c.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4965c",
      "incomplete_value": false,
      "site": "00c4965c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c495c0",
      "incomplete_value": false,
      "site": "00c495c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:7b0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c987b0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c98880",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c49590 ["INT_ADD", "register:40f0:8", ["const:c49590:8", "const:4:8"]]
+ 00c4962c ["INT_ADD", "register:40f0:8", ["const:c4962c:8", "const:4:8"]]
- 00c495b4 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00c49650 ["COPY", "tmp:0:8", ["const:880:8"]]
- 00c495f8 ["INT_ADD", "register:40f0:8", ["const:c495f8:8", "const:4:8"]]
+ 00c49694 ["INT_ADD", "register:40f0:8", ["const:c49694:8", "const:4:8"]]
~~~


### [`00c496f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c496f0.md) → [`00c4978c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c4978c.md) FUN_00c4978c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c49e74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c49f10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4996c",
      "incomplete_value": false,
      "site": "00c49970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c498d0",
      "incomplete_value": false,
      "site": "00c498d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c49ca4",
      "incomplete_value": false,
      "site": "00c49ca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c49c08",
      "incomplete_value": false,
      "site": "00c49c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      484,
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ],
    [
      1308,
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      484,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ],
    [
      1308,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c49744 ["INT_ADD", "register:40f0:8", ["const:c49744:8", "const:4:8"]]
+ 00c497e0 ["INT_ADD", "register:40f0:8", ["const:c497e0:8", "const:4:8"]]
- 00c497c0 ["INT_ADD", "register:40f0:8", ["const:c497c0:8", "const:4:8"]]
+ 00c4985c ["INT_ADD", "register:40f0:8", ["const:c4985c:8", "const:4:8"]]
- 00c497f0 ["INT_ADD", "register:40f0:8", ["const:c497f0:8", "const:4:8"]]
+ 00c4988c ["INT_ADD", "register:40f0:8", ["const:c4988c:8", "const:4:8"]]
~~~


### [`00c4a818`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4a818.md) → [`00c4a8b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4a8b4.md) FUN_00c4a8b4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4aa74",
      "incomplete_value": true,
      "site": "00c4aa80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:894:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4a9d8",
      "incomplete_value": true,
      "site": "00c4a9e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
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
      448,
      "READ",
      [
        "storage",
        "002b18f0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      448,
      "READ",
      [
        "storage",
        "002b1894",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4a860 ["INT_ADD", "register:40f0:8", ["const:c4a860:8", "const:4:8"]]
+ 00c4a8fc ["INT_ADD", "register:40f0:8", ["const:c4a8fc:8", "const:4:8"]]
- 00c4a8cc ["INT_ADD", "register:40f0:8", ["const:c4a8cc:8", "const:4:8"]]
+ 00c4a968 ["INT_ADD", "register:40f0:8", ["const:c4a968:8", "const:4:8"]]
- 00c4a900 ["INT_ADD", "register:40f0:8", ["const:c4a900:8", "const:4:8"]]
+ 00c4a99c ["INT_ADD", "register:40f0:8", ["const:c4a99c:8", "const:4:8"]]
~~~


### [`00c4ab04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ab04.md) → [`00c4aba0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4aba0.md) FUN_00c4aba0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ac04",
      "incomplete_value": true,
      "site": "00c4ac14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2ae:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ab68",
      "incomplete_value": true,
      "site": "00c4ab78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:302:8"
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
      100,
      "READ",
      [
        "storage",
        "002bc302",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bc2ae",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ab48 ["INT_ADD", "register:40f0:8", ["const:c4ab48:8", "const:4:8"]]
+ 00c4abe4 ["INT_ADD", "register:40f0:8", ["const:c4abe4:8", "const:4:8"]]
- 00c4ab60 ["COPY", "tmp:0:8", ["const:302:8"]]
+ 00c4abfc ["COPY", "tmp:0:8", ["const:2ae:8"]]
- 00c4ab98 ["INT_ADD", "register:40f0:8", ["const:c4ab98:8", "const:4:8"]]
+ 00c4ac34 ["INT_ADD", "register:40f0:8", ["const:c4ac34:8", "const:4:8"]]
~~~


### [`00c4ac28`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4a/00c4ac28.md) → [`00c4acc4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4a/00c4acc4.md) FUN_00c4acc4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ad28",
      "incomplete_value": true,
      "site": "00c4ad38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ac8c",
      "incomplete_value": true,
      "site": "00c4ac9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
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
      100,
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ac6c ["INT_ADD", "register:40f0:8", ["const:c4ac6c:8", "const:4:8"]]
+ 00c4ad08 ["INT_ADD", "register:40f0:8", ["const:c4ad08:8", "const:4:8"]]
- 00c4ac84 ["COPY", "tmp:0:8", ["const:e50:8"]]
+ 00c4ad20 ["COPY", "tmp:0:8", ["const:e90:8"]]
- 00c4acbc ["INT_ADD", "register:40f0:8", ["const:c4acbc:8", "const:4:8"]]
+ 00c4ad58 ["INT_ADD", "register:40f0:8", ["const:c4ad58:8", "const:4:8"]]
~~~


### [`00c4b0a4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b0a4.md) → [`00c4b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b140.md) FUN_00c4b140

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b260",
      "incomplete_value": true,
      "site": "00c4b26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b1c4",
      "incomplete_value": true,
      "site": "00c4b1d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea4:8"
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
      288,
      "READ",
      [
        "storage",
        "002b7ea4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      288,
      "READ",
      [
        "storage",
        "002b7ee4",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b0d0 ["INT_ADD", "register:40f0:8", ["const:c4b0d0:8", "const:4:8"]]
+ 00c4b16c ["INT_ADD", "register:40f0:8", ["const:c4b16c:8", "const:4:8"]]
- 00c4b0f4 ["INT_ADD", "register:40f0:8", ["const:c4b0f4:8", "const:4:8"]]
+ 00c4b190 ["INT_ADD", "register:40f0:8", ["const:c4b190:8", "const:4:8"]]
- 00c4b120 ["INT_ADD", "register:40f0:8", ["const:c4b120:8", "const:4:8"]]
+ 00c4b1bc ["INT_ADD", "register:40f0:8", ["const:c4b1bc:8", "const:4:8"]]
~~~


### [`00c4b3b4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b3b4.md) → [`00c4b450`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b450.md) FUN_00c4b450

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c49e74`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c49/00c49e74.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c49f10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c49/00c49f10.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b4b8",
      "incomplete_value": true,
      "site": "00c4b4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:524:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b41c",
      "incomplete_value": true,
      "site": "00c4b428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b544",
      "incomplete_value": false,
      "site": "00c4b548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:960:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b4a8",
      "incomplete_value": false,
      "site": "00c4b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      104,
      "READ",
      [
        "storage",
        "002ac580",
        null,
        "string"
      ]
    ],
    [
      248,
      "DATA",
      [
        "storage",
        "00c98890",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "READ",
      [
        "storage",
        "002ac524",
        null,
        "string"
      ]
    ],
    [
      248,
      "DATA",
      [
        "storage",
        "00c98960",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b3fc ["INT_ADD", "register:40f0:8", ["const:c4b3fc:8", "const:4:8"]]
+ 00c4b498 ["INT_ADD", "register:40f0:8", ["const:c4b498:8", "const:4:8"]]
- 00c4b414 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00c4b4b0 ["COPY", "tmp:0:8", ["const:524:8"]]
- 00c4b468 ["INT_ADD", "register:40f0:8", ["const:c4b468:8", "const:4:8"]]
+ 00c4b504 ["INT_ADD", "register:40f0:8", ["const:c4b504:8", "const:4:8"]]
~~~


### [`00c4b7ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) → [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) FUN_00c4b848

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c4366c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c43/00c4366c.md) · 呼出先 6件 [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4b628`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b628.md) [`00c4bb5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c43708`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c43/00c43708.md) · 呼出先 6件 [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4b6c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b6c4.md) [`00c4bbf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4b948",
      "incomplete_value": false,
      "site": "00c4b948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b8ac",
      "incomplete_value": false,
      "site": "00c4b8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
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
      "definition_site": "00c4b9f0",
      "incomplete_value": false,
      "site": "00c4b9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4b954",
      "incomplete_value": false,
      "site": "00c4b954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
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
      "definition_site": "00c4bab0",
      "incomplete_value": false,
      "site": "00c4bab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ba14",
      "incomplete_value": false,
      "site": "00c4ba14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
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
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ],
    [
      424,
      "DATA",
      [
        "storage",
        "00c98eb0",
        null,
        "undefined *"
      ]
    ],
    [
      616,
      "DATA",
      [
        "storage",
        "00c99540",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      256,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ],
    [
      424,
      "DATA",
      [
        "storage",
        "00c98f80",
        null,
        "undefined *"
      ]
    ],
    [
      616,
      "DATA",
      [
        "storage",
        "00c99610",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4b818 ["INT_ADD", "register:40f0:8", ["const:c4b818:8", "const:4:8"]]
+ 00c4b8b4 ["INT_ADD", "register:40f0:8", ["const:c4b8b4:8", "const:4:8"]]
- 00c4b828 ["INT_ADD", "register:40f0:8", ["const:c4b828:8", "const:4:8"]]
+ 00c4b8c4 ["INT_ADD", "register:40f0:8", ["const:c4b8c4:8", "const:4:8"]]
- 00c4b854 ["INT_ADD", "register:40f0:8", ["const:c4b854:8", "const:4:8"]]
+ 00c4b8f0 ["INT_ADD", "register:40f0:8", ["const:c4b8f0:8", "const:4:8"]]
~~~


### [`00c4bb5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bb5c.md) → [`00c4bbf8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4bbf8.md) FUN_00c4bbf8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) [`00c4b7ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4b7ac.md) · 呼出先 5件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3dfb0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3d/00c3dfb0.md) [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) [`00c4b848`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4b/00c4b848.md) · 呼出先 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e04c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e04c.md) [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4bd44",
      "incomplete_value": false,
      "site": "00c4bd44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:ff0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bca8",
      "incomplete_value": false,
      "site": "00c4bca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c98000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "definition_site": "00c4bf30",
      "incomplete_value": false,
      "site": "00c4bf30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4be94",
      "incomplete_value": false,
      "site": "00c4be94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
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
        "00c97960",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c97961",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c97970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      88,
      "READ",
      [
        "storage",
        "00c97a30",
        null,
        "undefined1"
      ]
    ],
    [
      104,
      "READ",
      [
        "storage",
        "00c97a31",
        null,
        "undefined1"
      ]
    ],
    [
      148,
      "READ",
      [
        "storage",
        "00c97a40",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4bb94 ["COPY", "register:4060:8", ["const:c97780:8"]]
+ 00c4bc30 ["COPY", "register:4060:8", ["const:c97850:8"]]
- 00c4bc40 ["INT_ADD", "register:40f0:8", ["const:c4bc40:8", "const:4:8"]]
+ 00c4bcdc ["INT_ADD", "register:40f0:8", ["const:c4bcdc:8", "const:4:8"]]
- 00c4bc74 ["INT_ADD", "register:40f0:8", ["const:c4bc74:8", "const:4:8"]]
+ 00c4bd10 ["INT_ADD", "register:40f0:8", ["const:c4bd10:8", "const:4:8"]]
~~~


### [`00c4bf78`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4b/00c4bf78.md) → [`00c4c014`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c014.md) FUN_00c4c014

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c078",
      "incomplete_value": true,
      "site": "00c4c088",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:641:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4bfdc",
      "incomplete_value": true,
      "site": "00c4bfec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:695:8"
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
      100,
      "READ",
      [
        "storage",
        "002bd695",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bd641",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4bfbc ["INT_ADD", "register:40f0:8", ["const:c4bfbc:8", "const:4:8"]]
+ 00c4c058 ["INT_ADD", "register:40f0:8", ["const:c4c058:8", "const:4:8"]]
- 00c4bfd4 ["COPY", "tmp:0:8", ["const:695:8"]]
+ 00c4c070 ["COPY", "tmp:0:8", ["const:641:8"]]
- 00c4c00c ["INT_ADD", "register:40f0:8", ["const:c4c00c:8", "const:4:8"]]
+ 00c4c0a8 ["INT_ADD", "register:40f0:8", ["const:c4c0a8:8", "const:4:8"]]
~~~


### [`00c4c05c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c05c.md) → [`00c4c0f8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c0f8.md) FUN_00c4c0f8

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c15c",
      "incomplete_value": true,
      "site": "00c4c16c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c0c0",
      "incomplete_value": true,
      "site": "00c4c0d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:30d:8"
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
      100,
      "READ",
      [
        "storage",
        "002bc30d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002bc2b9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c0a0 ["INT_ADD", "register:40f0:8", ["const:c4c0a0:8", "const:4:8"]]
+ 00c4c13c ["INT_ADD", "register:40f0:8", ["const:c4c13c:8", "const:4:8"]]
- 00c4c0b8 ["COPY", "tmp:0:8", ["const:30d:8"]]
+ 00c4c154 ["COPY", "tmp:0:8", ["const:2b9:8"]]
- 00c4c0f4 ["INT_ADD", "register:40f0:8", ["const:c4c0f4:8", "const:4:8"]]
+ 00c4c190 ["INT_ADD", "register:40f0:8", ["const:c4c190:8", "const:4:8"]]
~~~


### [`00c4c338`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c338.md) → [`00c4c3d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c3d4.md) FUN_00c4c3d4

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4c568",
      "incomplete_value": false,
      "site": "00c4c580",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c4cc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:ee2:8"
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
      "definition_site": "00c4c570",
      "incomplete_value": false,
      "site": "00c4c580",
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
            "const:8c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c4d4",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
            "const:896:8"
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
      "definition_site": "00c4c578",
      "incomplete_value": false,
      "site": "00c4c580",
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
      "definition_site": "00c4c4dc",
      "incomplete_value": false,
      "site": "00c4c4e4",
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
    "ordinal": 3,
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      260,
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002bd69f",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002b8d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      260,
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002bd64b",
        null,
        "string"
      ]
    ],
    [
      260,
      "READ",
      [
        "storage",
        "002b8d44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c380 ["INT_ADD", "register:40f0:8", ["const:c4c380:8", "const:4:8"]]
+ 00c4c41c ["INT_ADD", "register:40f0:8", ["const:c4c41c:8", "const:4:8"]]
- 00c4c3d4 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00c4c470 ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00c4c3f4 ["COPY", "tmp:0:8", ["const:69f:8"]]
+ 00c4c490 ["COPY", "tmp:0:8", ["const:64b:8"]]
~~~


### [`00c4c4f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c4f0.md) → [`00c4c58c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c58c.md) FUN_00c4c58c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c3800c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c38/00c3800c.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c380a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c38/00c380a8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00c4c64c",
      "incomplete_value": false,
      "site": "00c4c664",
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
            "const:e95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c5b0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:ee2:8"
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
      "definition_site": "00c4c654",
      "incomplete_value": false,
      "site": "00c4c664",
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
            "const:8c7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c5b8",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
            "const:896:8"
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
      "definition_site": "00c4c65c",
      "incomplete_value": false,
      "site": "00c4c664",
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
      "definition_site": "00c4c5c0",
      "incomplete_value": false,
      "site": "00c4c5c8",
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
    "slot": 4
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      32,
      "DATA",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "002b7eb0",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "002b9f23",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      32,
      "DATA",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ],
    [
      80,
      "DATA",
      [
        "storage",
        "002b7ef0",
        null,
        "string"
      ]
    ],
    [
      136,
      "READ",
      [
        "storage",
        "002b9ecf",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c510 ["COPY", "tmp:0:8", ["const:f23:8"]]
+ 00c4c5ac ["COPY", "tmp:0:8", ["const:ecf:8"]]
- 00c4c530 ["COPY", "tmp:0:8", ["const:69f:8"]]
+ 00c4c5cc ["COPY", "tmp:0:8", ["const:64b:8"]]
- 00c4c540 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 00c4c5dc ["COPY", "tmp:0:8", ["const:ef0:8"]]
~~~


### [`00c4c5d4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c5d4.md) → [`00c4c670`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c670.md) FUN_00c4c670

根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4c7b0",
      "incomplete_value": true,
      "site": "00c4c7b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ae1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c714",
      "incomplete_value": true,
      "site": "00c4c71c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ab0:8"
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
      "definition_site": "00c4c7b4",
      "incomplete_value": true,
      "site": "00c4c7bc",
      "value": [
        "LOAD",
        "16",
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
                "const:d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c718",
      "incomplete_value": true,
      "site": "00c4c720",
      "value": [
        "LOAD",
        "16",
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
                "const:d:8"
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
      "definition_site": "00c4c81c",
      "incomplete_value": true,
      "site": "00c4c824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:142:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c780",
      "incomplete_value": true,
      "site": "00c4c788",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:196:8"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      320,
      "READ",
      [
        "storage",
        "002b4ab0",
        null,
        "string"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "002b4abd",
        null,
        "string"
      ]
    ],
    [
      428,
      "READ",
      [
        "storage",
        "002bb196",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      320,
      "READ",
      [
        "storage",
        "002b4ae1",
        null,
        "string"
      ]
    ],
    [
      324,
      "READ",
      [
        "storage",
        "002b4aee",
        null,
        "string"
      ]
    ],
    [
      428,
      "READ",
      [
        "storage",
        "002bb142",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c61c ["INT_ADD", "register:40f0:8", ["const:c4c61c:8", "const:4:8"]]
+ 00c4c6b8 ["INT_ADD", "register:40f0:8", ["const:c4c6b8:8", "const:4:8"]]
- 00c4c660 ["INT_ADD", "register:40f0:8", ["const:c4c660:8", "const:4:8"]]
+ 00c4c6fc ["INT_ADD", "register:40f0:8", ["const:c4c6fc:8", "const:4:8"]]
- 00c4c698 ["INT_ADD", "register:40f0:8", ["const:c4c698:8", "const:4:8"]]
+ 00c4c734 ["INT_ADD", "register:40f0:8", ["const:c4c734:8", "const:4:8"]]
~~~


### [`00c4c810`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4c810.md) → [`00c4c8ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4c8ac.md) FUN_00c4c8ac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00c4c8cc",
      "incomplete_value": true,
      "site": "00c4c8d0",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:dc8:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4c830",
      "incomplete_value": true,
      "site": "00c4c834",
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
                "const:313000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
            ]
          ],
          [
            "INT_SEXT",
            "8",
            [
              "LOAD"
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


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      16,
      "DATA",
      [
        "storage",
        "00313d58",
        null,
        null
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00313d88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      16,
      "DATA",
      [
        "storage",
        "00313d98",
        null,
        null
      ]
    ],
    [
      28,
      "DATA",
      [
        "storage",
        "00313dc8",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4c81c ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00c4c8b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00c4c828 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00c4c8c4 ["COPY", "tmp:0:8", ["const:dc8:8"]]
~~~


### [`00c4cb04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cb04.md) → [`00c4cba0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4cba0.md) FUN_00c4cba0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3f310.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3f3ac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3f3ac.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cc10",
      "incomplete_value": false,
      "site": "00c4cc10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4cb74",
      "incomplete_value": false,
      "site": "00c4cb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:230:8"
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
      112,
      "DATA",
      [
        "storage",
        "00c99230",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      112,
      "DATA",
      [
        "storage",
        "00c99300",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4cb44 ["INT_ADD", "register:40f0:8", ["const:c4cb44:8", "const:4:8"]]
+ 00c4cbe0 ["INT_ADD", "register:40f0:8", ["const:c4cbe0:8", "const:4:8"]]
- 00c4cb70 ["COPY", "tmp:0:8", ["const:230:8"]]
+ 00c4cc0c ["COPY", "tmp:0:8", ["const:300:8"]]
- 00c4cbc0 ["INT_ADD", "register:40f0:8", ["const:c4cbc0:8", "const:4:8"]]
+ 00c4cc5c ["INT_ADD", "register:40f0:8", ["const:c4cc5c:8", "const:4:8"]]
~~~


### [`00c4cdec`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4c/00c4cdec.md) → [`00c4ce88`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4c/00c4ce88.md) FUN_00c4ce88

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4cf20",
      "incomplete_value": true,
      "site": "00c4cf30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ce84",
      "incomplete_value": true,
      "site": "00c4ce94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:294:8"
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
      152,
      "READ",
      [
        "storage",
        "002a5294",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      152,
      "READ",
      [
        "storage",
        "002a5238",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ce18 ["INT_ADD", "register:40f0:8", ["const:c4ce18:8", "const:4:8"]]
+ 00c4ceb4 ["INT_ADD", "register:40f0:8", ["const:c4ceb4:8", "const:4:8"]]
- 00c4ce3c ["INT_ADD", "register:40f0:8", ["const:c4ce3c:8", "const:4:8"]]
+ 00c4ced8 ["INT_ADD", "register:40f0:8", ["const:c4ced8:8", "const:4:8"]]
- 00c4ce68 ["INT_ADD", "register:40f0:8", ["const:c4ce68:8", "const:4:8"]]
+ 00c4cf04 ["INT_ADD", "register:40f0:8", ["const:c4cf04:8", "const:4:8"]]
~~~


### [`00c4d0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d0f0.md) → [`00c4d18c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d18c.md) FUN_00c4d18c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d1f8",
      "incomplete_value": false,
      "site": "00c4d1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d15c",
      "incomplete_value": false,
      "site": "00c4d15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d124 ["INT_ADD", "register:40f0:8", ["const:c4d124:8", "const:4:8"]]
+ 00c4d1c0 ["INT_ADD", "register:40f0:8", ["const:c4d1c0:8", "const:4:8"]]
- 00c4d14c ["INT_ADD", "register:40f0:8", ["const:c4d14c:8", "const:4:8"]]
+ 00c4d1e8 ["INT_ADD", "register:40f0:8", ["const:c4d1e8:8", "const:4:8"]]
- 00c4d154 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4d1f0 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c4d19c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d19c.md) → [`00c4d238`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d238.md) FUN_00c4d238

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d2a0",
      "incomplete_value": false,
      "site": "00c4d2a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d204",
      "incomplete_value": false,
      "site": "00c4d204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c993f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c994c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d1d4 ["INT_ADD", "register:40f0:8", ["const:c4d1d4:8", "const:4:8"]]
+ 00c4d270 ["INT_ADD", "register:40f0:8", ["const:c4d270:8", "const:4:8"]]
- 00c4d1f8 ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00c4d294 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00c4d240 ["INT_ADD", "register:40f0:8", ["const:c4d240:8", "const:4:8"]]
+ 00c4d2dc ["INT_ADD", "register:40f0:8", ["const:c4d2dc:8", "const:4:8"]]
~~~


### [`00c4d7cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4d7cc.md) → [`00c4d868`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4d868.md) FUN_00c4d868

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4d8cc",
      "incomplete_value": true,
      "site": "00c4d8e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4d830",
      "incomplete_value": true,
      "site": "00c4d844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e7c:8"
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
      100,
      "READ",
      [
        "storage",
        "002a3e7c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      100,
      "READ",
      [
        "storage",
        "002a3e2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4d810 ["INT_ADD", "register:40f0:8", ["const:c4d810:8", "const:4:8"]]
+ 00c4d8ac ["INT_ADD", "register:40f0:8", ["const:c4d8ac:8", "const:4:8"]]
- 00c4d828 ["COPY", "tmp:0:8", ["const:e7c:8"]]
+ 00c4d8c4 ["COPY", "tmp:0:8", ["const:e2f:8"]]
- 00c4d858 ["INT_ADD", "register:40f0:8", ["const:c4d858:8", "const:4:8"]]
+ 00c4d8f4 ["INT_ADD", "register:40f0:8", ["const:c4d8f4:8", "const:4:8"]]
~~~


### [`00c4dac8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4d/00c4dac8.md) → [`00c4db64`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4d/00c4db64.md) FUN_00c4db64

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00c45144`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c45/00c45144.md) [`00c5a0a0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a0a0.md) [`00c5b140`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5b/00c5b140.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00c451e0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c45/00c451e0.md) [`00c5a170`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a170.md) [`00c5b210`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b210.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4dcfc",
      "incomplete_value": true,
      "site": "00c4dd08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:659:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dc60",
      "incomplete_value": true,
      "site": "00c4dc6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ad:8"
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
      "definition_site": "00c4dd64",
      "incomplete_value": true,
      "site": "00c4dd70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aaf:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4dcc8",
      "incomplete_value": true,
      "site": "00c4dcd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b03:8"
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
      "definition_site": "00c4dec4",
      "incomplete_value": true,
      "site": "00c4ded4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4de28",
      "incomplete_value": true,
      "site": "00c4de38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      408,
      "READ",
      [
        "storage",
        "002bd6ad",
        null,
        "string"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "002beb03",
        null,
        "string"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "002c0e50",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      408,
      "READ",
      [
        "storage",
        "002bd659",
        null,
        "string"
      ]
    ],
    [
      512,
      "READ",
      [
        "storage",
        "002beaaf",
        null,
        "string"
      ]
    ],
    [
      864,
      "READ",
      [
        "storage",
        "002c0e90",
        null,
        "string"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4db18 ["INT_ADD", "register:40f0:8", ["const:c4db18:8", "const:4:8"]]
+ 00c4dbb4 ["INT_ADD", "register:40f0:8", ["const:c4dbb4:8", "const:4:8"]]
- 00c4db40 ["INT_ADD", "register:40f0:8", ["const:c4db40:8", "const:4:8"]]
+ 00c4dbdc ["INT_ADD", "register:40f0:8", ["const:c4dbdc:8", "const:4:8"]]
- 00c4db78 ["INT_ADD", "register:40f0:8", ["const:c4db78:8", "const:4:8"]]
+ 00c4dc14 ["INT_ADD", "register:40f0:8", ["const:c4dc14:8", "const:4:8"]]
~~~


### [`00c4e040`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e040.md) → [`00c4e0dc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e0dc.md) FUN_00c4e0dc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 8件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3cde0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3cde0.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c58000`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58000.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 8件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3ce7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3ce7c.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c580d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580d0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e2d4",
      "incomplete_value": false,
      "site": "00c4e2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e238",
      "incomplete_value": false,
      "site": "00c4e238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e2f8",
      "incomplete_value": false,
      "site": "00c4e2f8",
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
            "const:993:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e25c",
      "incomplete_value": false,
      "site": "00c4e25c",
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
            "const:9ef:8"
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
      "definition_site": "00c4e384",
      "incomplete_value": false,
      "site": "00c4e384",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e2e8",
      "incomplete_value": false,
      "site": "00c4e2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:850:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      540,
      "DATA",
      [
        "storage",
        "002a89ef",
        null,
        "string"
      ]
    ],
    [
      680,
      "DATA",
      [
        "storage",
        "00c99850",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      540,
      "DATA",
      [
        "storage",
        "002a8993",
        null,
        "string"
      ]
    ],
    [
      680,
      "DATA",
      [
        "storage",
        "00c99920",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4e144 ["INT_ADD", "register:40f0:8", ["const:c4e144:8", "const:4:8"]]
+ 00c4e1e0 ["INT_ADD", "register:40f0:8", ["const:c4e1e0:8", "const:4:8"]]
- 00c4e18c ["INT_ADD", "register:40f0:8", ["const:c4e18c:8", "const:4:8"]]
+ 00c4e228 ["INT_ADD", "register:40f0:8", ["const:c4e228:8", "const:4:8"]]
- 00c4e1bc ["INT_ADD", "register:40f0:8", ["const:c4e1bc:8", "const:4:8"]]
+ 00c4e258 ["INT_ADD", "register:40f0:8", ["const:c4e258:8", "const:4:8"]]
~~~


### [`00c4e5e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) → [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) FUN_00c4e684

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c4e5e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) · 呼出先 5件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3e5c4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3e/00c3e5c4.md) [`00c4e5e8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e5e8.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 2件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) · 呼出先 5件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3e660`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3e660.md) [`00c4e684`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4e684.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4e87c",
      "incomplete_value": false,
      "site": "00c4e87c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e7e0",
      "incomplete_value": false,
      "site": "00c4e7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00c4e904",
      "incomplete_value": false,
      "site": "00c4e904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e868",
      "incomplete_value": false,
      "site": "00c4e868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "definition_site": "00c4ea14",
      "incomplete_value": false,
      "site": "00c4ea14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4e978",
      "incomplete_value": false,
      "site": "00c4e978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:9a0:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c99a80",
        null,
        "undefined *"
      ]
    ],
    [
      640,
      "DATA",
      [
        "storage",
        "00c99a10",
        null,
        "undefined *"
      ]
    ],
    [
      912,
      "DATA",
      [
        "storage",
        "00c999a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      504,
      "DATA",
      [
        "storage",
        "00c99b50",
        null,
        "undefined *"
      ]
    ],
    [
      640,
      "DATA",
      [
        "storage",
        "00c99ae0",
        null,
        "undefined *"
      ]
    ],
    [
      912,
      "DATA",
      [
        "storage",
        "00c99a70",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4e704 ["INT_ADD", "register:40f0:8", ["const:c4e704:8", "const:4:8"]]
+ 00c4e7a0 ["INT_ADD", "register:40f0:8", ["const:c4e7a0:8", "const:4:8"]]
- 00c4e780 ["INT_ADD", "register:40f0:8", ["const:c4e780:8", "const:4:8"]]
+ 00c4e81c ["INT_ADD", "register:40f0:8", ["const:c4e81c:8", "const:4:8"]]
- 00c4e7a8 ["INT_ADD", "register:40f0:8", ["const:c4e7a8:8", "const:4:8"]]
+ 00c4e844 ["INT_ADD", "register:40f0:8", ["const:c4e844:8", "const:4:8"]]
~~~


### [`00c4e9c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4e9c0.md) → [`00c4ea5c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ea5c.md) FUN_00c4ea5c

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eac8",
      "incomplete_value": false,
      "site": "00c4eac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ea2c",
      "incomplete_value": false,
      "site": "00c4ea2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4e9f4 ["INT_ADD", "register:40f0:8", ["const:c4e9f4:8", "const:4:8"]]
+ 00c4ea90 ["INT_ADD", "register:40f0:8", ["const:c4ea90:8", "const:4:8"]]
- 00c4ea1c ["INT_ADD", "register:40f0:8", ["const:c4ea1c:8", "const:4:8"]]
+ 00c4eab8 ["INT_ADD", "register:40f0:8", ["const:c4eab8:8", "const:4:8"]]
- 00c4ea24 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4eac0 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c4ea6c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ea6c.md) → [`00c4eb08`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4eb08.md) FUN_00c4eb08

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eb74",
      "incomplete_value": false,
      "site": "00c4eb74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ead8",
      "incomplete_value": false,
      "site": "00c4ead8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4eaa0 ["INT_ADD", "register:40f0:8", ["const:c4eaa0:8", "const:4:8"]]
+ 00c4eb3c ["INT_ADD", "register:40f0:8", ["const:c4eb3c:8", "const:4:8"]]
- 00c4eac8 ["INT_ADD", "register:40f0:8", ["const:c4eac8:8", "const:4:8"]]
+ 00c4eb64 ["INT_ADD", "register:40f0:8", ["const:c4eb64:8", "const:4:8"]]
- 00c4ead0 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4eb6c ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c4eb18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4eb18.md) → [`00c4ebb4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ebb4.md) FUN_00c4ebb4

根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c57fe0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c57/00c57fe0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c580b0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580b0.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ec20",
      "incomplete_value": false,
      "site": "00c4ec20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4eb84",
      "incomplete_value": false,
      "site": "00c4eb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      108,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4eb4c ["INT_ADD", "register:40f0:8", ["const:c4eb4c:8", "const:4:8"]]
+ 00c4ebe8 ["INT_ADD", "register:40f0:8", ["const:c4ebe8:8", "const:4:8"]]
- 00c4eb74 ["INT_ADD", "register:40f0:8", ["const:c4eb74:8", "const:4:8"]]
+ 00c4ec10 ["INT_ADD", "register:40f0:8", ["const:c4ec10:8", "const:4:8"]]
- 00c4eb7c ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4ec18 ["COPY", "tmp:0:8", ["const:710:8"]]
~~~


### [`00c4ebc4`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ebc4.md) → [`00c4ec60`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ec60.md) FUN_00c4ec60

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ecc8",
      "incomplete_value": false,
      "site": "00c4ecc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ec2c",
      "incomplete_value": false,
      "site": "00c4ec2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:af0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99af0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99bc0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ebfc ["INT_ADD", "register:40f0:8", ["const:c4ebfc:8", "const:4:8"]]
+ 00c4ec98 ["INT_ADD", "register:40f0:8", ["const:c4ec98:8", "const:4:8"]]
- 00c4ec20 ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00c4ecbc ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00c4ec6c ["INT_ADD", "register:40f0:8", ["const:c4ec6c:8", "const:4:8"]]
+ 00c4ed08 ["INT_ADD", "register:40f0:8", ["const:c4ed08:8", "const:4:8"]]
~~~


### [`00c4ec70`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ec70.md) → [`00c4ed0c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ed0c.md) FUN_00c4ed0c

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ed70",
      "incomplete_value": false,
      "site": "00c4ed70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ecd4",
      "incomplete_value": false,
      "site": "00c4ecd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
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
        "00c99b60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      100,
      "DATA",
      [
        "storage",
        "00c99c30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4eca4 ["INT_ADD", "register:40f0:8", ["const:c4eca4:8", "const:4:8"]]
+ 00c4ed40 ["INT_ADD", "register:40f0:8", ["const:c4ed40:8", "const:4:8"]]
- 00c4ecc8 ["COPY", "tmp:0:8", ["const:b60:8"]]
+ 00c4ed64 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00c4ed0c ["INT_ADD", "register:40f0:8", ["const:c4ed0c:8", "const:4:8"]]
+ 00c4eda8 ["INT_ADD", "register:40f0:8", ["const:c4eda8:8", "const:4:8"]]
~~~


### [`00c4ed10`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ed10.md) → [`00c4edac`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4edac.md) FUN_00c4edac

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4ee14",
      "incomplete_value": false,
      "site": "00c4ee14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ed78",
      "incomplete_value": false,
      "site": "00c4ed78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:bd0:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99bd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ed48 ["INT_ADD", "register:40f0:8", ["const:c4ed48:8", "const:4:8"]]
+ 00c4ede4 ["INT_ADD", "register:40f0:8", ["const:c4ede4:8", "const:4:8"]]
- 00c4ed6c ["COPY", "tmp:0:8", ["const:bd0:8"]]
+ 00c4ee08 ["COPY", "tmp:0:8", ["const:ca0:8"]]
- 00c4edb8 ["INT_ADD", "register:40f0:8", ["const:c4edb8:8", "const:4:8"]]
+ 00c4ee54 ["INT_ADD", "register:40f0:8", ["const:c4ee54:8", "const:4:8"]]
~~~


### [`00c4edbc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4edbc.md) → [`00c4ee58`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ee58.md) FUN_00c4ee58

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4eec0",
      "incomplete_value": false,
      "site": "00c4eec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ee24",
      "incomplete_value": false,
      "site": "00c4ee24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      104,
      "DATA",
      [
        "storage",
        "00c99c40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99d10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4edf4 ["INT_ADD", "register:40f0:8", ["const:c4edf4:8", "const:4:8"]]
+ 00c4ee90 ["INT_ADD", "register:40f0:8", ["const:c4ee90:8", "const:4:8"]]
- 00c4ee18 ["COPY", "tmp:0:8", ["const:c40:8"]]
+ 00c4eeb4 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00c4ee64 ["INT_ADD", "register:40f0:8", ["const:c4ee64:8", "const:4:8"]]
+ 00c4ef00 ["INT_ADD", "register:40f0:8", ["const:c4ef00:8", "const:4:8"]]
~~~


### [`00c4ee68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4e/00c4ee68.md) → [`00c4ef04`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4e/00c4ef04.md) FUN_00c4ef04

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 6件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) [`00c3fd7c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3f/00c3fd7c.md) [`00c50830`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c50830.md) [`00c508d0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c50/00c508d0.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 6件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) [`00c3fe18`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3f/00c3fe18.md) [`00c508cc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c508cc.md) [`00c5096c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c50/00c5096c.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f000",
      "incomplete_value": false,
      "site": "00c4f000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4ef64",
      "incomplete_value": false,
      "site": "00c4ef64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c97000:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f040",
      "incomplete_value": false,
      "site": "00c4f040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f178",
      "incomplete_value": false,
      "site": "00c4f178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f0dc",
      "incomplete_value": false,
      "site": "00c4f0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
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
      "DATA",
      [
        "storage",
        "00c97640",
        null,
        "undefined *"
      ]
    ],
    [
      472,
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ],
    [
      628,
      "DATA",
      [
        "storage",
        "00c99d20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      252,
      "DATA",
      [
        "storage",
        "00c97710",
        null,
        "undefined *"
      ]
    ],
    [
      472,
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ],
    [
      628,
      "DATA",
      [
        "storage",
        "00c99df0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4ef2c ["INT_ADD", "register:40f0:8", ["const:c4ef2c:8", "const:4:8"]]
+ 00c4efc8 ["INT_ADD", "register:40f0:8", ["const:c4efc8:8", "const:4:8"]]
- 00c4ef60 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00c4effc ["COPY", "tmp:0:8", ["const:710:8"]]
- 00c4efd0 ["INT_ADD", "register:40f0:8", ["const:c4efd0:8", "const:4:8"]]
+ 00c4f06c ["INT_ADD", "register:40f0:8", ["const:c4f06c:8", "const:4:8"]]
~~~


### [`00c4f124`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f124.md) → [`00c4f1c0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f1c0.md) FUN_00c4f1c0

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 3件 [`00c3c20c`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3c/00c3c20c.md) [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 3件 [`00c3c2a8`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3c/00c3c2a8.md) [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f2cc",
      "incomplete_value": false,
      "site": "00c4f2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f230",
      "incomplete_value": false,
      "site": "00c4f230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:e70:8"
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
      268,
      "DATA",
      [
        "storage",
        "00c99e70",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002b364c",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      268,
      "DATA",
      [
        "storage",
        "00c99f40",
        null,
        "undefined *"
      ]
    ],
    [
      300,
      "DATA",
      [
        "storage",
        "002b367d",
        null,
        null
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f19c ["COPY", "tmp:0:8", ["const:64c:8"]]
+ 00c4f238 ["COPY", "tmp:0:8", ["const:67d:8"]]
- 00c4f1ac ["COPY", "tmp:0:8", ["const:c1e:8"]]
+ 00c4f248 ["COPY", "tmp:0:8", ["const:c5e:8"]]
- 00c4f1bc ["COPY", "tmp:0:8", ["const:847:8"]]
+ 00c4f258 ["COPY", "tmp:0:8", ["const:7eb:8"]]
~~~


### [`00c4f274`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f274.md) → [`00c4f310`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f310.md) FUN_00c4f310

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f378",
      "incomplete_value": false,
      "site": "00c4f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:fb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f2dc",
      "incomplete_value": false,
      "site": "00c4f2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 2
  }
]
~~~


参照の変更（関数入口からの相対位置）

~~~json
{
  "removed": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99ee0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      104,
      "DATA",
      [
        "storage",
        "00c99fb0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f2a8 ["INT_ADD", "register:40f0:8", ["const:c4f2a8:8", "const:4:8"]]
+ 00c4f344 ["INT_ADD", "register:40f0:8", ["const:c4f344:8", "const:4:8"]]
- 00c4f2d4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00c4f370 ["COPY", "tmp:0:8", ["const:fb0:8"]]
- 00c4f31c ["INT_ADD", "register:40f0:8", ["const:c4f31c:8", "const:4:8"]]
+ 00c4f3b8 ["INT_ADD", "register:40f0:8", ["const:c4f3b8:8", "const:4:8"]]
~~~


### [`00c4f320`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c4f/00c4f320.md) → [`00c4f3bc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c4f/00c4f3bc.md) FUN_00c4f3bc

根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00c3accc`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c3a/00c3accc.md) · 呼出先 2件 [`00c58020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c58/00c58020.md) [`00c5a020`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c5a/00c5a020.md)
- 新版 呼出元 1件 [`00c3ad68`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3a/00c3ad68.md) · 呼出先 2件 [`00c580f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c58/00c580f0.md) [`00c5a0f0`](https://github.com/sinsuirakv0/KBCS/blob/b2ee89d359d9e9e447994a0712362ea408eb031a/research/reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5a0f0.md)

変更の種類 constant, operands_and_dependencies, store_value

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00c4f430",
      "incomplete_value": false,
      "site": "00c4f430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c9a000:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00c4f394",
      "incomplete_value": false,
      "site": "00c4f394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c99000:8"
          ],
          [
            "leaf",
            "const:f50:8"
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
      116,
      "DATA",
      [
        "storage",
        "00c99f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      116,
      "DATA",
      [
        "storage",
        "00c9a020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


~~~diff
- 00c4f358 ["INT_ADD", "register:40f0:8", ["const:c4f358:8", "const:4:8"]]
+ 00c4f3f4 ["INT_ADD", "register:40f0:8", ["const:c4f3f4:8", "const:4:8"]]
- 00c4f380 ["COPY", "register:4050:8", ["const:c99000:8"]]
- 00c4f384 ["COPY", "tmp:0:8", ["const:f50:8"]]
+ 00c4f41c ["COPY", "register:4050:8", ["const:c9a000:8"]]
+ 00c4f420 ["COPY", "tmp:0:8", ["const:20:8"]]
- 00c4f3d8 ["INT_ADD", "register:40f0:8", ["const:c4f3d8:8", "const:4:8"]]
+ 00c4f474 ["INT_ADD", "register:40f0:8", ["const:c4f474:8", "const:4:8"]]
~~~


