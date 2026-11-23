# v15.7.3 → v15.7.4 · 最優先の変更候補 (33)

[一覧の目次](README.md)

<a id="compare-50734130fa9d34ad3b0e5bd01a4afd1e"></a>

### [`0073a424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md) → [`0073a424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a424.md) FUN_0073a424

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 5件 [`0070bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0070b/0070bedc.md) [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bd0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0062d23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062d/0062d23c.md) [`0070959c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00709/0070959c.md)
- 新版 呼出元 5件 [`0070bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0070b/0070bedc.md) [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`00868124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a5/008a5bd0.md) · 呼出先 16件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0062d23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062d/0062d23c.md) [`0070959c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00709/0070959c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.96% / 新版 93.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073a544",
      "incomplete_value": true,
      "site": "0073a568",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:e45:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a544",
      "incomplete_value": true,
      "site": "0073a568",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:ed2:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "0073a4b0",
      "incomplete_value": true,
      "site": "0073a4b0",
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
      "definition_site": "0073a4b0",
      "incomplete_value": true,
      "site": "0073a4b0",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0073a4b8",
      "incomplete_value": false,
      "site": "0073a4c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a4b8",
      "incomplete_value": false,
      "site": "0073a4c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "0073a4ac",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0073a4b8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073a4c0",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0073a4ac",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0073a4b8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073a4c0",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4ac) · [`0073a4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4b8) · [`0073a4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a424.md#insn-0073a4c0)
- 新版 `0073a4ac`（命令位置の公開資料なし） · `0073a4b8`（命令位置の公開資料なし） · `0073a4c0`（命令位置の公開資料なし）

~~~diff
- 0073a4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0073a4ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073a4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0073a4ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0073a4ac bytes 003d45f9
+ 0073a4ac bytes 005d45f9
- 0073a4b8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0073a4b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0073a4b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0073a4b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0073a4b8 bytes 21203991
+ 0073a4b8 bytes 21603a91
- 0073a4c0 ["COPY", "tmp:0:8", ["const:490:8"]]
- 0073a4c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0073a4c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0073a4c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0073a4c0 bytes 42401291
+ 0073a4c0 bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c855e0acabb4c6ca9cc2fe7af4835d1"></a>

### [`0073a780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md) → [`0073a780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a780.md) FUN_0073a780

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 10件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md) [`0075b45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b45c.md) [`0075b460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b460.md) [`0075b510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b510.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 10件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md) [`0075b45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b45c.md) [`0075b460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b460.md) [`0075b510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b510.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073a7dc",
      "incomplete_value": false,
      "site": "0073a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a7dc",
      "incomplete_value": false,
      "site": "0073a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "definition_site": "0073a828",
      "incomplete_value": false,
      "site": "0073a828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a828",
      "incomplete_value": false,
      "site": "0073a828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "0073a7dc",
      "DATA",
      [
        "storage",
        "00bfbe28",
        null,
        "undefined *"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbe48",
        null,
        "pointer"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbe50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073a7dc",
      "DATA",
      [
        "storage",
        "00bfbe78",
        null,
        "undefined *"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbe98",
        null,
        "pointer"
      ]
    ],
    [
      "0073a814",
      "READ",
      [
        "storage",
        "00bfbea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md#insn-0073a7d4) · [`0073a820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a780.md#insn-0073a820)
- 新版 `0073a7d4`（命令位置の公開資料なし） · `0073a820`（命令位置の公開資料なし）

~~~diff
- 0073a7d4 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 0073a7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 0073a7d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a7d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073a7d4 bytes 08a13891
+ 0073a7d4 bytes 08e13991
- 0073a820 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0073a820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073a820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073a820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0073a820 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073a820 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073a820 bytes 08a13a91
+ 0073a820 bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5fb2b49b0c359b5b170fcf70cd970078"></a>

### [`0073a8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md) → [`0073a8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a8e0.md) FUN_0073a8e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0073da58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 2件 [`00acf8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf8cc.md) [`00acf95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acf95c.md)
- 新版 呼出元 7件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0073da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073da58.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 2件 [`00acf910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf910.md) [`00acf9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acf/00acf9a0.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 99.42% / 新版 99.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0073a92c",
      "incomplete_value": true,
      "site": "0073a92c",
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
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073a92c",
      "incomplete_value": true,
      "site": "0073a92c",
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
            "const:f64:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0073ab64",
      "incomplete_value": false,
      "site": "0073ab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ab64",
      "incomplete_value": false,
      "site": "0073ab64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c27000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "0073ab8c",
      "incomplete_value": true,
      "site": "0073ab90",
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
      "definition_site": "0073ab8c",
      "incomplete_value": true,
      "site": "0073ab90",
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
      "0073a8e4",
      "READ",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "0073a92c",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ],
    [
      "0073ab64",
      "WRITE",
      [
        "storage",
        "00c27ee0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0073a8e4",
      "READ",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0073a92c",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ],
    [
      "0073ab64",
      "WRITE",
      [
        "storage",
        "00c27f20",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073a92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073a92c) · [`0073ab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073ab64) · [`0073a8e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md#insn-0073a8e4)
- 新版 `0073a92c`（命令位置の公開資料なし） · `0073ab64`（命令位置の公開資料なし） · `0073a8e4`（命令位置の公開資料なし）

~~~diff
- 0073a92c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0073a92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0073a92c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:f64:8"]]
- 0073a92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0073a92c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0073a92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0073a92c ["INT_ADD", "tmp:2:8", ["register:4040:8", "const:fb4:8"]]
+ 0073a92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0073a92c bytes 1f913d39
+ 0073a92c bytes 1fd13e39
- 0073ab64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
- 0073ab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 0073ab64 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 0073ab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 0073ab64 bytes 00e10eb9
+ 0073ab64 bytes 00210fb9
- 0073a8e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f64:8"]]
- 0073a8e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 0073a8e4 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
+ 0073a8e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb4:8"]]
+ 0073a8e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 0073a8e4 ["INT_ZEXT", "register:4048:8", ["tmp:1:1"]]
- 0073a8e4 bytes 09917d39
+ 0073a8e4 bytes 09d17e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ea40da4f1a9d35ab89c0fa13031e397"></a>

### [`0073addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md) → [`0073addc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md) FUN_0073addc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) · 呼出先 21件 [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md)
- 新版 呼出元 2件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) · 呼出先 21件 [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.92% / 新版 91.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae34",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073ae20",
      "incomplete_value": true,
      "site": "0073ae38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073af00",
      "incomplete_value": true,
      "site": "0073af04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0073af00",
      "incomplete_value": true,
      "site": "0073af04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0073ae20",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073aeec",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0073aef0",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0073ae20",
      "READ",
      [
        "storage",
        "0029f98d",
        null,
        "string"
      ]
    ],
    [
      "0073aeec",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "0073aef0",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073ae1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073ae1c) · [`0073aeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073aeec) · [`0073aef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md#insn-0073aef0)
- 新版 `0073ae1c`（命令位置の公開資料なし） · `0073aeec`（命令位置の公開資料なし） · `0073aef0`（命令位置の公開資料なし）

~~~diff
- 0073ae1c ["COPY", "tmp:0:8", ["const:902:8"]]
- 0073ae1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["COPY", "tmp:0:8", ["const:98d:8"]]
+ 0073ae1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073ae1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073ae1c bytes 08092491
+ 0073ae1c bytes 08352691
- 0073aeec ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
- 0073aeec ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073aeec ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e98:8"]]
+ 0073aeec ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073aeec bytes 7b2747f9
+ 0073aeec bytes 7b4f47f9
- 0073aef0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
- 0073aef0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073aef0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc8:8"]]
+ 0073aef0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0073aef0 bytes 29bd46f9
+ 0073aef0 bytes 29e546f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66f0f5f4854e9f6c39f865f844d62eb0"></a>

### [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md) → [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md) FUN_0073b3dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) · 呼出先 22件 [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053b/0053baf0.md) [`0053d580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053d/0053d580.md)
- 新版 呼出元 1件 [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) · 呼出先 22件 [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`0053baf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053b/0053baf0.md) [`0053d580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053d/0053d580.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073b438",
      "incomplete_value": true,
      "site": "0073b438",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
              ],
              [
                "leaf",
                "const:139:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b438",
      "incomplete_value": true,
      "site": "0073b438",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29a000:8"
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073b4a0",
      "incomplete_value": true,
      "site": "0073b4b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
              ]
            ]
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
      "0073b428",
      "READ",
      [
        "storage",
        "0029a13b",
        null,
        "string"
      ]
    ],
    [
      "0073b4a0",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073b568",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0073b428",
      "READ",
      [
        "storage",
        "0029a139",
        null,
        "string"
      ]
    ],
    [
      "0073b4a0",
      "READ",
      [
        "storage",
        "0029f98d",
        null,
        "string"
      ]
    ],
    [
      "0073b568",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073b424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b424) · [`0073b498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b498) · [`0073b568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md#insn-0073b568)
- 新版 `0073b424`（命令位置の公開資料なし） · `0073b498`（命令位置の公開資料なし） · `0073b568`（命令位置の公開資料なし）

~~~diff
- 0073b424 ["COPY", "tmp:0:8", ["const:13b:8"]]
- 0073b424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073b424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073b424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["COPY", "tmp:0:8", ["const:139:8"]]
+ 0073b424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073b424 bytes 29ed0491
+ 0073b424 bytes 29e50491
- 0073b498 ["COPY", "tmp:0:8", ["const:902:8"]]
- 0073b498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073b498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073b498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["COPY", "tmp:0:8", ["const:98d:8"]]
+ 0073b498 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073b498 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073b498 bytes 29092491
+ 0073b498 bytes 29352691
- 0073b568 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
- 0073b568 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073b568 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e98:8"]]
+ 0073b568 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073b568 bytes 7b2747f9
+ 0073b568 bytes 7b4f47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba6bf7be60143640bf78ff5f62bef7f0"></a>

### [`0073bad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md) → [`0073bad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bad0.md) FUN_0073bad0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436bf8.md) [`00574144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md) [`005742c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/005742c4.md) [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md)
- 新版 呼出元 3件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) · 呼出先 10件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436bf8.md) [`00574144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574144.md) [`005742c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/005742c4.md) [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.56% / 新版 88.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073bb20",
      "incomplete_value": true,
      "site": "0073bb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073bb20",
      "incomplete_value": true,
      "site": "0073bb30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073bb7c",
      "incomplete_value": true,
      "site": "0073bb7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073bb7c",
      "incomplete_value": true,
      "site": "0073bb7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c77:8"
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
      "definition_site": "0073bb80",
      "incomplete_value": true,
      "site": "0073bb80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073bb80",
      "incomplete_value": true,
      "site": "0073bb80",
      "value": [
        "LOAD",
        "8",
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
      "0073bb20",
      "READ",
      [
        "storage",
        "0029f902",
        null,
        "string"
      ]
    ],
    [
      "0073bb6c",
      "READ",
      [
        "storage",
        "00293c77",
        null,
        "string"
      ]
    ],
    [
      "0073bb70",
      "READ",
      [
        "storage",
        "00293c7c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073bb20",
      "READ",
      [
        "storage",
        "0029f98d",
        null,
        "string"
      ]
    ],
    [
      "0073bb6c",
      "READ",
      [
        "storage",
        "00293bea",
        null,
        "string"
      ]
    ],
    [
      "0073bb70",
      "READ",
      [
        "storage",
        "00293bef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bb18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bb18) · [`0073bb64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bb64) · [`0073bbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bad0.md#insn-0073bbfc)
- 新版 `0073bb18`（命令位置の公開資料なし） · `0073bb64`（命令位置の公開資料なし） · `0073bbfc`（命令位置の公開資料なし）

~~~diff
- 0073bb18 ["COPY", "tmp:0:8", ["const:902:8"]]
- 0073bb18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["COPY", "tmp:0:8", ["const:98d:8"]]
+ 0073bb18 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb18 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073bb18 bytes 29092491
+ 0073bb18 bytes 29352691
- 0073bb64 ["COPY", "tmp:0:8", ["const:c77:8"]]
- 0073bb64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["COPY", "tmp:0:8", ["const:bea:8"]]
+ 0073bb64 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073bb64 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073bb64 bytes 29dd3191
+ 0073bb64 bytes 29a92f91
- 0073bbfc ["COPY", "tmp:0:8", ["const:a80:8"]]
- 0073bbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 0073bbfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073bbfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073bbfc bytes 08012a91
+ 0073bbfc bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f1ba6c976dbe82b29b251eccfafc7b9"></a>

### [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) → [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) FUN_0073bf10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436518.md)
- 新版 呼出元 1件 [`0073ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) · 呼出先 27件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436518.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.31% / 新版 95.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c0bc",
      "incomplete_value": true,
      "site": "0073c0d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073c13c",
      "incomplete_value": true,
      "site": "0073c13c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073c13c",
      "incomplete_value": true,
      "site": "0073c13c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c77:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073bfe0",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073bff4",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073c01c",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073bfe0",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0073bff4",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "0073c01c",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073bfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073bfe0) · [`0073c0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073c0b4) · [`0073c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md#insn-0073c120)
- 新版 `0073bfe0`（命令位置の公開資料なし） · `0073c0b4`（命令位置の公開資料なし） · `0073c120`（命令位置の公開資料なし）

~~~diff
- 0073bfe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:de0:8"]]
- 0073bfe0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073bfe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e30:8"]]
+ 0073bfe0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 0073bfe0 bytes 73f246f9
+ 0073bfe0 bytes 731a47f9
- 0073c0b4 ["COPY", "tmp:0:8", ["const:902:8"]]
- 0073c0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["COPY", "tmp:0:8", ["const:98d:8"]]
+ 0073c0b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c0b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073c0b4 bytes 29092491
+ 0073c0b4 bytes 29352691
- 0073c120 ["COPY", "tmp:0:8", ["const:c77:8"]]
- 0073c120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073c120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073c120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["COPY", "tmp:0:8", ["const:bea:8"]]
+ 0073c120 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073c120 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073c120 bytes 29dd3191
+ 0073c120 bytes 29a92f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4893cf8435e7780233942b74ae54f75b"></a>

### [`0073ccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073ccd0.md) → [`0073ccd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073ccd0.md) FUN_0073ccd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574344.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) · 呼出先 5件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00574344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574344.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.59% / 新版 95.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073cd14",
      "incomplete_value": true,
      "site": "0073cd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0073cd14",
      "incomplete_value": true,
      "site": "0073cd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0073cd04",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073cd1c",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0073cd04",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0073cd1c",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073cd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073ccd0.md#insn-0073cd04)
- 新版 `0073cd04`（命令位置の公開資料なし）

~~~diff
- 0073cd04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:de0:8"]]
- 0073cd04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073cd04 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e30:8"]]
+ 0073cd04 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0073cd04 bytes 4af146f9
+ 0073cd04 bytes 4a1947f9
~~~


<a id="compare-44144904b525496ea316ad03d498c387"></a>

### [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) → [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) FUN_0073cdfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00670f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670f08.md) · 呼出先 28件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md)
- 新版 呼出元 1件 [`00670f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670f08.md) · 呼出先 28件 [`0041b064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b064.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0042e8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e8c4.md) [`0042eb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eb00.md) [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.74% / 新版 92.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073ced4",
      "incomplete_value": true,
      "site": "0073cedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0073ced4",
      "incomplete_value": true,
      "site": "0073cedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:98d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073cfa4",
      "incomplete_value": true,
      "site": "0073cfb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:902:8"
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
      "0073cec8",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073cedc",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073cf04",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073cec8",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0073cedc",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "0073cf04",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073cec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073cec8) · [`0073cf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073cf9c) · [`0073d008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md#insn-0073d008)
- 新版 `0073cec8`（命令位置の公開資料なし） · `0073cf9c`（命令位置の公開資料なし） · `0073d008`（命令位置の公開資料なし）

~~~diff
- 0073cec8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:de0:8"]]
- 0073cec8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073cec8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:e30:8"]]
+ 0073cec8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0073cec8 bytes d6f246f9
+ 0073cec8 bytes d61a47f9
- 0073cf9c ["COPY", "tmp:0:8", ["const:902:8"]]
- 0073cf9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["COPY", "tmp:0:8", ["const:98d:8"]]
+ 0073cf9c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073cf9c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073cf9c bytes 29092491
+ 0073cf9c bytes 29352691
- 0073d008 ["COPY", "tmp:0:8", ["const:c77:8"]]
- 0073d008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073d008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073d008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["COPY", "tmp:0:8", ["const:bea:8"]]
+ 0073d008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073d008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073d008 bytes 29dd3191
+ 0073d008 bytes 29a92f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-384be9873b9c908f7a0e07b87f5e5c44"></a>

### [`0073da58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md) → [`0073da58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073da58.md) FUN_0073da58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00853f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00853/00853f6c.md) · 呼出先 8件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`0073a8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a8e0.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) [`00853f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00853/00853f6c.md) · 呼出先 8件 [`00436954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574238.md) [`0073a8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a8e0.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

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
      "definition_site": "0073daf4",
      "incomplete_value": true,
      "site": "0073dafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0073daf4",
      "incomplete_value": true,
      "site": "0073dafc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0073dae8",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0073dafc",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0073db24",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073dae8",
      "READ",
      [
        "storage",
        "00c1ae30",
        null,
        "pointer"
      ]
    ],
    [
      "0073dafc",
      "DATA",
      [
        "storage",
        "00bf0648",
        null,
        "pointer"
      ]
    ],
    [
      "0073db24",
      "READ",
      [
        "storage",
        "00bf0650",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073dae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073da58.md#insn-0073dae8)
- 新版 `0073dae8`（命令位置の公開資料なし）

~~~diff
- 0073dae8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:de0:8"]]
- 0073dae8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073dae8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e30:8"]]
+ 0073dae8 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0073dae8 bytes f7f246f9
+ 0073dae8 bytes f71a47f9
~~~


<a id="compare-cad6c09063a3a0f8db3fd3927894cd15"></a>

### [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md) → [`0073dc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073dc48.md) FUN_0073dc48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 17件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0073addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073addc.md) [`0073b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073b3dc.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00adc4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adc4c8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 17件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073ab94.md) [`0073addc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073addc.md) [`0073b3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073b3dc.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00adc50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adc50c.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.41% / 新版 95.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073dcbc",
      "incomplete_value": true,
      "site": "0073dcbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073dcbc",
      "incomplete_value": true,
      "site": "0073dcbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
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
      "definition_site": "0073dcb0",
      "incomplete_value": true,
      "site": "0073dcc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073dcb0",
      "incomplete_value": true,
      "site": "0073dcc0",
      "value": [
        "LOAD",
        "8",
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
      "0073dcac",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ],
    [
      "0073dcb0",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073dcac",
      "READ",
      [
        "storage",
        "002a0983",
        null,
        "string"
      ]
    ],
    [
      "0073dcb0",
      "READ",
      [
        "storage",
        "002a098a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073dca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md#insn-0073dca4)
- 新版 `0073dca4`（命令位置の公開資料なし）

~~~diff
- 0073dca4 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0073dca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["COPY", "tmp:0:8", ["const:983:8"]]
+ 0073dca4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073dca4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073dca4 bytes 29e12391
+ 0073dca4 bytes 290d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-decf1cfd699965e0805e678806bbdb37"></a>

### [`0073de68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md) → [`0073de68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073de68.md) FUN_0073de68

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00851b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00851/00851b9c.md) [`009a9ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00845f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00845/00845f8c.md) [`00adca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adca98.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 2件 [`00851b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00851/00851b9c.md) [`009a9ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a9/009a9ce0.md) · 呼出先 9件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00845f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00845/00845f8c.md) [`00adcadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adcadc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.95% / 新版 94.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073def0",
      "incomplete_value": true,
      "site": "0073def0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073def0",
      "incomplete_value": true,
      "site": "0073def0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
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
      "definition_site": "0073dee4",
      "incomplete_value": true,
      "site": "0073def4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073dee4",
      "incomplete_value": true,
      "site": "0073def4",
      "value": [
        "LOAD",
        "8",
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
      "0073dee0",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ],
    [
      "0073dee4",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073dee0",
      "READ",
      [
        "storage",
        "002a0983",
        null,
        "string"
      ]
    ],
    [
      "0073dee4",
      "READ",
      [
        "storage",
        "002a098a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073ded8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073de68.md#insn-0073ded8)
- 新版 `0073ded8`（命令位置の公開資料なし）

~~~diff
- 0073ded8 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0073ded8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["COPY", "tmp:0:8", ["const:983:8"]]
+ 0073ded8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073ded8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073ded8 bytes 29e12391
+ 0073ded8 bytes 290d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7defd2e1284df4940ce043d4bc369822"></a>

### [`0073e0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e0c8.md) → [`0073e0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e0c8.md) FUN_0073e0c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00996ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996ea0.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`00adcc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adc/00adcc80.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00996ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996ea0.md) · 呼出先 8件 [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`00adccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adc/00adccc4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073e148",
      "incomplete_value": true,
      "site": "0073e158",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073e148",
      "incomplete_value": true,
      "site": "0073e158",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073e15c",
      "incomplete_value": true,
      "site": "0073e15c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:983:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073e15c",
      "incomplete_value": true,
      "site": "0073e15c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
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
      "0073e148",
      "READ",
      [
        "storage",
        "002a08ff",
        null,
        "string"
      ]
    ],
    [
      "0073e14c",
      "READ",
      [
        "storage",
        "002a08f8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073e148",
      "READ",
      [
        "storage",
        "002a098a",
        null,
        "string"
      ]
    ],
    [
      "0073e14c",
      "READ",
      [
        "storage",
        "002a0983",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073e140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e0c8.md#insn-0073e140)
- 新版 `0073e140`（命令位置の公開資料なし）

~~~diff
- 0073e140 ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 0073e140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0073e140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0073e140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["COPY", "tmp:0:8", ["const:983:8"]]
+ 0073e140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0073e140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0073e140 bytes 29e12391
+ 0073e140 bytes 290d2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d790d7aefd4355dbf5aa80de0b7e457"></a>

### [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) → [`0073ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) FUN_0073ef14

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 6件 [`0073f4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md) [`0073f8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f8bc.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`0085c4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0085c/0085c4c4.md) · 呼出先 11件 [`0051d884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d884.md) [`00574fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574fe4.md) [`0073bf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073b/0073bf10.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md)
- 新版 呼出元 6件 [`0073f4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f4a8.md) [`0073f8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f8bc.md) [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`00859898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00859/00859898.md) [`0085c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0085c/0085c4c4.md) · 呼出先 11件 [`0051d884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d884.md) [`00574fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574fe4.md) [`0073bf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073b/0073bf10.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073dc48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073f224",
      "incomplete_value": false,
      "site": "0073f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f224",
      "incomplete_value": false,
      "site": "0073f22c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:dd8:8"
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
      "0073f22c",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0073f22c",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073f224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md#insn-0073f224)
- 新版 `0073f224`（命令位置の公開資料なし）

~~~diff
- 0073f224 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 0073f224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073f224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073f224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0073f224 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f224 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073f224 bytes 08613791
+ 0073f224 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93309fb638a73dd06878c8114242ef0a"></a>

### [`0073f4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md) → [`0073f4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073f4a8.md) FUN_0073f4a8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0084f0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f0f8.md) [`008eeba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ee/008eeba0.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0073d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073d/0073dc48.md) [`0073ef14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ef14.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 2件 [`0084f0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084f/0084f0f8.md) [`008eeba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ee/008eeba0.md) · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0073d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073d968.md) [`0073dc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073d/0073dc48.md) [`0073ef14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ef14.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.32% / 新版 94.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0073f5a8",
      "incomplete_value": true,
      "site": "0073f5b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f5a8",
      "incomplete_value": true,
      "site": "0073f5b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:77d:8"
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
      "definition_site": "0073f5ac",
      "incomplete_value": true,
      "site": "0073f5bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073f5ac",
      "incomplete_value": true,
      "site": "0073f5bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0073f740",
      "incomplete_value": true,
      "site": "0073f750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:808:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073f740",
      "incomplete_value": true,
      "site": "0073f750",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:77d:8"
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
      "0073f540",
      "READ",
      [
        "storage",
        "00293c77",
        null,
        "string"
      ]
    ],
    [
      "0073f544",
      "READ",
      [
        "storage",
        "00293c7c",
        null,
        "string"
      ]
    ],
    [
      "0073f5a8",
      "READ",
      [
        "storage",
        "0029e77d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0073f540",
      "READ",
      [
        "storage",
        "00293bea",
        null,
        "string"
      ]
    ],
    [
      "0073f544",
      "READ",
      [
        "storage",
        "00293bef",
        null,
        "string"
      ]
    ],
    [
      "0073f5a8",
      "READ",
      [
        "storage",
        "0029e808",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073f538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md#insn-0073f538) · [`0073f5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md#insn-0073f5a0) · [`0073f5a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073f4a8.md#insn-0073f5a4)
- 新版 `0073f538`（命令位置の公開資料なし） · `0073f5a0`（命令位置の公開資料なし）

~~~diff
- 0073f538 ["COPY", "tmp:0:8", ["const:c77:8"]]
- 0073f538 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["COPY", "tmp:0:8", ["const:bea:8"]]
+ 0073f538 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0073f538 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0073f538 bytes d6de3191
+ 0073f538 bytes d6aa2f91
- 0073f5a0 ["COPY", "tmp:0:8", ["const:77d:8"]]
- 0073f5a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 0073f5a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0073f5a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0073f5a0 bytes 08f51d91
+ 0073f5a0 bytes 08212091
- 0073f5a4 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0073f5a4 bytes 89dbffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-977e1877c722ecf7ef87296fe2859e75"></a>

### [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) → [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) FUN_0073fa38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 267件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 267件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041dfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041d/0041dfc0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.98% / 新版 98.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 24件, `store_value` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073fec4",
      "incomplete_value": false,
      "site": "0073fed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073fec4",
      "incomplete_value": false,
      "site": "0073fed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0073fed8",
      "incomplete_value": false,
      "site": "0073fee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0073fed8",
      "incomplete_value": false,
      "site": "0073fee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "definition_site": "00740108",
      "incomplete_value": false,
      "site": "00740110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00740108",
      "incomplete_value": false,
      "site": "00740110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0073fa70",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0073fa7c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073fa84",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0073fa70",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0073fa7c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0073fa84",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0073fa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa70) · [`0073fa7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa7c) · [`0073fa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/assembly/0073f/0073fa38-0073fa38-0074855c.md#insn-0073fa84)
- 新版 `0073fa70`（命令位置の公開資料なし） · `0073fa7c`（命令位置の公開資料なし） · `0073fa84`（命令位置の公開資料なし）

~~~diff
- 0073fa70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0073fa70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0073fa70 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0073fa70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0073fa70 bytes 083d45f9
+ 0073fa70 bytes 085d45f9
- 0073fa7c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0073fa7c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0073fa7c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0073fa7c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0073fa7c bytes 21203991
+ 0073fa7c bytes 21603a91
- 0073fa84 ["COPY", "tmp:0:8", ["const:490:8"]]
- 0073fa84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0073fa84 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0073fa84 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0073fa84 bytes 42401291
+ 0073fa84 bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed0d9bbe62403623b0e225e429cb2279"></a>

### [`00748560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md) → [`00748560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00748/00748560.md) FUN_00748560

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)
- 新版 呼出元 2件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) [`008e0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008e0/008e0bc0.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00748670",
      "incomplete_value": true,
      "site": "00748680",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:e5b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748670",
      "incomplete_value": true,
      "site": "00748680",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:ee8:8"
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
      "definition_site": "00748904",
      "incomplete_value": true,
      "site": "00748918",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:e6d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00748904",
      "incomplete_value": true,
      "site": "00748918",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:296000:8"
              ],
              [
                "leaf",
                "const:efa:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074891c",
      "incomplete_value": true,
      "site": "0074891c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0074891c",
      "incomplete_value": true,
      "site": "0074891c",
      "value": [
        "LOAD",
        "8",
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
      "00748630",
      "READ",
      [
        "storage",
        "002aee2a",
        null,
        "string"
      ]
    ],
    [
      "00748634",
      "READ",
      [
        "storage",
        "002aee33",
        null,
        "string"
      ]
    ],
    [
      "00748670",
      "READ",
      [
        "storage",
        "00296ee8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00748630",
      "READ",
      [
        "storage",
        "002aed96",
        null,
        "string"
      ]
    ],
    [
      "00748634",
      "READ",
      [
        "storage",
        "002aed9f",
        null,
        "string"
      ]
    ],
    [
      "00748670",
      "READ",
      [
        "storage",
        "00296e5b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00748628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-00748628) · [`00748668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-00748668) · [`007488fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00748/00748560.md#insn-007488fc)
- 新版 `00748628`（命令位置の公開資料なし） · `00748668`（命令位置の公開資料なし） · `007488fc`（命令位置の公開資料なし）

~~~diff
- 00748628 ["COPY", "tmp:0:8", ["const:e2a:8"]]
- 00748628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00748628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00748628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00748628 ["COPY", "tmp:0:8", ["const:d96:8"]]
+ 00748628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00748628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00748628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00748628 bytes 08a93891
+ 00748628 bytes 08593691
- 00748668 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00748668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00748668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00748668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["COPY", "tmp:0:8", ["const:e5b:8"]]
+ 00748668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00748668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00748668 bytes 29a13b91
+ 00748668 bytes 296d3991
- 007488fc ["COPY", "tmp:0:8", ["const:efa:8"]]
- 007488fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007488fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007488fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["COPY", "tmp:0:8", ["const:e6d:8"]]
+ 007488fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007488fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007488fc bytes 08e93b91
+ 007488fc bytes 08b53991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3343e146a12d33eaaad5ce5f92591117"></a>

### [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) → [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) FUN_00749514

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 126件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 126件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.85% / 新版 98.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0074b580",
      "incomplete_value": true,
      "site": "0074b580",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074b580",
      "incomplete_value": true,
      "site": "0074b580",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:715:8"
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
      "definition_site": "0074b584",
      "incomplete_value": true,
      "site": "0074b584",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0074b584",
      "incomplete_value": true,
      "site": "0074b584",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0074954c",
      "incomplete_value": true,
      "site": "0074954c",
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
      "definition_site": "0074954c",
      "incomplete_value": true,
      "site": "0074954c",
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
      "00749548",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0074955c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00749564",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00749548",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0074955c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00749564",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00749548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-00749548) · [`0074955c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-0074955c) · [`00749564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md#insn-00749564)
- 新版 `00749548`（命令位置の公開資料なし） · `0074955c`（命令位置の公開資料なし） · `00749564`（命令位置の公開資料なし）

~~~diff
- 00749548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00749548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00749548 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00749548 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00749548 bytes 083d45f9
+ 00749548 bytes 085d45f9
- 0074955c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0074955c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0074955c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0074955c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0074955c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0074955c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0074955c bytes 21203991
+ 0074955c bytes 21603a91
- 00749564 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00749564 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00749564 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00749564 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00749564 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00749564 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00749564 bytes 42401291
+ 00749564 bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b832536254d168ef8426ec0573561ee9"></a>

### [`0074ff74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md) → [`0074ff74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0074f/0074ff74.md) FUN_0074ff74

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 10件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0074ffac",
      "incomplete_value": true,
      "site": "0074ffac",
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
      "definition_site": "0074ffac",
      "incomplete_value": true,
      "site": "0074ffac",
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
      "definition_site": "0074ffb4",
      "incomplete_value": false,
      "site": "0074ffc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074ffb4",
      "incomplete_value": false,
      "site": "0074ffc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "0074ffbc",
      "incomplete_value": false,
      "site": "0074ffc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0074ffbc",
      "incomplete_value": false,
      "site": "0074ffc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "0074ffa8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0074ffb4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0074ffbc",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0074ffa8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0074ffb4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0074ffbc",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0074ffa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffa8) · [`0074ffb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffb4) · [`0074ffbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0074f/0074ff74.md#insn-0074ffbc)
- 新版 `0074ffa8`（命令位置の公開資料なし） · `0074ffb4`（命令位置の公開資料なし） · `0074ffbc`（命令位置の公開資料なし）

~~~diff
- 0074ffa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0074ffa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0074ffa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0074ffa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0074ffa8 bytes 083d45f9
+ 0074ffa8 bytes 085d45f9
- 0074ffb4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0074ffb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0074ffb4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0074ffb4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0074ffb4 bytes 21203991
+ 0074ffb4 bytes 21603a91
- 0074ffbc ["COPY", "tmp:0:8", ["const:490:8"]]
- 0074ffbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0074ffbc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0074ffbc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0074ffbc bytes 42401291
+ 0074ffbc bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d68b318bfdb5f25b2ca04acebc86a65"></a>

### [`00750454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md) → [`00750454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750454.md) FUN_00750454

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00749514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00749/00749514.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`0044abfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044abfc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md)
- 新版 呼出元 1件 [`00749514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00749/00749514.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`0044abfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044abfc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

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
      "definition_site": "00750490",
      "incomplete_value": true,
      "site": "00750490",
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
      "definition_site": "00750490",
      "incomplete_value": true,
      "site": "00750490",
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
      "definition_site": "00750498",
      "incomplete_value": false,
      "site": "007504ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00750498",
      "incomplete_value": false,
      "site": "007504ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "007504a0",
      "incomplete_value": false,
      "site": "007504ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007504a0",
      "incomplete_value": false,
      "site": "007504ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "0075048c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00750498",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007504a0",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0075048c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00750498",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "007504a0",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075048c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-0075048c) · [`00750498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-00750498) · [`007504a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750454.md#insn-007504a0)
- 新版 `0075048c`（命令位置の公開資料なし） · `00750498`（命令位置の公開資料なし） · `007504a0`（命令位置の公開資料なし）

~~~diff
- 0075048c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0075048c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075048c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0075048c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0075048c bytes 083d45f9
+ 0075048c bytes 085d45f9
- 00750498 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00750498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00750498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00750498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00750498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00750498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00750498 bytes 21203991
+ 00750498 bytes 21603a91
- 007504a0 ["COPY", "tmp:0:8", ["const:490:8"]]
- 007504a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 007504a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 007504a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 007504a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 007504a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 007504a0 bytes 42401291
+ 007504a0 bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e546320d35993168c4c63057538a77af"></a>

### [`00750ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md) → [`00750ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00750/00750ac4.md) FUN_00750ac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.45% / 新版 93.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00750b08",
      "incomplete_value": false,
      "site": "00750b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00750b08",
      "incomplete_value": false,
      "site": "00750b0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be7000:8"
          ],
          [
            "leaf",
            "const:d28:8"
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
      "definition_site": "00750c84",
      "incomplete_value": true,
      "site": "00750c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00750c84",
      "incomplete_value": true,
      "site": "00750c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00750c80",
      "incomplete_value": true,
      "site": "00750c8c",
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
      "definition_site": "00750c80",
      "incomplete_value": true,
      "site": "00750c8c",
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
      "00750b0c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00750c74",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "00750c78",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00750b0c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00750c74",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00750c78",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00750b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md#insn-00750b08) · [`00750c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md#insn-00750c74) · [`00750c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00750/00750ac4.md#insn-00750c78)
- 新版 `00750b08`（命令位置の公開資料なし） · `00750c74`（命令位置の公開資料なし） · `00750c78`（命令位置の公開資料なし）

~~~diff
- 00750b08 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00750b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00750b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00750b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00750b08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00750b08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00750b08 bytes 29a13491
+ 00750b08 bytes 29e13591
- 00750c74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00750c74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00750c74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00750c74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00750c74 bytes 08b946f9
+ 00750c74 bytes 08e146f9
- 00750c78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00750c78 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00750c78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 00750c78 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00750c78 bytes b5be46f9
+ 00750c78 bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b5da08f025a87f9f3c5df3038f39cd"></a>

### [`0075171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md) → [`0075171c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/0075171c.md) FUN_0075171c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00751b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751b90.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`0072e2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e2e4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`00751b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751b90.md) · 呼出先 6件 [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`0072e2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e2e4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00751738",
      "incomplete_value": false,
      "site": "0075173c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:de8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751738",
      "incomplete_value": false,
      "site": "0075173c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:d98:8"
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
      "definition_site": "00751b48",
      "incomplete_value": false,
      "site": "00751b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751b48",
      "incomplete_value": false,
      "site": "00751b4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "0075173c",
      "DATA",
      [
        "storage",
        "00bfad98",
        null,
        "pointer"
      ]
    ],
    [
      "00751b10",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751b4c",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0075173c",
      "DATA",
      [
        "storage",
        "00bfade8",
        null,
        "pointer"
      ]
    ],
    [
      "00751b10",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "00751b4c",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00751738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751738) · [`00751b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751b0c) · [`00751b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/0075171c.md#insn-00751b48)
- 新版 `00751738`（命令位置の公開資料なし） · `00751b0c`（命令位置の公開資料なし） · `00751b48`（命令位置の公開資料なし）

~~~diff
- 00751738 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00751738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00751738 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751738 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751738 bytes 08613691
+ 00751738 bytes 08a13791
- 00751b0c ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00751b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00751b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751b0c bytes 08e13691
+ 00751b0c bytes 08213891
- 00751b48 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00751b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00751b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751b48 bytes 08610a91
+ 00751b48 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1866eb615ed606ad278cbbc8917f9c63"></a>

### [`00751bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md) → [`00751bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751bb4.md) FUN_00751bb4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00751bcc",
      "incomplete_value": false,
      "site": "00751bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751bcc",
      "incomplete_value": false,
      "site": "00751bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "00751c08",
      "incomplete_value": false,
      "site": "00751c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751c08",
      "incomplete_value": false,
      "site": "00751c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "00751bd0",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751c0c",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00751bd0",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "00751c0c",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00751bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md#insn-00751bcc) · [`00751c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751bb4.md#insn-00751c08)
- 新版 `00751bcc`（命令位置の公開資料なし） · `00751c08`（命令位置の公開資料なし）

~~~diff
- 00751bcc ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00751bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00751bcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751bcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751bcc bytes 08e13691
+ 00751bcc bytes 08213891
- 00751c08 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00751c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00751c08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751c08 bytes 08610a91
+ 00751c08 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ff786e9c0dbdd5f37214daffd77f41"></a>

### [`00751c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md) → [`00751c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00751/00751c4c.md) FUN_00751c4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00751c64",
      "incomplete_value": false,
      "site": "00751c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751c64",
      "incomplete_value": false,
      "site": "00751c68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "00751ca0",
      "incomplete_value": false,
      "site": "00751ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00751ca0",
      "incomplete_value": false,
      "site": "00751ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf7000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "00751c68",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00751ca4",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00751c68",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "00751ca4",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00751c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md#insn-00751c64) · [`00751ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00751/00751c4c.md#insn-00751ca0)
- 新版 `00751c64`（命令位置の公開資料なし） · `00751ca0`（命令位置の公開資料なし）

~~~diff
- 00751c64 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 00751c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00751c64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751c64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751c64 bytes 08e13691
+ 00751c64 bytes 08213891
- 00751ca0 ["COPY", "tmp:0:8", ["const:298:8"]]
- 00751ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00751ca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00751ca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00751ca0 bytes 08610a91
+ 00751ca0 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d94a5aae7eae431bfe4f53411191fdf0"></a>

### [`0075233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075233c.md) → [`0075233c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075233c.md) FUN_0075233c

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
      "definition_site": "00752340",
      "incomplete_value": false,
      "site": "00752344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00752340",
      "incomplete_value": false,
      "site": "00752344",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "00752344",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00752344",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00752340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075233c.md#insn-00752340)
- 新版 `00752340`（命令位置の公開資料なし）

~~~diff
- 00752340 ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 00752340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00752340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00752340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00752340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00752340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00752340 bytes 08613791
+ 00752340 bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03f27f4edf54d51652820a2dfbb4ca2f"></a>

### [`0075234c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075234c.md) → [`0075234c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075234c.md) FUN_0075234c

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
      "definition_site": "0075235c",
      "incomplete_value": false,
      "site": "00752364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075235c",
      "incomplete_value": false,
      "site": "00752364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
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
      "00752364",
      "DATA",
      [
        "storage",
        "00bfadd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00752364",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075235c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075234c.md#insn-0075235c)
- 新版 `0075235c`（命令位置の公開資料なし）

~~~diff
- 0075235c ["COPY", "tmp:0:8", ["const:dd8:8"]]
- 0075235c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075235c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075235c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 0075235c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075235c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075235c bytes 08613791
+ 0075235c bytes 08a13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbf81b90e09422acd9c8a9ec5bfd1c03"></a>

### [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) → [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) FUN_007525f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0075246c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/0075246c.md) [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0075246c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/0075246c.md) [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.88% / 新版 98.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0075278c",
      "incomplete_value": false,
      "site": "00752794",
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
      "definition_site": "0075278c",
      "incomplete_value": false,
      "site": "00752794",
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
      "definition_site": "00752844",
      "incomplete_value": false,
      "site": "0075284c",
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
      "definition_site": "00752844",
      "incomplete_value": false,
      "site": "0075284c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00752860",
      "incomplete_value": false,
      "site": "0075286c",
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
      "definition_site": "00752860",
      "incomplete_value": false,
      "site": "0075286c",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0075278c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00752844",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00752860",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0075278c",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00752844",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00752860",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-0075278c) · [`00752844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-00752844) · [`00752860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md#insn-00752860)
- 新版 `0075278c`（命令位置の公開資料なし） · `00752844`（命令位置の公開資料なし） · `00752860`（命令位置の公開資料なし）

~~~diff
- 0075278c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0075278c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075278c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075278c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 0075278c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075278c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075278c bytes 21280c91
+ 0075278c bytes 21900e91
- 00752844 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00752844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00752844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00752844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00752844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00752844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00752844 bytes 21b80b91
+ 00752844 bytes 21e40d91
- 00752860 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00752860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00752860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00752860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00752860 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00752860 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00752860 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00752860 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00752860 bytes 21642491
+ 00752860 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c71709cf2498b39b8fbc6a0d6788ffc3"></a>

### [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) → [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) FUN_007530d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007525f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007525f0.md) [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007525f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007525f0.md) [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00753250",
      "incomplete_value": false,
      "site": "00753258",
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
      "definition_site": "00753250",
      "incomplete_value": false,
      "site": "00753258",
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
      "definition_site": "0075330c",
      "incomplete_value": false,
      "site": "00753314",
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
      "definition_site": "0075330c",
      "incomplete_value": false,
      "site": "00753314",
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
    "ordinal": 4,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00753324",
      "incomplete_value": false,
      "site": "00753330",
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
      "definition_site": "00753324",
      "incomplete_value": false,
      "site": "00753330",
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
      "00753250",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0075330c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00753324",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00753250",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0075330c",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "00753324",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00753250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-00753250) · [`0075330c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-0075330c) · [`00753324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md#insn-00753324)
- 新版 `00753250`（命令位置の公開資料なし） · `0075330c`（命令位置の公開資料なし） · `00753324`（命令位置の公開資料なし）

~~~diff
- 00753250 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00753250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00753250 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753250 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753250 bytes 21280c91
+ 00753250 bytes 21900e91
- 0075330c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0075330c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075330c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075330c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0075330c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075330c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075330c bytes 21b80b91
+ 0075330c bytes 21e40d91
- 00753324 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00753324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753324 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00753324 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753324 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753324 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753324 bytes 21642491
+ 00753324 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71cc72450e09abfcfa6b2024503a85bf"></a>

### [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) → [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) FUN_00753c40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/007530d8.md) [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007530d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/007530d8.md) [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.74% / 新版 98.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00753db0",
      "incomplete_value": false,
      "site": "00753db8",
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
      "definition_site": "00753db0",
      "incomplete_value": false,
      "site": "00753db8",
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
      "definition_site": "00753dd4",
      "incomplete_value": false,
      "site": "00753de0",
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
      "definition_site": "00753dd4",
      "incomplete_value": false,
      "site": "00753de0",
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
      "definition_site": "00753f08",
      "incomplete_value": false,
      "site": "00753f10",
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
      "definition_site": "00753f08",
      "incomplete_value": false,
      "site": "00753f10",
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
      "00753db0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00753dd4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00753f08",
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
      "00753db0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00753dd4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00753f08",
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

- 旧版 [`00753db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753db0) · [`00753dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753dd4) · [`00753f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md#insn-00753f08)
- 新版 `00753db0`（命令位置の公開資料なし） · `00753dd4`（命令位置の公開資料なし） · `00753f08`（命令位置の公開資料なし）

~~~diff
- 00753db0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00753db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00753db0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753db0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753db0 bytes 21280c91
+ 00753db0 bytes 21900e91
- 00753dd4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00753dd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753dd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753dd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753dd4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00753dd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753dd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753dd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753dd4 bytes 21642491
+ 00753dd4 bytes 21142291
- 00753f08 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00753f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00753f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00753f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00753f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00753f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00753f08 bytes 21b80b91
+ 00753f08 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-694aff9d3adc3307d2715687c5683f72"></a>

### [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) → [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) FUN_007545ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00753c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00753/00753c40.md) [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00753c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00753/00753c40.md) [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.71% / 新版 98.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00754754",
      "incomplete_value": false,
      "site": "0075475c",
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
      "definition_site": "00754754",
      "incomplete_value": false,
      "site": "0075475c",
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
      "definition_site": "007548c4",
      "incomplete_value": false,
      "site": "007548d0",
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
      "definition_site": "007548c4",
      "incomplete_value": false,
      "site": "007548d0",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00754954",
      "incomplete_value": false,
      "site": "00754960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:7da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00754954",
      "incomplete_value": false,
      "site": "00754960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:296000:8"
          ],
          [
            "leaf",
            "const:867:8"
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
      "00754754",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00754778",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "007548ac",
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
      "00754754",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00754778",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "007548ac",
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

- 旧版 [`00754754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-00754754) · [`00754778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-00754778) · [`007548ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md#insn-007548ac)
- 新版 `00754754`（命令位置の公開資料なし） · `00754778`（命令位置の公開資料なし） · `007548ac`（命令位置の公開資料なし）

~~~diff
- 00754754 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00754754 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00754754 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00754754 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00754754 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00754754 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00754754 bytes 21280c91
+ 00754754 bytes 21900e91
- 00754778 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00754778 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00754778 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00754778 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00754778 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00754778 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00754778 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00754778 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00754778 bytes 21642491
+ 00754778 bytes 21142291
- 007548ac ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 007548ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007548ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007548ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["COPY", "tmp:0:8", ["const:379:8"]]
+ 007548ac ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007548ac ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007548ac bytes 21b80b91
+ 007548ac bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d3ee7fdc1dad38fddcdf3e5c13d3053"></a>

### [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) → [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) FUN_00754f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007545ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/007545ec.md) [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007545ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/007545ec.md) [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "007550d4",
      "incomplete_value": false,
      "site": "007550dc",
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
      "definition_site": "007550d4",
      "incomplete_value": false,
      "site": "007550dc",
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
      "definition_site": "007550f8",
      "incomplete_value": false,
      "site": "00755104",
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
      "definition_site": "007550f8",
      "incomplete_value": false,
      "site": "00755104",
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
      "definition_site": "0075522c",
      "incomplete_value": false,
      "site": "00755234",
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
      "definition_site": "0075522c",
      "incomplete_value": false,
      "site": "00755234",
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
      "007550d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "007550f8",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "0075522c",
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
      "007550d4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "007550f8",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "0075522c",
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

- 旧版 [`007550d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-007550d4) · [`007550f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-007550f8) · [`0075522c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md#insn-0075522c)
- 新版 `007550d4`（命令位置の公開資料なし） · `007550f8`（命令位置の公開資料なし） · `0075522c`（命令位置の公開資料なし）

~~~diff
- 007550d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007550d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007550d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007550d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 007550d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007550d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007550d4 bytes 21280c91
+ 007550d4 bytes 21900e91
- 007550f8 ["COPY", "tmp:0:8", ["const:919:8"]]
- 007550f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007550f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007550f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007550f8 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 007550f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007550f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007550f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007550f8 bytes 21642491
+ 007550f8 bytes 21142291
- 0075522c ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 0075522c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075522c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075522c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["COPY", "tmp:0:8", ["const:379:8"]]
+ 0075522c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075522c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075522c bytes 21b80b91
+ 0075522c bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2fa7263569f11feedc8d31ac514e25"></a>

### [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) → [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) FUN_007558dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00754f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00754/00754f70.md) [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`00754f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00754/00754f70.md) [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00755a64",
      "incomplete_value": false,
      "site": "00755a70",
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
      "definition_site": "00755a64",
      "incomplete_value": false,
      "site": "00755a70",
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
      "definition_site": "00755b98",
      "incomplete_value": false,
      "site": "00755ba0",
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
      "definition_site": "00755b98",
      "incomplete_value": false,
      "site": "00755ba0",
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
      "definition_site": "00755bb0",
      "incomplete_value": false,
      "site": "00755bbc",
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
      "definition_site": "00755bb0",
      "incomplete_value": false,
      "site": "00755bbc",
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
      "00755a40",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00755a64",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00755b98",
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
      "00755a40",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00755a64",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00755b98",
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

- 旧版 [`00755a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755a40) · [`00755a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755a64) · [`00755b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md#insn-00755b98)
- 新版 `00755a40`（命令位置の公開資料なし） · `00755a64`（命令位置の公開資料なし） · `00755b98`（命令位置の公開資料なし）

~~~diff
- 00755a40 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00755a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00755a40 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a40 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755a40 bytes 21280c91
+ 00755a40 bytes 21900e91
- 00755a64 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00755a64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755a64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755a64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755a64 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00755a64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755a64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755a64 bytes 21642491
+ 00755a64 bytes 21142291
- 00755b98 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00755b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00755b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00755b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00755b98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00755b98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00755b98 bytes 21b80b91
+ 00755b98 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd65b4cad7197e0782fac448406d6474"></a>

### [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) → [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) FUN_00756248

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`007558dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00755/007558dc.md) [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`007558dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00755/007558dc.md) [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "007563a8",
      "incomplete_value": false,
      "site": "007563b0",
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
      "definition_site": "007563a8",
      "incomplete_value": false,
      "site": "007563b0",
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
      "definition_site": "007563cc",
      "incomplete_value": false,
      "site": "007563d8",
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
      "definition_site": "007563cc",
      "incomplete_value": false,
      "site": "007563d8",
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
      "definition_site": "00756500",
      "incomplete_value": false,
      "site": "00756508",
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
      "definition_site": "00756500",
      "incomplete_value": false,
      "site": "00756508",
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
      "007563a8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "007563cc",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00756500",
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
      "007563a8",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "007563cc",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00756500",
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

- 旧版 [`007563a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-007563a8) · [`007563cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-007563cc) · [`00756500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md#insn-00756500)
- 新版 `007563a8`（命令位置の公開資料なし） · `007563cc`（命令位置の公開資料なし） · `00756500`（命令位置の公開資料なし）

~~~diff
- 007563a8 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 007563a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007563a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007563a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 007563a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007563a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007563a8 bytes 21280c91
+ 007563a8 bytes 21900e91
- 007563cc ["COPY", "tmp:0:8", ["const:919:8"]]
- 007563cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 007563cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 007563cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 007563cc ["COPY", "tmp:0:8", ["const:885:8"]]
+ 007563cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 007563cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 007563cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 007563cc bytes 21642491
+ 007563cc bytes 21142291
- 00756500 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00756500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00756500 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756500 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756500 bytes 21b80b91
+ 00756500 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b49636522e507b7baf8ea690dcff662"></a>

### [`00756ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md) → [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) FUN_00756ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00756248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756248.md) [`00756ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md) [`00a00ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a00/00a00ca0.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 3件 [`00756248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756248.md) [`00756ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00756/00756ba0.md) [`00a00ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a00/00a00ce4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00756d00",
      "incomplete_value": false,
      "site": "00756d08",
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
      "definition_site": "00756d00",
      "incomplete_value": false,
      "site": "00756d08",
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
      "definition_site": "00756d24",
      "incomplete_value": true,
      "site": "00756d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
          ],
          [
            "leaf",
            "const:885:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00756d24",
      "incomplete_value": true,
      "site": "00756d30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4008:8"
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
      "definition_site": "00756e58",
      "incomplete_value": false,
      "site": "00756e60",
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
      "definition_site": "00756e58",
      "incomplete_value": false,
      "site": "00756e60",
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
      "00756d00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00756d24",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00756e58",
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
      "00756d00",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "00756d24",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00756e58",
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

- 旧版 [`00756d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756d00) · [`00756d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756d24) · [`00756e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00756/00756ba0.md#insn-00756e58)
- 新版 `00756d00`（命令位置の公開資料なし） · `00756d24`（命令位置の公開資料なし） · `00756e58`（命令位置の公開資料なし）

~~~diff
- 00756d00 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00756d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00756d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756d00 bytes 21280c91
+ 00756d00 bytes 21900e91
- 00756d24 ["COPY", "tmp:0:8", ["const:919:8"]]
- 00756d24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756d24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756d24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756d24 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 00756d24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756d24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756d24 bytes 21642491
+ 00756d24 bytes 21142291
- 00756e58 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00756e58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00756e58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00756e58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00756e58 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00756e58 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00756e58 bytes 21b80b91
+ 00756e58 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d3ca81e36c7abdb1271218770238421"></a>

### [`00757514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757514.md) → [`00757514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757514.md) FUN_00757514

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00757538",
      "incomplete_value": false,
      "site": "00757538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757538",
      "incomplete_value": false,
      "site": "00757538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00757538",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757538",
      "DATA",
      [
        "storage",
        "00bfae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757514.md#insn-00757534)
- 新版 `00757534`（命令位置の公開資料なし）

~~~diff
- 00757534 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00757534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00757534 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757534 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757534 bytes 08a13891
+ 00757534 bytes 08e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1616bbf2792702d80c78e5dd1eb207f0"></a>

### [`00757548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757548.md) → [`00757548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757548.md) FUN_00757548

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00757554",
      "incomplete_value": false,
      "site": "00757554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757554",
      "incomplete_value": false,
      "site": "00757554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:e28:8"
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
      "00757554",
      "DATA",
      [
        "storage",
        "00bfae28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757554",
      "DATA",
      [
        "storage",
        "00bfae78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757548.md#insn-00757550)
- 新版 `00757550`（命令位置の公開資料なし）

~~~diff
- 00757550 ["COPY", "tmp:0:8", ["const:e28:8"]]
- 00757550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["COPY", "tmp:0:8", ["const:e78:8"]]
+ 00757550 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757550 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757550 bytes 29a13891
+ 00757550 bytes 29e13991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55d87e7378b042643f6428a14f7b623c"></a>

### [`007575fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007575fc.md) → [`007575fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007575fc.md) FUN_007575fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00757620",
      "incomplete_value": false,
      "site": "00757620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757620",
      "incomplete_value": false,
      "site": "00757620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "00757620",
      "DATA",
      [
        "storage",
        "00bfaea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757620",
      "DATA",
      [
        "storage",
        "00bfaef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075761c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007575fc.md#insn-0075761c)
- 新版 `0075761c`（命令位置の公開資料なし）

~~~diff
- 0075761c ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 0075761c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075761c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 0075761c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075761c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075761c bytes 08a13a91
+ 0075761c bytes 08e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a420f9e30069d84a2ae16acc42f79c5e"></a>

### [`00757630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757630.md) → [`00757630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757630.md) FUN_00757630

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075763c",
      "incomplete_value": false,
      "site": "0075763c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075763c",
      "incomplete_value": false,
      "site": "0075763c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
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
      "0075763c",
      "DATA",
      [
        "storage",
        "00bfaea8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075763c",
      "DATA",
      [
        "storage",
        "00bfaef8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757630.md#insn-00757638)
- 新版 `00757638`（命令位置の公開資料なし）

~~~diff
- 00757638 ["COPY", "tmp:0:8", ["const:ea8:8"]]
- 00757638 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757638 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757638 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["COPY", "tmp:0:8", ["const:ef8:8"]]
+ 00757638 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757638 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757638 bytes 29a13a91
+ 00757638 bytes 29e13b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-895808caaf49ac6cccf4ddccdea3316e"></a>

### [`007576dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007576dc.md) → [`007576dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007576dc.md) FUN_007576dc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00757700",
      "incomplete_value": true,
      "site": "00757700",
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
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757700",
      "incomplete_value": true,
      "site": "00757700",
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
            "const:f28:8"
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
      "00757700",
      "DATA",
      [
        "storage",
        "00bfaf28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757700",
      "DATA",
      [
        "storage",
        "00bfaf78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007576fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007576dc.md#insn-007576fc)
- 新版 `007576fc`（命令位置の公開資料なし）

~~~diff
- 007576fc ["COPY", "tmp:0:8", ["const:f28:8"]]
- 007576fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007576fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007576fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 007576fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007576fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007576fc bytes 08a13c91
+ 007576fc bytes 08e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f9838b678a1f96e00e783b855fd820"></a>

### [`00757710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757710.md) → [`00757710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757710.md) FUN_00757710

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075771c",
      "incomplete_value": false,
      "site": "0075771c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:f78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075771c",
      "incomplete_value": false,
      "site": "0075771c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "0075771c",
      "DATA",
      [
        "storage",
        "00bfaf28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075771c",
      "DATA",
      [
        "storage",
        "00bfaf78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757710.md#insn-00757718)
- 新版 `00757718`（命令位置の公開資料なし）

~~~diff
- 00757718 ["COPY", "tmp:0:8", ["const:f28:8"]]
- 00757718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["COPY", "tmp:0:8", ["const:f78:8"]]
+ 00757718 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757718 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757718 bytes 29a13c91
+ 00757718 bytes 29e13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0631f7e70a262a82dc7eddafe27a81ed"></a>

### [`0075772c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075772c.md) → [`0075772c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075772c.md) FUN_0075772c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00883c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c6c.md) [`00883cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883cc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00883c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883c6c.md) [`00883cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883cc0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00757868",
      "incomplete_value": false,
      "site": "0075786c",
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
            "const:65a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757868",
      "incomplete_value": false,
      "site": "0075786c",
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
            "const:5cf:8"
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
      "00757868",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00757868",
      "PARAM",
      [
        "storage",
        "002a365a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075772c.md#insn-00757868)
- 新版 `00757868`（命令位置の公開資料なし）

~~~diff
- 00757868 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 00757868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00757868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00757868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 00757868 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00757868 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00757868 bytes 003c1791
+ 00757868 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba243f7eb8827dec9330bdc49899a8fb"></a>

### [`0075789c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075789c.md) → [`0075789c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/0075789c.md) FUN_0075789c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007578c0",
      "incomplete_value": false,
      "site": "007578c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007578c0",
      "incomplete_value": false,
      "site": "007578c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007578c0",
      "DATA",
      [
        "storage",
        "00bfafa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007578c0",
      "DATA",
      [
        "storage",
        "00bfaff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007578bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/0075789c.md#insn-007578bc)
- 新版 `007578bc`（命令位置の公開資料なし）

~~~diff
- 007578bc ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007578bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007578bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007578bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007578bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007578bc bytes 08a13e91
+ 007578bc bytes 08e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db7f53331ef95d9310a48bcc61b3c612"></a>

### [`007578d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007578d0.md) → [`007578d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007578d0.md) FUN_007578d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007578dc",
      "incomplete_value": false,
      "site": "007578dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007578dc",
      "incomplete_value": false,
      "site": "007578dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
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
      "007578dc",
      "DATA",
      [
        "storage",
        "00bfafa8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007578dc",
      "DATA",
      [
        "storage",
        "00bfaff8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007578d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007578d0.md#insn-007578d8)
- 新版 `007578d8`（命令位置の公開資料なし）

~~~diff
- 007578d8 ["COPY", "tmp:0:8", ["const:fa8:8"]]
- 007578d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007578d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007578d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["COPY", "tmp:0:8", ["const:ff8:8"]]
+ 007578d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007578d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007578d8 bytes 29a13e91
+ 007578d8 bytes 29e13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5233ddc29207c1739b86ae519341ea6d"></a>

### [`007579a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579a4.md) → [`007579a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579a4.md) FUN_007579a4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007579c8",
      "incomplete_value": false,
      "site": "007579c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007579c8",
      "incomplete_value": false,
      "site": "007579c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "007579c8",
      "DATA",
      [
        "storage",
        "00bfb028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007579c8",
      "DATA",
      [
        "storage",
        "00bfb078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007579c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579a4.md#insn-007579c4)
- 新版 `007579c4`（命令位置の公開資料なし）

~~~diff
- 007579c4 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007579c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007579c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007579c4 bytes 08a10091
+ 007579c4 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f7d90a78675fec3f138ffa14371b4e"></a>

### [`007579d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579d8.md) → [`007579d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579d8.md) FUN_007579d8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007579e4",
      "incomplete_value": false,
      "site": "007579e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007579e4",
      "incomplete_value": false,
      "site": "007579e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "007579e4",
      "DATA",
      [
        "storage",
        "00bfb028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007579e4",
      "DATA",
      [
        "storage",
        "00bfb078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007579e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579d8.md#insn-007579e0)
- 新版 `007579e0`（命令位置の公開資料なし）

~~~diff
- 007579e0 ["COPY", "tmp:0:8", ["const:28:8"]]
- 007579e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007579e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007579e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 007579e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007579e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007579e0 bytes 29a10091
+ 007579e0 bytes 29e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93fa6781804014c6eeaa03573f2a6409"></a>

### [`007579f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md) → [`007579f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/007579f4.md) FUN_007579f4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.78% / 新版 94.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00757b8c",
      "incomplete_value": true,
      "site": "00757b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:7b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757b8c",
      "incomplete_value": true,
      "site": "00757b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29d000:8"
              ],
              [
                "leaf",
                "const:725:8"
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
      "definition_site": "00757b94",
      "incomplete_value": true,
      "site": "00757b94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00757b94",
      "incomplete_value": true,
      "site": "00757b94",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00757c48",
      "incomplete_value": true,
      "site": "00757c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a0a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757c48",
      "incomplete_value": true,
      "site": "00757c58",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:97f:8"
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
      "00757b74",
      "READ",
      [
        "storage",
        "0029d725",
        null,
        "string"
      ]
    ],
    [
      "00757b7c",
      "READ",
      [
        "storage",
        "0029d72b",
        null,
        "string"
      ]
    ],
    [
      "00757c48",
      "READ",
      [
        "storage",
        "002a597f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00757b74",
      "READ",
      [
        "storage",
        "0029d7b0",
        null,
        "string"
      ]
    ],
    [
      "00757b7c",
      "READ",
      [
        "storage",
        "0029d7b6",
        null,
        "string"
      ]
    ],
    [
      "00757c48",
      "READ",
      [
        "storage",
        "002a5a0a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md#insn-00757b70) · [`00757c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md#insn-00757c40) · [`00757cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/007579f4.md#insn-00757cdc)
- 新版 `00757b70`（命令位置の公開資料なし） · `00757c40`（命令位置の公開資料なし） · `00757cdc`（命令位置の公開資料なし）

~~~diff
- 00757b70 ["COPY", "tmp:0:8", ["const:725:8"]]
- 00757b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["COPY", "tmp:0:8", ["const:7b0:8"]]
+ 00757b70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757b70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757b70 bytes 29951c91
+ 00757b70 bytes 29c11e91
- 00757c40 ["COPY", "tmp:0:8", ["const:97f:8"]]
- 00757c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00757c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00757c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00757c40 ["COPY", "tmp:0:8", ["const:a0a:8"]]
+ 00757c40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00757c40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00757c40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00757c40 bytes 29fd2591
+ 00757c40 bytes 29292891
- 00757cdc ["COPY", "tmp:0:8", ["const:98:8"]]
- 00757cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757cdc ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00757cdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757cdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757cdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757cdc bytes 08610291
+ 00757cdc bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b076787e2c717665e48d3a419e58a905"></a>

### [`00757f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f0c.md) → [`00757f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f0c.md) FUN_00757f0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00757f20",
      "incomplete_value": false,
      "site": "00757f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757f20",
      "incomplete_value": false,
      "site": "00757f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00757f24",
      "DATA",
      [
        "storage",
        "00bfb098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757f24",
      "DATA",
      [
        "storage",
        "00bfb0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f0c.md#insn-00757f20)
- 新版 `00757f20`（命令位置の公開資料なし）

~~~diff
- 00757f20 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00757f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00757f20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757f20 bytes 08610291
+ 00757f20 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750f032ad77301fb1c8fa3fa0454f88f"></a>

### [`00757f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f30.md) → [`00757f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f30.md) FUN_00757f30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00757f34",
      "incomplete_value": false,
      "site": "00757f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00757f34",
      "incomplete_value": false,
      "site": "00757f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "00757f38",
      "DATA",
      [
        "storage",
        "00bfb098",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00757f38",
      "DATA",
      [
        "storage",
        "00bfb0e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00757f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f30.md#insn-00757f34)
- 新版 `00757f34`（命令位置の公開資料なし）

~~~diff
- 00757f34 ["COPY", "tmp:0:8", ["const:98:8"]]
- 00757f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00757f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["COPY", "tmp:0:8", ["const:e8:8"]]
+ 00757f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00757f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00757f34 bytes 08610291
+ 00757f34 bytes 08a10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1003d6710088aa69c5bd6966b2ab5fc5"></a>

### [`00757f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md) → [`00757f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00757/00757f48.md) FUN_00757f48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041bce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041bce8.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "007580cc",
      "incomplete_value": false,
      "site": "007580cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007580cc",
      "incomplete_value": false,
      "site": "007580cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "007580cc",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ],
    [
      "00758124",
      "READ",
      [
        "storage",
        "00bfb128",
        null,
        "pointer"
      ]
    ],
    [
      "00758124",
      "READ",
      [
        "storage",
        "00bfb130",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007580cc",
      "DATA",
      [
        "storage",
        "00bfb158",
        null,
        "undefined *"
      ]
    ],
    [
      "00758124",
      "READ",
      [
        "storage",
        "00bfb178",
        null,
        "pointer"
      ]
    ],
    [
      "00758124",
      "READ",
      [
        "storage",
        "00bfb180",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md#insn-007580c4) · [`007580c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00757/00757f48.md#insn-007580c8)
- 新版 `007580c4`（命令位置の公開資料なし） · `007580c8`（命令位置の公開資料なし）

~~~diff
- 007580c4 ["COPY", "tmp:0:8", ["const:108:8"]]
- 007580c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007580c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007580c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 007580c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007580c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007580c4 bytes 08210491
+ 007580c4 bytes 08610591
- 007580c8 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
- 007580c8 bytes b40301d1
+ 007580c8 ["INT_SUB", "register:40a0:8", ["register:40e8:8", "const:40:8"]]
+ 007580c8 bytes b40301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a23869bfab86ddd9b648195e39760474"></a>

### [`0075833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/0075833c.md) → [`0075833c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/0075833c.md) FUN_0075833c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758350",
      "incomplete_value": false,
      "site": "00758354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758350",
      "incomplete_value": false,
      "site": "00758354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00758354",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758354",
      "DATA",
      [
        "storage",
        "00bfb158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/0075833c.md#insn-00758350)
- 新版 `00758350`（命令位置の公開資料なし）

~~~diff
- 00758350 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00758350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00758350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758350 bytes 08210491
+ 00758350 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-891c63040901da2c2fa195d023d56803"></a>

### [`00758360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758360.md) → [`00758360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758360.md) FUN_00758360

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758364",
      "incomplete_value": false,
      "site": "00758368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758364",
      "incomplete_value": false,
      "site": "00758368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00758368",
      "DATA",
      [
        "storage",
        "00bfb108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758368",
      "DATA",
      [
        "storage",
        "00bfb158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758360.md#insn-00758364)
- 新版 `00758364`（命令位置の公開資料なし）

~~~diff
- 00758364 ["COPY", "tmp:0:8", ["const:108:8"]]
- 00758364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 00758364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758364 bytes 08210491
+ 00758364 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa8432746aa8fc9754ada3d48fddf6b2"></a>

### [`00758378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md) → [`00758378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758378.md) FUN_00758378

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f2/006f23b4.md) [`0072f020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072f/0072f020.md)
- 新版 呼出元 0件  · 呼出先 14件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006f23b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f2/006f23b4.md) [`0072f020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072f/0072f020.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.26% / 新版 91.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00758424",
      "incomplete_value": true,
      "site": "00758434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dbe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758424",
      "incomplete_value": true,
      "site": "00758434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e52:8"
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
      "definition_site": "00758428",
      "incomplete_value": true,
      "site": "00758438",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00758428",
      "incomplete_value": true,
      "site": "00758438",
      "value": [
        "LOAD",
        "16",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00758454",
      "incomplete_value": false,
      "site": "0075845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758454",
      "incomplete_value": false,
      "site": "0075845c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "00758424",
      "READ",
      [
        "storage",
        "002aee52",
        null,
        "string"
      ]
    ],
    [
      "00758428",
      "READ",
      [
        "storage",
        "002aee60",
        null,
        "string"
      ]
    ],
    [
      "0075845c",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758424",
      "READ",
      [
        "storage",
        "002aedbe",
        null,
        "string"
      ]
    ],
    [
      "00758428",
      "READ",
      [
        "storage",
        "002aedcc",
        null,
        "string"
      ]
    ],
    [
      "0075845c",
      "DATA",
      [
        "storage",
        "00bfb1c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075841c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md#insn-0075841c) · [`00758420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758378.md#insn-00758420)
- 新版 `0075841c`（命令位置の公開資料なし） · `00758420`（命令位置の公開資料なし）

~~~diff
- 0075841c ["COPY", "tmp:0:8", ["const:e52:8"]]
- 0075841c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075841c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075841c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075841c ["COPY", "tmp:0:8", ["const:dbe:8"]]
+ 0075841c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075841c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075841c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075841c bytes 08493991
+ 0075841c bytes 08f93691
- 00758420 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00758420 bytes c9daff90
+ 00758420 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00758420 bytes c9daff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2a11316b963f1020cc9aa971460b8e4"></a>

### [`007585d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585d0.md) → [`007585d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585d0.md) FUN_007585d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007585e4",
      "incomplete_value": false,
      "site": "007585e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585e4",
      "incomplete_value": false,
      "site": "007585e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007585e8",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007585e8",
      "DATA",
      [
        "storage",
        "00bfb1c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585d0.md#insn-007585e4)
- 新版 `007585e4`（命令位置の公開資料なし）

~~~diff
- 007585e4 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007585e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 007585e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007585e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585e4 bytes 08e10591
+ 007585e4 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d89ed1c4f5ac25714d72d291934c102e"></a>

### [`007585f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585f4.md) → [`007585f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007585f4.md) FUN_007585f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007585f8",
      "incomplete_value": false,
      "site": "007585fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:1c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007585f8",
      "incomplete_value": false,
      "site": "007585fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:178:8"
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
      "007585fc",
      "DATA",
      [
        "storage",
        "00bfb178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007585fc",
      "DATA",
      [
        "storage",
        "00bfb1c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007585f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007585f4.md#insn-007585f8)
- 新版 `007585f8`（命令位置の公開資料なし）

~~~diff
- 007585f8 ["COPY", "tmp:0:8", ["const:178:8"]]
- 007585f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007585f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 007585f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007585f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007585f8 bytes 08e10591
+ 007585f8 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87931204ed49f34b05e60a38c0ece61e"></a>

### [`007586cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586cc.md) → [`007586cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586cc.md) FUN_007586cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "007586d8",
      "incomplete_value": false,
      "site": "007586dc",
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
      "definition_site": "007586d8",
      "incomplete_value": false,
      "site": "007586dc",
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
      "007586d8",
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
      "007586d8",
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

- 旧版 [`007586d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586cc.md#insn-007586d8)
- 新版 `007586d8`（命令位置の公開資料なし）

~~~diff
- 007586d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 007586d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 007586d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 007586d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 007586d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 007586d8 bytes 000c0c91
+ 007586d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c397bbef94d8e64b2939f1277c0a05e"></a>

### [`007586e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586e4.md) → [`007586e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007586e4.md) FUN_007586e4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758708",
      "incomplete_value": false,
      "site": "00758708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758708",
      "incomplete_value": false,
      "site": "00758708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "00758708",
      "DATA",
      [
        "storage",
        "00bfb228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758708",
      "DATA",
      [
        "storage",
        "00bfb278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007586e4.md#insn-00758704)
- 新版 `00758704`（命令位置の公開資料なし）

~~~diff
- 00758704 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00758704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00758704 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758704 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758704 bytes 08a10891
+ 00758704 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34226c7e57e731a881fd29a37324c360"></a>

### [`00758718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758718.md) → [`00758718`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758718.md) FUN_00758718

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758724",
      "incomplete_value": false,
      "site": "00758724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758724",
      "incomplete_value": false,
      "site": "00758724",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:228:8"
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
      "00758724",
      "DATA",
      [
        "storage",
        "00bfb228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758724",
      "DATA",
      [
        "storage",
        "00bfb278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758718.md#insn-00758720)
- 新版 `00758720`（命令位置の公開資料なし）

~~~diff
- 00758720 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00758720 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00758720 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00758720 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 00758720 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00758720 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00758720 bytes 29a10891
+ 00758720 bytes 29e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc7bd1ac5d4986108f684d3d937b60c1"></a>

### [`007587d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587d4.md) → [`007587d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587d4.md) FUN_007587d4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "007587e8",
      "incomplete_value": false,
      "site": "007587ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007587e8",
      "incomplete_value": false,
      "site": "007587ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "007587ec",
      "DATA",
      [
        "storage",
        "00bfb2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007587ec",
      "DATA",
      [
        "storage",
        "00bfb2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007587e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587d4.md#insn-007587e8)
- 新版 `007587e8`（命令位置の公開資料なし）

~~~diff
- 007587e8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007587e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007587e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007587e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007587e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007587e8 bytes 08a10a91
+ 007587e8 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a73d9f5588e19abdcf3de2518725aab1"></a>

### [`007587f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587f8.md) → [`007587f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007587f8.md) FUN_007587f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007587fc",
      "incomplete_value": false,
      "site": "00758800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007587fc",
      "incomplete_value": false,
      "site": "00758800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "00758800",
      "DATA",
      [
        "storage",
        "00bfb2a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758800",
      "DATA",
      [
        "storage",
        "00bfb2f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007587fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007587f8.md#insn-007587fc)
- 新版 `007587fc`（命令位置の公開資料なし）

~~~diff
- 007587fc ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 007587fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007587fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007587fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 007587fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007587fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007587fc bytes 08a10a91
+ 007587fc bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59afee1ded7c41a471ddefcb5ac35ba3"></a>

### [`00758884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758884.md) → [`00758884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758884.md) FUN_00758884

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758898",
      "incomplete_value": false,
      "site": "0075889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758898",
      "incomplete_value": false,
      "site": "0075889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "0075889c",
      "DATA",
      [
        "storage",
        "00bfb328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075889c",
      "DATA",
      [
        "storage",
        "00bfb378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758884.md#insn-00758898)
- 新版 `00758898`（命令位置の公開資料なし）

~~~diff
- 00758898 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00758898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00758898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758898 bytes 08a10c91
+ 00758898 bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0713de4eac78a32252d1653200703d30"></a>

### [`007588a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007588a8.md) → [`007588a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/007588a8.md) FUN_007588a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "007588ac",
      "incomplete_value": false,
      "site": "007588b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007588ac",
      "incomplete_value": false,
      "site": "007588b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "007588b0",
      "DATA",
      [
        "storage",
        "00bfb328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007588b0",
      "DATA",
      [
        "storage",
        "00bfb378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/007588a8.md#insn-007588ac)
- 新版 `007588ac`（命令位置の公開資料なし）

~~~diff
- 007588ac ["COPY", "tmp:0:8", ["const:328:8"]]
- 007588ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 007588ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 007588ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["COPY", "tmp:0:8", ["const:378:8"]]
+ 007588ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 007588ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 007588ac bytes 08a10c91
+ 007588ac bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-823259aa86a5fca1b177b87e60ea6ed0"></a>

### [`00758934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758934.md) → [`00758934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758934.md) FUN_00758934

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758948",
      "incomplete_value": false,
      "site": "0075894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758948",
      "incomplete_value": false,
      "site": "0075894c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "0075894c",
      "DATA",
      [
        "storage",
        "00bfb3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075894c",
      "DATA",
      [
        "storage",
        "00bfb3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758934.md#insn-00758948)
- 新版 `00758948`（命令位置の公開資料なし）

~~~diff
- 00758948 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00758948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00758948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758948 bytes 08a10e91
+ 00758948 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cfcf8cc96385e2eba403bf02be921f0"></a>

### [`00758958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758958.md) → [`00758958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758958.md) FUN_00758958

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075895c",
      "incomplete_value": false,
      "site": "00758960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075895c",
      "incomplete_value": false,
      "site": "00758960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "00758960",
      "DATA",
      [
        "storage",
        "00bfb3a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758960",
      "DATA",
      [
        "storage",
        "00bfb3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075895c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758958.md#insn-0075895c)
- 新版 `0075895c`（命令位置の公開資料なし）

~~~diff
- 0075895c ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 0075895c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075895c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075895c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 0075895c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075895c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075895c bytes 08a10e91
+ 0075895c bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbfecdaa4eebeac418da63266bca4b09"></a>

### [`00758a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a0c.md) → [`00758a0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758a0c.md) FUN_00758a0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758a20",
      "incomplete_value": false,
      "site": "00758a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758a20",
      "incomplete_value": false,
      "site": "00758a24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00758a24",
      "DATA",
      [
        "storage",
        "00bfb428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758a24",
      "DATA",
      [
        "storage",
        "00bfb478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a0c.md#insn-00758a20)
- 新版 `00758a20`（命令位置の公開資料なし）

~~~diff
- 00758a20 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00758a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00758a20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758a20 bytes 08a11091
+ 00758a20 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4137f29ba4c1dc7c3bab6dc197d9e62b"></a>

### [`00758a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a30.md) → [`00758a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758a30.md) FUN_00758a30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758a34",
      "incomplete_value": false,
      "site": "00758a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:478:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758a34",
      "incomplete_value": false,
      "site": "00758a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:428:8"
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
      "00758a38",
      "DATA",
      [
        "storage",
        "00bfb428",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758a38",
      "DATA",
      [
        "storage",
        "00bfb478",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758a30.md#insn-00758a34)
- 新版 `00758a34`（命令位置の公開資料なし）

~~~diff
- 00758a34 ["COPY", "tmp:0:8", ["const:428:8"]]
- 00758a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00758a34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758a34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758a34 bytes 08a11091
+ 00758a34 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-873346de6d1c366c7dfd57d53619b7e9"></a>

### [`00758abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758abc.md) → [`00758abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758abc.md) FUN_00758abc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758ad0",
      "incomplete_value": false,
      "site": "00758ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ad0",
      "incomplete_value": false,
      "site": "00758ad4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "00758ad4",
      "DATA",
      [
        "storage",
        "00bfb4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ad4",
      "DATA",
      [
        "storage",
        "00bfb4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758abc.md#insn-00758ad0)
- 新版 `00758ad0`（命令位置の公開資料なし）

~~~diff
- 00758ad0 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00758ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00758ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ad0 bytes 08a11291
+ 00758ad0 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5351a6c0882fd5a60f61162d2274913"></a>

### [`00758ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ae0.md) → [`00758ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758ae0.md) FUN_00758ae0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758ae4",
      "incomplete_value": false,
      "site": "00758ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ae4",
      "incomplete_value": false,
      "site": "00758ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:4a8:8"
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
      "00758ae8",
      "DATA",
      [
        "storage",
        "00bfb4a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ae8",
      "DATA",
      [
        "storage",
        "00bfb4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ae0.md#insn-00758ae4)
- 新版 `00758ae4`（命令位置の公開資料なし）

~~~diff
- 00758ae4 ["COPY", "tmp:0:8", ["const:4a8:8"]]
- 00758ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00758ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ae4 bytes 08a11291
+ 00758ae4 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-118865c01a4f6a1f740919e8603d4bdf"></a>

### [`00758b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b64.md) → [`00758b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758b64.md) FUN_00758b64

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758b78",
      "incomplete_value": false,
      "site": "00758b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758b78",
      "incomplete_value": false,
      "site": "00758b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "00758b7c",
      "DATA",
      [
        "storage",
        "00bfb528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758b7c",
      "DATA",
      [
        "storage",
        "00bfb578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b64.md#insn-00758b78)
- 新版 `00758b78`（命令位置の公開資料なし）

~~~diff
- 00758b78 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00758b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00758b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758b78 bytes 08a11491
+ 00758b78 bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-709442b7af6451c7400aacc78031e480"></a>

### [`00758b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b88.md) → [`00758b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758b88.md) FUN_00758b88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758b8c",
      "incomplete_value": false,
      "site": "00758b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758b8c",
      "incomplete_value": false,
      "site": "00758b90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:528:8"
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
      "00758b90",
      "DATA",
      [
        "storage",
        "00bfb528",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758b90",
      "DATA",
      [
        "storage",
        "00bfb578",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758b88.md#insn-00758b8c)
- 新版 `00758b8c`（命令位置の公開資料なし）

~~~diff
- 00758b8c ["COPY", "tmp:0:8", ["const:528:8"]]
- 00758b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["COPY", "tmp:0:8", ["const:578:8"]]
+ 00758b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758b8c bytes 08a11491
+ 00758b8c bytes 08e11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d587300d2be261e719fa254441b2bd7b"></a>

### [`00758c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c34.md) → [`00758c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758c34.md) FUN_00758c34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758c48",
      "incomplete_value": false,
      "site": "00758c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758c48",
      "incomplete_value": false,
      "site": "00758c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "00758c4c",
      "DATA",
      [
        "storage",
        "00bfb5a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758c4c",
      "DATA",
      [
        "storage",
        "00bfb5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c34.md#insn-00758c48)
- 新版 `00758c48`（命令位置の公開資料なし）

~~~diff
- 00758c48 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 00758c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00758c48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758c48 bytes 08a11691
+ 00758c48 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3716bae770f6e6e07ef629388a3d498d"></a>

### [`00758c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c58.md) → [`00758c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758c58.md) FUN_00758c58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758c5c",
      "incomplete_value": false,
      "site": "00758c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758c5c",
      "incomplete_value": false,
      "site": "00758c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "00758c60",
      "DATA",
      [
        "storage",
        "00bfb5a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758c60",
      "DATA",
      [
        "storage",
        "00bfb5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758c58.md#insn-00758c5c)
- 新版 `00758c5c`（命令位置の公開資料なし）

~~~diff
- 00758c5c ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 00758c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00758c5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758c5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758c5c bytes 08a11691
+ 00758c5c bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-701fbaead0968e08fcc735469a18ddf8"></a>

### [`00758ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ce4.md) → [`00758ce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758ce4.md) FUN_00758ce4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758cf8",
      "incomplete_value": false,
      "site": "00758cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758cf8",
      "incomplete_value": false,
      "site": "00758cfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "00758cfc",
      "DATA",
      [
        "storage",
        "00bfb628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758cfc",
      "DATA",
      [
        "storage",
        "00bfb678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ce4.md#insn-00758cf8)
- 新版 `00758cf8`（命令位置の公開資料なし）

~~~diff
- 00758cf8 ["COPY", "tmp:0:8", ["const:628:8"]]
- 00758cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00758cf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758cf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758cf8 bytes 08a11891
+ 00758cf8 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6077955cb9b4975643653b87e0e54f2d"></a>

### [`00758d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d08.md) → [`00758d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758d08.md) FUN_00758d08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758d0c",
      "incomplete_value": false,
      "site": "00758d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758d0c",
      "incomplete_value": false,
      "site": "00758d10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:628:8"
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
      "00758d10",
      "DATA",
      [
        "storage",
        "00bfb628",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758d10",
      "DATA",
      [
        "storage",
        "00bfb678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d08.md#insn-00758d0c)
- 新版 `00758d0c`（命令位置の公開資料なし）

~~~diff
- 00758d0c ["COPY", "tmp:0:8", ["const:628:8"]]
- 00758d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00758d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758d0c bytes 08a11891
+ 00758d0c bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839fcd56f864fe9a6c0b1cf3c78db08d"></a>

### [`00758d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d94.md) → [`00758d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758d94.md) FUN_00758d94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758da8",
      "incomplete_value": false,
      "site": "00758dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758da8",
      "incomplete_value": false,
      "site": "00758dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00758dac",
      "DATA",
      [
        "storage",
        "00bfb6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758dac",
      "DATA",
      [
        "storage",
        "00bfb6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758d94.md#insn-00758da8)
- 新版 `00758da8`（命令位置の公開資料なし）

~~~diff
- 00758da8 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00758da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00758da8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758da8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758da8 bytes 08a11a91
+ 00758da8 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3bcd6dc5f07e930bd3be7c2e86fc1f58"></a>

### [`00758db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758db8.md) → [`00758db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758db8.md) FUN_00758db8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758dbc",
      "incomplete_value": false,
      "site": "00758dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758dbc",
      "incomplete_value": false,
      "site": "00758dc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00758dc0",
      "DATA",
      [
        "storage",
        "00bfb6a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758dc0",
      "DATA",
      [
        "storage",
        "00bfb6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758db8.md#insn-00758dbc)
- 新版 `00758dbc`（命令位置の公開資料なし）

~~~diff
- 00758dbc ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00758dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00758dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758dbc bytes 08a11a91
+ 00758dbc bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197862f002265de7f2577b7d2df22114"></a>

### [`00758f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f24.md) → [`00758f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758f24.md) FUN_00758f24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00758f38",
      "incomplete_value": false,
      "site": "00758f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758f38",
      "incomplete_value": false,
      "site": "00758f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00758f3c",
      "DATA",
      [
        "storage",
        "00bfb728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758f3c",
      "DATA",
      [
        "storage",
        "00bfb778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f24.md#insn-00758f38)
- 新版 `00758f38`（命令位置の公開資料なし）

~~~diff
- 00758f38 ["COPY", "tmp:0:8", ["const:728:8"]]
- 00758f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00758f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758f38 bytes 08a11c91
+ 00758f38 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc666df4cc748e9cd8090f294276d332"></a>

### [`00758f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f48.md) → [`00758f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758f48.md) FUN_00758f48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758f4c",
      "incomplete_value": false,
      "site": "00758f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758f4c",
      "incomplete_value": false,
      "site": "00758f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00758f50",
      "DATA",
      [
        "storage",
        "00bfb728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758f50",
      "DATA",
      [
        "storage",
        "00bfb778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758f48.md#insn-00758f4c)
- 新版 `00758f4c`（命令位置の公開資料なし）

~~~diff
- 00758f4c ["COPY", "tmp:0:8", ["const:728:8"]]
- 00758f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00758f4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758f4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758f4c bytes 08a11c91
+ 00758f4c bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-631d0cbfd4c24bffbba6ca3342086a88"></a>

### [`00758ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ff4.md) → [`00758ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00758/00758ff4.md) FUN_00758ff4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00758ff8",
      "incomplete_value": false,
      "site": "00758ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:7f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00758ff8",
      "incomplete_value": false,
      "site": "00758ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:7a8:8"
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
      "00758ffc",
      "DATA",
      [
        "storage",
        "00bfb7a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00758ffc",
      "DATA",
      [
        "storage",
        "00bfb7f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00758ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00758/00758ff4.md#insn-00758ff8)
- 新版 `00758ff8`（命令位置の公開資料なし）

~~~diff
- 00758ff8 ["COPY", "tmp:0:8", ["const:7a8:8"]]
- 00758ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["COPY", "tmp:0:8", ["const:7f8:8"]]
+ 00758ff8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00758ff8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00758ff8 bytes 08a11e91
+ 00758ff8 bytes 08e11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cb82d6d1423b5c4a2c6d2200305f474"></a>

### [`0075916c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075916c.md) → [`0075916c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/0075916c.md) FUN_0075916c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00759180",
      "incomplete_value": false,
      "site": "00759184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759180",
      "incomplete_value": false,
      "site": "00759184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "00759184",
      "DATA",
      [
        "storage",
        "00bfb828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759184",
      "DATA",
      [
        "storage",
        "00bfb878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075916c.md#insn-00759180)
- 新版 `00759180`（命令位置の公開資料なし）

~~~diff
- 00759180 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00759180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 00759180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759180 bytes 08a12091
+ 00759180 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c674c3c737206a88d6898c14b90492a"></a>

### [`00759190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759190.md) → [`00759190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759190.md) FUN_00759190

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00759194",
      "incomplete_value": false,
      "site": "00759198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759194",
      "incomplete_value": false,
      "site": "00759198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:828:8"
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
      "00759198",
      "DATA",
      [
        "storage",
        "00bfb828",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759198",
      "DATA",
      [
        "storage",
        "00bfb878",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759190.md#insn-00759194)
- 新版 `00759194`（命令位置の公開資料なし）

~~~diff
- 00759194 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00759194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["COPY", "tmp:0:8", ["const:878:8"]]
+ 00759194 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759194 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759194 bytes 08a12091
+ 00759194 bytes 08e12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5238d6f09954e14d356eada925b3c8f4"></a>

### [`00759248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759248.md) → [`00759248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759248.md) FUN_00759248

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0075925c",
      "incomplete_value": false,
      "site": "00759260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075925c",
      "incomplete_value": false,
      "site": "00759260",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "00759260",
      "DATA",
      [
        "storage",
        "00bfb8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759260",
      "DATA",
      [
        "storage",
        "00bfb8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075925c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759248.md#insn-0075925c)
- 新版 `0075925c`（命令位置の公開資料なし）

~~~diff
- 0075925c ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 0075925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 0075925c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075925c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075925c bytes 08a12291
+ 0075925c bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23145d1d4a7206896ded3f3bf8753e1a"></a>

### [`0075926c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075926c.md) → [`0075926c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/0075926c.md) FUN_0075926c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00759270",
      "incomplete_value": false,
      "site": "00759274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759270",
      "incomplete_value": false,
      "site": "00759274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "00759274",
      "DATA",
      [
        "storage",
        "00bfb8a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759274",
      "DATA",
      [
        "storage",
        "00bfb8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/0075926c.md#insn-00759270)
- 新版 `00759270`（命令位置の公開資料なし）

~~~diff
- 00759270 ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00759270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00759270 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759270 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759270 bytes 08a12291
+ 00759270 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a38b80707f941ea8ff95042ce3b0e2b2"></a>

### [`007592ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/007592ec.md) → [`007592ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/007592ec.md) FUN_007592ec

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
      "definition_site": "007592f8",
      "incomplete_value": false,
      "site": "007592fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "007592f8",
      "incomplete_value": false,
      "site": "007592fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "007592fc",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "007592fc",
      "DATA",
      [
        "storage",
        "00bfb978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`007592f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/007592ec.md#insn-007592f8)
- 新版 `007592f8`（命令位置の公開資料なし）

~~~diff
- 007592f8 ["COPY", "tmp:0:8", ["const:928:8"]]
- 007592f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 007592f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 007592f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 007592f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 007592f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 007592f8 bytes 29a12491
+ 007592f8 bytes 29e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e5e761b0c8cd1ee4c9969b5bcc40e01"></a>

### [`00759310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759310.md) → [`00759310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759310.md) FUN_00759310

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
      "definition_site": "00759318",
      "incomplete_value": false,
      "site": "0075931c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759318",
      "incomplete_value": false,
      "site": "0075931c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "0075931c",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075931c",
      "DATA",
      [
        "storage",
        "00bfb978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759310.md#insn-00759318)
- 新版 `00759318`（命令位置の公開資料なし）

~~~diff
- 00759318 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00759318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00759318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00759318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00759318 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00759318 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00759318 bytes 29a12491
+ 00759318 bytes 29e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f75fc1db1aed52267327eaa10377fc6b"></a>

### [`00759350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759350.md) → [`00759350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759350.md) FUN_00759350

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`007523a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00752/007523a8.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`007523a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00752/007523a8.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00759370",
      "incomplete_value": false,
      "site": "00759378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759370",
      "incomplete_value": false,
      "site": "00759378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:928:8"
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
      "00759378",
      "DATA",
      [
        "storage",
        "00bfb928",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759378",
      "DATA",
      [
        "storage",
        "00bfb978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759350.md#insn-00759370)
- 新版 `00759370`（命令位置の公開資料なし）

~~~diff
- 00759370 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00759370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00759370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759370 bytes 08a12491
+ 00759370 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-421ea0e5adcd88d86869b8a9126a8f41"></a>

### [`00759544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md) → [`00759544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759544.md) FUN_00759544

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00759910",
      "incomplete_value": true,
      "site": "00759910",
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
            "const:f6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759910",
      "incomplete_value": true,
      "site": "00759910",
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
            "const:ff9:8"
          ]
        ]
      ]
    },
    "ordinal": 57,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00759910",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "00759964",
      "READ",
      [
        "storage",
        "0029e7b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00759910",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "00759964",
      "READ",
      [
        "storage",
        "0029e844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md#insn-00759908) · [`00759960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759544.md#insn-00759960)
- 新版 `00759908`（命令位置の公開資料なし） · `00759960`（命令位置の公開資料なし）

~~~diff
- 00759908 ["COPY", "tmp:0:8", ["const:ff9:8"]]
- 00759908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["COPY", "tmp:0:8", ["const:f6c:8"]]
+ 00759908 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759908 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759908 bytes 08e53f91
+ 00759908 bytes 08b13d91
- 00759960 ["COPY", "tmp:0:8", ["const:7b9:8"]]
- 00759960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["COPY", "tmp:0:8", ["const:844:8"]]
+ 00759960 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759960 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759960 bytes 08e51e91
+ 00759960 bytes 08112191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e701b165383171518fe0fc2fb84bd4cd"></a>

### [`00759e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e68.md) → [`00759e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759e68.md) FUN_00759e68

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00759e8c",
      "incomplete_value": false,
      "site": "00759e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759e8c",
      "incomplete_value": false,
      "site": "00759e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "00759e8c",
      "DATA",
      [
        "storage",
        "00bfb9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759e8c",
      "DATA",
      [
        "storage",
        "00bfb9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e68.md#insn-00759e88)
- 新版 `00759e88`（命令位置の公開資料なし）

~~~diff
- 00759e88 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00759e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00759e88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759e88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759e88 bytes 08a12691
+ 00759e88 bytes 08e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fd5289f1f27d57a1ba85cd8d60c0b73"></a>

### [`00759e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e9c.md) → [`00759e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759e9c.md) FUN_00759e9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00759ea8",
      "incomplete_value": false,
      "site": "00759ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759ea8",
      "incomplete_value": false,
      "site": "00759ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
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
      "00759ea8",
      "DATA",
      [
        "storage",
        "00bfb9a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759ea8",
      "DATA",
      [
        "storage",
        "00bfb9f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759e9c.md#insn-00759ea4)
- 新版 `00759ea4`（命令位置の公開資料なし）

~~~diff
- 00759ea4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00759ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["COPY", "tmp:0:8", ["const:9f8:8"]]
+ 00759ea4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00759ea4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00759ea4 bytes 29a12691
+ 00759ea4 bytes 29e12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6c4ab526e4c2e33700a7fb5476410b6"></a>

### [`00759f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f48.md) → [`00759f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759f48.md) FUN_00759f48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00759f6c",
      "incomplete_value": false,
      "site": "00759f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759f6c",
      "incomplete_value": false,
      "site": "00759f70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00759f70",
      "DATA",
      [
        "storage",
        "00bfba28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759f70",
      "DATA",
      [
        "storage",
        "00bfba78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f48.md#insn-00759f6c)
- 新版 `00759f6c`（命令位置の公開資料なし）

~~~diff
- 00759f6c ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00759f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00759f6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759f6c bytes 08a12891
+ 00759f6c bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dc344a009fea3b3bdef626c84e0ae01"></a>

### [`00759f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f88.md) → [`00759f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759f88.md) FUN_00759f88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00759f8c",
      "incomplete_value": false,
      "site": "00759f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00759f8c",
      "incomplete_value": false,
      "site": "00759f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a28:8"
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
      "00759f90",
      "DATA",
      [
        "storage",
        "00bfba28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00759f90",
      "DATA",
      [
        "storage",
        "00bfba78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00759f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759f88.md#insn-00759f8c)
- 新版 `00759f8c`（命令位置の公開資料なし）

~~~diff
- 00759f8c ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00759f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00759f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00759f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 00759f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00759f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00759f8c bytes 08a12891
+ 00759f8c bytes 08e12991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a938a48054214e08953097a390384fc7"></a>

### [`00759fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md) → [`00759fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00759/00759fb0.md) FUN_00759fb0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.10% / 新版 95.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0075a0b8",
      "incomplete_value": true,
      "site": "0075a0b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:da7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a0b8",
      "incomplete_value": true,
      "site": "0075a0b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:291000:8"
              ],
              [
                "leaf",
                "const:e34:8"
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
      "definition_site": "0075a0ac",
      "incomplete_value": true,
      "site": "0075a0bc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0075a0ac",
      "incomplete_value": true,
      "site": "0075a0bc",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0075a0d8",
      "incomplete_value": false,
      "site": "0075a0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a0d8",
      "incomplete_value": false,
      "site": "0075a0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "0075a0a8",
      "READ",
      [
        "storage",
        "00291e34",
        null,
        "string"
      ]
    ],
    [
      "0075a0ac",
      "READ",
      [
        "storage",
        "00291e3b",
        null,
        "string"
      ]
    ],
    [
      "0075a0d8",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a0a8",
      "READ",
      [
        "storage",
        "00291da7",
        null,
        "string"
      ]
    ],
    [
      "0075a0ac",
      "READ",
      [
        "storage",
        "00291dae",
        null,
        "string"
      ]
    ],
    [
      "0075a0d8",
      "DATA",
      [
        "storage",
        "00bfbb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md#insn-0075a0a0) · [`0075a0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md#insn-0075a0d0) · [`0075a0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00759/00759fb0.md#insn-0075a0d4)
- 新版 `0075a0a0`（命令位置の公開資料なし） · `0075a0d0`（命令位置の公開資料なし）

~~~diff
- 0075a0a0 ["COPY", "tmp:0:8", ["const:e34:8"]]
- 0075a0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["COPY", "tmp:0:8", ["const:da7:8"]]
+ 0075a0a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075a0a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075a0a0 bytes 29d13891
+ 0075a0a0 bytes 299d3691
- 0075a0d0 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0075a0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0075a0d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a0d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a0d0 bytes 08612c91
+ 0075a0d0 bytes 08a12d91
- 0075a0d4 ["INT_SUB", "register:4098:8", ["register:40e8:8", "const:b0:8"]]
- 0075a0d4 bytes b3c302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e94ce716e3e69104983c4d3c4b22b829"></a>

### [`0075a7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7b4.md) → [`0075a7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075a7b4.md) FUN_0075a7b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0075a7d8",
      "incomplete_value": false,
      "site": "0075a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a7d8",
      "incomplete_value": false,
      "site": "0075a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "0075a7dc",
      "DATA",
      [
        "storage",
        "00bfba98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a7dc",
      "DATA",
      [
        "storage",
        "00bfbae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7b4.md#insn-0075a7d8)
- 新版 `0075a7d8`（命令位置の公開資料なし）

~~~diff
- 0075a7d8 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0075a7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0075a7d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a7d8 bytes 08612a91
+ 0075a7d8 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b295e68e4681981dea4d659968e7a4"></a>

### [`0075a7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7f4.md) → [`0075a7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075a7f4.md) FUN_0075a7f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0075a7f8",
      "incomplete_value": false,
      "site": "0075a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075a7f8",
      "incomplete_value": false,
      "site": "0075a7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:a98:8"
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
      "0075a7fc",
      "DATA",
      [
        "storage",
        "00bfba98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075a7fc",
      "DATA",
      [
        "storage",
        "00bfbae8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075a7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075a7f4.md#insn-0075a7f8)
- 新版 `0075a7f8`（命令位置の公開資料なし）

~~~diff
- 0075a7f8 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 0075a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 0075a7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075a7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075a7f8 bytes 08612a91
+ 0075a7f8 bytes 08a12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de811a0ba7de6ac18f140d01c5ca6066"></a>

### [`0075ac88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ac88.md) → [`0075ac88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075ac88.md) FUN_0075ac88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0075acac",
      "incomplete_value": false,
      "site": "0075acac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075acac",
      "incomplete_value": false,
      "site": "0075acac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "0075acac",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075acac",
      "DATA",
      [
        "storage",
        "00bfbb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075aca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ac88.md#insn-0075aca8)
- 新版 `0075aca8`（命令位置の公開資料なし）

~~~diff
- 0075aca8 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0075aca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0075aca8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075aca8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075aca8 bytes 08612c91
+ 0075aca8 bytes 08a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a492c74acd70405133f144fa7e25a98"></a>

### [`0075acbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075acbc.md) → [`0075acbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075acbc.md) FUN_0075acbc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075acc8",
      "incomplete_value": false,
      "site": "0075acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075acc8",
      "incomplete_value": false,
      "site": "0075acc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "0075acc8",
      "DATA",
      [
        "storage",
        "00bfbb18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075acc8",
      "DATA",
      [
        "storage",
        "00bfbb68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075acc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075acbc.md#insn-0075acc4)
- 新版 `0075acc4`（命令位置の公開資料なし）

~~~diff
- 0075acc4 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 0075acc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["COPY", "tmp:0:8", ["const:b68:8"]]
+ 0075acc4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0075acc4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0075acc4 bytes 29612c91
+ 0075acc4 bytes 29a12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5c38c42defde3b12eb4bee8e0d771aa"></a>

### [`0075ada8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ada8.md) → [`0075ada8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075ada8.md) FUN_0075ada8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0075adbc",
      "incomplete_value": false,
      "site": "0075adc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075adbc",
      "incomplete_value": false,
      "site": "0075adc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "0075adc0",
      "DATA",
      [
        "storage",
        "00bfbba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075adc0",
      "DATA",
      [
        "storage",
        "00bfbbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075adbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ada8.md#insn-0075adbc)
- 新版 `0075adbc`（命令位置の公開資料なし）

~~~diff
- 0075adbc ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 0075adbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075adbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075adbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 0075adbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075adbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075adbc bytes 08a12e91
+ 0075adbc bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17132f4ca0067a367fddc686795cfe3c"></a>

### [`0075adcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075adcc.md) → [`0075adcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075adcc.md) FUN_0075adcc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075add0",
      "incomplete_value": false,
      "site": "0075add4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075add0",
      "incomplete_value": false,
      "site": "0075add4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "0075add4",
      "DATA",
      [
        "storage",
        "00bfbba8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075add4",
      "DATA",
      [
        "storage",
        "00bfbbf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075add0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075adcc.md#insn-0075add0)
- 新版 `0075add0`（命令位置の公開資料なし）

~~~diff
- 0075add0 ["COPY", "tmp:0:8", ["const:ba8:8"]]
- 0075add0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075add0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075add0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075add0 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 0075add0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075add0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075add0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075add0 bytes 08a12e91
+ 0075add0 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba16f4fcd28354191633d0746182f955"></a>

### [`0075ade4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ade4.md) → [`0075ade4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075ade4.md) FUN_0075ade4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`006f1e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006f1/006f1e2c.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

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
      "definition_site": "0075ae2c",
      "incomplete_value": true,
      "site": "0075ae2c",
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
      "definition_site": "0075ae2c",
      "incomplete_value": true,
      "site": "0075ae2c",
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
      "definition_site": "0075ae34",
      "incomplete_value": false,
      "site": "0075ae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075ae34",
      "incomplete_value": false,
      "site": "0075ae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be8000:8"
          ],
          [
            "leaf",
            "const:e48:8"
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
      "definition_site": "0075ae3c",
      "incomplete_value": false,
      "site": "0075ae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:4e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075ae3c",
      "incomplete_value": false,
      "site": "0075ae44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfa000:8"
          ],
          [
            "leaf",
            "const:490:8"
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
      "0075ae28",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0075ae34",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0075ae3c",
      "PARAM",
      [
        "storage",
        "00bfa490",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0075ae28",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0075ae34",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0075ae3c",
      "PARAM",
      [
        "storage",
        "00bfa4e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ade4.md#insn-0075ae28) · [`0075ae34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ade4.md#insn-0075ae34) · [`0075ae3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075ade4.md#insn-0075ae3c)
- 新版 `0075ae28`（命令位置の公開資料なし） · `0075ae34`（命令位置の公開資料なし） · `0075ae3c`（命令位置の公開資料なし）

~~~diff
- 0075ae28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0075ae28 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0075ae28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0075ae28 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0075ae28 bytes 003d45f9
+ 0075ae28 bytes 005d45f9
- 0075ae34 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0075ae34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0075ae34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0075ae34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0075ae34 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0075ae34 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0075ae34 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0075ae34 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0075ae34 bytes 21203991
+ 0075ae34 bytes 21603a91
- 0075ae3c ["COPY", "tmp:0:8", ["const:490:8"]]
- 0075ae3c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0075ae3c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0075ae3c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0075ae3c ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 0075ae3c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0075ae3c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0075ae3c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0075ae3c bytes 42401291
+ 0075ae3c bytes 42801391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a314617428a92d5a5774c2f9cb6d785"></a>

### [`0075afe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075afe8.md) → [`0075afe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075a/0075afe8.md) FUN_0075afe8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0075affc",
      "incomplete_value": false,
      "site": "0075b000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075affc",
      "incomplete_value": false,
      "site": "0075b000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "0075b000",
      "DATA",
      [
        "storage",
        "00bfbc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b000",
      "DATA",
      [
        "storage",
        "00bfbc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075affc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075a/0075afe8.md#insn-0075affc)
- 新版 `0075affc`（命令位置の公開資料なし）

~~~diff
- 0075affc ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0075affc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075affc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075affc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075affc ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 0075affc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075affc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075affc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075affc bytes 08a13091
+ 0075affc bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47c22fe3c5e75e6b09fd7a0d296b2f2d"></a>

### [`0075b00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b00c.md) → [`0075b00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0075b/0075b00c.md) FUN_0075b00c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0075b010",
      "incomplete_value": false,
      "site": "0075b014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0075b010",
      "incomplete_value": false,
      "site": "0075b014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bfb000:8"
          ],
          [
            "leaf",
            "const:c28:8"
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
      "0075b014",
      "DATA",
      [
        "storage",
        "00bfbc28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0075b014",
      "DATA",
      [
        "storage",
        "00bfbc78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0075b010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0075b/0075b00c.md#insn-0075b010)
- 新版 `0075b010`（命令位置の公開資料なし）

~~~diff
- 0075b010 ["COPY", "tmp:0:8", ["const:c28:8"]]
- 0075b010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0075b010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0075b010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0075b010 ["COPY", "tmp:0:8", ["const:c78:8"]]
+ 0075b010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0075b010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0075b010 bytes 08a13091
+ 0075b010 bytes 08e13191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

