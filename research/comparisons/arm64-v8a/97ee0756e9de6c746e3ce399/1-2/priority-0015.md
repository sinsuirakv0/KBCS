# v15.7.3 → v15.7.4 · 最優先の変更候補 (15)

[一覧の目次](README.md)

<a id="compare-a3cf5ae83c0aae8b7092289485962472"></a>

### [`0052c558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md) → [`0052c558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052c/0052c558.md) _INIT_25

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`004c45bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c45bc.md) [`004c4764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c4/004c4764.md) [`004f25dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f25dc.md) [`004f26f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004f2/004f26f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md) [`004c45bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c45bc.md) [`004c4764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c4/004c4764.md) [`004f25dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f25dc.md) [`004f26f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004f2/004f26f8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052c87c",
      "incomplete_value": false,
      "site": "0052c890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052cb74",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052cb7c",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052cb7c",
      "incomplete_value": false,
      "site": "0052cb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052c87c",
      "PARAM",
      [
        "storage",
        "00c25368",
        null,
        null
      ]
    ],
    [
      "0052cb74",
      "PARAM",
      [
        "storage",
        "00c25368",
        null,
        null
      ]
    ],
    [
      "0052cb7c",
      "PARAM",
      [
        "storage",
        "00be5f80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052c87c",
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ],
    [
      "0052cb74",
      "PARAM",
      [
        "storage",
        "00c253a8",
        null,
        null
      ]
    ],
    [
      "0052cb7c",
      "PARAM",
      [
        "storage",
        "00be5fd0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052c87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052c87c) · [`0052cb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052cb74) · [`0052cb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052c/0052c558.md#insn-0052cb7c)
- 新版 `0052c87c`（命令位置の公開資料なし） · `0052cb74`（命令位置の公開資料なし） · `0052cb7c`（命令位置の公開資料なし）

~~~diff
- 0052c87c ["COPY", "tmp:0:8", ["const:368:8"]]
- 0052c87c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0052c87c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0052c87c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0052c87c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0052c87c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0052c87c bytes 00a00d91
+ 0052c87c bytes 00a00e91
- 0052cb74 ["COPY", "tmp:0:8", ["const:368:8"]]
- 0052cb74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0052cb74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052cb74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052cb74 bytes 21a00d91
+ 0052cb74 bytes 21a00e91
- 0052cb7c ["COPY", "tmp:0:8", ["const:f80:8"]]
- 0052cb7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0052cb7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0052cb7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0052cb7c bytes 42003e91
+ 0052cb7c bytes 42403f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4691e07ad057c65acd9bc948825ca4"></a>

### [`0052db54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db54.md) → [`0052db54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db54.md) FUN_0052db54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0052db6c",
      "incomplete_value": true,
      "site": "0052db70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052db6c",
      "incomplete_value": true,
      "site": "0052db70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0052db68",
      "READ",
      [
        "storage",
        "00c1b3e8",
        null,
        "pointer"
      ]
    ],
    [
      "0052db70",
      "DATA",
      [
        "storage",
        "00bedb30",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "0052db68",
      "READ",
      [
        "storage",
        "00c1b438",
        null,
        "pointer"
      ]
    ],
    [
      "0052db70",
      "DATA",
      [
        "storage",
        "00bedb80",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052db68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db54.md#insn-0052db68)
- 新版 `0052db68`（命令位置の公開資料なし）

~~~diff
- 0052db68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:3e8:8"]]
- 0052db68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052db68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:438:8"]]
+ 0052db68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052db68 bytes 08f541f9
+ 0052db68 bytes 081d42f9
~~~


<a id="compare-b84d6ce2a21b2a0dd30aa7d2f2051299"></a>

### [`0052db94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md) → [`0052db94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db94.md) FUN_0052db94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0052db88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`0052db88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db88.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.52% / 新版 94.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052dc38",
      "incomplete_value": true,
      "site": "0052dc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "definition_site": "0052dc14",
      "incomplete_value": true,
      "site": "0052dc1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "0052dc14",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0052dc14",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0052dc34",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052dc14",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "0052dc14",
      "PARAM",
      [
        "storage",
        "00c12f08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0052dc34",
      "READ",
      [
        "storage",
        "00c1ae70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052dc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md#insn-0052dc14) · [`0052dc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db94.md#insn-0052dc34)
- 新版 `0052dc14`（命令位置の公開資料なし） · `0052dc34`（命令位置の公開資料なし）

~~~diff
- 0052dc14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0052dc14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052dc14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e68:8"]]
+ 0052dc14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0052dc14 bytes 210c47f9
+ 0052dc14 bytes 213447f9
- 0052dc34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
- 0052dc34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052dc34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0052dc34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052dc34 bytes 081147f9
+ 0052dc34 bytes 083947f9
~~~


<a id="compare-3e6113bb5e08f6f7b470ec84b1ca313c"></a>

### [`0052e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md) → [`0052e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md) FUN_0052e05c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005321d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b668.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`005321d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) · 呼出先 5件 [`0053b668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b668.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.91% / 新版 95.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e0a0",
      "incomplete_value": false,
      "site": "0052e0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0052e0a4",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0c0",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0dc",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0052e0a4",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0c0",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ],
    [
      "0052e0dc",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md#insn-0052e0a0) · [`0052e0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md#insn-0052e0dc)
- 新版 `0052e0a0`（命令位置の公開資料なし） · `0052e0dc`（命令位置の公開資料なし）

~~~diff
- 0052e0a0 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0052e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 0052e0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e0a0 bytes 08412f91
+ 0052e0a0 bytes 08813091
- 0052e0dc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:400:8"]]
- 0052e0dc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052e0dc ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:450:8"]]
+ 0052e0dc ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0052e0dc bytes 390342f9
+ 0052e0dc bytes 392b42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e50fe04379f8f8566211f192c75e774"></a>

### [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) → [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) FUN_0052e39c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) [`0053980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053980c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 4件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) · 呼出先 6件 [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) [`0053980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053980c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.36% / 新版 90.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:293000:8"
              ],
              [
                "leaf",
                "const:9aa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:293000:8"
              ],
              [
                "leaf",
                "const:a37:8"
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0052e3f0",
      "incomplete_value": true,
      "site": "0052e400",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052e404",
      "incomplete_value": true,
      "site": "0052e410",
      "value": [
        "LOAD",
        "16",
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
                "const:1c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052e404",
      "incomplete_value": true,
      "site": "0052e410",
      "value": [
        "LOAD",
        "16",
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
                "const:1c:8"
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
      "0052e3f0",
      "READ",
      [
        "storage",
        "00293a37",
        null,
        "string"
      ]
    ],
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "00293a47",
        null,
        "string"
      ]
    ],
    [
      "0052e404",
      "READ",
      [
        "storage",
        "00293a53",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "002939aa",
        null,
        "string"
      ]
    ],
    [
      "0052e3f0",
      "READ",
      [
        "storage",
        "002939ba",
        null,
        "string"
      ]
    ],
    [
      "0052e404",
      "READ",
      [
        "storage",
        "002939c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052e3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md#insn-0052e3e8) · [`0052e3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md#insn-0052e3ec)
- 新版 `0052e3e8`（命令位置の公開資料なし） · `0052e3ec`（命令位置の公開資料なし）

~~~diff
- 0052e3e8 ["COPY", "tmp:0:8", ["const:a37:8"]]
- 0052e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["COPY", "tmp:0:8", ["const:9aa:8"]]
+ 0052e3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052e3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052e3e8 bytes 08dd2891
+ 0052e3e8 bytes 08a92691
- 0052e3ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0052e3ec bytes 09ecfff0
+ 0052e3ec ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0052e3ec bytes 09ecfff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ddd9bc5697c695d92a8ec93bc54489b5"></a>

### [`0052eee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eee8.md) → [`0052eee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052eee8.md) FUN_0052eee8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b74c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b74c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052ef38",
      "incomplete_value": true,
      "site": "0052ef38",
      "value": [
        "LOAD",
        "8",
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
                "const:20:8"
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
      "definition_site": "0052ef28",
      "incomplete_value": true,
      "site": "0052ef38",
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
      "0052ef20",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "0052ef28",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0052ef20",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "0052ef28",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052ef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052eee8.md#insn-0052ef20)
- 新版 `0052ef20`（命令位置の公開資料なし）

~~~diff
- 0052ef20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 0052ef20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0052ef20 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 0052ef20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0052ef20 bytes 080142f9
+ 0052ef20 bytes 082942f9
~~~


<a id="compare-30b01bc1a087c62293cdf364b694107d"></a>

### [`0052f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md) → [`0052f034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md) FUN_0052f034

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f044",
      "incomplete_value": true,
      "site": "0052f050",
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
            "const:bd0:8"
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
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "const:c20:8"
              ]
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
      "definition_site": "0052f054",
      "incomplete_value": true,
      "site": "0052f058",
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
                "const:bd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0052f050",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f058",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0052f050",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f058",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md#insn-0052f044)
- 新版 `0052f044`（命令位置の公開資料なし）

~~~diff
- 0052f044 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0052f044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 0052f044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f044 bytes 08412f91
+ 0052f044 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-874572674ef19a7f2775f38c5bf38935"></a>

### [`0052f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md) → [`0052f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md) FUN_0052f0a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f0b4",
      "incomplete_value": false,
      "site": "0052f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f0b4",
      "incomplete_value": false,
      "site": "0052f0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
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
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0052f0c4",
      "incomplete_value": false,
      "site": "0052f0c8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:c20:8"
              ]
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
      "definition_site": "0052f0c4",
      "incomplete_value": false,
      "site": "0052f0c8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:bd0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0052f0c0",
      "DATA",
      [
        "storage",
        "00bedbd0",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f0c8",
      "DATA",
      [
        "storage",
        "00bedc38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0052f0c0",
      "DATA",
      [
        "storage",
        "00bedc20",
        null,
        "undefined *"
      ]
    ],
    [
      "0052f0c8",
      "DATA",
      [
        "storage",
        "00bedc88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md#insn-0052f0b4)
- 新版 `0052f0b4`（命令位置の公開資料なし）

~~~diff
- 0052f0b4 ["COPY", "tmp:0:8", ["const:bd0:8"]]
- 0052f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 0052f0b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0052f0b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0052f0b4 bytes 08412f91
+ 0052f0b4 bytes 08813091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce500338f90631ad03a7328b58a30b35"></a>

### [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) → [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) FUN_0052f11c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052e39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e39c.md) [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052e39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e39c.md) [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.54% / 新版 98.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052f284",
      "incomplete_value": false,
      "site": "0052f28c",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f284",
      "incomplete_value": false,
      "site": "0052f28c",
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
            "const:30a:8"
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
      "definition_site": "0052f3e4",
      "incomplete_value": false,
      "site": "0052f3ec",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f3e4",
      "incomplete_value": false,
      "site": "0052f3ec",
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
            "const:2ee:8"
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
      "definition_site": "0052f3fc",
      "incomplete_value": false,
      "site": "0052f408",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052f3fc",
      "incomplete_value": false,
      "site": "0052f408",
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
            "const:919:8"
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
      "0052f284",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0052f2a8",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0052f3e4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0052f284",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0052f2a8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0052f3e4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052f284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f284) · [`0052f2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f2a8) · [`0052f3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md#insn-0052f3e4)
- 新版 `0052f284`（命令位置の公開資料なし） · `0052f2a8`（命令位置の公開資料なし） · `0052f3e4`（命令位置の公開資料なし）

~~~diff
- 0052f284 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052f284 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f284 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f284 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0052f284 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f284 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f284 bytes 21280c91
+ 0052f284 bytes 21900e91
- 0052f2a8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0052f2a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f2a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f2a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f2a8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0052f2a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f2a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f2a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f2a8 bytes 21642491
+ 0052f2a8 bytes 21142291
- 0052f3e4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0052f3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0052f3e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052f3e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052f3e4 bytes 21b80b91
+ 0052f3e4 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c7f61f2ab35c12606932d185af4a6be"></a>

### [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) → [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) FUN_0052f968

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f11c.md) [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052f11c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f11c.md) [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0052facc",
      "incomplete_value": false,
      "site": "0052fad4",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052facc",
      "incomplete_value": false,
      "site": "0052fad4",
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
            "const:30a:8"
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
      "definition_site": "0052faf0",
      "incomplete_value": false,
      "site": "0052fafc",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052faf0",
      "incomplete_value": false,
      "site": "0052fafc",
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
            "const:919:8"
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
      "definition_site": "0052fc2c",
      "incomplete_value": false,
      "site": "0052fc34",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0052fc2c",
      "incomplete_value": false,
      "site": "0052fc34",
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
            "const:2ee:8"
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
      "0052facc",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0052faf0",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0052fc2c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0052facc",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0052faf0",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0052fc2c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0052facc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052facc) · [`0052faf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052faf0) · [`0052fc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md#insn-0052fc2c)
- 新版 `0052facc`（命令位置の公開資料なし） · `0052faf0`（命令位置の公開資料なし） · `0052fc2c`（命令位置の公開資料なし）

~~~diff
- 0052facc ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0052facc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052facc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052facc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0052facc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052facc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052facc bytes 21280c91
+ 0052facc bytes 21900e91
- 0052faf0 ["COPY", "tmp:0:8", ["const:919:8"]]
- 0052faf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052faf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052faf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052faf0 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0052faf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052faf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052faf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052faf0 bytes 21642491
+ 0052faf0 bytes 21142291
- 0052fc2c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0052fc2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0052fc2c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0052fc2c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0052fc2c bytes 21b80b91
+ 0052fc2c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc82802b262cc625ba923c9a7a028441"></a>

### [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) → [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) FUN_005301a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0052f968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f968.md) [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0052f968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f968.md) [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.52% / 新版 98.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530300",
      "incomplete_value": false,
      "site": "00530308",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530300",
      "incomplete_value": false,
      "site": "00530308",
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
            "const:30a:8"
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
      "definition_site": "00530324",
      "incomplete_value": false,
      "site": "00530330",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530324",
      "incomplete_value": false,
      "site": "00530330",
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
            "const:919:8"
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
      "definition_site": "00530460",
      "incomplete_value": false,
      "site": "00530468",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530460",
      "incomplete_value": false,
      "site": "00530468",
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
            "const:2ee:8"
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
      "00530300",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00530324",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00530460",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00530300",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00530324",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00530460",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530300) · [`00530324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530324) · [`00530460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md#insn-00530460)
- 新版 `00530300`（命令位置の公開資料なし） · `00530324`（命令位置の公開資料なし） · `00530460`（命令位置の公開資料なし）

~~~diff
- 00530300 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00530300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00530300 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530300 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530300 bytes 21280c91
+ 00530300 bytes 21900e91
- 00530324 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00530324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530324 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00530324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530324 bytes 21642491
+ 00530324 bytes 21142291
- 00530460 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00530460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00530460 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530460 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530460 bytes 21b80b91
+ 00530460 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85e05b6dde4d45bf5c0bce931df784b7"></a>

### [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) → [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) FUN_005309d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005301a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005301a0.md) [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005301a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005301a0.md) [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00530b30",
      "incomplete_value": false,
      "site": "00530b38",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530b30",
      "incomplete_value": false,
      "site": "00530b38",
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
            "const:30a:8"
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
      "definition_site": "00530b54",
      "incomplete_value": false,
      "site": "00530b60",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530b54",
      "incomplete_value": false,
      "site": "00530b60",
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
            "const:919:8"
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
      "definition_site": "00530c90",
      "incomplete_value": false,
      "site": "00530c98",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00530c90",
      "incomplete_value": false,
      "site": "00530c98",
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
            "const:2ee:8"
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
      "00530b30",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00530b54",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00530c90",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00530b30",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00530b54",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00530c90",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00530b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530b30) · [`00530b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530b54) · [`00530c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md#insn-00530c90)
- 新版 `00530b30`（命令位置の公開資料なし） · `00530b54`（命令位置の公開資料なし） · `00530c90`（命令位置の公開資料なし）

~~~diff
- 00530b30 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00530b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00530b30 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b30 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530b30 bytes 21280c91
+ 00530b30 bytes 21900e91
- 00530b54 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00530b54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530b54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530b54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530b54 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00530b54 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b54 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530b54 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530b54 bytes 21642491
+ 00530b54 bytes 21142291
- 00530c90 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00530c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00530c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00530c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00530c90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00530c90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00530c90 bytes 21b80b91
+ 00530c90 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30dc5b67fe2ca23091043471f34fe3ea"></a>

### [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) → [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) FUN_005311f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`005309d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00530/005309d4.md) [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`005309d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00530/005309d4.md) [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "00531348",
      "incomplete_value": false,
      "site": "00531350",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531348",
      "incomplete_value": false,
      "site": "00531350",
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
            "const:30a:8"
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
      "definition_site": "0053136c",
      "incomplete_value": false,
      "site": "00531378",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053136c",
      "incomplete_value": false,
      "site": "00531378",
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
            "const:919:8"
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
      "definition_site": "005314a4",
      "incomplete_value": false,
      "site": "005314ac",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005314a4",
      "incomplete_value": false,
      "site": "005314ac",
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
            "const:2ee:8"
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
      "00531348",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0053136c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "005314a4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00531348",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0053136c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "005314a4",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-00531348) · [`0053136c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-0053136c) · [`005314a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md#insn-005314a4)
- 新版 `00531348`（命令位置の公開資料なし） · `0053136c`（命令位置の公開資料なし） · `005314a4`（命令位置の公開資料なし）

~~~diff
- 00531348 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00531348 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531348 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531348 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00531348 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531348 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531348 bytes 21280c91
+ 00531348 bytes 21900e91
- 0053136c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0053136c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053136c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053136c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053136c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0053136c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053136c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053136c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053136c bytes 21642491
+ 0053136c bytes 21142291
- 005314a4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 005314a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 005314a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 005314a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 005314a4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 005314a4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 005314a4 bytes 21b80b91
+ 005314a4 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c812e70dab3b5e0104f2f89b57fe6efc"></a>

### [`005319f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md) → [`005319f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md) FUN_005319f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`005311f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005311f4.md) [`005319f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`005311f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005311f4.md) [`005319f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00531/005319f0.md) [`00829478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/00829478.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00531b40",
      "incomplete_value": false,
      "site": "00531b48",
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
            "const:3a4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531b40",
      "incomplete_value": false,
      "site": "00531b48",
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
            "const:30a:8"
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
      "definition_site": "00531c9c",
      "incomplete_value": false,
      "site": "00531ca4",
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
            "const:379:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531c9c",
      "incomplete_value": false,
      "site": "00531ca4",
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
            "const:2ee:8"
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
      "definition_site": "00531cb4",
      "incomplete_value": false,
      "site": "00531cc0",
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
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00531cb4",
      "incomplete_value": false,
      "site": "00531cc0",
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
            "const:919:8"
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
      "00531b40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00531b64",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00531c9c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00531b40",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00531b64",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00531c9c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00531b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531b40) · [`00531b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531b64) · [`00531c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00531/005319f0.md#insn-00531c9c)
- 新版 `00531b40`（命令位置の公開資料なし） · `00531b64`（命令位置の公開資料なし） · `00531c9c`（命令位置の公開資料なし）

~~~diff
- 00531b40 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00531b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00531b40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531b40 bytes 21280c91
+ 00531b40 bytes 21900e91
- 00531b64 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00531b64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531b64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531b64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531b64 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00531b64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531b64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531b64 bytes 21642491
+ 00531b64 bytes 21142291
- 00531c9c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00531c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00531c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00531c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00531c9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00531c9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00531c9c bytes 21b80b91
+ 00531c9c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42ca8dbb173480f11a9b10978f9f776b"></a>

### [`005321d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md) → [`005321d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005321d8.md) FUN_005321d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0052efd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052efd4.md) · 呼出先 6件 [`0052e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052e/0052e05c.md) [`0053233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053233c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0052efd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052efd4.md) · 呼出先 6件 [`0052e05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052e/0052e05c.md) [`0053233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053233c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00532210",
      "incomplete_value": false,
      "site": "0053222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532210",
      "incomplete_value": false,
      "site": "0053222c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "0053222c",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ],
    [
      "005322c0",
      "READ",
      [
        "storage",
        "00bedcd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053222c",
      "DATA",
      [
        "storage",
        "00bedd18",
        null,
        "pointer"
      ]
    ],
    [
      "005322c0",
      "READ",
      [
        "storage",
        "00bedd28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005321d8.md#insn-00532210)
- 新版 `00532210`（命令位置の公開資料なし）

~~~diff
- 00532210 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00532210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00532210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532210 bytes 08213391
+ 00532210 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a85e3ee8145b5db20d1c81cee9508a98"></a>

### [`005322fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005322fc.md) → [`005322fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005322fc.md) FUN_005322fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00532300",
      "incomplete_value": false,
      "site": "00532304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532300",
      "incomplete_value": false,
      "site": "00532304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00532304",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532304",
      "DATA",
      [
        "storage",
        "00bedd18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005322fc.md#insn-00532300)
- 新版 `00532300`（命令位置の公開資料なし）

~~~diff
- 00532300 ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 00532300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00532300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00532300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 00532300 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00532300 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00532300 bytes 08213391
+ 00532300 bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adab7e578281a0a11e5df1bf301329e0"></a>

### [`0053230c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053230c.md) → [`0053230c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053230c.md) FUN_0053230c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053231c",
      "incomplete_value": false,
      "site": "00532324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053231c",
      "incomplete_value": false,
      "site": "00532324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:cc8:8"
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
      "00532324",
      "DATA",
      [
        "storage",
        "00bedcc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00532324",
      "DATA",
      [
        "storage",
        "00bedd18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053231c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053230c.md#insn-0053231c)
- 新版 `0053231c`（命令位置の公開資料なし）

~~~diff
- 0053231c ["COPY", "tmp:0:8", ["const:cc8:8"]]
- 0053231c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053231c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053231c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["COPY", "tmp:0:8", ["const:d18:8"]]
+ 0053231c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053231c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053231c bytes 08213391
+ 0053231c bytes 08613491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22dbfd82eb9f93c63b4545f19f797a01"></a>

### [`0053239c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md) → [`0053239c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/0053239c.md) FUN_0053239c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056dee0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0056dee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056dee0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "005323a8",
      "incomplete_value": false,
      "site": "005323a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005323a8",
      "incomplete_value": false,
      "site": "005323a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d08:8"
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
      "005323a0",
      "READ",
      [
        "storage",
        "00c25d08",
        null,
        "undefined4"
      ]
    ],
    [
      "005323a8",
      "WRITE",
      [
        "storage",
        "00c25d08",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005323a0",
      "READ",
      [
        "storage",
        "00c25d48",
        null,
        "undefined4"
      ]
    ],
    [
      "005323a8",
      "WRITE",
      [
        "storage",
        "00c25d48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005323a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md#insn-005323a8) · [`005323a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053239c.md#insn-005323a0)
- 新版 `005323a8`（命令位置の公開資料なし） · `005323a0`（命令位置の公開資料なし）

~~~diff
- 005323a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
- 005323a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 005323a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
+ 005323a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 005323a8 bytes 09090db9
+ 005323a8 bytes 09490db9
- 005323a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d08:8"]]
- 005323a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 005323a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 005323a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
+ 005323a0 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 005323a0 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 005323a0 bytes 09094db9
+ 005323a0 bytes 09494db9
~~~


<a id="compare-7bb58515fcb8a7c32ef3ce381d796871"></a>

### [`005325a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md) → [`005325a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005325a0.md) FUN_005325a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005323ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323ec.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00449574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449574.md) [`00532f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532f34.md) [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md)
- 新版 呼出元 1件 [`005323ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323ec.md) · 呼出先 13件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00532670",
      "incomplete_value": true,
      "site": "00532670",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532670",
      "incomplete_value": true,
      "site": "00532670",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00532744",
      "incomplete_value": true,
      "site": "00532744",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00532744",
      "incomplete_value": true,
      "site": "00532744",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053281c",
      "incomplete_value": true,
      "site": "0053281c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053281c",
      "incomplete_value": true,
      "site": "0053281c",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "ordinal": 63,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "005325f8",
      "READ",
      [
        "storage",
        "00c25d68",
        null,
        "undefined1"
      ]
    ],
    [
      "00532600",
      "READ",
      [
        "storage",
        "00c25d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00532604",
      "WRITE",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005325f8",
      "READ",
      [
        "storage",
        "00c25da8",
        null,
        "undefined1"
      ]
    ],
    [
      "00532600",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00532604",
      "WRITE",
      [
        "storage",
        "00c25d98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00532670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-00532670) · [`00532744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-00532744) · [`0053281c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005325a0.md#insn-0053281c)
- 新版 `00532670`（命令位置の公開資料なし） · `00532744`（命令位置の公開資料なし） · `0053281c`（命令位置の公開資料なし）

~~~diff
- 00532670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 00532670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
+ 00532670 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
+ 00532670 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d8:8"]]
- 00532670 bytes 3bad06f9
+ 00532670 bytes 3bcd06f9
- 00532744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 00532744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
+ 00532744 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
+ 00532744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40d0:8"]]
- 00532744 bytes 3aad06f9
+ 00532744 bytes 3acd06f9
- 0053281c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d58:8"]]
- 0053281c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
+ 0053281c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d98:8"]]
+ 0053281c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40e0:8"]]
- 0053281c bytes 3cad06f9
+ 0053281c bytes 3ccd06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b6dc250c68d12ce96fa0e36c73a5e61"></a>

### [`00536a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md) → [`00536a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536a8c.md) FUN_00536a8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00537664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537664.md) · 呼出先 14件 [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00449588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449588.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md)
- 新版 呼出元 1件 [`00537664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537664.md) · 呼出先 14件 [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00449588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449588.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.58% / 新版 94.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00536bb0",
      "incomplete_value": false,
      "site": "00536bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536bb0",
      "incomplete_value": false,
      "site": "00536bb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00536c14",
      "incomplete_value": false,
      "site": "00536c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c14",
      "incomplete_value": false,
      "site": "00536c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00536c5c",
      "incomplete_value": false,
      "site": "00536c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00536c5c",
      "incomplete_value": false,
      "site": "00536c6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "00536ac4",
      "READ",
      [
        "storage",
        "00c25d28",
        null,
        "undefined1"
      ]
    ],
    [
      "00536acc",
      "READ",
      [
        "storage",
        "00c25d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00536ad0",
      "WRITE",
      [
        "storage",
        "00c25d18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00536ac4",
      "READ",
      [
        "storage",
        "00c25d68",
        null,
        "undefined1"
      ]
    ],
    [
      "00536acc",
      "READ",
      [
        "storage",
        "00c25d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00536ad0",
      "WRITE",
      [
        "storage",
        "00c25d58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00536ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ab8) · [`00536ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ac0) · [`00536ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536a8c.md#insn-00536ba8)
- 新版 `00536ab8`（命令位置の公開資料なし） · `00536ac0`（命令位置の公開資料なし） · `00536ba8`（命令位置の公開資料なし）

~~~diff
- 00536ab8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00536ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 00536ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00536ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00536ab8 bytes 08a13491
+ 00536ab8 bytes 08a13591
- 00536ac0 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00536ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00536ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00536ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00536ac0 bytes 73423491
+ 00536ac0 bytes 73423591
- 00536ba8 ["COPY", "tmp:0:8", ["const:d10:8"]]
- 00536ba8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00536ba8 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00536ba8 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00536ba8 bytes 94423491
+ 00536ba8 bytes 94423591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-662f71242f785534b003601b2e0d9dde"></a>

### [`00537560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md) → [`00537560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537560.md) FUN_00537560

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00445124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445124.md) · 呼出先 8件 [`00445610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445610.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md) [`0056d0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056d/0056d0d0.md)
- 新版 呼出元 1件 [`00445124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445124.md) · 呼出先 8件 [`00445610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445610.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00536d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/00536d38.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md) [`0056d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056d/0056d0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00537600",
      "incomplete_value": false,
      "site": "0053760c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537600",
      "incomplete_value": false,
      "site": "0053760c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d48:8"
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
      "definition_site": "00537630",
      "incomplete_value": false,
      "site": "00537640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537630",
      "incomplete_value": false,
      "site": "00537640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "definition_site": "00537648",
      "incomplete_value": false,
      "site": "0053764c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537648",
      "incomplete_value": false,
      "site": "0053764c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
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
      "00537578",
      "READ",
      [
        "storage",
        "00c25d48",
        null,
        "undefined1"
      ]
    ],
    [
      "00537588",
      "READ",
      [
        "storage",
        "00c25d30",
        null,
        "undefined8"
      ]
    ],
    [
      "00537598",
      "PARAM",
      [
        "storage",
        "00c25d30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00537578",
      "READ",
      [
        "storage",
        "00c25d88",
        null,
        "undefined1"
      ]
    ],
    [
      "00537588",
      "READ",
      [
        "storage",
        "00c25d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00537598",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md#insn-00537574) · [`0053757c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537560.md#insn-0053757c)
- 新版 `00537574`（命令位置の公開資料なし） · `0053757c`（命令位置の公開資料なし）

~~~diff
- 00537574 ["COPY", "tmp:0:8", ["const:d48:8"]]
- 00537574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00537574 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537574 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537574 bytes 08213591
+ 00537574 bytes 08213691
- 0053757c ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0053757c bytes 683700d0
+ 0053757c ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 0053757c bytes 683700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f81887322a142a336d8a94b35df45314"></a>

### [`005376d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005376d0.md) → [`005376d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005376d0.md) FUN_005376d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 4件 [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447c70.md) · 呼出先 0件 

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
      "definition_site": "005376d8",
      "incomplete_value": true,
      "site": "005376dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005376d8",
      "incomplete_value": true,
      "site": "005376dc",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "005376d8",
      "READ",
      [
        "storage",
        "00c26510",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005376d8",
      "READ",
      [
        "storage",
        "00c26550",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005376d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005376d0.md#insn-005376d4)
- 新版 `005376d4`（命令位置の公開資料なし）

~~~diff
- 005376d4 ["COPY", "tmp:0:8", ["const:510:8"]]
- 005376d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005376d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["COPY", "tmp:0:8", ["const:550:8"]]
+ 005376d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005376d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005376d4 bytes 08411491
+ 005376d4 bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16d0159e76a1736c7ba315a3cc963623"></a>

### [`00537724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md) → [`00537724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537724.md) FUN_00537724

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00444ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444ee4.md) [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447c70.md) · 呼出先 0件 
- 新版 呼出元 5件 [`00444ee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444ee4.md) [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md) [`00445f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445f48.md) [`00447b24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447b24.md) [`00447c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447c70.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00537744",
      "incomplete_value": true,
      "site": "00537744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:478:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00537744",
      "incomplete_value": true,
      "site": "00537744",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:428:8"
              ]
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
      "00537730",
      "READ",
      [
        "storage",
        "00c1b400",
        null,
        "pointer"
      ]
    ],
    [
      "00537734",
      "READ",
      [
        "storage",
        "00c26610",
        null,
        "undefined8"
      ]
    ],
    [
      "0053773c",
      "READ",
      [
        "storage",
        "00c1b428",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00537730",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "00537734",
      "READ",
      [
        "storage",
        "00c26650",
        null,
        "undefined8"
      ]
    ],
    [
      "0053773c",
      "READ",
      [
        "storage",
        "00c1b478",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md#insn-00537730) · [`0053773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537724.md#insn-0053773c)
- 新版 `00537730`（命令位置の公開資料なし） · `0053773c`（命令位置の公開資料なし）

~~~diff
- 00537730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:400:8"]]
- 00537730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537730 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:450:8"]]
+ 00537730 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537730 bytes 080142f9
+ 00537730 bytes 082942f9
- 0053773c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:428:8"]]
- 0053773c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053773c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:478:8"]]
+ 0053773c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053773c bytes 291542f9
+ 0053773c bytes 293d42f9
~~~


<a id="compare-88f8bdc7f22dda803986f4a9d6efabad"></a>

### [`0053774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md) → [`0053774c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053774c.md) FUN_0053774c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00444a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444a94.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445044.md) · 呼出先 0件 
- 新版 呼出元 3件 [`00444a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444a94.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00445044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445044.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
              ],
              [
                "leaf",
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1b000:8"
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053775c",
      "incomplete_value": true,
      "site": "0053775c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053776c",
      "incomplete_value": true,
      "site": "0053776c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0053776c",
      "incomplete_value": true,
      "site": "0053776c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:8:8"
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
      "00537758",
      "READ",
      [
        "storage",
        "00c1b430",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23ee8",
        null,
        "undefined4"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23eec",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537758",
      "READ",
      [
        "storage",
        "00c1b480",
        null,
        "pointer"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23f38",
        null,
        "undefined4"
      ]
    ],
    [
      "0053775c",
      "WRITE",
      [
        "storage",
        "00c23f3c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md#insn-00537758) · [`00537768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053774c.md#insn-00537768)
- 新版 `00537758`（命令位置の公開資料なし） · `00537768`（命令位置の公開資料なし）

~~~diff
- 00537758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:430:8"]]
- 00537758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537758 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:480:8"]]
+ 00537758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00537758 bytes 081942f9
+ 00537758 bytes 084142f9
- 00537768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:408:8"]]
- 00537768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00537768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:458:8"]]
+ 00537768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00537768 bytes 290542f9
+ 00537768 bytes 292d42f9
~~~


<a id="compare-8eb5b0364e43c11c0ac539d9a9510b2f"></a>

### [`005377dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377dc.md) → [`005377dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377dc.md) FUN_005377dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 0件 

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
      "definition_site": "005377e4",
      "incomplete_value": true,
      "site": "005377e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005377e4",
      "incomplete_value": true,
      "site": "005377e8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "005377e4",
      "READ",
      [
        "storage",
        "00c26560",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005377e4",
      "READ",
      [
        "storage",
        "00c265a0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377dc.md#insn-005377e0)
- 新版 `005377e0`（命令位置の公開資料なし）

~~~diff
- 005377e0 ["COPY", "tmp:0:8", ["const:560:8"]]
- 005377e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 005377e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005377e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377e0 bytes 08811591
+ 005377e0 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7742c3c399e1a278702c8b60f43f24bc"></a>

### [`005377ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377ec.md) → [`005377ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377ec.md) FUN_005377ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005f2980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a4/008a4e38.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 0件 
- 新版 呼出元 5件 [`005f2980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005f2/005f2980.md) [`00877a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00877/00877a44.md) [`00878b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00878/00878b14.md) [`008a4e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a4/008a4e38.md) [`00accf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acc/00accf90.md) · 呼出先 0件 

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
      "definition_site": "005377f4",
      "incomplete_value": true,
      "site": "005377f8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "005377f4",
      "incomplete_value": true,
      "site": "005377f8",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "005377f4",
      "READ",
      [
        "storage",
        "00c2655c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "005377f4",
      "READ",
      [
        "storage",
        "00c2659c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377ec.md#insn-005377f0)
- 新版 `005377f0`（命令位置の公開資料なし）

~~~diff
- 005377f0 ["COPY", "tmp:0:8", ["const:55c:8"]]
- 005377f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005377f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["COPY", "tmp:0:8", ["const:59c:8"]]
+ 005377f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005377f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005377f0 bytes 08711591
+ 005377f0 bytes 08711691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56a8fbe0ad8a87d44b2e8e477b74353a"></a>

### [`005377fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377fc.md) → [`005377fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/005377fc.md) FUN_005377fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 0件 

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
      "definition_site": "00537804",
      "incomplete_value": true,
      "site": "00537808",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00537804",
      "incomplete_value": true,
      "site": "00537808",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "00537804",
      "READ",
      [
        "storage",
        "00c26568",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537804",
      "READ",
      [
        "storage",
        "00c265a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/005377fc.md#insn-00537800)
- 新版 `00537800`（命令位置の公開資料なし）

~~~diff
- 00537800 ["COPY", "tmp:0:8", ["const:568:8"]]
- 00537800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00537800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537800 bytes 08a11591
+ 00537800 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ba372b4a474fd788ef18e5a5707328"></a>

### [`0053780c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053780c.md) → [`0053780c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053780c.md) FUN_0053780c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 0件 

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
      "definition_site": "00537814",
      "incomplete_value": true,
      "site": "00537818",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "definition_site": "00537814",
      "incomplete_value": true,
      "site": "00537818",
      "value": [
        "INT_ZEXT",
        "8",
        [
          [
            "LOAD",
            "4",
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
      "00537814",
      "READ",
      [
        "storage",
        "00c26564",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00537814",
      "READ",
      [
        "storage",
        "00c265a4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00537810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053780c.md#insn-00537810)
- 新版 `00537810`（命令位置の公開資料なし）

~~~diff
- 00537810 ["COPY", "tmp:0:8", ["const:564:8"]]
- 00537810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00537810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00537810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["COPY", "tmp:0:8", ["const:5a4:8"]]
+ 00537810 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00537810 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00537810 bytes 08911591
+ 00537810 bytes 08911691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1f7ee54befedcebcdd1f122cef7f9c6"></a>

### [`00538260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538260.md) → [`00538260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538260.md) FUN_00538260

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0053826c",
      "incomplete_value": false,
      "site": "00538270",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053826c",
      "incomplete_value": false,
      "site": "00538270",
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
            "const:303:8"
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
      "0053826c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053826c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053826c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538260.md#insn-0053826c)
- 新版 `0053826c`（命令位置の公開資料なし）

~~~diff
- 0053826c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0053826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0053826c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053826c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053826c bytes 000c0c91
+ 0053826c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e56d5937b1db6d9a0be0b4256b6c503a"></a>

### [`00538274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538274.md) → [`00538274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538274.md) FUN_00538274

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0053781c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0053781c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/0053781c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00538280",
      "incomplete_value": false,
      "site": "00538284",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00538280",
      "incomplete_value": false,
      "site": "00538284",
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
            "const:303:8"
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
      "00538280",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00538280",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538274.md#insn-00538280)
- 新版 `00538280`（命令位置の公開資料なし）

~~~diff
- 00538280 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00538280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00538280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00538280 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00538280 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00538280 bytes 000c0c91
+ 00538280 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-391a71f10b9bacb4ae24d7bd63894611"></a>

### [`00538370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538370.md) → [`00538370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538370.md) FUN_00538370

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`005323ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/005323ec.md) [`00532dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532dbc.md) [`00532f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/00532f34.md) [`0053699c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00536/0053699c.md) [`00537068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00537/00537068.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 5件 [`005323ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/005323ec.md) [`00532dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532dbc.md) [`00532f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00532/00532f34.md) [`0053699c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00536/0053699c.md) [`00537068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00537/00537068.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0053837c",
      "incomplete_value": false,
      "site": "00538380",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053837c",
      "incomplete_value": false,
      "site": "00538380",
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
            "const:303:8"
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
      "0053837c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053837c",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053837c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538370.md#insn-0053837c)
- 新版 `0053837c`（命令位置の公開資料なし）

~~~diff
- 0053837c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0053837c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053837c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0053837c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053837c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053837c bytes 000c0c91
+ 0053837c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a798db4e331c3955ba38a52b0873472e"></a>

### [`00538384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md) → [`00538384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538384.md) FUN_00538384

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00539488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md) · 呼出先 5件 [`005384a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/005384a8.md) [`005397fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539804.md) [`0053b668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b668.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`00539488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md) · 呼出先 5件 [`005384a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/005384a8.md) [`005397fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005397fc.md) [`00539804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539804.md) [`0053b668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b668.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005383a4",
      "incomplete_value": false,
      "site": "005383a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383a4",
      "incomplete_value": false,
      "site": "005383a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
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
      "definition_site": "005383c0",
      "incomplete_value": false,
      "site": "005383c0",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "005383a4",
      "DATA",
      [
        "storage",
        "00bede28",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005383a4",
      "DATA",
      [
        "storage",
        "00bede78",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "005383c0",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00538398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md#insn-00538398) · [`005383b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md#insn-005383b0)
- 新版 `00538398`（命令位置の公開資料なし） · `005383b0`（命令位置の公開資料なし）

~~~diff
- 00538398 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00538398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00538398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00538398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00538398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00538398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00538398 bytes 08a13891
+ 00538398 bytes 08e13991
- 005383b0 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 005383b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005383b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005383b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 005383b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005383b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005383b0 bytes 08e13491
+ 005383b0 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28340fbe3704c33955b62749b413bacf"></a>

### [`00539488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md) → [`00539488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539488.md) FUN_00539488

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`004665d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00466/004665d0.md) [`00a3b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a3b/00a3b374.md) · 呼出先 2件 [`00538384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00538/00538384.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`004665d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00466/004665d0.md) [`00a3b3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a3b/00a3b3b8.md) · 呼出先 2件 [`00538384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00538/00538384.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "005394b8",
      "incomplete_value": false,
      "site": "005394c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005394b8",
      "incomplete_value": false,
      "site": "005394c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "005394c4",
      "DATA",
      [
        "storage",
        "00bede50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005394c4",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005394b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539488.md#insn-005394b8)
- 新版 `005394b8`（命令位置の公開資料なし）

~~~diff
- 005394b8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 005394b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005394b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005394b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 005394b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005394b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005394b8 bytes 08413991
+ 005394b8 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9df49795c45f23632ddcf793b0591626"></a>

### [`0053950c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md) → [`0053950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md) FUN_0053950c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539520",
      "incomplete_value": false,
      "site": "0053952c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539520",
      "incomplete_value": false,
      "site": "0053952c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "00539538",
      "incomplete_value": false,
      "site": "00539538",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
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
      "definition_site": "00539538",
      "incomplete_value": false,
      "site": "00539538",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "0053952c",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00539538",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053952c",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "00539538",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md#insn-00539520) · [`00539528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md#insn-00539528)
- 新版 `00539520`（命令位置の公開資料なし） · `00539528`（命令位置の公開資料なし）

~~~diff
- 00539520 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00539520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00539520 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539520 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539520 bytes 08e13491
+ 00539520 bytes 08213691
- 00539528 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00539528 bytes f40300aa
+ 00539528 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00539528 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-278193cb7bb94127818d1989758cb86f"></a>

### [`005395ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md) → [`005395ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md) FUN_005395ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005395c0",
      "incomplete_value": false,
      "site": "005395cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005395c0",
      "incomplete_value": false,
      "site": "005395cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "005395d8",
      "incomplete_value": false,
      "site": "005395d8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
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
      "definition_site": "005395d8",
      "incomplete_value": false,
      "site": "005395d8",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "005395cc",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "005395d8",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005395cc",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "005395d8",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005395c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md#insn-005395c0) · [`005395c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md#insn-005395c8)
- 新版 `005395c0`（命令位置の公開資料なし） · `005395c8`（命令位置の公開資料なし）

~~~diff
- 005395c0 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 005395c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005395c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 005395c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005395c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005395c0 bytes 08e13491
+ 005395c0 bytes 08213691
- 005395c8 ["COPY", "register:4098:8", ["register:4000:8"]]
- 005395c8 bytes f30300aa
+ 005395c8 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 005395c8 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36fe2569072343915ee185aaa75ec98c"></a>

### [`00539654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md) → [`00539654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md) FUN_00539654

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d88:8"
              ]
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
      "definition_site": "00539674",
      "incomplete_value": false,
      "site": "00539674",
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
                "const:bed000:8"
              ],
              [
                "leaf",
                "const:d38:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "00539674",
      "DATA",
      [
        "storage",
        "00bedd38",
        null,
        "undefined *"
      ]
    ],
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00bedda0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00bedd88",
        null,
        "undefined *"
      ]
    ],
    [
      "00539674",
      "DATA",
      [
        "storage",
        "00beddf0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md#insn-00539664)
- 新版 `00539664`（命令位置の公開資料なし）

~~~diff
- 00539664 ["COPY", "tmp:0:8", ["const:d38:8"]]
- 00539664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00539664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539664 bytes 08e13491
+ 00539664 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9601be55dd4849a80f44ed38c3fa20d"></a>

### [`0053978c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053978c.md) → [`0053978c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053978c.md) FUN_0053978c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00539790",
      "incomplete_value": false,
      "site": "00539794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539790",
      "incomplete_value": false,
      "site": "00539794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "00539794",
      "DATA",
      [
        "storage",
        "00bede50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539794",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053978c.md#insn-00539790)
- 新版 `00539790`（命令位置の公開資料なし）

~~~diff
- 00539790 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00539790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00539790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539790 bytes 08413991
+ 00539790 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e5c4738015c8cba813c720284abdffc"></a>

### [`0053994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053994c.md) → [`0053994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053994c.md) FUN_0053994c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00539958",
      "incomplete_value": false,
      "site": "0053995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539958",
      "incomplete_value": false,
      "site": "0053995c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "0053995c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053995c",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053994c.md#insn-00539958)
- 新版 `00539958`（命令位置の公開資料なし）

~~~diff
- 00539958 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00539958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539958 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00539958 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539958 bytes 29813a91
+ 00539958 bytes 29c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f0c369b8acf7094b3454e28be9a05fc"></a>

### [`00539970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539970.md) → [`00539970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539970.md) FUN_00539970

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00539978",
      "incomplete_value": false,
      "site": "0053997c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539978",
      "incomplete_value": false,
      "site": "0053997c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "0053997c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053997c",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539970.md#insn-00539978)
- 新版 `00539978`（命令位置の公開資料なし）

~~~diff
- 00539978 ["COPY", "tmp:0:8", ["const:ea0:8"]]
- 00539978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00539978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["COPY", "tmp:0:8", ["const:ef0:8"]]
+ 00539978 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00539978 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00539978 bytes 29813a91
+ 00539978 bytes 29c13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bb2eecebde6d12c81d5f3d76c5fc0ff"></a>

### [`00539adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539adc.md) → [`00539adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539adc.md) FUN_00539adc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00539ae0",
      "incomplete_value": false,
      "site": "00539ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539ae0",
      "incomplete_value": false,
      "site": "00539ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "00539ae4",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539ae4",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539adc.md#insn-00539ae0)
- 新版 `00539ae0`（命令位置の公開資料なし）

~~~diff
- 00539ae0 ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00539ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00539ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539ae0 bytes 08c13b91
+ 00539ae0 bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6731da7a53914280e21832e0ff1b0eb2"></a>

### [`00539aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539aec.md) → [`00539aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539aec.md) FUN_00539aec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00539afc",
      "incomplete_value": false,
      "site": "00539b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539afc",
      "incomplete_value": false,
      "site": "00539b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "00539b04",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539b04",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539aec.md#insn-00539afc)
- 新版 `00539afc`（命令位置の公開資料なし）

~~~diff
- 00539afc ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00539afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00539afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539afc bytes 08c13b91
+ 00539afc bytes 08013d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee92ed04e80674f30b034acff388d65c"></a>

### [`00539b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md) → [`00539b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539b2c.md) FUN_00539b2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`005398ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005398ec.md) · 呼出先 3件 [`005399b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005399b0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`005398ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005398ec.md) · 呼出先 3件 [`005399b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005399b0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 86.05% / 新版 86.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539b5c",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b5c",
      "incomplete_value": false,
      "site": "00539b68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
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
      "definition_site": "00539b7c",
      "incomplete_value": false,
      "site": "00539b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539b7c",
      "incomplete_value": false,
      "site": "00539b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:ea0:8"
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
      "00539b68",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ],
    [
      "00539b7c",
      "DATA",
      [
        "storage",
        "00bedea0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539b68",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "00539b7c",
      "DATA",
      [
        "storage",
        "00bedef0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md#insn-00539b5c) · [`00539b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539b2c.md#insn-00539b6c)
- 新版 `00539b5c`（命令位置の公開資料なし） · `00539b6c`（命令位置の公開資料なし）

~~~diff
- 00539b5c ["COPY", "tmp:0:8", ["const:ef0:8"]]
- 00539b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00539b5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539b5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539b5c bytes 08c13b91
+ 00539b5c bytes 08013d91
- 00539b6c ["COPY", "register:4040:8", ["const:bed000:8"]]
- 00539b6c bytes a8350090
+ 00539b6c ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 00539b6c bytes a8350090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c266d3afda9d719abd634360c4119992"></a>

### [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) → [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) FUN_00539c08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053a518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md) · 呼出先 11件 [`00449574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449574.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`0053a5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`0053a518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md) · 呼出先 11件 [`00449574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449574.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`0053a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.50% / 新版 96.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00539c38",
      "incomplete_value": false,
      "site": "00539c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c38",
      "incomplete_value": false,
      "site": "00539c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "definition_site": "00539c8c",
      "incomplete_value": false,
      "site": "00539c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00539c8c",
      "incomplete_value": false,
      "site": "00539c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "00539c44",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ],
    [
      "00539c98",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00539c44",
      "DATA",
      [
        "storage",
        "00bedf90",
        null,
        "undefined *"
      ]
    ],
    [
      "00539c98",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00539c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md#insn-00539c38) · [`00539c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md#insn-00539c3c)
- 新版 `00539c38`（命令位置の公開資料なし） · `00539c3c`（命令位置の公開資料なし）

~~~diff
- 00539c38 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00539c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00539c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 00539c38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00539c38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00539c38 bytes 08013d91
+ 00539c38 bytes 08413e91
- 00539c3c ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00539c3c bytes f40300aa
+ 00539c3c ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00539c3c bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57f5ce96ef92d05092407da6621e6397"></a>

### [`0053a518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md) → [`0053a518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a518.md) FUN_0053a518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00444d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444d18.md) · 呼出先 2件 [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00444d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444d18.md) · 呼出先 2件 [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053a54c",
      "incomplete_value": false,
      "site": "0053a558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a54c",
      "incomplete_value": false,
      "site": "0053a558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053a558",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a558",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a518.md#insn-0053a54c)
- 新版 `0053a54c`（命令位置の公開資料なし）

~~~diff
- 0053a54c ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053a54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0053a54c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a54c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a54c bytes 08410091
+ 0053a54c bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8d216c58b65fa15c687635748117b29"></a>

### [`0053a5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5a4.md) → [`0053a5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5a4.md) FUN_0053a5a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053a5a8",
      "incomplete_value": false,
      "site": "0053a5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a5a8",
      "incomplete_value": false,
      "site": "0053a5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "0053a5ac",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a5ac",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5a4.md#insn-0053a5a8)
- 新版 `0053a5a8`（命令位置の公開資料なし）

~~~diff
- 0053a5a8 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 0053a5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0053a5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a5a8 bytes 08013e91
+ 0053a5a8 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45226137b7e7037032c4052bda147541"></a>

### [`0053a5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5b4.md) → [`0053a5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5b4.md) FUN_0053a5b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053a5c4",
      "incomplete_value": false,
      "site": "0053a5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a5c4",
      "incomplete_value": false,
      "site": "0053a5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "0053a5cc",
      "DATA",
      [
        "storage",
        "00bedf80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a5cc",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5b4.md#insn-0053a5c4)
- 新版 `0053a5c4`（命令位置の公開資料なし）

~~~diff
- 0053a5c4 ["COPY", "tmp:0:8", ["const:f80:8"]]
- 0053a5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["COPY", "tmp:0:8", ["const:fd0:8"]]
+ 0053a5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a5c4 bytes 08013e91
+ 0053a5c4 bytes 08413f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6420e0735c881f7e2f057bec7449c3eb"></a>

### [`0053a5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md) → [`0053a5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053a/0053a5f0.md) FUN_0053a5f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00539c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539c08.md) · 呼出先 1件 [`0053b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b028.md)
- 新版 呼出元 1件 [`00539c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539c08.md) · 呼出先 1件 [`0053b028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b028.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053a60c",
      "incomplete_value": true,
      "site": "0053a610",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053a60c",
      "incomplete_value": true,
      "site": "0053a610",
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
            "const:fd0:8"
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
      "0053a610",
      "DATA",
      [
        "storage",
        "00bedfd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053a610",
      "DATA",
      [
        "storage",
        "00bee020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053a608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md#insn-0053a608) · [`0053a60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053a/0053a5f0.md#insn-0053a60c)
- 新版 `0053a608`（命令位置の公開資料なし） · `0053a60c`（命令位置の公開資料なし）

~~~diff
- 0053a608 ["COPY", "register:4040:8", ["const:bed000:8"]]
+ 0053a608 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053a608 bytes 883500f0
+ 0053a608 bytes a8350090
- 0053a60c ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 0053a60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053a60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["COPY", "tmp:0:8", ["const:20:8"]]
+ 0053a60c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053a60c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053a60c bytes 08413f91
+ 0053a60c bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d32ec54d3ebf35685af1da97d85c337"></a>

### [`0053b5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5a4.md) → [`0053b5a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5a4.md) FUN_0053b5a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053b5a8",
      "incomplete_value": false,
      "site": "0053b5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5a8",
      "incomplete_value": false,
      "site": "0053b5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053b5ac",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b5ac",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5a4.md#insn-0053b5a8)
- 新版 `0053b5a8`（命令位置の公開資料なし）

~~~diff
- 0053b5a8 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0053b5a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5a8 bytes 08410091
+ 0053b5a8 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9902c6185495e7dc9397804434a7a100"></a>

### [`0053b5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5b4.md) → [`0053b5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5b4.md) FUN_0053b5b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053b5c4",
      "incomplete_value": false,
      "site": "0053b5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5c4",
      "incomplete_value": false,
      "site": "0053b5cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053b5cc",
      "DATA",
      [
        "storage",
        "00bee010",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b5cc",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5b4.md#insn-0053b5c4)
- 新版 `0053b5c4`（命令位置の公開資料なし）

~~~diff
- 0053b5c4 ["COPY", "tmp:0:8", ["const:10:8"]]
- 0053b5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["COPY", "tmp:0:8", ["const:60:8"]]
+ 0053b5c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5c4 bytes 08410091
+ 0053b5c4 bytes 08810191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-270506cd3a5cee09d5094238ac215210"></a>

### [`0053b5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5e4.md) → [`0053b5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b5e4.md) FUN_0053b5e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053b5fc",
      "incomplete_value": false,
      "site": "0053b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b5fc",
      "incomplete_value": false,
      "site": "0053b600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bed000:8"
          ],
          [
            "leaf",
            "const:f40:8"
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
      "0053b600",
      "DATA",
      [
        "storage",
        "00bedf40",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b600",
      "DATA",
      [
        "storage",
        "00bedf90",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b5e4.md#insn-0053b5fc)
- 新版 `0053b5fc`（命令位置の公開資料なし）

~~~diff
- 0053b5fc ["COPY", "tmp:0:8", ["const:f40:8"]]
- 0053b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["COPY", "tmp:0:8", ["const:f90:8"]]
+ 0053b5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b5fc bytes 08013d91
+ 0053b5fc bytes 08413e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8c8efb23be12e5a6d27b84d20d2072e"></a>

### [`0053b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md) → [`0053b6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053b6d4.md) FUN_0053b6d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0052f034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f034.md) [`0052f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052f/0052f0a4.md) [`0053950c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/0053950c.md) [`005395ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/005395ac.md) [`00539654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00539/00539654.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 6件 [`0052f034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f034.md) [`0052f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052f/0052f0a4.md) [`0053950c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/0053950c.md) [`005395ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/005395ac.md) [`00539654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00539/00539654.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0053b6e8",
      "incomplete_value": false,
      "site": "0053b6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053b6e8",
      "incomplete_value": false,
      "site": "0053b6ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "0053b6ec",
      "DATA",
      [
        "storage",
        "00bee060",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053b6ec",
      "DATA",
      [
        "storage",
        "00bee0b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053b6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053b6d4.md#insn-0053b6e8)
- 新版 `0053b6e8`（命令位置の公開資料なし）

~~~diff
- 0053b6e8 ["COPY", "tmp:0:8", ["const:60:8"]]
- 0053b6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["COPY", "tmp:0:8", ["const:b0:8"]]
+ 0053b6e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053b6e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053b6e8 bytes 08810191
+ 0053b6e8 bytes 08c10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5debc13f7cee33e681e7009bd1a70fe7"></a>

### [`0053be30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md) → [`0053be30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053be30.md) FUN_0053be30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0046a54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a54c.md) · 呼出先 7件 [`0055e5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0055e/0055e5bc.md) [`00574740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574740.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0046a54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046a/0046a54c.md) · 呼出先 7件 [`0055e5bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0055e/0055e5bc.md) [`00574740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574740.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.00% / 新版 97.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053c024",
      "incomplete_value": false,
      "site": "0053c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c024",
      "incomplete_value": false,
      "site": "0053c02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "definition_site": "0053c050",
      "incomplete_value": false,
      "site": "0053c050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c050",
      "incomplete_value": false,
      "site": "0053c050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "definition_site": "0053c06c",
      "incomplete_value": false,
      "site": "0053c06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c06c",
      "incomplete_value": false,
      "site": "0053c06c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "0053c02c",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c050",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c06c",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c02c",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c050",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ],
    [
      "0053c06c",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c024) · [`0053c044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c044) · [`0053c064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053be30.md#insn-0053c064)
- 新版 `0053c024`（命令位置の公開資料なし） · `0053c044`（命令位置の公開資料なし） · `0053c064`（命令位置の公開資料なし）

~~~diff
- 0053c024 ["COPY", "tmp:0:8", ["const:138:8"]]
- 0053c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0053c024 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c024 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c024 bytes 08e10491
+ 0053c024 bytes 08210691
- 0053c044 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0053c044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0053c044 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c044 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c044 bytes 08010391
+ 0053c044 bytes 08410491
- 0053c064 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0053c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0053c064 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c064 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c064 bytes 08010391
+ 0053c064 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82fbf657938f53fb2972b4941ffa2dd7"></a>

### [`0053c470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c470.md) → [`0053c470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c470.md) FUN_0053c470

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0053c488",
      "incomplete_value": false,
      "site": "0053c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c488",
      "incomplete_value": false,
      "site": "0053c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "0053c48c",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c48c",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c470.md#insn-0053c488)
- 新版 `0053c488`（命令位置の公開資料なし）

~~~diff
- 0053c488 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0053c488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0053c488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c488 bytes 08010391
+ 0053c488 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c634e7914154c2b2d3c851275b604db2"></a>

### [`0053c50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c50c.md) → [`0053c50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c50c.md) FUN_0053c50c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053c524",
      "incomplete_value": false,
      "site": "0053c528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c524",
      "incomplete_value": false,
      "site": "0053c528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:c0:8"
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
      "0053c528",
      "DATA",
      [
        "storage",
        "00bee0c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c528",
      "DATA",
      [
        "storage",
        "00bee110",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c50c.md#insn-0053c524)
- 新版 `0053c524`（命令位置の公開資料なし）

~~~diff
- 0053c524 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0053c524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0053c524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c524 bytes 08010391
+ 0053c524 bytes 08410491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d13882433c83929da45c6190c69ed9"></a>

### [`0053c598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c598.md) → [`0053c598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c598.md) FUN_0053c598

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053c59c",
      "incomplete_value": false,
      "site": "0053c5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c59c",
      "incomplete_value": false,
      "site": "0053c5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "0053c5a0",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c5a0",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c598.md#insn-0053c59c)
- 新版 `0053c59c`（命令位置の公開資料なし）

~~~diff
- 0053c59c ["COPY", "tmp:0:8", ["const:138:8"]]
- 0053c59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0053c59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c59c bytes 08e10491
+ 0053c59c bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8215a7bb2e11cf1d3cdad9f3a0c6ece"></a>

### [`0053c5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5a8.md) → [`0053c5a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5a8.md) FUN_0053c5a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053c5b8",
      "incomplete_value": false,
      "site": "0053c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c5b8",
      "incomplete_value": false,
      "site": "0053c5c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:138:8"
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
      "0053c5c0",
      "DATA",
      [
        "storage",
        "00bee138",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053c5c0",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5a8.md#insn-0053c5b8)
- 新版 `0053c5b8`（命令位置の公開資料なし）

~~~diff
- 0053c5b8 ["COPY", "tmp:0:8", ["const:138:8"]]
- 0053c5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 0053c5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c5b8 bytes 08e10491
+ 0053c5b8 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7e8c58c0a3fcec27beb92a4fbad98f"></a>

### [`0053c5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md) → [`0053c5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c5ec.md) FUN_0053c5ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 18件 [`0045d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d484.md) [`0045d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d518.md) [`0045d5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d5ac.md) [`0045d750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d750.md) [`0045d7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045d/0045d7e4.md) · 呼出先 2件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 18件 [`0045d484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d484.md) [`0045d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d518.md) [`0045d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d5ac.md) [`0045d750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d750.md) [`0045d7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045d/0045d7e4.md) · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination

命令の説明率　旧版 68.18% / 新版 68.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053c634",
      "incomplete_value": true,
      "site": "0053c634",
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
            "const:db4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c634",
      "incomplete_value": true,
      "site": "0053c634",
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
            "const:d74:8"
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
      "definition_site": "0053c618",
      "incomplete_value": false,
      "site": "0053c61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c618",
      "incomplete_value": false,
      "site": "0053c61c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "definition_site": "0053c630",
      "incomplete_value": false,
      "site": "0053c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c630",
      "incomplete_value": false,
      "site": "0053c638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d78:8"
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
      "0053c5fc",
      "READ",
      [
        "storage",
        "00c25d78",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c608",
      "READ",
      [
        "storage",
        "00c25d74",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c618",
      "PARAM",
      [
        "storage",
        "00c25d78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c5fc",
      "READ",
      [
        "storage",
        "00c25db8",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c608",
      "READ",
      [
        "storage",
        "00c25db4",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c618",
      "PARAM",
      [
        "storage",
        "00c25db8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md#insn-0053c634) · [`0053c5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md#insn-0053c5f8) · [`0053c600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5ec.md#insn-0053c600)
- 新版 `0053c634`（命令位置の公開資料なし） · `0053c5f8`（命令位置の公開資料なし）

~~~diff
- 0053c634 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 0053c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:d74:8"]]
- 0053c634 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0053c634 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 0053c634 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:db4:8"]]
+ 0053c634 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0053c634 bytes 09d13539
+ 0053c634 bytes 09d13639
- 0053c5f8 ["COPY", "tmp:0:8", ["const:d78:8"]]
- 0053c5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0053c5f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c5f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c5f8 bytes 08e13591
+ 0053c5f8 bytes 08e13691
- 0053c600 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0053c600 bytes 483700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44cb6cc5622ed2ddf6cc59b65ad1f788"></a>

### [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) → [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) FUN_0053c6a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md) [`00a412d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a41/00a412d8.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d590.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 2件 [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md) [`00a4131c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a41/00a4131c.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 79.41% / 新版 79.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c6e4",
      "incomplete_value": true,
      "site": "0053c6e8",
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
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c6e4",
      "incomplete_value": true,
      "site": "0053c6e8",
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
            "const:d90:8"
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
      "definition_site": "0053c708",
      "incomplete_value": false,
      "site": "0053c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c708",
      "incomplete_value": false,
      "site": "0053c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "definition_site": "0053c710",
      "incomplete_value": false,
      "site": "0053c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c710",
      "incomplete_value": false,
      "site": "0053c714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "0053c6b8",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c6c4",
      "READ",
      [
        "storage",
        "00c25d80",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c6e4",
      "PARAM",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c6b8",
      "READ",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c6c4",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c6e4",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6b0) · [`0053c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6c4) · [`0053c6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md#insn-0053c6e4)
- 新版 `0053c6b0`（命令位置の公開資料なし） · `0053c6c4`（命令位置の公開資料なし） · `0053c6e4`（命令位置の公開資料なし）

~~~diff
- 0053c6b0 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0053c6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0053c6b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c6b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c6b0 bytes 08413691
+ 0053c6b0 bytes 08413791
- 0053c6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 0053c6c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c6c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0053c6c4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c6c4 bytes 00c146f9
+ 0053c6c4 bytes 00e146f9
- 0053c6e4 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0053c6e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0053c6e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c6e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053c6e4 bytes 00403691
+ 0053c6e4 bytes 00403791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a446fb1518668d256b88884bf83fe28a"></a>

### [`0053c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md) → [`0053c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md) FUN_0053c740

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d590.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 5件 [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) [`0053d590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d590.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c78c",
      "incomplete_value": false,
      "site": "0053c790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c78c",
      "incomplete_value": false,
      "site": "0053c790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "definition_site": "0053c7b0",
      "incomplete_value": false,
      "site": "0053c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:dc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c7b0",
      "incomplete_value": false,
      "site": "0053c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d80:8"
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
      "definition_site": "0053c7b8",
      "incomplete_value": false,
      "site": "0053c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c7b8",
      "incomplete_value": false,
      "site": "0053c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be5000:8"
          ],
          [
            "leaf",
            "const:f80:8"
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
      "0053c758",
      "READ",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c76c",
      "READ",
      [
        "storage",
        "00c25d80",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c78c",
      "PARAM",
      [
        "storage",
        "00c25d90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0053c758",
      "READ",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0053c76c",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053c78c",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c750) · [`0053c76c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c76c) · [`0053c78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md#insn-0053c78c)
- 新版 `0053c750`（命令位置の公開資料なし） · `0053c76c`（命令位置の公開資料なし） · `0053c78c`（命令位置の公開資料なし）

~~~diff
- 0053c750 ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0053c750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053c750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053c750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0053c750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053c750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053c750 bytes 08413691
+ 0053c750 bytes 08413791
- 0053c76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 0053c76c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c76c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0053c76c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c76c bytes 00c146f9
+ 0053c76c bytes 00e146f9
- 0053c78c ["COPY", "tmp:0:8", ["const:d90:8"]]
- 0053c78c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053c78c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053c78c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["COPY", "tmp:0:8", ["const:dd0:8"]]
+ 0053c78c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053c78c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053c78c bytes 00403691
+ 0053c78c bytes 00403791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-689a03b3bd6c7084d5474f58b51fa7de"></a>

### [`0053c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md) → [`0053c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md) FUN_0053c7f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0053c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053c898",
      "incomplete_value": true,
      "site": "0053c89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0053c898",
      "incomplete_value": true,
      "site": "0053c89c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0053c820",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0053c828",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0053c83c",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0053c820",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0053c828",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "0053c83c",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c820) · [`0053c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c828) · [`0053c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md#insn-0053c894)
- 新版 `0053c820`（命令位置の公開資料なし） · `0053c828`（命令位置の公開資料なし） · `0053c894`（命令位置の公開資料なし）

~~~diff
- 0053c820 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e48:8"]]
- 0053c820 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c820 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e98:8"]]
+ 0053c820 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c820 bytes 392747f9
+ 0053c820 bytes 394f47f9
- 0053c828 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d78:8"]]
- 0053c828 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c828 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:dc8:8"]]
+ 0053c828 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c828 bytes 18bf46f9
+ 0053c828 bytes 18e746f9
- 0053c894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d80:8"]]
- 0053c894 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c894 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dd0:8"]]
+ 0053c894 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c894 bytes b5c246f9
+ 0053c894 bytes b5ea46f9
~~~


<a id="compare-5d8025317909bf26080d959f68d1dfe5"></a>

### [`0053c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md) → [`0053c990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c990.md) FUN_0053c990

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053c7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c7f0.md) · 呼出先 6件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md)
- 新版 呼出元 1件 [`0053c7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c7f0.md) · 呼出先 6件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053c9fc",
      "incomplete_value": true,
      "site": "0053ca00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053c9fc",
      "incomplete_value": true,
      "site": "0053ca00",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053ca58",
      "incomplete_value": true,
      "site": "0053ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ca58",
      "incomplete_value": true,
      "site": "0053ca5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053caa8",
      "incomplete_value": true,
      "site": "0053caac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053caa8",
      "incomplete_value": true,
      "site": "0053caac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "0053c9fc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "0053c9fc",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053ca58",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053c9fc",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0053c9fc",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053ca58",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053c9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053c9fc) · [`0053ca58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053ca58) · [`0053caa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c990.md#insn-0053caa8)
- 新版 `0053c9fc`（命令位置の公開資料なし） · `0053ca58`（命令位置の公開資料なし） · `0053caa8`（命令位置の公開資料なし）

~~~diff
- 0053c9fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0053c9fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053c9fc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0053c9fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053c9fc bytes 21f846f9
+ 0053c9fc bytes 212047f9
- 0053ca58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0053ca58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ca58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0053ca58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ca58 bytes 21f846f9
+ 0053ca58 bytes 212047f9
- 0053caa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0053caa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053caa8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0053caa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053caa8 bytes 21f846f9
+ 0053caa8 bytes 212047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0bcb4612d2bcd83890f1c5985d5dd70"></a>

### [`0053d168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md) → [`0053d168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d168.md) FUN_0053d168

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d080.md) [`005748e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005748e4.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00525/00525380.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb350.md) [`00bdb590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb590.md)
- 新版 呼出元 2件 [`0053d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d080.md) [`005748e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005748e4.md) · 呼出先 4件 [`00525380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00525/00525380.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3a0.md) [`00bdb5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb5e0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d1ac",
      "incomplete_value": true,
      "site": "0053d1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0053d1ac",
      "incomplete_value": true,
      "site": "0053d1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d1a4",
      "incomplete_value": true,
      "site": "0053d1b0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0053d1a4",
      "incomplete_value": true,
      "site": "0053d1b0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0053d1bc",
      "incomplete_value": true,
      "site": "0053d1bc",
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
      "definition_site": "0053d1bc",
      "incomplete_value": true,
      "site": "0053d1bc",
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
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053d18c",
      "READ",
      [
        "storage",
        "00c1b450",
        null,
        "pointer"
      ]
    ],
    [
      "0053d190",
      "READ",
      [
        "storage",
        "00c1b448",
        null,
        "pointer"
      ]
    ],
    [
      "0053d1a4",
      "READ",
      [
        "storage",
        "00c13480",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0053d18c",
      "READ",
      [
        "storage",
        "00c1b4a0",
        null,
        "pointer"
      ]
    ],
    [
      "0053d190",
      "READ",
      [
        "storage",
        "00c1b498",
        null,
        "pointer"
      ]
    ],
    [
      "0053d1a4",
      "READ",
      [
        "storage",
        "00c134d0",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d18c) · [`0053d190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d190) · [`0053d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d168.md#insn-0053d204)
- 新版 `0053d18c`（命令位置の公開資料なし） · `0053d190`（命令位置の公開資料なし） · `0053d204`（命令位置の公開資料なし）

~~~diff
- 0053d18c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:450:8"]]
- 0053d18c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d18c ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:4a0:8"]]
+ 0053d18c ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d18c bytes 392b42f9
+ 0053d18c bytes 395342f9
- 0053d190 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:448:8"]]
- 0053d190 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d190 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:498:8"]]
+ 0053d190 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d190 bytes 182742f9
+ 0053d190 bytes 184f42f9
- 0053d204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
- 0053d204 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d204 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
+ 0053d204 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d204 bytes 08c146f9
+ 0053d204 bytes 08e946f9
~~~


<a id="compare-37e532283105c3c3361692866ff4f1e2"></a>

### [`0053d294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md) → [`0053d294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d294.md) FUN_0053d294

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0053d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d080.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb3d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3d0.md) [`00bdb3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3e0.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`0053d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d080.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb420.md) [`00bdb430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb430.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d304",
      "incomplete_value": true,
      "site": "0053d308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d304",
      "incomplete_value": true,
      "site": "0053d308",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4008:8"
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d3bc",
      "incomplete_value": true,
      "site": "0053d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d3bc",
      "incomplete_value": true,
      "site": "0053d3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "0053d304",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "0053d304",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053d3bc",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0053d304",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0053d304",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "0053d3bc",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md#insn-0053d304) · [`0053d3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d294.md#insn-0053d3bc)
- 新版 `0053d304`（命令位置の公開資料なし） · `0053d3bc`（命令位置の公開資料なし）

~~~diff
- 0053d304 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0053d304 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d304 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0053d304 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d304 bytes 21f846f9
+ 0053d304 bytes 212047f9
- 0053d3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0053d3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d3bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0053d3bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d3bc bytes 21f846f9
+ 0053d3bc bytes 212047f9
~~~


<a id="compare-97a0f1c3220a9e6ef9fc01096a82e41a"></a>

### [`0053d46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md) → [`0053d46c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d46c.md) FUN_0053d46c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md) [`00bdc970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc970.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md) [`00bdc9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc9c0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 67.74% / 新版 67.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d490",
      "incomplete_value": true,
      "site": "0053d498",
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
      "definition_site": "0053d490",
      "incomplete_value": true,
      "site": "0053d498",
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
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
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
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
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
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4a4",
      "incomplete_value": true,
      "site": "0053d4a4",
      "value": [
        "LOAD",
        "8",
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
                "const:18:8"
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
      "0053d488",
      "READ",
      [
        "storage",
        "00c1b448",
        null,
        "pointer"
      ]
    ],
    [
      "0053d490",
      "READ",
      [
        "storage",
        "00c13478",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0053d494",
      "READ",
      [
        "storage",
        "00c13490",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ],
  "added": [
    [
      "0053d488",
      "READ",
      [
        "storage",
        "00c1b498",
        null,
        "pointer"
      ]
    ],
    [
      "0053d490",
      "READ",
      [
        "storage",
        "00c134c8",
        "_ZTTNSt6__ndk119basic_istringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "0053d494",
      "READ",
      [
        "storage",
        "00c134e0",
        null,
        "pointer __((offset(0x40)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md#insn-0053d488) · [`0053d48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d46c.md#insn-0053d48c)
- 新版 `0053d488`（命令位置の公開資料なし） · `0053d48c`（命令位置の公開資料なし）

~~~diff
- 0053d488 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:448:8"]]
- 0053d488 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053d488 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:498:8"]]
+ 0053d488 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 0053d488 bytes b52642f9
+ 0053d488 bytes b54e42f9
- 0053d48c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0053d48c bytes f30300aa
+ 0053d48c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0053d48c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-430271ff7e81296797d19bc1c91a67ed"></a>

### [`0053d4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md) → [`0053d4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d4e8.md) FUN_0053d4e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c740.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb510.md)
- 新版 呼出元 2件 [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) [`0053c740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c740.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb560.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053d4f8",
      "incomplete_value": false,
      "site": "0053d500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d4f8",
      "incomplete_value": false,
      "site": "0053d500",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "0053d4f8",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ],
    [
      "0053d520",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d52c",
      "DATA",
      [
        "storage",
        "00bee188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d4f8",
      "PARAM",
      [
        "storage",
        "00c25db0",
        null,
        null
      ]
    ],
    [
      "0053d520",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d52c",
      "DATA",
      [
        "storage",
        "00bee1d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d4f8) · [`0053d514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d514) · [`0053d51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d4e8.md#insn-0053d51c)
- 新版 `0053d4f8`（命令位置の公開資料なし） · `0053d514`（命令位置の公開資料なし） · `0053d51c`（命令位置の公開資料なし）

~~~diff
- 0053d4f8 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0053d4f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0053d4f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d4f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d4f8 bytes 00c03591
+ 0053d4f8 bytes 00c03691
- 0053d514 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0053d514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d514 bytes 08410891
+ 0053d514 bytes 08810991
- 0053d51c ["COPY", "tmp:0:8", ["const:188:8"]]
- 0053d51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053d51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053d51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0053d51c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053d51c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053d51c bytes 29210691
+ 0053d51c bytes 29610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cc1d843b9c03b5608ae4a139426325f"></a>

### [`0053d86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d86c.md) → [`0053d86c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d86c.md) FUN_0053d86c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053d870",
      "incomplete_value": false,
      "site": "0053d874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d870",
      "incomplete_value": false,
      "site": "0053d874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "0053d874",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d874",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d86c.md#insn-0053d870)
- 新版 `0053d870`（命令位置の公開資料なし）

~~~diff
- 0053d870 ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053d870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0053d870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d870 bytes 08410891
+ 0053d870 bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7e537d59fe1e7dda84552fee0c9851"></a>

### [`0053d87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d87c.md) → [`0053d87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d87c.md) FUN_0053d87c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053d88c",
      "incomplete_value": false,
      "site": "0053d894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d88c",
      "incomplete_value": false,
      "site": "0053d894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:210:8"
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
      "0053d894",
      "DATA",
      [
        "storage",
        "00bee210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d894",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d87c.md#insn-0053d88c)
- 新版 `0053d88c`（命令位置の公開資料なし）

~~~diff
- 0053d88c ["COPY", "tmp:0:8", ["const:210:8"]]
- 0053d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["COPY", "tmp:0:8", ["const:260:8"]]
+ 0053d88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d88c bytes 08410891
+ 0053d88c bytes 08810991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a70b700c44f063e0ab0a2ca73eb8226"></a>

### [`0053d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md) → [`0053d8b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d8b4.md) _INIT_26

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b7dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7dea4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb500.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b7dee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7d/00b7dee8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb550.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d8f0",
      "incomplete_value": true,
      "site": "0053d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:13b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d8f0",
      "incomplete_value": true,
      "site": "0053d8f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a1:8"
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
      "definition_site": "0053d8fc",
      "incomplete_value": false,
      "site": "0053d904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d8fc",
      "incomplete_value": false,
      "site": "0053d904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c25000:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "0053d924",
      "incomplete_value": true,
      "site": "0053d930",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
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
      "definition_site": "0053d924",
      "incomplete_value": true,
      "site": "0053d930",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1a000:8"
              ],
              [
                "leaf",
                "const:e40:8"
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


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053d8d4",
      "READ",
      [
        "storage",
        "002a80a1",
        null,
        "string"
      ]
    ],
    [
      "0053d8fc",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ],
    [
      "0053d920",
      "PARAM",
      [
        "storage",
        "00c25d70",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053d8d4",
      "READ",
      [
        "storage",
        "002a813b",
        null,
        "string"
      ]
    ],
    [
      "0053d8fc",
      "PARAM",
      [
        "storage",
        "00c25db0",
        null,
        null
      ]
    ],
    [
      "0053d920",
      "PARAM",
      [
        "storage",
        "00c25db0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d8cc) · [`0053d8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d8fc) · [`0053d920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d8b4.md#insn-0053d920)
- 新版 `0053d8cc`（命令位置の公開資料なし） · `0053d8fc`（命令位置の公開資料なし） · `0053d920`（命令位置の公開資料なし）

~~~diff
- 0053d8cc ["COPY", "tmp:0:8", ["const:a1:8"]]
- 0053d8cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["COPY", "tmp:0:8", ["const:13b:8"]]
+ 0053d8cc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053d8cc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053d8cc bytes 4a850291
+ 0053d8cc bytes 4aed0491
- 0053d8fc ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0053d8fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0053d8fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053d8fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053d8fc bytes 00c03591
+ 0053d8fc bytes 00c03691
- 0053d920 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0053d920 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053d920 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053d920 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0053d920 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053d920 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053d920 bytes 21c03591
+ 0053d920 bytes 21c03691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4124a714400165650b061c9e8e8305"></a>

### [`0053d984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md) → [`0053d984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d984.md) FUN_0053d984

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`004508a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0084e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e0c0.md) [`008fc35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fc35c.md) [`008fcaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008fc/008fcaf4.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 12件 [`004508a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/004508a4.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`0084e0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084e/0084e0c0.md) [`008fc35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fc35c.md) [`008fcaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008fc/008fcaf4.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053d9a0",
      "incomplete_value": false,
      "site": "0053d9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9a0",
      "incomplete_value": false,
      "site": "0053d9a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "definition_site": "0053d9b8",
      "incomplete_value": false,
      "site": "0053d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053d9b8",
      "incomplete_value": false,
      "site": "0053d9b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
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
      "0053d9a8",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d9b8",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053d9a8",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ],
    [
      "0053d9b8",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053d9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md#insn-0053d9a0) · [`0053d9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d984.md#insn-0053d9ac)
- 新版 `0053d9a0`（命令位置の公開資料なし） · `0053d9ac`（命令位置の公開資料なし）

~~~diff
- 0053d9a0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 0053d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 0053d9a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053d9a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053d9a0 bytes 08010b91
+ 0053d9a0 bytes 08410c91
- 0053d9ac ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053d9ac bytes 883500b0
+ 0053d9ac ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0053d9ac bytes 883500b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74dbbc26bd62578a2462e4a492a95f77"></a>

### [`0053d9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d9cc.md) → [`0053d9cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d9cc.md) FUN_0053d9cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0052db3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db3c.md) [`0053df70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053df70.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0052db3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0052d/0052db3c.md) [`0053df70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053df70.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.18% / 新版 98.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053da64",
      "incomplete_value": false,
      "site": "0053da64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053da64",
      "incomplete_value": false,
      "site": "0053da64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "0053da64",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ],
    [
      "0053dae4",
      "READ",
      [
        "storage",
        "00bee388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053da64",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053dae4",
      "READ",
      [
        "storage",
        "00bee3d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053da5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d9cc.md#insn-0053da5c)
- 新版 `0053da5c`（命令位置の公開資料なし）

~~~diff
- 0053da5c ["COPY", "tmp:0:8", ["const:360:8"]]
- 0053da5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053da5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053da5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0053da5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053da5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053da5c bytes 08810d91
+ 0053da5c bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ec0f36e92fb1848625661752e2b7285"></a>

### [`0053dc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc90.md) → [`0053dc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc90.md) FUN_0053dc90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053dca8",
      "incomplete_value": false,
      "site": "0053dcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dca8",
      "incomplete_value": false,
      "site": "0053dcac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0053dcac",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dcac",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc90.md#insn-0053dca8)
- 新版 `0053dca8`（命令位置の公開資料なし）

~~~diff
- 0053dca8 ["COPY", "tmp:0:8", ["const:260:8"]]
- 0053dca8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 0053dca8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dca8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dca8 bytes 29810991
+ 0053dca8 bytes 29c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ed1a22bfac48da8a8b81945997b295b"></a>

### [`0053dce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dce0.md) → [`0053dce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dce0.md) FUN_0053dce0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053dcf8",
      "incomplete_value": false,
      "site": "0053dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dcf8",
      "incomplete_value": false,
      "site": "0053dcfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0053dcfc",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dcfc",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dce0.md#insn-0053dcf8)
- 新版 `0053dcf8`（命令位置の公開資料なし）

~~~diff
- 0053dcf8 ["COPY", "tmp:0:8", ["const:260:8"]]
- 0053dcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 0053dcf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dcf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dcf8 bytes 29810991
+ 0053dcf8 bytes 29c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64369498f50783bed14ec108c35ebcd9"></a>

### [`0053dd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd34.md) → [`0053dd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd34.md) FUN_0053dd34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053dd38",
      "incomplete_value": false,
      "site": "0053dd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dd38",
      "incomplete_value": false,
      "site": "0053dd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "0053dd3c",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dd3c",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd34.md#insn-0053dd38)
- 新版 `0053dd38`（命令位置の公開資料なし）

~~~diff
- 0053dd38 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 0053dd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 0053dd38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053dd38 bytes 08010b91
+ 0053dd38 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936621cad4a2a218b5ea42e1d141e3b1"></a>

### [`0053dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd44.md) → [`0053dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dd44.md) FUN_0053dd44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053dd54",
      "incomplete_value": false,
      "site": "0053dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dd54",
      "incomplete_value": false,
      "site": "0053dd5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2c0:8"
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
      "0053dd5c",
      "DATA",
      [
        "storage",
        "00bee2c0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dd5c",
      "DATA",
      [
        "storage",
        "00bee310",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dd44.md#insn-0053dd54)
- 新版 `0053dd54`（命令位置の公開資料なし）

~~~diff
- 0053dd54 ["COPY", "tmp:0:8", ["const:2c0:8"]]
- 0053dd54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["COPY", "tmp:0:8", ["const:310:8"]]
+ 0053dd54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053dd54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053dd54 bytes 08010b91
+ 0053dd54 bytes 08410c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e4963947a151ed1e2e7c6f7c4c1e12"></a>

### [`0053dde0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dde0.md) → [`0053dde0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dde0.md) FUN_0053dde0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053ddf8",
      "incomplete_value": false,
      "site": "0053de04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ddf8",
      "incomplete_value": false,
      "site": "0053de04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "0053de04",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053de04",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ddf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dde0.md#insn-0053ddf8)
- 新版 `0053ddf8`（命令位置の公開資料なし）

~~~diff
- 0053ddf8 ["COPY", "tmp:0:8", ["const:360:8"]]
- 0053ddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0053ddf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ddf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ddf8 bytes 08810d91
+ 0053ddf8 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a65b9ddba9073f614ca4d44ffbed8a7"></a>

### [`0053de3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053de3c.md) → [`0053de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053de3c.md) FUN_0053de3c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0053de68",
      "incomplete_value": false,
      "site": "0053de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053de68",
      "incomplete_value": false,
      "site": "0053de68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:360:8"
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
      "0053de68",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053de68",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053de60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053de3c.md#insn-0053de60)
- 新版 `0053de60`（命令位置の公開資料なし）

~~~diff
- 0053de60 ["COPY", "tmp:0:8", ["const:360:8"]]
- 0053de60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053de60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0053de60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053de60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053de60 bytes 08810d91
+ 0053de60 bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b05a3ef2fbc85be87bfef9ab5f65d31a"></a>

### [`0053dec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dec4.md) → [`0053dec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dec4.md) FUN_0053dec4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0053dee0",
      "incomplete_value": true,
      "site": "0053dee0",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053dee0",
      "incomplete_value": true,
      "site": "0053dee0",
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
            "const:360:8"
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
      "0053dee0",
      "DATA",
      [
        "storage",
        "00bee360",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053dee0",
      "DATA",
      [
        "storage",
        "00bee3b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053dedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dec4.md#insn-0053dedc)
- 新版 `0053dedc`（命令位置の公開資料なし）

~~~diff
- 0053dedc ["COPY", "tmp:0:8", ["const:360:8"]]
- 0053dedc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053dedc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 0053dedc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053dedc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053dedc bytes 29810d91
+ 0053dedc bytes 29c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35a52a729e3fbd7d75f4c7eedb8c4353"></a>

### [`0053e008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md) → [`0053e008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e008.md) FUN_0053e008

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0053dc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053dc30.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`0053dc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053dc30.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053e020",
      "incomplete_value": false,
      "site": "0053e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e020",
      "incomplete_value": false,
      "site": "0053e020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053e02c",
      "incomplete_value": false,
      "site": "0053e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e02c",
      "incomplete_value": false,
      "site": "0053e02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:260:8"
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
      "0053e020",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053e02c",
      "DATA",
      [
        "storage",
        "00bee260",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e020",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ],
    [
      "0053e02c",
      "DATA",
      [
        "storage",
        "00bee2b0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md#insn-0053e018) · [`0053e024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e008.md#insn-0053e024)
- 新版 `0053e018`（命令位置の公開資料なし） · `0053e024`（命令位置の公開資料なし）

~~~diff
- 0053e018 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0053e018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0053e018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e018 bytes 08810f91
+ 0053e018 bytes 08c11091
- 0053e024 ["COPY", "register:4040:8", ["const:bee000:8"]]
- 0053e024 bytes 88350090
+ 0053e024 ["COPY", "register:4040:8", ["const:bee000:8"]]
+ 0053e024 bytes 88350090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ba4cbe114c41689342482d579fde730"></a>

### [`0053e0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0bc.md) → [`0053e0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e0bc.md) FUN_0053e0bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "0053e0c0",
      "incomplete_value": false,
      "site": "0053e0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e0c0",
      "incomplete_value": false,
      "site": "0053e0c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0053e0c4",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e0c4",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0bc.md#insn-0053e0c0)
- 新版 `0053e0c0`（命令位置の公開資料なし）

~~~diff
- 0053e0c0 ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0053e0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0053e0c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e0c0 bytes 08810f91
+ 0053e0c0 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89628504cc76cd3989a26fea0773b2f"></a>

### [`0053e0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0cc.md) → [`0053e0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e0cc.md) FUN_0053e0cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0053e0dc",
      "incomplete_value": false,
      "site": "0053e0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e0dc",
      "incomplete_value": false,
      "site": "0053e0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "0053e0e4",
      "DATA",
      [
        "storage",
        "00bee3e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e0e4",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e0cc.md#insn-0053e0dc)
- 新版 `0053e0dc`（命令位置の公開資料なし）

~~~diff
- 0053e0dc ["COPY", "tmp:0:8", ["const:3e0:8"]]
- 0053e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["COPY", "tmp:0:8", ["const:430:8"]]
+ 0053e0dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e0dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e0dc bytes 08810f91
+ 0053e0dc bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9c826226733ad12e552fa2e442b3ec"></a>

### [`0053e1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md) → [`0053e1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e1dc.md) FUN_0053e1dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) · 呼出先 14件 [`0053c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c6a0.md) [`00574738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574738.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 2件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 14件 [`0053c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053c/0053c6a0.md) [`00574738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574738.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.65% / 新版 96.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e234",
      "incomplete_value": false,
      "site": "0053e240",
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
            "const:8fb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e234",
      "incomplete_value": false,
      "site": "0053e240",
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
            "const:861:8"
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
      "definition_site": "0053e4c4",
      "incomplete_value": false,
      "site": "0053e4cc",
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
            "const:74b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e4c4",
      "incomplete_value": false,
      "site": "0053e4cc",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053e564",
      "incomplete_value": false,
      "site": "0053e568",
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
            "const:75b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e564",
      "incomplete_value": false,
      "site": "0053e568",
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
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053e234",
      "PARAM",
      [
        "storage",
        "002a6861",
        null,
        "string"
      ]
    ],
    [
      "0053e318",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "0053e3d0",
      "PARAM",
      [
        "storage",
        "002a687b",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053e234",
      "PARAM",
      [
        "storage",
        "002a68fb",
        null,
        "string"
      ]
    ],
    [
      "0053e318",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "0053e3d0",
      "PARAM",
      [
        "storage",
        "002a6915",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e234) · [`0053e310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e310) · [`0053e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e1dc.md#insn-0053e380)
- 新版 `0053e234`（命令位置の公開資料なし） · `0053e310`（命令位置の公開資料なし） · `0053e380`（命令位置の公開資料なし）

~~~diff
- 0053e234 ["COPY", "tmp:0:8", ["const:861:8"]]
- 0053e234 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0053e234 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0053e234 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["COPY", "tmp:0:8", ["const:8fb:8"]]
+ 0053e234 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0053e234 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0053e234 bytes 42842191
+ 0053e234 bytes 42ec2391
- 0053e310 ["COPY", "tmp:0:8", ["const:169:8"]]
- 0053e310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053e310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053e310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["COPY", "tmp:0:8", ["const:1f4:8"]]
+ 0053e310 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053e310 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053e310 bytes 29a50591
+ 0053e310 bytes 29d10791
- 0053e380 ["COPY", "tmp:0:8", ["const:87b:8"]]
- 0053e380 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 0053e380 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 0053e380 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 0053e380 ["COPY", "tmp:0:8", ["const:915:8"]]
+ 0053e380 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 0053e380 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 0053e380 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 0053e380 bytes 94ee2191
+ 0053e380 bytes 94562491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b776d6c42736e1ad6cc1bdbf4e5cbb1f"></a>

### [`0053e9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e9d0.md) → [`0053e9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053e9d0.md) FUN_0053e9d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00431534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00433/00433930.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`00431534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00431/00431534.md) [`00433930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00433/00433930.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0053e9ec",
      "incomplete_value": false,
      "site": "0053e9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053e9ec",
      "incomplete_value": false,
      "site": "0053e9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:430:8"
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
      "0053e9f4",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053e9f4",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053e9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053e9d0.md#insn-0053e9ec)
- 新版 `0053e9ec`（命令位置の公開資料なし）

~~~diff
- 0053e9ec ["COPY", "tmp:0:8", ["const:430:8"]]
- 0053e9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0053e9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053e9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053e9ec bytes 08c11091
+ 0053e9ec bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecddd6a2c7dd0f8348f6639dcf45db68"></a>

### [`0053ea14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md) → [`0053ea14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ea14.md) FUN_0053ea14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 5件 [`0053d588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d588.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 5件 [`0053d588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d588.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0053ea90",
      "incomplete_value": false,
      "site": "0053ea98",
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
            "const:65c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ea90",
      "incomplete_value": false,
      "site": "0053ea98",
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
            "const:5d1:8"
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
      "0053ea74",
      "PARAM",
      [
        "storage",
        "00298cdb",
        null,
        null
      ]
    ],
    [
      "0053ea90",
      "PARAM",
      [
        "storage",
        "002a45d1",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0053ea74",
      "PARAM",
      [
        "storage",
        "00298c4e",
        null,
        null
      ]
    ],
    [
      "0053ea90",
      "PARAM",
      [
        "storage",
        "002a465c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ea74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md#insn-0053ea74) · [`0053ea90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ea14.md#insn-0053ea90)
- 新版 `0053ea74`（命令位置の公開資料なし） · `0053ea90`（命令位置の公開資料なし）

~~~diff
- 0053ea74 ["COPY", "tmp:0:8", ["const:cdb:8"]]
- 0053ea74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["COPY", "tmp:0:8", ["const:c4e:8"]]
+ 0053ea74 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea74 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053ea74 bytes 216c3391
+ 0053ea74 bytes 21383191
- 0053ea90 ["COPY", "tmp:0:8", ["const:5d1:8"]]
- 0053ea90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["COPY", "tmp:0:8", ["const:65c:8"]]
+ 0053ea90 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0053ea90 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0053ea90 bytes 21441791
+ 0053ea90 bytes 21701991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-011f8474b2fe9c439a73f1776ea68f98"></a>

### [`0053ec4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md) → [`0053ec4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ec4c.md) FUN_0053ec4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.68% / 新版 93.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0053ec98",
      "incomplete_value": true,
      "site": "0053ec98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ec98",
      "incomplete_value": true,
      "site": "0053ec98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:169:8"
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
      "0053ec70",
      "READ",
      [
        "storage",
        "002a3169",
        null,
        "string"
      ]
    ],
    [
      "0053ed30",
      "READ",
      [
        "storage",
        "002a6883",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053ec70",
      "READ",
      [
        "storage",
        "002a31f4",
        null,
        "string"
      ]
    ],
    [
      "0053ed30",
      "READ",
      [
        "storage",
        "002a691d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ec68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md#insn-0053ec68) · [`0053ed20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ec4c.md#insn-0053ed20)
- 新版 `0053ec68`（命令位置の公開資料なし） · `0053ed20`（命令位置の公開資料なし）

~~~diff
- 0053ec68 ["COPY", "tmp:0:8", ["const:169:8"]]
- 0053ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["COPY", "tmp:0:8", ["const:1f4:8"]]
+ 0053ec68 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0053ec68 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0053ec68 bytes 4aa50591
+ 0053ec68 bytes 4ad10791
- 0053ed20 ["COPY", "tmp:0:8", ["const:883:8"]]
- 0053ed20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ed20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ed20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ed20 ["COPY", "tmp:0:8", ["const:91d:8"]]
+ 0053ed20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ed20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ed20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ed20 bytes 080d2291
+ 0053ed20 bytes 08752491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9619a6617d74caa901571c38c02b9595"></a>

### [`0053ee14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee14.md) → [`0053ee14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee14.md) FUN_0053ee14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`008a1458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 2件 [`008a1458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a1/008a1458.md) [`008a2cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a2/008a2cac.md) · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0053ee30",
      "incomplete_value": false,
      "site": "0053ee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ee30",
      "incomplete_value": false,
      "site": "0053ee38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "0053ee38",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053ee38",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee14.md#insn-0053ee30)
- 新版 `0053ee30`（命令位置の公開資料なし）

~~~diff
- 0053ee30 ["COPY", "tmp:0:8", ["const:480:8"]]
- 0053ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 0053ee30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053ee30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053ee30 bytes 08011291
+ 0053ee30 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32a49d6f6be86ab8e12496bdacdac06d"></a>

### [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) → [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) FUN_0053ee5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 21件 [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`0042ca70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042ce34.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00540878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540878.md) [`0056244c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00562/0056244c.md) [`0057476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/0057476c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 21件 [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041ba38.md) [`004222e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00422/004222e0.md) [`0042ca70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ca70.md) [`0042ce34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042ce34.md) · 呼出先 7件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00540878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540878.md) [`0056244c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00562/0056244c.md) [`0057476c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/0057476c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053ef1c",
      "incomplete_value": false,
      "site": "0053ef1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053ef1c",
      "incomplete_value": false,
      "site": "0053ef1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0053eea0",
      "incomplete_value": true,
      "site": "0053eea0",
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
      "definition_site": "0053eea0",
      "incomplete_value": true,
      "site": "0053eea0",
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
      "0053ee9c",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ],
    [
      "0053ef1c",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ],
    [
      "0053efa8",
      "READ",
      [
        "storage",
        "00bee4f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053ee9c",
      "READ",
      [
        "storage",
        "00c25e00",
        null,
        "undefined8"
      ]
    ],
    [
      "0053ef1c",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ],
    [
      "0053efa8",
      "READ",
      [
        "storage",
        "00bee548",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053ee9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md#insn-0053ee9c) · [`0053ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md#insn-0053ef14) · [`0053ef18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md#insn-0053ef18)
- 新版 `0053ee9c`（命令位置の公開資料なし） · `0053ef14`（命令位置の公開資料なし）

~~~diff
- 0053ee9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc0:8"]]
- 0053ee9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0053ee9c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e00:8"]]
+ 0053ee9c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0053ee9c bytes 29e146f9
+ 0053ee9c bytes 290147f9
- 0053ef14 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0053ef14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0053ef14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0053ef14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0053ef14 bytes 29411391
+ 0053ef14 bytes 29811491
- 0053ef18 ["COPY", "register:40b8:8", ["register:4000:8"]]
- 0053ef18 bytes f70300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18e37afb381b13347f72b3fada29e860"></a>

### [`0053f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md) → [`0053f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f0f8.md) FUN_0053f0f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 3件 [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00949/00949c4c.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`00541908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/00541908.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 3件 [`0041b470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b470.md) [`00435c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00435/00435c18.md) [`00949c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00949/00949c4c.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`0041fddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fddc.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00541908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541908.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0053f510",
      "incomplete_value": false,
      "site": "0053f51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:660:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053f510",
      "incomplete_value": false,
      "site": "0053f51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:610:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0053f51c",
      "DATA",
      [
        "storage",
        "00bee610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0053f51c",
      "DATA",
      [
        "storage",
        "00bee660",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053f510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f0f8.md#insn-0053f510)
- 新版 `0053f510`（命令位置の公開資料なし）

~~~diff
- 0053f510 ["COPY", "tmp:0:8", ["const:610:8"]]
- 0053f510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0053f510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0053f510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["COPY", "tmp:0:8", ["const:660:8"]]
+ 0053f510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0053f510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0053f510 bytes 08411891
+ 0053f510 bytes 08811991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31e3d79c0a47c24df934d9b6e05ee9dc"></a>

### [`0053fe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053fe04.md) → [`0053fe04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053fe04.md) FUN_0053fe04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0053feb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005401c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0053feb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053feb8.md) [`005401c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005401c0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0053fe10",
      "incomplete_value": false,
      "site": "0053fe14",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0053fe10",
      "incomplete_value": false,
      "site": "0053fe14",
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
            "const:303:8"
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
      "0053fe10",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0053fe10",
      "PARAM",
      [
        "storage",
        "002a739d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0053fe10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053fe04.md#insn-0053fe10)
- 新版 `0053fe10`（命令位置の公開資料なし）

~~~diff
- 0053fe10 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0053fe10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0053fe10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0053fe10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0053fe10 bytes 000c0c91
+ 0053fe10 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c191659a05c1d1b1242da1770e470c44"></a>

### [`0054050c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054050c.md) → [`0054050c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/0054050c.md) FUN_0054050c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00540510",
      "incomplete_value": false,
      "site": "00540514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540510",
      "incomplete_value": false,
      "site": "00540514",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00540514",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540514",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054050c.md#insn-00540510)
- 新版 `00540510`（命令位置の公開資料なし）

~~~diff
- 00540510 ["COPY", "tmp:0:8", ["const:430:8"]]
- 00540510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["COPY", "tmp:0:8", ["const:480:8"]]
+ 00540510 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540510 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540510 bytes 08c11091
+ 00540510 bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8792a287615392b913a0186c3334e09c"></a>

### [`0054051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054051c.md) → [`0054051c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/0054051c.md) FUN_0054051c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0054052c",
      "incomplete_value": false,
      "site": "00540534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054052c",
      "incomplete_value": false,
      "site": "00540534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
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
      "00540534",
      "DATA",
      [
        "storage",
        "00bee430",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540534",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054052c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/0054051c.md#insn-0054052c)
- 新版 `0054052c`（命令位置の公開資料なし）

~~~diff
- 0054052c ["COPY", "tmp:0:8", ["const:430:8"]]
- 0054052c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0054052c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0054052c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["COPY", "tmp:0:8", ["const:480:8"]]
+ 0054052c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0054052c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0054052c bytes 08c11091
+ 0054052c bytes 08011291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92da4ae973429c7cafe196758fa2e31b"></a>

### [`005405bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405bc.md) → [`005405bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005405bc.md) FUN_005405bc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "005405c0",
      "incomplete_value": false,
      "site": "005405c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405c0",
      "incomplete_value": false,
      "site": "005405c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "005405c4",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005405c4",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005405c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405bc.md#insn-005405c0)
- 新版 `005405c0`（命令位置の公開資料なし）

~~~diff
- 005405c0 ["COPY", "tmp:0:8", ["const:480:8"]]
- 005405c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005405c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005405c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 005405c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005405c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005405c0 bytes 08011291
+ 005405c0 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b41c34a9d31a0b713dad6a3e355d9eca"></a>

### [`005405cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405cc.md) → [`005405cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005405cc.md) FUN_005405cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "005405dc",
      "incomplete_value": false,
      "site": "005405e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005405dc",
      "incomplete_value": false,
      "site": "005405e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:480:8"
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
      "005405e4",
      "DATA",
      [
        "storage",
        "00bee480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005405e4",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005405dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005405cc.md#insn-005405dc)
- 新版 `005405dc`（命令位置の公開資料なし）

~~~diff
- 005405dc ["COPY", "tmp:0:8", ["const:480:8"]]
- 005405dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 005405dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 005405dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 005405dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 005405dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 005405dc bytes 08011291
+ 005405dc bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09877a3db222e992196af639657a311e"></a>

### [`00540614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540614.md) → [`00540614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540614.md) FUN_00540614

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0054062c",
      "incomplete_value": false,
      "site": "00540630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054062c",
      "incomplete_value": false,
      "site": "00540630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "00540630",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540630",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540614.md#insn-0054062c)
- 新版 `0054062c`（命令位置の公開資料なし）

~~~diff
- 0054062c ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0054062c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054062c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0054062c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054062c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054062c bytes 29411391
+ 0054062c bytes 29811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12133aae8c6fb32c9865362e77a828b0"></a>

### [`00540664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540664.md) → [`00540664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540664.md) FUN_00540664

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0054067c",
      "incomplete_value": false,
      "site": "00540680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0054067c",
      "incomplete_value": false,
      "site": "00540680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "00540680",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540680",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0054067c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540664.md#insn-0054067c)
- 新版 `0054067c`（命令位置の公開資料なし）

~~~diff
- 0054067c ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 0054067c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0054067c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["COPY", "tmp:0:8", ["const:520:8"]]
+ 0054067c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0054067c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0054067c bytes 29411391
+ 0054067c bytes 29811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a7cf468c2357e9afae746887be81dac"></a>

### [`005406b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005406b0.md) → [`005406b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005406b0.md) FUN_005406b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005406e4",
      "incomplete_value": false,
      "site": "005406e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:520:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005406e4",
      "incomplete_value": false,
      "site": "005406e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "005406e4",
      "DATA",
      [
        "storage",
        "00bee4d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005406e4",
      "DATA",
      [
        "storage",
        "00bee520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005406d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005406b0.md#insn-005406d8) · [`005406e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005406b0.md#insn-005406e0)
- 新版 `005406d8`（命令位置の公開資料なし） · `005406e0`（命令位置の公開資料なし）

~~~diff
- 005406d8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
- 005406d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005406d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 005406d8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005406d8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005406d8 bytes 4a411391
+ 005406d8 bytes 4a811491
- 005406e0 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 005406e0 bytes f50300aa
+ 005406e0 ["COPY", "register:40a8:8", ["register:4000:8"]]
+ 005406e0 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4ee339a2d662df22b00db6c1a371c9"></a>

### [`005408b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005408b8.md) → [`005408b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005408b8.md) FUN_005408b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e4",
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
      "definition_site": "005408e4",
      "incomplete_value": true,
      "site": "005408e4",
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
      "005408dc",
      "READ",
      [
        "storage",
        "00c25dc0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "005408dc",
      "READ",
      [
        "storage",
        "00c25e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005408dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005408b8.md#insn-005408dc)
- 新版 `005408dc`（命令位置の公開資料なし）

~~~diff
- 005408dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
- 005408dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 005408dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e00:8"]]
+ 005408dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 005408dc bytes 08e146f9
+ 005408dc bytes 080147f9
~~~


<a id="compare-40a2a4ad710f9fc4026dfa30558d3164"></a>

### [`00540964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540964.md) → [`00540964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540964.md) FUN_00540964

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md)

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
      "definition_site": "00540968",
      "incomplete_value": false,
      "site": "0054096c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540968",
      "incomplete_value": false,
      "site": "0054096c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0054096c",
      "DATA",
      [
        "storage",
        "00bee550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054096c",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540964.md#insn-00540968)
- 新版 `00540968`（命令位置の公開資料なし）

~~~diff
- 00540968 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00540968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00540968 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540968 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540968 bytes 08411591
+ 00540968 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-313c58f8c5ac21240bafeda48e309b15"></a>

### [`00540974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540974.md) → [`00540974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540974.md) FUN_00540974

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00540984",
      "incomplete_value": false,
      "site": "0054098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00540984",
      "incomplete_value": false,
      "site": "0054098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:550:8"
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
      "0054098c",
      "DATA",
      [
        "storage",
        "00bee550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0054098c",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00540984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540974.md#insn-00540984)
- 新版 `00540984`（命令位置の公開資料なし）

~~~diff
- 00540984 ["COPY", "tmp:0:8", ["const:550:8"]]
- 00540984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00540984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00540984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["COPY", "tmp:0:8", ["const:5a0:8"]]
+ 00540984 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00540984 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00540984 bytes 08411591
+ 00540984 bytes 08811691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9e458af61c37e36c8b993475560224a"></a>

### [`005409a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409a4.md) → [`005409a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409a4.md) FUN_005409a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005409b4",
      "incomplete_value": false,
      "site": "005409b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409b4",
      "incomplete_value": false,
      "site": "005409b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "005409b8",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "005409b8",
      "DATA",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409a4.md#insn-005409b4)
- 新版 `005409b4`（命令位置の公開資料なし）

~~~diff
- 005409b4 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 005409b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 005409b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 005409b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 005409b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 005409b4 bytes 29811691
+ 005409b4 bytes 29c11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8c3bccd97eecb3db3d2fc4e74f0be53"></a>

### [`005409c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409c4.md) → [`005409c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/005409c4.md) FUN_005409c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0054243c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00542/0054243c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0053f81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053f/0053f81c.md) [`00540c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/00540c2c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0054243c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00542/0054243c.md) · 呼出先 5件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0053f81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053f/0053f81c.md) [`00540c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00540/00540c2c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "005409f0",
      "incomplete_value": false,
      "site": "00540a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "005409f0",
      "incomplete_value": false,
      "site": "00540a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bee000:8"
          ],
          [
            "leaf",
            "const:5a0:8"
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
      "00540a0c",
      "DATA",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ],
    [
      "00540abc",
      "READ",
      [
        "storage",
        "00bee5a0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00540a0c",
      "DATA",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ],
    [
      "00540abc",
      "READ",
      [
        "storage",
        "00bee5f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`005409f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00540/005409c4.md#insn-005409f0)
- 新版 `005409f0`（命令位置の公開資料なし）

~~~diff
- 005409f0 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 005409f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 005409f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["COPY", "tmp:0:8", ["const:5f0:8"]]
+ 005409f0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 005409f0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 005409f0 bytes 4a811691
+ 005409f0 bytes 4ac11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

