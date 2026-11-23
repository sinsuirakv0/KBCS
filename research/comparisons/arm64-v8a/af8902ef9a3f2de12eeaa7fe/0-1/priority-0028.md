# v15.7.3 → v15.7.4 · 最優先の変更候補 (28)

[一覧の目次](README.md)

<a id="compare-fecfdfab3ec7919c5d72906e33948ddf"></a>

### [`00660438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660438.md) → [`00660438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660438.md) FUN_00660438

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 13件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 13件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.95% / 新版 92.95%

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
      "definition_site": "00660474",
      "incomplete_value": false,
      "site": "0066047c",
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
      "definition_site": "00660474",
      "incomplete_value": false,
      "site": "0066047c",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660604",
      "incomplete_value": true,
      "site": "00660608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00660604",
      "incomplete_value": true,
      "site": "00660608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00660600",
      "incomplete_value": true,
      "site": "0066060c",
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
      "definition_site": "00660600",
      "incomplete_value": true,
      "site": "0066060c",
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
      "0066047c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006605f4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "006605f8",
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
      "0066047c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006605f4",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "006605f8",
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

- 旧版 [`00660474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660438.md#insn-00660474) · [`006605f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660438.md#insn-006605f4) · [`006605f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660438.md#insn-006605f8)
- 新版 [`00660474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660438.md#insn-00660474) · [`006605f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660438.md#insn-006605f4) · [`006605f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660438.md#insn-006605f8)

~~~diff
- 00660474 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00660474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00660474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00660474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00660474 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00660474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00660474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00660474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00660474 bytes 08a13491
+ 00660474 bytes 08e13591
- 006605f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 006605f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006605f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 006605f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006605f4 bytes 08b946f9
+ 006605f4 bytes 08e146f9
- 006605f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 006605f8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 006605f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 006605f8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 006605f8 bytes b5be46f9
+ 006605f8 bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4e47e6ab937d90f1899c300fb1d83cc"></a>

### [`00660748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660748.md) → [`00660748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660748.md) FUN_00660748

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 13件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 13件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465680.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.51% / 新版 93.51%

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
      "definition_site": "00660784",
      "incomplete_value": false,
      "site": "0066078c",
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
      "definition_site": "00660784",
      "incomplete_value": false,
      "site": "0066078c",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660988",
      "incomplete_value": true,
      "site": "0066098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00660988",
      "incomplete_value": true,
      "site": "0066098c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00660984",
      "incomplete_value": true,
      "site": "00660990",
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
      "definition_site": "00660984",
      "incomplete_value": true,
      "site": "00660990",
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
      "0066078c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006607b0",
      "READ",
      [
        "storage",
        "002a1832",
        null,
        "string"
      ]
    ],
    [
      "006607b4",
      "READ",
      [
        "storage",
        "002a183b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0066078c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006607b0",
      "READ",
      [
        "storage",
        "002a18bd",
        null,
        "string"
      ]
    ],
    [
      "006607b4",
      "READ",
      [
        "storage",
        "002a18c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00660784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660748.md#insn-00660784) · [`006607a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660748.md#insn-006607a8) · [`00660978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660748.md#insn-00660978)
- 新版 [`00660784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660748.md#insn-00660784) · [`006607a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660748.md#insn-006607a8) · [`00660978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660748.md#insn-00660978)

~~~diff
- 00660784 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00660784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00660784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00660784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00660784 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00660784 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00660784 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00660784 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00660784 bytes 08a13491
+ 00660784 bytes 08e13591
- 006607a8 ["COPY", "tmp:0:8", ["const:832:8"]]
- 006607a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006607a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006607a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006607a8 ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 006607a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006607a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006607a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006607a8 bytes 08c92091
+ 006607a8 bytes 08f52291
- 00660978 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00660978 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00660978 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00660978 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00660978 bytes 08b946f9
+ 00660978 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-582584abaf350e5e384d7ad22cdfdcc7"></a>

### [`00660ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660ab4.md) → [`00660ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660ab4.md) FUN_00660ab4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 18件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.32% / 新版 96.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660e14",
      "incomplete_value": true,
      "site": "00660e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00660e14",
      "incomplete_value": true,
      "site": "00660e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "definition_site": "00660e10",
      "incomplete_value": true,
      "site": "00660e1c",
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
      "definition_site": "00660e10",
      "incomplete_value": true,
      "site": "00660e1c",
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
    "ordinal": 49,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00660e28",
      "incomplete_value": true,
      "site": "00660e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "00660e28",
      "incomplete_value": true,
      "site": "00660e28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
    "ordinal": 50,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00660b08",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00660e04",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "00660e08",
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
      "00660b08",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00660e04",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "00660e08",
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

- 旧版 [`00660b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660ab4.md#insn-00660b00) · [`00660e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660ab4.md#insn-00660e04) · [`00660e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660ab4.md#insn-00660e08)
- 新版 [`00660b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660ab4.md#insn-00660b00) · [`00660e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660ab4.md#insn-00660e04) · [`00660e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660ab4.md#insn-00660e08)

~~~diff
- 00660b00 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00660b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00660b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00660b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00660b00 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00660b00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00660b00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00660b00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00660b00 bytes 08a13491
+ 00660b00 bytes 08e13591
- 00660e04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00660e04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00660e04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00660e04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00660e04 bytes 08b946f9
+ 00660e04 bytes 08e146f9
- 00660e08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d78:8"]]
- 00660e08 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00660e08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:dc8:8"]]
+ 00660e08 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00660e08 bytes b5be46f9
+ 00660e08 bytes b5e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e86750ba466455e09b8ea0b81077b723"></a>

### [`00660f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660f48.md) → [`00660f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660f48.md) FUN_00660f48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.00% / 新版 94.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00660f88",
      "incomplete_value": false,
      "site": "00660f98",
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
      "definition_site": "00660f88",
      "incomplete_value": false,
      "site": "00660f98",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00660fb4",
      "incomplete_value": true,
      "site": "00660fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:75a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00660fb4",
      "incomplete_value": true,
      "site": "00660fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6cf:8"
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
      "definition_site": "006611c0",
      "incomplete_value": true,
      "site": "006611c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "006611c0",
      "incomplete_value": true,
      "site": "006611c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00660f98",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00660fb4",
      "READ",
      [
        "storage",
        "002a36cf",
        null,
        "string"
      ]
    ],
    [
      "006611b0",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00660f98",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00660fb4",
      "READ",
      [
        "storage",
        "002a375a",
        null,
        "string"
      ]
    ],
    [
      "006611b0",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00660f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660f48.md#insn-00660f88) · [`00660fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660f48.md#insn-00660fa8) · [`006611b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660f48.md#insn-006611b0)
- 新版 [`00660f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660f48.md#insn-00660f88) · [`00660fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660f48.md#insn-00660fa8) · [`006611b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660f48.md#insn-006611b0)

~~~diff
- 00660f88 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00660f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00660f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00660f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00660f88 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00660f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00660f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00660f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00660f88 bytes 08a13491
+ 00660f88 bytes 08e13591
- 00660fa8 ["COPY", "tmp:0:8", ["const:6cf:8"]]
- 00660fa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00660fa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00660fa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00660fa8 ["COPY", "tmp:0:8", ["const:75a:8"]]
+ 00660fa8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00660fa8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00660fa8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00660fa8 bytes 293d1b91
+ 00660fa8 bytes 29691d91
- 006611b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 006611b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006611b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 006611b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006611b0 bytes 08b946f9
+ 006611b0 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7915f5d24ea6d1a4296f3cbf69d01d5"></a>

### [`00663f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663f40.md) → [`00663f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663f40.md) FUN_00663f40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00663e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663e24.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`00663e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663e24.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 6件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00663f80",
      "incomplete_value": false,
      "site": "00663f88",
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
      "definition_site": "00663f80",
      "incomplete_value": false,
      "site": "00663f88",
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
      "definition_site": "00663fb0",
      "incomplete_value": true,
      "site": "00663fc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:959:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00663fb0",
      "incomplete_value": true,
      "site": "00663fc4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8ce:8"
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
      "definition_site": "00663fb4",
      "incomplete_value": true,
      "site": "00663fc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00663fb4",
      "incomplete_value": true,
      "site": "00663fc8",
      "value": [
        "LOAD",
        "16",
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
      "00663f88",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00663fb0",
      "READ",
      [
        "storage",
        "002a58ce",
        null,
        "string"
      ]
    ],
    [
      "00663fb4",
      "READ",
      [
        "storage",
        "002a58d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00663f88",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00663fb0",
      "READ",
      [
        "storage",
        "002a5959",
        null,
        "string"
      ]
    ],
    [
      "00663fb4",
      "READ",
      [
        "storage",
        "002a5964",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00663f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663f40.md#insn-00663f80) · [`00663fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663f40.md#insn-00663fa8) · [`00663fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663f40.md#insn-00663fac)
- 新版 [`00663f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663f40.md#insn-00663f80) · [`00663fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663f40.md#insn-00663fa8)

~~~diff
- 00663f80 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00663f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00663f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00663f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00663f80 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00663f80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00663f80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00663f80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00663f80 bytes 08a13491
+ 00663f80 bytes 08e13591
- 00663fa8 ["COPY", "tmp:0:8", ["const:8ce:8"]]
- 00663fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00663fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00663fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00663fa8 ["COPY", "tmp:0:8", ["const:959:8"]]
+ 00663fa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00663fa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00663fa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00663fa8 bytes 08392391
+ 00663fa8 bytes 08652591
- 00663fac ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00663fac bytes 69e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1089e584aea536275dd4e53dcd81a40"></a>

### [`0066434c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/0066434c.md) → [`0066434c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/0066434c.md) FUN_0066434c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00665850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665850.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`0066c164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c164.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00665850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665850.md) · 呼出先 11件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`0066c164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c164.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.38% / 新版 95.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066443c",
      "incomplete_value": true,
      "site": "0066444c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
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
      "definition_site": "0066443c",
      "incomplete_value": true,
      "site": "0066444c",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:292000:8"
              ],
              [
                "leaf",
                "const:bd3:8"
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
      "definition_site": "00664440",
      "incomplete_value": true,
      "site": "00664450",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00664440",
      "incomplete_value": true,
      "site": "00664450",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066447c",
      "incomplete_value": false,
      "site": "00664488",
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
            "const:b0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066447c",
      "incomplete_value": false,
      "site": "00664488",
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
            "const:a72:8"
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
      "0066443c",
      "READ",
      [
        "storage",
        "00292bd3",
        null,
        "string"
      ]
    ],
    [
      "00664440",
      "READ",
      [
        "storage",
        "00292bdd",
        null,
        "string"
      ]
    ],
    [
      "0066447c",
      "PARAM",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0066443c",
      "READ",
      [
        "storage",
        "00292b46",
        null,
        "string"
      ]
    ],
    [
      "00664440",
      "READ",
      [
        "storage",
        "00292b50",
        null,
        "string"
      ]
    ],
    [
      "0066447c",
      "PARAM",
      [
        "storage",
        "002a6b0c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00664434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/0066434c.md#insn-00664434) · [`00664438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/0066434c.md#insn-00664438)
- 新版 [`00664434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/0066434c.md#insn-00664434) · [`00664438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/0066434c.md#insn-00664438)

~~~diff
- 00664434 ["COPY", "tmp:0:8", ["const:bd3:8"]]
- 00664434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00664434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00664434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00664434 ["COPY", "tmp:0:8", ["const:b46:8"]]
+ 00664434 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00664434 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00664434 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00664434 bytes 084d2f91
+ 00664434 bytes 08192d91
- 00664438 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00664438 bytes 69e2ffb0
+ 00664438 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00664438 bytes 69e2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09cc698c6022a07b404732e35d1c84d8"></a>

### [`00664ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664ab8.md) → [`00664ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md) FUN_00664ab8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a1e2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1e/00a1e2a0.md) [`00a205e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a20/00a205e0.md) · 呼出先 26件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0066cff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066cff8.md)
- 新版 呼出元 2件 [`00a1e2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a1e/00a1e2e4.md) [`00a20624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a20/00a20624.md) · 呼出先 26件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0066cff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cff8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.79% / 新版 97.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00664b98",
      "incomplete_value": false,
      "site": "00664b98",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00664b98",
      "incomplete_value": false,
      "site": "00664b98",
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
            "const:2d8:8"
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
      "definition_site": "00664dd4",
      "incomplete_value": false,
      "site": "00664dd4",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00664dd4",
      "incomplete_value": false,
      "site": "00664dd4",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00665004",
      "incomplete_value": false,
      "site": "00665004",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00665004",
      "incomplete_value": false,
      "site": "00665004",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00664b98",
      "DATA",
      [
        "storage",
        "00bf72d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00664bf4",
      "READ",
      [
        "storage",
        "00bf72f8",
        null,
        "pointer"
      ]
    ],
    [
      "00664bf4",
      "READ",
      [
        "storage",
        "00bf7300",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00664b98",
      "DATA",
      [
        "storage",
        "00bf7328",
        null,
        "undefined *"
      ]
    ],
    [
      "00664bf4",
      "READ",
      [
        "storage",
        "00bf7348",
        null,
        "pointer"
      ]
    ],
    [
      "00664bf4",
      "READ",
      [
        "storage",
        "00bf7350",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00664b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664ab8.md#insn-00664b94) · [`00664c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664ab8.md#insn-00664c04) · [`00664c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664ab8.md#insn-00664c30)
- 新版 [`00664b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md#insn-00664b94) · [`00664c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md#insn-00664c04) · [`00664c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664ab8.md#insn-00664c30)

~~~diff
- 00664b94 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 00664b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00664b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00664b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00664b94 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00664b94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00664b94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00664b94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00664b94 bytes 08610b91
+ 00664b94 bytes 08a10c91
- 00664c04 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:520:8"]]
- 00664c04 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00664c04 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:570:8"]]
+ 00664c04 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00664c04 bytes 5a9342f9
+ 00664c04 bytes 5abb42f9
- 00664c30 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:528:8"]]
- 00664c30 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00664c30 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:578:8"]]
+ 00664c30 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00664c30 bytes 189742f9
+ 00664c30 bytes 18bf42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d151095bf89a7408df87aced66a8591"></a>

### [`00665850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665850.md) → [`00665850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665850.md) FUN_00665850

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`006675d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00667/006675d0.md) [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0066434c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/0066434c.md) [`00664710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00664/00664710.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 2件 [`006675d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00667/006675d0.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 10件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0066434c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/0066434c.md) [`00664710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00664/00664710.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.41% / 新版 95.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00665920",
      "incomplete_value": true,
      "site": "00665930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00665920",
      "incomplete_value": true,
      "site": "00665930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bc5:8"
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
      "00665920",
      "READ",
      [
        "storage",
        "00293bc5",
        null,
        "string"
      ]
    ],
    [
      "00665934",
      "READ",
      [
        "storage",
        "00293bd0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00665920",
      "READ",
      [
        "storage",
        "00293b38",
        null,
        "string"
      ]
    ],
    [
      "00665934",
      "READ",
      [
        "storage",
        "00293b43",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066591c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665850.md#insn-0066591c)
- 新版 [`0066591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665850.md#insn-0066591c)

~~~diff
- 0066591c ["COPY", "tmp:0:8", ["const:bc5:8"]]
- 0066591c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066591c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066591c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066591c ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 0066591c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066591c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066591c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066591c bytes 29152f91
+ 0066591c bytes 29e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e56d35baa836197c9628e2cda4c734b"></a>

### [`00666298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md) → [`00666298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md) FUN_00666298

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006afcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006af/006afcec.md) [`0096d6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0096d/0096d6b8.md) [`00a8db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md) · 呼出先 38件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 3件 [`006afcec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006af/006afcec.md) [`0096d6b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0096d/0096d6b8.md) [`00a8db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8d/00a8db90.md) · 呼出先 38件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.08% / 新版 97.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066637c",
      "incomplete_value": false,
      "site": "0066637c",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066637c",
      "incomplete_value": false,
      "site": "0066637c",
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
            "const:558:8"
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
      "definition_site": "006665bc",
      "incomplete_value": false,
      "site": "006665bc",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006665bc",
      "incomplete_value": false,
      "site": "006665bc",
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
            "const:5d8:8"
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
      "definition_site": "006667f0",
      "incomplete_value": false,
      "site": "006667f0",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006667f0",
      "incomplete_value": false,
      "site": "006667f0",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066637c",
      "DATA",
      [
        "storage",
        "00bf7558",
        null,
        "undefined *"
      ]
    ],
    [
      "006663d8",
      "READ",
      [
        "storage",
        "00bf7578",
        null,
        "pointer"
      ]
    ],
    [
      "006663d8",
      "READ",
      [
        "storage",
        "00bf7580",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066637c",
      "DATA",
      [
        "storage",
        "00bf75a8",
        null,
        "undefined *"
      ]
    ],
    [
      "006663d8",
      "READ",
      [
        "storage",
        "00bf75c8",
        null,
        "pointer"
      ]
    ],
    [
      "006663d8",
      "READ",
      [
        "storage",
        "00bf75d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00666378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md#insn-00666378) · [`006663e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md#insn-006663e8) · [`00666414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md#insn-00666414)
- 新版 [`00666378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md#insn-00666378) · [`006663e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md#insn-006663e8) · [`00666414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00666/00666298.md#insn-00666414)

~~~diff
- 00666378 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00666378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00666378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00666378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00666378 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 00666378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00666378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00666378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00666378 bytes 08611591
+ 00666378 bytes 08a11691
- 006663e8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:520:8"]]
- 006663e8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 006663e8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:570:8"]]
+ 006663e8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 006663e8 bytes 5a9342f9
+ 006663e8 bytes 5abb42f9
- 00666414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:528:8"]]
- 00666414 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00666414 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:578:8"]]
+ 00666414 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00666414 bytes 189742f9
+ 00666414 bytes 18bf42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0872724427165e97a416e33355a3f8cd"></a>

### [`006683dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/006683dc.md) → [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) FUN_006683dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 25件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006615d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006615d4.md) [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md)
- 新版 呼出元 1件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 25件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006615d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006615d4.md) [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.45% / 新版 96.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00668450",
      "incomplete_value": false,
      "site": "00668450",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668450",
      "incomplete_value": false,
      "site": "00668450",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00668720",
      "incomplete_value": false,
      "site": "00668724",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668720",
      "incomplete_value": false,
      "site": "00668724",
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
            "const:9d8:8"
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
      "definition_site": "006687e4",
      "incomplete_value": true,
      "site": "006687ec",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006687e4",
      "incomplete_value": true,
      "site": "006687ec",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00668450",
      "DATA",
      [
        "storage",
        "00bf7958",
        null,
        "undefined *"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "00bf7978",
        null,
        "pointer"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "00bf7980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00668450",
      "DATA",
      [
        "storage",
        "00bf79a8",
        null,
        "undefined *"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "00bf79c8",
        null,
        "pointer"
      ]
    ],
    [
      "006684c0",
      "READ",
      [
        "storage",
        "00bf79d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00668444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/006683dc.md#insn-00668444) · [`00668504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/006683dc.md#insn-00668504) · [`00668580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/006683dc.md#insn-00668580)
- 新版 [`00668444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md#insn-00668444) · [`00668504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md#insn-00668504) · [`00668580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md#insn-00668580)

~~~diff
- 00668444 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00668444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00668444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00668444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00668444 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 00668444 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00668444 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00668444 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00668444 bytes 08612591
+ 00668444 bytes 08a12691
- 00668504 ["COPY", "tmp:0:8", ["const:861:8"]]
- 00668504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00668504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00668504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00668504 ["COPY", "tmp:0:8", ["const:8ec:8"]]
+ 00668504 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00668504 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00668504 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00668504 bytes 29852191
+ 00668504 bytes 29b12391
- 00668580 ["COPY", "tmp:0:8", ["const:791:8"]]
- 00668580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00668580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00668580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00668580 ["COPY", "tmp:0:8", ["const:82b:8"]]
+ 00668580 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00668580 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00668580 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00668580 bytes 08451e91
+ 00668580 bytes 08ad2091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fd1ef310da96257653f4da7486e65df"></a>

### [`00668a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/00668a08.md) → [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md) FUN_00668a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0066e78c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e78c.md) [`00670a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md) [`00672a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672a4c.md) [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 31件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 4件 [`0066e78c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e78c.md) [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) [`00672a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a4c.md) [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 31件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.67% / 新版 95.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00668abc",
      "incomplete_value": true,
      "site": "00668acc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7b1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668abc",
      "incomplete_value": true,
      "site": "00668acc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:726:8"
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
      "definition_site": "00668ac0",
      "incomplete_value": true,
      "site": "00668ad0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00668ac0",
      "incomplete_value": true,
      "site": "00668ad0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00668bac",
      "incomplete_value": false,
      "site": "00668bac",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00668bac",
      "incomplete_value": false,
      "site": "00668bac",
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
            "const:b08:8"
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
      "00668abc",
      "READ",
      [
        "storage",
        "0029e726",
        null,
        "string"
      ]
    ],
    [
      "00668ac0",
      "READ",
      [
        "storage",
        "0029e732",
        null,
        "string"
      ]
    ],
    [
      "00668bac",
      "DATA",
      [
        "storage",
        "00bf7b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00668abc",
      "READ",
      [
        "storage",
        "0029e7b1",
        null,
        "string"
      ]
    ],
    [
      "00668ac0",
      "READ",
      [
        "storage",
        "0029e7bd",
        null,
        "string"
      ]
    ],
    [
      "00668bac",
      "DATA",
      [
        "storage",
        "00bf7b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00668ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/00668a08.md#insn-00668ab4) · [`00668ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/00668a08.md#insn-00668ab8)
- 新版 [`00668ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md#insn-00668ab4) · [`00668ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md#insn-00668ab8)

~~~diff
- 00668ab4 ["COPY", "tmp:0:8", ["const:726:8"]]
- 00668ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00668ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00668ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00668ab4 ["COPY", "tmp:0:8", ["const:7b1:8"]]
+ 00668ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00668ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00668ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00668ab4 bytes 08991c91
+ 00668ab4 bytes 08c51e91
- 00668ab8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00668ab8 bytes 49e2ffb0
+ 00668ab8 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00668ab8 bytes 49e2ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ae6378f42a776bf67dc052997b5df58e"></a>

### [`00669250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00669/00669250.md) → [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) FUN_00669250

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006700bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006700bc.md) [`00672400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672400.md) · 呼出先 43件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`006700bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md) [`00672400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672400.md) · 呼出先 43件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.80% / 新版 93.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006692d8",
      "incomplete_value": false,
      "site": "006692d8",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006692d8",
      "incomplete_value": false,
      "site": "006692d8",
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
            "const:d08:8"
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
      "definition_site": "006693a4",
      "incomplete_value": true,
      "site": "006693b4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:b61:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006693a4",
      "incomplete_value": true,
      "site": "006693b4",
      "value": [
        "LOAD",
        "16",
        [
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
                "const:bee:8"
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
      "definition_site": "006693b8",
      "incomplete_value": true,
      "site": "006693b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "006693b8",
      "incomplete_value": true,
      "site": "006693b8",
      "value": [
        "LOAD",
        "8",
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
      "006692d8",
      "DATA",
      [
        "storage",
        "00bf7d08",
        null,
        "undefined *"
      ]
    ],
    [
      "00669340",
      "READ",
      [
        "storage",
        "00bf7d28",
        null,
        "pointer"
      ]
    ],
    [
      "00669340",
      "READ",
      [
        "storage",
        "00bf7d30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006692d8",
      "DATA",
      [
        "storage",
        "00bf7d58",
        null,
        "undefined *"
      ]
    ],
    [
      "00669340",
      "READ",
      [
        "storage",
        "00bf7d78",
        null,
        "pointer"
      ]
    ],
    [
      "00669340",
      "READ",
      [
        "storage",
        "00bf7d80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006692cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00669/00669250.md#insn-006692cc) · [`006692d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00669/00669250.md#insn-006692d0)
- 新版 [`006692cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md#insn-006692cc) · [`006692d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md#insn-006692d0)

~~~diff
- 006692cc ["COPY", "tmp:0:8", ["const:d08:8"]]
- 006692cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006692cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006692cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006692cc ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 006692cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006692cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006692cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006692cc bytes 08213491
+ 006692cc bytes 08613591
- 006692d0 ["INT_SUB", "register:40a8:8", ["register:40e8:8", "const:50:8"]]
- 006692d0 bytes b54301d1
+ 006692d0 ["INT_SUB", "register:40a8:8", ["register:40e8:8", "const:50:8"]]
+ 006692d0 bytes b54301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de73783983c35cce6fa7ffb775589d79"></a>

### [`0066a360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066a360.md) → [`0066a360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md) FUN_0066a360

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00670a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md) · 呼出先 35件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) · 呼出先 35件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066a734",
      "incomplete_value": false,
      "site": "0066a734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a734",
      "incomplete_value": false,
      "site": "0066a734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "definition_site": "0066a8f4",
      "incomplete_value": false,
      "site": "0066a8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a8f4",
      "incomplete_value": false,
      "site": "0066a8f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066a628",
      "incomplete_value": true,
      "site": "0066a644",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066a628",
      "incomplete_value": true,
      "site": "0066a644",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 24,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066a498",
      "DATA",
      [
        "storage",
        "00bf7f88",
        null,
        "undefined *"
      ]
    ],
    [
      "0066a510",
      "READ",
      [
        "storage",
        "00bf7fa8",
        null,
        "pointer"
      ]
    ],
    [
      "0066a510",
      "READ",
      [
        "storage",
        "00bf7fb0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066a498",
      "DATA",
      [
        "storage",
        "00bf7fd8",
        null,
        "undefined *"
      ]
    ],
    [
      "0066a510",
      "READ",
      [
        "storage",
        "00bf7ff8",
        null,
        "pointer"
      ]
    ],
    [
      "0066a510",
      "READ",
      [
        "storage",
        "00bf8000",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066a490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066a360.md#insn-0066a490) · [`0066a5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066a360.md#insn-0066a5ac) · [`0066a5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066a360.md#insn-0066a5b0)
- 新版 [`0066a490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md#insn-0066a490) · [`0066a5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md#insn-0066a5ac) · [`0066a5b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md#insn-0066a5b0)

~~~diff
- 0066a490 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0066a490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066a490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066a490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066a490 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0066a490 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066a490 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066a490 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066a490 bytes 08213e91
+ 0066a490 bytes 08613f91
- 0066a5ac ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0066a5ac ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0066a5ac ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0066a5ac ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0066a5ac ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0066a5ac ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0066a5ac ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0066a5ac ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0066a5ac bytes d6223991
+ 0066a5ac bytes d6623a91
- 0066a5b0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
- 0066a5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0066a5b0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:ab8:8"]]
+ 0066a5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0066a5b0 bytes 883f45f9
+ 0066a5b0 bytes 885f45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4079dca5d22f841e88ef1882c619ddc"></a>

### [`0066ab18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066ab18.md) → [`0066ab18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066ab18.md) FUN_0066ab18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006700bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006700bc.md) · 呼出先 37件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md)
- 新版 呼出元 1件 [`006700bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700bc.md) · 呼出先 37件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0044ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.07% / 新版 96.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066b0b4",
      "incomplete_value": false,
      "site": "0066b0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066b0b4",
      "incomplete_value": false,
      "site": "0066b0b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "definition_site": "0066b1ac",
      "incomplete_value": false,
      "site": "0066b1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066b1ac",
      "incomplete_value": false,
      "site": "0066b1ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066b204",
      "incomplete_value": false,
      "site": "0066b204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066b204",
      "incomplete_value": false,
      "site": "0066b204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:308:8"
          ]
        ]
      ]
    },
    "ordinal": 65,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0066ab6c",
      "READ",
      [
        "storage",
        "002a0873",
        null,
        "string"
      ]
    ],
    [
      "0066ab70",
      "READ",
      [
        "storage",
        "002a0883",
        null,
        "string"
      ]
    ],
    [
      "0066ac68",
      "DATA",
      [
        "storage",
        "00bf8188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ab6c",
      "READ",
      [
        "storage",
        "002a08fe",
        null,
        "string"
      ]
    ],
    [
      "0066ab70",
      "READ",
      [
        "storage",
        "002a090e",
        null,
        "string"
      ]
    ],
    [
      "0066ac68",
      "DATA",
      [
        "storage",
        "00bf81d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066ab18.md#insn-0066ab64) · [`0066ab68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066ab18.md#insn-0066ab68)
- 新版 [`0066ab64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066ab18.md#insn-0066ab64) · [`0066ab68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066ab18.md#insn-0066ab68)

~~~diff
- 0066ab64 ["COPY", "tmp:0:8", ["const:873:8"]]
- 0066ab64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ab64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ab64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066ab64 ["COPY", "tmp:0:8", ["const:8fe:8"]]
+ 0066ab64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ab64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ab64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ab64 bytes 08cd2191
+ 0066ab64 bytes 08f92391
- 0066ab68 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0066ab68 bytes 29e2ffd0
+ 0066ab68 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0066ab68 bytes 29e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a5435f2a491fc720b51594fc5d6c342"></a>

### [`0066b890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066b890.md) → [`0066b890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b890.md) FUN_0066b890

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0066b744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066b744.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0066b744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b744.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066b89c",
      "incomplete_value": false,
      "site": "0066b8a0",
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
      "definition_site": "0066b89c",
      "incomplete_value": false,
      "site": "0066b8a0",
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
      "0066b89c",
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
      "0066b89c",
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

- 旧版 [`0066b89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066b890.md#insn-0066b89c)
- 新版 [`0066b89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b890.md#insn-0066b89c)

~~~diff
- 0066b89c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066b89c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066b89c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066b89c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066b89c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066b89c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066b89c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066b89c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066b89c bytes 000c0c91
+ 0066b89c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71facef6dfc6d322dc26332e174564e5"></a>

### [`0066ba90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066ba90.md) → [`0066ba90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066ba90.md) FUN_0066ba90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0065f7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0065f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066ba9c",
      "incomplete_value": false,
      "site": "0066baa0",
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
      "definition_site": "0066ba9c",
      "incomplete_value": false,
      "site": "0066baa0",
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
      "0066ba9c",
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
      "0066ba9c",
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

- 旧版 [`0066ba9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066ba90.md#insn-0066ba9c)
- 新版 [`0066ba9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066ba90.md#insn-0066ba9c)

~~~diff
- 0066ba9c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066ba9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066ba9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066ba9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066ba9c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066ba9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066ba9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066ba9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066ba9c bytes 000c0c91
+ 0066ba9c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267ce1cf08a5afdc60752216afc02c5a"></a>

### [`0066baa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066baa4.md) → [`0066baa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066baa4.md) FUN_0066baa4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 17件 [`0065ebdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ebdc.md) [`0065f7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md) [`006612f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612f8.md) [`00661320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/00661320.md) [`0066181c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/0066181c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 17件 [`0065ebdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ebdc.md) [`0065f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md) [`006612f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612f8.md) [`00661320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/00661320.md) [`0066181c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/0066181c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0066bab0",
      "incomplete_value": false,
      "site": "0066bab4",
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
      "definition_site": "0066bab0",
      "incomplete_value": false,
      "site": "0066bab4",
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
      "0066bab0",
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
      "0066bab0",
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

- 旧版 [`0066bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066baa4.md#insn-0066bab0)
- 新版 [`0066bab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066baa4.md#insn-0066bab0)

~~~diff
- 0066bab0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066bab0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066bab0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066bab0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066bab0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066bab0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bab0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bab0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066bab0 bytes 000c0c91
+ 0066bab0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1719083aac4add359cbe5842fe2be6d"></a>

### [`0066bab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bab8.md) → [`0066bab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bab8.md) FUN_0066bab8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0065fcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0065fcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066bac4",
      "incomplete_value": false,
      "site": "0066bac8",
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
      "definition_site": "0066bac4",
      "incomplete_value": false,
      "site": "0066bac8",
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
      "0066bac4",
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
      "0066bac4",
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

- 旧版 [`0066bac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bab8.md#insn-0066bac4)
- 新版 [`0066bac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bab8.md#insn-0066bac4)

~~~diff
- 0066bac4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066bac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066bac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066bac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066bac4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066bac4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bac4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bac4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066bac4 bytes 000c0c91
+ 0066bac4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ef7cc83802165b3a111214cbb915fbd"></a>

### [`0066bacc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bacc.md) → [`0066bacc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bacc.md) FUN_0066bacc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0065eb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065eb0c.md) [`0065eb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065eb54.md) [`0065eba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065eba8.md) [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065fcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 7件 [`0065eb0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065eb0c.md) [`0065eb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065eb54.md) [`0065eba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065eba8.md) [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065fcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0066bad8",
      "incomplete_value": false,
      "site": "0066badc",
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
      "definition_site": "0066bad8",
      "incomplete_value": false,
      "site": "0066badc",
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
      "0066bad8",
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
      "0066bad8",
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

- 旧版 [`0066bad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bacc.md#insn-0066bad8)
- 新版 [`0066bad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bacc.md#insn-0066bad8)

~~~diff
- 0066bad8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066bad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066bad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066bad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066bad8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066bad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066bad8 bytes 000c0c91
+ 0066bad8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c888a754fcf8301175c5f2735447936"></a>

### [`0066bc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bc80.md) → [`0066bc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc80.md) FUN_0066bc80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0066bae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bae0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0066bae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bae0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066bc8c",
      "incomplete_value": false,
      "site": "0066bc90",
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
      "definition_site": "0066bc8c",
      "incomplete_value": false,
      "site": "0066bc90",
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
      "0066bc8c",
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
      "0066bc8c",
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

- 旧版 [`0066bc8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bc80.md#insn-0066bc8c)
- 新版 [`0066bc8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc80.md#insn-0066bc8c)

~~~diff
- 0066bc8c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066bc8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066bc8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066bc8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066bc8c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066bc8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bc8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066bc8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066bc8c bytes 000c0c91
+ 0066bc8c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb0653b593fff76f40b3e7cc0c97bca"></a>

### [`0066c094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c094.md) → [`0066c094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md) FUN_0066c094

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0066bc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066bc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0066bc94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066bc94.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066c0a0",
      "incomplete_value": false,
      "site": "0066c0a4",
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
      "definition_site": "0066c0a0",
      "incomplete_value": false,
      "site": "0066c0a4",
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
      "0066c0a0",
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
      "0066c0a0",
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

- 旧版 [`0066c0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c094.md#insn-0066c0a0)
- 新版 [`0066c0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c094.md#insn-0066c0a0)

~~~diff
- 0066c0a0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066c0a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066c0a0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066c0a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c0a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c0a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c0a0 bytes 000c0c91
+ 0066c0a0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d3c32f19576f9ba561349cbe7999bc9"></a>

### [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) → [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) FUN_0066c13c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 11件 [`006615d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006615d4.md) [`006683dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/006683dc.md) [`00669250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00669/00669250.md) [`0066e9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e9a0.md) [`0066ea58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ea58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 11件 [`006615d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006615d4.md) [`006683dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/006683dc.md) [`00669250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00669/00669250.md) [`0066e9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md) [`0066ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066c148",
      "incomplete_value": false,
      "site": "0066c14c",
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
      "definition_site": "0066c148",
      "incomplete_value": false,
      "site": "0066c14c",
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
      "0066c148",
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
      "0066c148",
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

- 旧版 [`0066c148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md#insn-0066c148)
- 新版 [`0066c148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md#insn-0066c148)

~~~diff
- 0066c148 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066c148 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c148 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066c148 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066c148 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c148 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c148 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c148 bytes 000c0c91
+ 0066c148 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc546db2b2cdcb43d6c05ab72178f7a4"></a>

### [`0066c150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c150.md) → [`0066c150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md) FUN_0066c150

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065ef18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ef18.md) [`0065f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f044.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 3件 [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065ef18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ef18.md) [`0065f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f044.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "0066c15c",
      "incomplete_value": false,
      "site": "0066c160",
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
      "definition_site": "0066c15c",
      "incomplete_value": false,
      "site": "0066c160",
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
      "0066c15c",
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
      "0066c15c",
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

- 旧版 [`0066c15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c150.md#insn-0066c15c)
- 新版 [`0066c15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md#insn-0066c15c)

~~~diff
- 0066c15c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066c15c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c15c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c15c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066c15c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066c15c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c15c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c15c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c15c bytes 000c0c91
+ 0066c15c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b052e584597e9dda63602eef1361495"></a>

### [`0066c178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c178.md) → [`0066c178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md) FUN_0066c178

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00663f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00663/00663f40.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00663f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00663/00663f40.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0066c184",
      "incomplete_value": false,
      "site": "0066c188",
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
      "definition_site": "0066c184",
      "incomplete_value": false,
      "site": "0066c188",
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
      "0066c184",
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
      "0066c184",
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

- 旧版 [`0066c184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c178.md#insn-0066c184)
- 新版 [`0066c184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c178.md#insn-0066c184)

~~~diff
- 0066c184 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0066c184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0066c184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0066c184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0066c184 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0066c184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0066c184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0066c184 bytes 000c0c91
+ 0066c184 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-492f8218048b06ea2cf3ac83bbed8fd6"></a>

### [`0066cfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066cfb0.md) → [`0066cfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md) FUN_0066cfb0

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
      "definition_site": "0066cfd4",
      "incomplete_value": false,
      "site": "0066cfd4",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066cfd4",
      "incomplete_value": false,
      "site": "0066cfd4",
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
            "const:2d8:8"
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
      "0066cfd4",
      "DATA",
      [
        "storage",
        "00bf72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066cfd4",
      "DATA",
      [
        "storage",
        "00bf7328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066cfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066cfb0.md#insn-0066cfd0)
- 新版 [`0066cfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfb0.md#insn-0066cfd0)

~~~diff
- 0066cfd0 ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0066cfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066cfd0 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0066cfd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066cfd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066cfd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066cfd0 bytes 08610b91
+ 0066cfd0 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a8f43242c52c8d659b0bcb852e795e3"></a>

### [`0066cfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066cfe4.md) → [`0066cfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfe4.md) FUN_0066cfe4

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
      "definition_site": "0066cff0",
      "incomplete_value": false,
      "site": "0066cff0",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066cff0",
      "incomplete_value": false,
      "site": "0066cff0",
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
            "const:2d8:8"
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
      "0066cff0",
      "DATA",
      [
        "storage",
        "00bf72d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066cff0",
      "DATA",
      [
        "storage",
        "00bf7328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066cfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066cfe4.md#insn-0066cfec)
- 新版 [`0066cfec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066cfe4.md#insn-0066cfec)

~~~diff
- 0066cfec ["COPY", "tmp:0:8", ["const:2d8:8"]]
- 0066cfec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066cfec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066cfec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066cfec ["COPY", "tmp:0:8", ["const:328:8"]]
+ 0066cfec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066cfec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066cfec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066cfec bytes 29610b91
+ 0066cfec bytes 29a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-476bf172849c68fb9f01b149fc4443bd"></a>

### [`0066d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d080.md) → [`0066d080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d080.md) FUN_0066d080

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
      "definition_site": "0066d0a4",
      "incomplete_value": false,
      "site": "0066d0a4",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d0a4",
      "incomplete_value": false,
      "site": "0066d0a4",
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
            "const:358:8"
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
      "0066d0a4",
      "DATA",
      [
        "storage",
        "00bf7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d0a4",
      "DATA",
      [
        "storage",
        "00bf73a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d080.md#insn-0066d0a0)
- 新版 [`0066d0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d080.md#insn-0066d0a0)

~~~diff
- 0066d0a0 ["COPY", "tmp:0:8", ["const:358:8"]]
- 0066d0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d0a0 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0066d0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d0a0 bytes 08610d91
+ 0066d0a0 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a61c021bd08f7f9b2cbbe4ae4d7b9a3"></a>

### [`0066d0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d0b4.md) → [`0066d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0b4.md) FUN_0066d0b4

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
      "definition_site": "0066d0c0",
      "incomplete_value": false,
      "site": "0066d0c0",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d0c0",
      "incomplete_value": false,
      "site": "0066d0c0",
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
            "const:358:8"
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
      "0066d0c0",
      "DATA",
      [
        "storage",
        "00bf7358",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d0c0",
      "DATA",
      [
        "storage",
        "00bf73a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d0b4.md#insn-0066d0bc)
- 新版 [`0066d0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0b4.md#insn-0066d0bc)

~~~diff
- 0066d0bc ["COPY", "tmp:0:8", ["const:358:8"]]
- 0066d0bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066d0bc ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0066d0bc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d0bc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d0bc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d0bc bytes 29610d91
+ 0066d0bc bytes 29a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b1cb9930f16cc94d4d61a8fb49105834"></a>

### [`0066d0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d0d0.md) → [`0066d0d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md) FUN_0066d0d0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00665758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665758.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00665758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665758.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.84% / 新版 93.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0066d230",
      "incomplete_value": true,
      "site": "0066d240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:75f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d230",
      "incomplete_value": true,
      "site": "0066d240",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6d4:8"
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
      "definition_site": "0066d244",
      "incomplete_value": true,
      "site": "0066d244",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0066d244",
      "incomplete_value": true,
      "site": "0066d244",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066d268",
      "incomplete_value": false,
      "site": "0066d268",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d268",
      "incomplete_value": false,
      "site": "0066d268",
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
            "const:3c8:8"
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
      "0066d230",
      "READ",
      [
        "storage",
        "002a26d4",
        null,
        "string"
      ]
    ],
    [
      "0066d234",
      "READ",
      [
        "storage",
        "002a26e3",
        null,
        "string"
      ]
    ],
    [
      "0066d268",
      "DATA",
      [
        "storage",
        "00bf73c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d230",
      "READ",
      [
        "storage",
        "002a275f",
        null,
        "string"
      ]
    ],
    [
      "0066d234",
      "READ",
      [
        "storage",
        "002a276e",
        null,
        "string"
      ]
    ],
    [
      "0066d268",
      "DATA",
      [
        "storage",
        "00bf7418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d0d0.md#insn-0066d228) · [`0066d22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d0d0.md#insn-0066d22c)
- 新版 [`0066d228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md#insn-0066d228) · [`0066d22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d0d0.md#insn-0066d22c)

~~~diff
- 0066d228 ["COPY", "tmp:0:8", ["const:6d4:8"]]
- 0066d228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d228 ["COPY", "tmp:0:8", ["const:75f:8"]]
+ 0066d228 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d228 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d228 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d228 bytes 08511b91
+ 0066d228 bytes 087d1d91
- 0066d22c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 0066d22c bytes 09e2fff0
+ 0066d22c ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 0066d22c bytes 09e2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff2ef46edfe9d9a69142aaf1bb739d56"></a>

### [`0066d3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d3d4.md) → [`0066d3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md) FUN_0066d3d4

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
      "definition_site": "0066d3f8",
      "incomplete_value": false,
      "site": "0066d3f8",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d3f8",
      "incomplete_value": false,
      "site": "0066d3f8",
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
            "const:3c8:8"
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
      "0066d3f8",
      "DATA",
      [
        "storage",
        "00bf73c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d3f8",
      "DATA",
      [
        "storage",
        "00bf7418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d3d4.md#insn-0066d3f4)
- 新版 [`0066d3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d3d4.md#insn-0066d3f4)

~~~diff
- 0066d3f4 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0066d3f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d3f4 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0066d3f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d3f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d3f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d3f4 bytes 08210f91
+ 0066d3f4 bytes 08611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79980e114e4d0aa5cfde5d172fbb0a94"></a>

### [`0066d408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d408.md) → [`0066d408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d408.md) FUN_0066d408

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
      "definition_site": "0066d414",
      "incomplete_value": false,
      "site": "0066d414",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d414",
      "incomplete_value": false,
      "site": "0066d414",
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
            "const:3c8:8"
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
      "0066d414",
      "DATA",
      [
        "storage",
        "00bf73c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d414",
      "DATA",
      [
        "storage",
        "00bf7418",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d408.md#insn-0066d410)
- 新版 [`0066d410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d408.md#insn-0066d410)

~~~diff
- 0066d410 ["COPY", "tmp:0:8", ["const:3c8:8"]]
- 0066d410 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d410 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d410 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066d410 ["COPY", "tmp:0:8", ["const:418:8"]]
+ 0066d410 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d410 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d410 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d410 bytes 29210f91
+ 0066d410 bytes 29611091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7da4d7270b76c5c57ee386929ba21364"></a>

### [`0066d490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d490.md) → [`0066d490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md) FUN_0066d490

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
      "definition_site": "0066d4b4",
      "incomplete_value": false,
      "site": "0066d4b4",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d4b4",
      "incomplete_value": false,
      "site": "0066d4b4",
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
            "const:458:8"
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
      "0066d4b4",
      "DATA",
      [
        "storage",
        "00bf7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d4b4",
      "DATA",
      [
        "storage",
        "00bf74a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d490.md#insn-0066d4b0)
- 新版 [`0066d4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d490.md#insn-0066d4b0)

~~~diff
- 0066d4b0 ["COPY", "tmp:0:8", ["const:458:8"]]
- 0066d4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d4b0 ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0066d4b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d4b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d4b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d4b0 bytes 08611191
+ 0066d4b0 bytes 08a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cb091999116780d64f568c857e7cfb0"></a>

### [`0066d4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d4c4.md) → [`0066d4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4c4.md) FUN_0066d4c4

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
      "definition_site": "0066d4d0",
      "incomplete_value": false,
      "site": "0066d4d0",
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
            "const:4a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d4d0",
      "incomplete_value": false,
      "site": "0066d4d0",
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
            "const:458:8"
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
      "0066d4d0",
      "DATA",
      [
        "storage",
        "00bf7458",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d4d0",
      "DATA",
      [
        "storage",
        "00bf74a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d4c4.md#insn-0066d4cc)
- 新版 [`0066d4cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d4c4.md#insn-0066d4cc)

~~~diff
- 0066d4cc ["COPY", "tmp:0:8", ["const:458:8"]]
- 0066d4cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066d4cc ["COPY", "tmp:0:8", ["const:4a8:8"]]
+ 0066d4cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d4cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d4cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d4cc bytes 29611191
+ 0066d4cc bytes 29a11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8f683a33dfe0751ded3599e945ea956"></a>

### [`0066d5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d5c4.md) → [`0066d5c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md) FUN_0066d5c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066d5e8",
      "incomplete_value": false,
      "site": "0066d5f0",
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
            "const:528:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d5e8",
      "incomplete_value": false,
      "site": "0066d5f0",
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
            "const:4d8:8"
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
      "0066d5f0",
      "DATA",
      [
        "storage",
        "00bf74d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d5f0",
      "DATA",
      [
        "storage",
        "00bf7528",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d5c4.md#insn-0066d5e8)
- 新版 [`0066d5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d5c4.md#insn-0066d5e8)

~~~diff
- 0066d5e8 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 0066d5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d5e8 ["COPY", "tmp:0:8", ["const:528:8"]]
+ 0066d5e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d5e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d5e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d5e8 bytes 08611391
+ 0066d5e8 bytes 08a11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af9cbce7df16d149213e1c592a478cbf"></a>

### [`0066d8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d8e0.md) → [`0066d8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md) FUN_0066d8e0

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
      "definition_site": "0066d904",
      "incomplete_value": false,
      "site": "0066d904",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d904",
      "incomplete_value": false,
      "site": "0066d904",
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
            "const:558:8"
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
      "0066d904",
      "DATA",
      [
        "storage",
        "00bf7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d904",
      "DATA",
      [
        "storage",
        "00bf75a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d8e0.md#insn-0066d900)
- 新版 [`0066d900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d8e0.md#insn-0066d900)

~~~diff
- 0066d900 ["COPY", "tmp:0:8", ["const:558:8"]]
- 0066d900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d900 ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 0066d900 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d900 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d900 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d900 bytes 08611591
+ 0066d900 bytes 08a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-017ef122ff32ac23e8a3c967478b5c26"></a>

### [`0066d914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d914.md) → [`0066d914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d914.md) FUN_0066d914

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
      "definition_site": "0066d920",
      "incomplete_value": false,
      "site": "0066d920",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d920",
      "incomplete_value": false,
      "site": "0066d920",
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
            "const:558:8"
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
      "0066d920",
      "DATA",
      [
        "storage",
        "00bf7558",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d920",
      "DATA",
      [
        "storage",
        "00bf75a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d914.md#insn-0066d91c)
- 新版 [`0066d91c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d914.md#insn-0066d91c)

~~~diff
- 0066d91c ["COPY", "tmp:0:8", ["const:558:8"]]
- 0066d91c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d91c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d91c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066d91c ["COPY", "tmp:0:8", ["const:5a8:8"]]
+ 0066d91c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d91c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d91c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d91c bytes 29611591
+ 0066d91c bytes 29a11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b03987c3185e9e30074141904079698"></a>

### [`0066d9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d9b0.md) → [`0066d9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d9b0.md) FUN_0066d9b0

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
      "definition_site": "0066d9d4",
      "incomplete_value": false,
      "site": "0066d9d4",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d9d4",
      "incomplete_value": false,
      "site": "0066d9d4",
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
            "const:5d8:8"
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
      "0066d9d4",
      "DATA",
      [
        "storage",
        "00bf75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d9d4",
      "DATA",
      [
        "storage",
        "00bf7628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d9b0.md#insn-0066d9d0)
- 新版 [`0066d9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d9b0.md#insn-0066d9d0)

~~~diff
- 0066d9d0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0066d9d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066d9d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066d9d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066d9d0 ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0066d9d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d9d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066d9d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066d9d0 bytes 08611791
+ 0066d9d0 bytes 08a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7df9e9a62baaf5b1c7652ef7045f540"></a>

### [`0066d9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d9e4.md) → [`0066d9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d9e4.md) FUN_0066d9e4

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
      "definition_site": "0066d9f0",
      "incomplete_value": false,
      "site": "0066d9f0",
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
            "const:628:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066d9f0",
      "incomplete_value": false,
      "site": "0066d9f0",
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
            "const:5d8:8"
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
      "0066d9f0",
      "DATA",
      [
        "storage",
        "00bf75d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066d9f0",
      "DATA",
      [
        "storage",
        "00bf7628",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066d9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066d9e4.md#insn-0066d9ec)
- 新版 [`0066d9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066d9e4.md#insn-0066d9ec)

~~~diff
- 0066d9ec ["COPY", "tmp:0:8", ["const:5d8:8"]]
- 0066d9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066d9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066d9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066d9ec ["COPY", "tmp:0:8", ["const:628:8"]]
+ 0066d9ec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d9ec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066d9ec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066d9ec bytes 29611791
+ 0066d9ec bytes 29a11891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9c1639ed47e0b7b12256a6da7a454f7"></a>

### [`0066da00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066da00.md) → [`0066da00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md) FUN_0066da00

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 13件 [`0044dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044dabc.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00665758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00665/00665758.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0044dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044dabc.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00665758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00665/00665758.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066dd90",
      "incomplete_value": false,
      "site": "0066dd90",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066dd90",
      "incomplete_value": false,
      "site": "0066dd90",
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
            "const:648:8"
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
      "0066dd90",
      "DATA",
      [
        "storage",
        "00bf7648",
        null,
        "undefined *"
      ]
    ],
    [
      "0066dde8",
      "READ",
      [
        "storage",
        "00bf7668",
        null,
        "pointer"
      ]
    ],
    [
      "0066dde8",
      "READ",
      [
        "storage",
        "00bf7670",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066dd90",
      "DATA",
      [
        "storage",
        "00bf7698",
        null,
        "undefined *"
      ]
    ],
    [
      "0066dde8",
      "READ",
      [
        "storage",
        "00bf76b8",
        null,
        "pointer"
      ]
    ],
    [
      "0066dde8",
      "READ",
      [
        "storage",
        "00bf76c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066dd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066da00.md#insn-0066dd88) · [`0066dd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066da00.md#insn-0066dd8c)
- 新版 [`0066dd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md#insn-0066dd88) · [`0066dd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066da00.md#insn-0066dd8c)

~~~diff
- 0066dd88 ["COPY", "tmp:0:8", ["const:648:8"]]
- 0066dd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066dd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066dd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066dd88 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0066dd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066dd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066dd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066dd88 bytes 08211991
+ 0066dd88 bytes 08611a91
- 0066dd8c ["COPY", "tmp:0:8", ["const:30:8"]]
- 0066dd8c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 0066dd8c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 0066dd8c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 0066dd8c bytes f5c30091
+ 0066dd8c ["COPY", "tmp:0:8", ["const:30:8"]]
+ 0066dd8c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 0066dd8c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 0066dd8c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 0066dd8c bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02282e4696e558dad83e0fc513eb7e31"></a>

### [`0066df3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066df3c.md) → [`0066df3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066df3c.md) FUN_0066df3c

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
      "definition_site": "0066df48",
      "incomplete_value": false,
      "site": "0066df48",
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
            "const:698:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066df48",
      "incomplete_value": false,
      "site": "0066df48",
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
            "const:648:8"
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
      "0066df48",
      "DATA",
      [
        "storage",
        "00bf7648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066df48",
      "DATA",
      [
        "storage",
        "00bf7698",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066df44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066df3c.md#insn-0066df44)
- 新版 [`0066df44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066df3c.md#insn-0066df44)

~~~diff
- 0066df44 ["COPY", "tmp:0:8", ["const:648:8"]]
- 0066df44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066df44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066df44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066df44 ["COPY", "tmp:0:8", ["const:698:8"]]
+ 0066df44 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066df44 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066df44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066df44 bytes 29211991
+ 0066df44 bytes 29611a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42e5b8d67c4e1512638c4706b3c8fac5"></a>

### [`0066dfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066dfc4.md) → [`0066dfc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066dfc4.md) FUN_0066dfc4

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
      "definition_site": "0066dfe8",
      "incomplete_value": false,
      "site": "0066dfe8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066dfe8",
      "incomplete_value": false,
      "site": "0066dfe8",
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
            "const:6d8:8"
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
      "0066dfe8",
      "DATA",
      [
        "storage",
        "00bf76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066dfe8",
      "DATA",
      [
        "storage",
        "00bf7728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066dfe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066dfc4.md#insn-0066dfe4)
- 新版 [`0066dfe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066dfc4.md#insn-0066dfe4)

~~~diff
- 0066dfe4 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0066dfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066dfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066dfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066dfe4 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 0066dfe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066dfe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066dfe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066dfe4 bytes 08611b91
+ 0066dfe4 bytes 08a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aec46601cf27c1f1b3823b447d1b58a5"></a>

### [`0066dff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066dff8.md) → [`0066dff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066dff8.md) FUN_0066dff8

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
      "definition_site": "0066e004",
      "incomplete_value": false,
      "site": "0066e004",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e004",
      "incomplete_value": false,
      "site": "0066e004",
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
            "const:6d8:8"
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
      "0066e004",
      "DATA",
      [
        "storage",
        "00bf76d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e004",
      "DATA",
      [
        "storage",
        "00bf7728",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066d/0066dff8.md#insn-0066e000)
- 新版 [`0066e000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066d/0066dff8.md#insn-0066e000)

~~~diff
- 0066e000 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 0066e000 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e000 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e000 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e000 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 0066e000 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e000 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e000 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e000 bytes 29611b91
+ 0066e000 bytes 29a11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0a5bf7376915327d0f8ef496190d40f"></a>

### [`0066e0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e0f8.md) → [`0066e0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e0f8.md) FUN_0066e0f8

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
      "definition_site": "0066e11c",
      "incomplete_value": false,
      "site": "0066e11c",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e11c",
      "incomplete_value": false,
      "site": "0066e11c",
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
            "const:758:8"
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
      "0066e11c",
      "DATA",
      [
        "storage",
        "00bf7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e11c",
      "DATA",
      [
        "storage",
        "00bf77a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e0f8.md#insn-0066e118)
- 新版 [`0066e118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e0f8.md#insn-0066e118)

~~~diff
- 0066e118 ["COPY", "tmp:0:8", ["const:758:8"]]
- 0066e118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e118 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0066e118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e118 bytes 08611d91
+ 0066e118 bytes 08a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d527f33893ca0fafc7951945d94cf39"></a>

### [`0066e12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e12c.md) → [`0066e12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e12c.md) FUN_0066e12c

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
      "definition_site": "0066e138",
      "incomplete_value": false,
      "site": "0066e138",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e138",
      "incomplete_value": false,
      "site": "0066e138",
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
            "const:758:8"
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
      "0066e138",
      "DATA",
      [
        "storage",
        "00bf7758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e138",
      "DATA",
      [
        "storage",
        "00bf77a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e12c.md#insn-0066e134)
- 新版 [`0066e134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e12c.md#insn-0066e134)

~~~diff
- 0066e134 ["COPY", "tmp:0:8", ["const:758:8"]]
- 0066e134 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e134 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e134 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e134 ["COPY", "tmp:0:8", ["const:7a8:8"]]
+ 0066e134 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e134 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e134 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e134 bytes 29611d91
+ 0066e134 bytes 29a11e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eccd841d1f79941dc335ff3bc702ff4b"></a>

### [`0066e1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e1e4.md) → [`0066e1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md) FUN_0066e1e4

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
      "definition_site": "0066e208",
      "incomplete_value": false,
      "site": "0066e208",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e208",
      "incomplete_value": false,
      "site": "0066e208",
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
            "const:7d8:8"
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
      "0066e208",
      "DATA",
      [
        "storage",
        "00bf77d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e208",
      "DATA",
      [
        "storage",
        "00bf7828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e1e4.md#insn-0066e204)
- 新版 [`0066e204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e1e4.md#insn-0066e204)

~~~diff
- 0066e204 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0066e204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e204 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0066e204 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e204 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e204 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e204 bytes 08611f91
+ 0066e204 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5d8259c05af02373faa7c2735e13b4a"></a>

### [`0066e218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e218.md) → [`0066e218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e218.md) FUN_0066e218

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
      "definition_site": "0066e224",
      "incomplete_value": false,
      "site": "0066e224",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e224",
      "incomplete_value": false,
      "site": "0066e224",
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
            "const:7d8:8"
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
      "0066e224",
      "DATA",
      [
        "storage",
        "00bf77d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e224",
      "DATA",
      [
        "storage",
        "00bf7828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e218.md#insn-0066e220)
- 新版 [`0066e220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e218.md#insn-0066e220)

~~~diff
- 0066e220 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0066e220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e220 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0066e220 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e220 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e220 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e220 bytes 29611f91
+ 0066e220 bytes 29a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c923b293230de1f5e9945612ef08a5e6"></a>

### [`0066e34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e34c.md) → [`0066e34c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md) FUN_0066e34c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066e370",
      "incomplete_value": false,
      "site": "0066e378",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e370",
      "incomplete_value": false,
      "site": "0066e378",
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
            "const:858:8"
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
      "0066e378",
      "DATA",
      [
        "storage",
        "00bf7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e378",
      "DATA",
      [
        "storage",
        "00bf78a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e34c.md#insn-0066e370)
- 新版 [`0066e370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e34c.md#insn-0066e370)

~~~diff
- 0066e370 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0066e370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e370 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0066e370 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e370 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e370 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e370 bytes 08612191
+ 0066e370 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b67bd5d8db0fe919c5978e0194b10e08"></a>

### [`0066e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e394.md) → [`0066e394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e394.md) FUN_0066e394

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066e398",
      "incomplete_value": false,
      "site": "0066e39c",
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
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e398",
      "incomplete_value": false,
      "site": "0066e39c",
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
            "const:858:8"
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
      "0066e39c",
      "DATA",
      [
        "storage",
        "00bf7858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e39c",
      "DATA",
      [
        "storage",
        "00bf78a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e394.md#insn-0066e398)
- 新版 [`0066e398`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e394.md#insn-0066e398)

~~~diff
- 0066e398 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0066e398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e398 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0066e398 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e398 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e398 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e398 bytes 08612191
+ 0066e398 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e6a1a43af1dc785136d1f751f2d373a"></a>

### [`0066e668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e668.md) → [`0066e668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md) FUN_0066e668

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
      "definition_site": "0066e68c",
      "incomplete_value": false,
      "site": "0066e68c",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e68c",
      "incomplete_value": false,
      "site": "0066e68c",
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
            "const:8d8:8"
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
      "0066e68c",
      "DATA",
      [
        "storage",
        "00bf78d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e68c",
      "DATA",
      [
        "storage",
        "00bf7928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e668.md#insn-0066e688)
- 新版 [`0066e688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e668.md#insn-0066e688)

~~~diff
- 0066e688 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0066e688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e688 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0066e688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e688 bytes 08612391
+ 0066e688 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a9dedf74742921ffac409ce8a9b8268"></a>

### [`0066e69c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e69c.md) → [`0066e69c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e69c.md) FUN_0066e69c

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
      "definition_site": "0066e6a8",
      "incomplete_value": false,
      "site": "0066e6a8",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e6a8",
      "incomplete_value": false,
      "site": "0066e6a8",
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
            "const:8d8:8"
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
      "0066e6a8",
      "DATA",
      [
        "storage",
        "00bf78d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e6a8",
      "DATA",
      [
        "storage",
        "00bf7928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e69c.md#insn-0066e6a4)
- 新版 [`0066e6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e69c.md#insn-0066e6a4)

~~~diff
- 0066e6a4 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0066e6a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e6a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e6a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e6a4 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0066e6a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e6a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e6a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e6a4 bytes 29612391
+ 0066e6a4 bytes 29a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76eed5816d0e8441fe99041df87d6534"></a>

### [`0066e724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e724.md) → [`0066e724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md) FUN_0066e724

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
      "definition_site": "0066e748",
      "incomplete_value": false,
      "site": "0066e74c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e748",
      "incomplete_value": false,
      "site": "0066e74c",
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
            "const:958:8"
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
      "0066e74c",
      "DATA",
      [
        "storage",
        "00bf7958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e74c",
      "DATA",
      [
        "storage",
        "00bf79a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e724.md#insn-0066e748)
- 新版 [`0066e748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e724.md#insn-0066e748)

~~~diff
- 0066e748 ["COPY", "tmp:0:8", ["const:958:8"]]
- 0066e748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e748 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 0066e748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e748 bytes 08612591
+ 0066e748 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73eb52f848b7fb52b60e95a7b6bda9b6"></a>

### [`0066e764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e764.md) → [`0066e764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e764.md) FUN_0066e764

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
      "definition_site": "0066e768",
      "incomplete_value": false,
      "site": "0066e76c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e768",
      "incomplete_value": false,
      "site": "0066e76c",
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
            "const:958:8"
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
      "0066e76c",
      "DATA",
      [
        "storage",
        "00bf7958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e76c",
      "DATA",
      [
        "storage",
        "00bf79a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e764.md#insn-0066e768)
- 新版 [`0066e768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e764.md#insn-0066e768)

~~~diff
- 0066e768 ["COPY", "tmp:0:8", ["const:958:8"]]
- 0066e768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e768 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 0066e768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e768 bytes 08612591
+ 0066e768 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68c31d4844d919139c79416f3a71d3e1"></a>

### [`0066e93c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e93c.md) → [`0066e93c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e93c.md) FUN_0066e93c

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
      "definition_site": "0066e948",
      "incomplete_value": false,
      "site": "0066e94c",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e948",
      "incomplete_value": false,
      "site": "0066e94c",
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
            "const:9d8:8"
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
      "0066e94c",
      "DATA",
      [
        "storage",
        "00bf79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e94c",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e93c.md#insn-0066e948)
- 新版 [`0066e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e93c.md#insn-0066e948)

~~~diff
- 0066e948 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0066e948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e948 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0066e948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e948 bytes 29612791
+ 0066e948 bytes 29a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb2966baa72b0705ff3964a016dbf2d7"></a>

### [`0066e960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e960.md) → [`0066e960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e960.md) FUN_0066e960

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
      "definition_site": "0066e968",
      "incomplete_value": false,
      "site": "0066e96c",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e968",
      "incomplete_value": false,
      "site": "0066e96c",
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
            "const:9d8:8"
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
      "0066e96c",
      "DATA",
      [
        "storage",
        "00bf79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e96c",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e960.md#insn-0066e968)
- 新版 [`0066e968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e960.md#insn-0066e968)

~~~diff
- 0066e968 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0066e968 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066e968 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066e968 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066e968 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0066e968 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e968 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066e968 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066e968 bytes 29612791
+ 0066e968 bytes 29a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f714c71aa7e27bfead0df6f60b4f6186"></a>

### [`0066e9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e9a0.md) → [`0066e9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md) FUN_0066e9a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066e9c0",
      "incomplete_value": false,
      "site": "0066e9c8",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066e9c0",
      "incomplete_value": false,
      "site": "0066e9c8",
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
            "const:9d8:8"
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
      "0066e9c8",
      "DATA",
      [
        "storage",
        "00bf79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066e9c8",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066e9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066e9a0.md#insn-0066e9c0)
- 新版 [`0066e9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066e9a0.md#insn-0066e9c0)

~~~diff
- 0066e9c0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0066e9c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066e9c0 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0066e9c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e9c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066e9c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066e9c0 bytes 08612791
+ 0066e9c0 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5aa8db9fa236dc71d19ba76803a9ddd"></a>

### [`0066ea58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ea58.md) → [`0066ea58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md) FUN_0066ea58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066ea6c",
      "incomplete_value": false,
      "site": "0066ea74",
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
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ea6c",
      "incomplete_value": false,
      "site": "0066ea74",
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
            "const:9d8:8"
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
      "0066ea74",
      "DATA",
      [
        "storage",
        "00bf79d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ea74",
      "DATA",
      [
        "storage",
        "00bf7a28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ea58.md#insn-0066ea6c)
- 新版 [`0066ea6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ea58.md#insn-0066ea6c)

~~~diff
- 0066ea6c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0066ea6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066ea6c ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0066ea6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ea6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ea6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ea6c bytes 08612791
+ 0066ea6c bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49678fb51c12f623be75f8b09485e2ef"></a>

### [`0066eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066eb44.md) → [`0066eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066eb44.md) FUN_0066eb44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f044.md) [`0066baa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066baa4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f044.md) [`0066baa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066baa4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066ec74",
      "incomplete_value": false,
      "site": "0066ec80",
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
            "const:b0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ec74",
      "incomplete_value": false,
      "site": "0066ec80",
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
            "const:a72:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066ed28",
      "incomplete_value": false,
      "site": "0066ed30",
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
            "const:4f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ed28",
      "incomplete_value": false,
      "site": "0066ed30",
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
            "const:457:8"
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
      "0066ec74",
      "PARAM",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ],
    [
      "0066ed28",
      "PARAM",
      [
        "storage",
        "002a8457",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0066ec74",
      "PARAM",
      [
        "storage",
        "002a6b0c",
        null,
        "string"
      ]
    ],
    [
      "0066ed28",
      "PARAM",
      [
        "storage",
        "002a84f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ec74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066eb44.md#insn-0066ec74) · [`0066ed28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066eb44.md#insn-0066ed28)
- 新版 [`0066ec74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066eb44.md#insn-0066ec74) · [`0066ed28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066eb44.md#insn-0066ed28)

~~~diff
- 0066ec74 ["COPY", "tmp:0:8", ["const:a72:8"]]
- 0066ec74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0066ec74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0066ec74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0066ec74 ["COPY", "tmp:0:8", ["const:b0c:8"]]
+ 0066ec74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0066ec74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0066ec74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0066ec74 bytes 42c82991
+ 0066ec74 bytes 42302c91
- 0066ed28 ["COPY", "tmp:0:8", ["const:457:8"]]
- 0066ed28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0066ed28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0066ed28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0066ed28 ["COPY", "tmp:0:8", ["const:4f1:8"]]
+ 0066ed28 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0066ed28 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0066ed28 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0066ed28 bytes 215c1191
+ 0066ed28 bytes 21c41391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9bf4ff67114a1b9312cb70b51953683"></a>

### [`0066ef6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ef6c.md) → [`0066ef6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef6c.md) FUN_0066ef6c

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
      "definition_site": "0066ef78",
      "incomplete_value": false,
      "site": "0066ef7c",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ef78",
      "incomplete_value": false,
      "site": "0066ef7c",
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
            "const:a88:8"
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
      "0066ef7c",
      "DATA",
      [
        "storage",
        "00bf7a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ef7c",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ef78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ef6c.md#insn-0066ef78)
- 新版 [`0066ef78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef6c.md#insn-0066ef78)

~~~diff
- 0066ef78 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0066ef78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066ef78 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0066ef78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066ef78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066ef78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066ef78 bytes 29212a91
+ 0066ef78 bytes 29612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c61c554af15b2e058bd44b6652a8f029"></a>

### [`0066ef90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ef90.md) → [`0066ef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md) FUN_0066ef90

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
      "definition_site": "0066ef98",
      "incomplete_value": false,
      "site": "0066ef9c",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ef98",
      "incomplete_value": false,
      "site": "0066ef9c",
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
            "const:a88:8"
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
      "0066ef9c",
      "DATA",
      [
        "storage",
        "00bf7a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ef9c",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ef98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066ef90.md#insn-0066ef98)
- 新版 [`0066ef98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066ef90.md#insn-0066ef98)

~~~diff
- 0066ef98 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0066ef98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0066ef98 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0066ef98 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0066ef98 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0066ef98 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0066ef98 bytes 29212a91
+ 0066ef98 bytes 29612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6990a83525469c0373ecfdb9b62b7807"></a>

### [`0066efd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066efd0.md) → [`0066efd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md) FUN_0066efd0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066eff0",
      "incomplete_value": false,
      "site": "0066eff8",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066eff0",
      "incomplete_value": false,
      "site": "0066eff8",
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
            "const:a88:8"
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
      "0066eff8",
      "DATA",
      [
        "storage",
        "00bf7a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066eff8",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066eff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066e/0066efd0.md#insn-0066eff0)
- 新版 [`0066eff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066e/0066efd0.md#insn-0066eff0)

~~~diff
- 0066eff0 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0066eff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066eff0 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0066eff0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066eff0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066eff0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066eff0 bytes 08212a91
+ 0066eff0 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d4386c5cde8f03c4385a7af5aaeec93"></a>

### [`0066f090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f090.md) → [`0066f090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md) FUN_0066f090

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0066f0a4",
      "incomplete_value": false,
      "site": "0066f0ac",
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
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066f0a4",
      "incomplete_value": false,
      "site": "0066f0ac",
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
            "const:a88:8"
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
      "0066f0ac",
      "DATA",
      [
        "storage",
        "00bf7a88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066f0ac",
      "DATA",
      [
        "storage",
        "00bf7ad8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066f0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f090.md#insn-0066f0a4)
- 新版 [`0066f0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f090.md#insn-0066f0a4)

~~~diff
- 0066f0a4 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0066f0a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066f0a4 ["COPY", "tmp:0:8", ["const:ad8:8"]]
+ 0066f0a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066f0a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066f0a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066f0a4 bytes 08212a91
+ 0066f0a4 bytes 08612b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2e8e7f3c88cf0a555e41192fb09ee83"></a>

### [`0066f184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f184.md) → [`0066f184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md) FUN_0066f184

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 24件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 0件  · 呼出先 24件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.93% / 新版 96.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066f208",
      "incomplete_value": true,
      "site": "0066f20c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066f208",
      "incomplete_value": true,
      "site": "0066f20c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066f1f4",
      "incomplete_value": false,
      "site": "0066f20c",
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
      "definition_site": "0066f1f4",
      "incomplete_value": false,
      "site": "0066f20c",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0066f200",
      "incomplete_value": false,
      "site": "0066f20c",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066f200",
      "incomplete_value": false,
      "site": "0066f20c",
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
            "const:a60:8"
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
      "0066f1f4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066f1f8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0066f200",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0066f1f4",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0066f1f8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0066f200",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066f1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f184.md#insn-0066f1f4) · [`0066f1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f184.md#insn-0066f1f8) · [`0066f1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066f184.md#insn-0066f1fc)
- 新版 [`0066f1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md#insn-0066f1f4) · [`0066f1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066f184.md#insn-0066f1f8)

~~~diff
- 0066f1f4 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0066f1f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0066f1f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0066f1f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0066f1f4 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0066f1f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0066f1f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0066f1f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0066f1f4 bytes 21203991
+ 0066f1f4 bytes 21603a91
- 0066f1f8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
- 0066f1f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0066f1f8 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:ab8:8"]]
+ 0066f1f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0066f1f8 bytes 883f45f9
+ 0066f1f8 bytes 885f45f9
- 0066f1fc ["COPY", "register:4010:8", ["const:bf7000:8"]]
- 0066f1fc bytes 422c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bd11462fd7b6bd3caaf398ed5d14404"></a>

### [`0066fef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066fef0.md) → [`0066fef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md) FUN_0066fef0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0066ff10",
      "incomplete_value": false,
      "site": "0066ff14",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ff10",
      "incomplete_value": false,
      "site": "0066ff14",
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
            "const:b08:8"
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
      "0066ff14",
      "DATA",
      [
        "storage",
        "00bf7b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ff14",
      "DATA",
      [
        "storage",
        "00bf7b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ff10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066fef0.md#insn-0066ff10)
- 新版 [`0066ff10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066fef0.md#insn-0066ff10)

~~~diff
- 0066ff10 ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0066ff10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066ff10 ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0066ff10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ff10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ff10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ff10 bytes 08212c91
+ 0066ff10 bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63d6310692df98b031b688c50064f1cc"></a>

### [`0066ff28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066ff28.md) → [`0066ff28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066ff28.md) FUN_0066ff28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0066ff2c",
      "incomplete_value": false,
      "site": "0066ff30",
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
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0066ff2c",
      "incomplete_value": false,
      "site": "0066ff30",
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
            "const:b08:8"
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
      "0066ff30",
      "DATA",
      [
        "storage",
        "00bf7b08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0066ff30",
      "DATA",
      [
        "storage",
        "00bf7b58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0066ff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066f/0066ff28.md#insn-0066ff2c)
- 新版 [`0066ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066f/0066ff28.md#insn-0066ff2c)

~~~diff
- 0066ff2c ["COPY", "tmp:0:8", ["const:b08:8"]]
- 0066ff2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0066ff2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0066ff2c ["COPY", "tmp:0:8", ["const:b58:8"]]
+ 0066ff2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ff2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0066ff2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0066ff2c bytes 08212c91
+ 0066ff2c bytes 08612d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-640c6ae30c7ee702142238c4351d0e29"></a>

### [`0067006c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/0067006c.md) → [`0067006c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md) FUN_0067006c

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
      "definition_site": "00670090",
      "incomplete_value": false,
      "site": "00670090",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670090",
      "incomplete_value": false,
      "site": "00670090",
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
            "const:b88:8"
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
      "00670090",
      "DATA",
      [
        "storage",
        "00bf7b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670090",
      "DATA",
      [
        "storage",
        "00bf7bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067008c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/0067006c.md#insn-0067008c)
- 新版 [`0067008c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/0067006c.md#insn-0067008c)

~~~diff
- 0067008c ["COPY", "tmp:0:8", ["const:b88:8"]]
- 0067008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067008c ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 0067008c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067008c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067008c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067008c bytes 08212e91
+ 0067008c bytes 08612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33a5848c1518eb38973730062cf46439"></a>

### [`006700a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006700a0.md) → [`006700a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700a0.md) FUN_006700a0

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
      "definition_site": "006700ac",
      "incomplete_value": false,
      "site": "006700ac",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006700ac",
      "incomplete_value": false,
      "site": "006700ac",
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
            "const:b88:8"
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
      "006700ac",
      "DATA",
      [
        "storage",
        "00bf7b88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006700ac",
      "DATA",
      [
        "storage",
        "00bf7bd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006700a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006700a0.md#insn-006700a8)
- 新版 [`006700a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006700a0.md#insn-006700a8)

~~~diff
- 006700a8 ["COPY", "tmp:0:8", ["const:b88:8"]]
- 006700a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006700a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006700a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006700a8 ["COPY", "tmp:0:8", ["const:bd8:8"]]
+ 006700a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006700a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006700a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006700a8 bytes 29212e91
+ 006700a8 bytes 29612f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c0fcdd5c4b419210064f05af31ca453"></a>

### [`006701a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006701a8.md) → [`006701a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md) FUN_006701a8

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
      "definition_site": "006701cc",
      "incomplete_value": false,
      "site": "006701cc",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006701cc",
      "incomplete_value": false,
      "site": "006701cc",
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
            "const:c08:8"
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
      "006701cc",
      "DATA",
      [
        "storage",
        "00bf7c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006701cc",
      "DATA",
      [
        "storage",
        "00bf7c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006701c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006701a8.md#insn-006701c8)
- 新版 [`006701c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701a8.md#insn-006701c8)

~~~diff
- 006701c8 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 006701c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006701c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006701c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006701c8 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 006701c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006701c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006701c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006701c8 bytes 08213091
+ 006701c8 bytes 08613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b286db18c3b43c2b419c4b4fb9c8ddae"></a>

### [`006701dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006701dc.md) → [`006701dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701dc.md) FUN_006701dc

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
      "definition_site": "006701e8",
      "incomplete_value": false,
      "site": "006701e8",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006701e8",
      "incomplete_value": false,
      "site": "006701e8",
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
            "const:c08:8"
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
      "006701e8",
      "DATA",
      [
        "storage",
        "00bf7c08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006701e8",
      "DATA",
      [
        "storage",
        "00bf7c58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006701e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/006701dc.md#insn-006701e4)
- 新版 [`006701e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/006701dc.md#insn-006701e4)

~~~diff
- 006701e4 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 006701e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006701e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006701e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006701e4 ["COPY", "tmp:0:8", ["const:c58:8"]]
+ 006701e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006701e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006701e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006701e4 bytes 29213091
+ 006701e4 bytes 29613191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dd81fbcc7ea1ec0d8028a2cbe165054"></a>

### [`00670330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670330.md) → [`00670330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670330.md) FUN_00670330

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00670350",
      "incomplete_value": false,
      "site": "00670354",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670350",
      "incomplete_value": false,
      "site": "00670354",
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
            "const:c88:8"
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
      "00670354",
      "DATA",
      [
        "storage",
        "00bf7c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670354",
      "DATA",
      [
        "storage",
        "00bf7cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670330.md#insn-00670350)
- 新版 [`00670350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670330.md#insn-00670350)

~~~diff
- 00670350 ["COPY", "tmp:0:8", ["const:c88:8"]]
- 00670350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00670350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00670350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00670350 ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 00670350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00670350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00670350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00670350 bytes 08213291
+ 00670350 bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdedfcfac284085520eff514acec6b24"></a>

### [`00670368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670368.md) → [`00670368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670368.md) FUN_00670368

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "0067036c",
      "incomplete_value": false,
      "site": "00670370",
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
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067036c",
      "incomplete_value": false,
      "site": "00670370",
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
            "const:c88:8"
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
      "00670370",
      "DATA",
      [
        "storage",
        "00bf7c88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670370",
      "DATA",
      [
        "storage",
        "00bf7cd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067036c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670368.md#insn-0067036c)
- 新版 [`0067036c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670368.md#insn-0067036c)

~~~diff
- 0067036c ["COPY", "tmp:0:8", ["const:c88:8"]]
- 0067036c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067036c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067036c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067036c ["COPY", "tmp:0:8", ["const:cd8:8"]]
+ 0067036c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067036c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067036c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067036c bytes 08213291
+ 0067036c bytes 08613391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fefcaee376baffd08d815aed4a3690dd"></a>

### [`00670388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670388.md) → [`00670388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md) FUN_00670388

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 21件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449bac.md)
- 新版 呼出元 0件  · 呼出先 21件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00449bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449bac.md)

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
      "definition_site": "0067045c",
      "incomplete_value": true,
      "site": "00670474",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067045c",
      "incomplete_value": true,
      "site": "00670474",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
              ]
            ]
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
      "definition_site": "00670464",
      "incomplete_value": false,
      "site": "00670474",
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
      "definition_site": "00670464",
      "incomplete_value": false,
      "site": "00670474",
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
      "definition_site": "0067046c",
      "incomplete_value": false,
      "site": "00670474",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067046c",
      "incomplete_value": false,
      "site": "00670474",
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
            "const:a60:8"
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
      "0067045c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00670464",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0067046c",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0067045c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00670464",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0067046c",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067045c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670388.md#insn-0067045c) · [`00670464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670388.md#insn-00670464) · [`0067046c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670388.md#insn-0067046c)
- 新版 [`0067045c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md#insn-0067045c) · [`00670464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md#insn-00670464) · [`0067046c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670388.md#insn-0067046c)

~~~diff
- 0067045c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:a78:8"]]
- 0067045c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0067045c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:ab8:8"]]
+ 0067045c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0067045c bytes 603f45f9
+ 0067045c bytes 605f45f9
- 00670464 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00670464 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00670464 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00670464 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00670464 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00670464 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00670464 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00670464 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00670464 bytes 21203991
+ 00670464 bytes 21603a91
- 0067046c ["COPY", "tmp:0:8", ["const:a60:8"]]
- 0067046c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0067046c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0067046c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0067046c ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 0067046c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0067046c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0067046c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0067046c bytes 42802991
+ 0067046c bytes 42c02a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-214b4a1835a13ce1aa023258ad2a1399"></a>

### [`00670a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a44.md) → [`00670a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a44.md) FUN_00670a44

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00670a64",
      "incomplete_value": false,
      "site": "00670a68",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670a64",
      "incomplete_value": false,
      "site": "00670a68",
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
            "const:d08:8"
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
      "00670a68",
      "DATA",
      [
        "storage",
        "00bf7d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670a68",
      "DATA",
      [
        "storage",
        "00bf7d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a44.md#insn-00670a64)
- 新版 [`00670a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a44.md#insn-00670a64)

~~~diff
- 00670a64 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00670a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00670a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00670a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00670a64 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00670a64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00670a64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00670a64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00670a64 bytes 08213491
+ 00670a64 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9733dbf5aeb98ee808338a0e80af16ea"></a>

### [`00670a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a7c.md) → [`00670a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a7c.md) FUN_00670a7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00670a80",
      "incomplete_value": false,
      "site": "00670a84",
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
            "const:d58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670a80",
      "incomplete_value": false,
      "site": "00670a84",
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
            "const:d08:8"
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
      "00670a84",
      "DATA",
      [
        "storage",
        "00bf7d08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00670a84",
      "DATA",
      [
        "storage",
        "00bf7d58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a7c.md#insn-00670a80)
- 新版 [`00670a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a7c.md#insn-00670a80)

~~~diff
- 00670a80 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00670a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00670a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00670a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00670a80 ["COPY", "tmp:0:8", ["const:d58:8"]]
+ 00670a80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00670a80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00670a80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00670a80 bytes 08213491
+ 00670a80 bytes 08613591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2db37e1aa10559d33d4791fd8e271917"></a>

### [`00670a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md) → [`00670a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md) FUN_00670a9c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00668a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00668/00668a08.md) [`0066a360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066a/0066a360.md) [`00670de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670de0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00668a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00668/00668a08.md) [`0066a360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066a/0066a360.md) [`00670de0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670de0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00670c2c",
      "incomplete_value": false,
      "site": "00670c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:f6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670c2c",
      "incomplete_value": false,
      "site": "00670c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:298000:8"
          ],
          [
            "leaf",
            "const:ff9:8"
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
      "definition_site": "00670c54",
      "incomplete_value": false,
      "site": "00670c60",
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
            "const:917:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00670c54",
      "incomplete_value": false,
      "site": "00670c60",
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
            "const:88c:8"
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
      "00670c34",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "00670c60",
      "DATA",
      [
        "storage",
        "002a088c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00670c34",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "00670c60",
      "DATA",
      [
        "storage",
        "002a0917",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00670c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md#insn-00670c2c) · [`00670c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00670/00670a9c.md#insn-00670c30)
- 新版 [`00670c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md#insn-00670c2c) · [`00670c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00670/00670a9c.md#insn-00670c30)

~~~diff
- 00670c2c ["COPY", "tmp:0:8", ["const:ff9:8"]]
- 00670c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00670c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00670c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00670c2c ["COPY", "tmp:0:8", ["const:f6c:8"]]
+ 00670c2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00670c2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00670c2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00670c2c bytes 08e53f91
+ 00670c2c bytes 08b13d91
- 00670c30 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00670c30 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00670c30 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00670c30 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00670c30 bytes f4630091
+ 00670c30 ["COPY", "tmp:0:8", ["const:18:8"]]
+ 00670c30 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 00670c30 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 00670c30 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 00670c30 bytes f4630091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd1af02754f1b1540632e858d1d4f87"></a>

### [`0067102c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/0067102c.md) → [`0067102c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md) FUN_0067102c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0067104c",
      "incomplete_value": false,
      "site": "00671050",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067104c",
      "incomplete_value": false,
      "site": "00671050",
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
            "const:d88:8"
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
      "00671050",
      "DATA",
      [
        "storage",
        "00bf7d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671050",
      "DATA",
      [
        "storage",
        "00bf7dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067104c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/0067102c.md#insn-0067104c)
- 新版 [`0067104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067102c.md#insn-0067104c)

~~~diff
- 0067104c ["COPY", "tmp:0:8", ["const:d88:8"]]
- 0067104c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0067104c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0067104c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0067104c ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 0067104c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0067104c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0067104c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0067104c bytes 08213691
+ 0067104c bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45f5d417c47d59984c369b5cf8bd94b3"></a>

### [`00671064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671064.md) → [`00671064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671064.md) FUN_00671064

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00671068",
      "incomplete_value": true,
      "site": "0067106c",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671068",
      "incomplete_value": true,
      "site": "0067106c",
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
            "const:d88:8"
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
      "0067106c",
      "DATA",
      [
        "storage",
        "00bf7d88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0067106c",
      "DATA",
      [
        "storage",
        "00bf7dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671064.md#insn-00671068)
- 新版 [`00671068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671064.md#insn-00671068)

~~~diff
- 00671068 ["COPY", "tmp:0:8", ["const:d88:8"]]
- 00671068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671068 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00671068 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671068 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671068 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671068 bytes 08213691
+ 00671068 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c93b44462e8be3efd14248ed069e4b22"></a>

### [`00671128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671128.md) → [`00671128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671128.md) FUN_00671128

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00671148",
      "incomplete_value": true,
      "site": "0067114c",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671148",
      "incomplete_value": true,
      "site": "0067114c",
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
            "const:e08:8"
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
      "0067114c",
      "DATA",
      [
        "storage",
        "00bf7e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0067114c",
      "DATA",
      [
        "storage",
        "00bf7e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671128.md#insn-00671148)
- 新版 [`00671148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671128.md#insn-00671148)

~~~diff
- 00671148 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00671148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671148 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00671148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671148 bytes 08213891
+ 00671148 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd62962fd278a0fda4f29a7077742f7"></a>

### [`00671160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671160.md) → [`00671160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671160.md) FUN_00671160

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00671164",
      "incomplete_value": false,
      "site": "00671168",
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
            "const:e58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671164",
      "incomplete_value": false,
      "site": "00671168",
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
            "const:e08:8"
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
      "00671168",
      "DATA",
      [
        "storage",
        "00bf7e08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671168",
      "DATA",
      [
        "storage",
        "00bf7e58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671160.md#insn-00671164)
- 新版 [`00671164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671160.md#insn-00671164)

~~~diff
- 00671164 ["COPY", "tmp:0:8", ["const:e08:8"]]
- 00671164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671164 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00671164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671164 bytes 08213891
+ 00671164 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eefa975c1abd929b8c08e3b374deafc7"></a>

### [`00671220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671220.md) → [`00671220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671220.md) FUN_00671220

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
      "definition_site": "0067122c",
      "incomplete_value": false,
      "site": "00671230",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067122c",
      "incomplete_value": false,
      "site": "00671230",
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
            "const:e88:8"
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
      "00671230",
      "DATA",
      [
        "storage",
        "00bf7e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671230",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067122c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671220.md#insn-0067122c)
- 新版 [`0067122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671220.md#insn-0067122c)

~~~diff
- 0067122c ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0067122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0067122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0067122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0067122c ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 0067122c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0067122c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0067122c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0067122c bytes 29213a91
+ 0067122c bytes 29613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d60e2988e1af92d15f6a64b6231d260d"></a>

### [`00671244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671244.md) → [`00671244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md) FUN_00671244

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
      "definition_site": "0067124c",
      "incomplete_value": false,
      "site": "00671250",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0067124c",
      "incomplete_value": false,
      "site": "00671250",
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
            "const:e88:8"
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
      "00671250",
      "DATA",
      [
        "storage",
        "00bf7e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671250",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0067124c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671244.md#insn-0067124c)
- 新版 [`0067124c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671244.md#insn-0067124c)

~~~diff
- 0067124c ["COPY", "tmp:0:8", ["const:e88:8"]]
- 0067124c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0067124c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0067124c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0067124c ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 0067124c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0067124c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0067124c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0067124c bytes 29213a91
+ 0067124c bytes 29613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aea109f059618bd2c1f355347f035e76"></a>

### [`0067133c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/0067133c.md) → [`0067133c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md) FUN_0067133c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.00% / 新版 95.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00671350",
      "incomplete_value": false,
      "site": "00671358",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671350",
      "incomplete_value": false,
      "site": "00671358",
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
            "const:e88:8"
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
      "00671358",
      "DATA",
      [
        "storage",
        "00bf7e88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671358",
      "DATA",
      [
        "storage",
        "00bf7ed8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/0067133c.md#insn-00671350)
- 新版 [`00671350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/0067133c.md#insn-00671350)

~~~diff
- 00671350 ["COPY", "tmp:0:8", ["const:e88:8"]]
- 00671350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671350 ["COPY", "tmp:0:8", ["const:ed8:8"]]
+ 00671350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671350 bytes 08213a91
+ 00671350 bytes 08613b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8040da25b4b1142884a386d17607dd60"></a>

### [`00671428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671428.md) → [`00671428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671428.md) FUN_00671428

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 24件 [`0065ec80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f044.md) [`0066baa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066baa4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008292ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/008292ec.md)
- 新版 呼出元 0件  · 呼出先 24件 [`0065ec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ec80.md) [`0065f044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f044.md) [`0066baa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066baa4.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008292ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00829/008292ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00671738",
      "incomplete_value": false,
      "site": "00671744",
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
            "const:b0c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671738",
      "incomplete_value": false,
      "site": "00671744",
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
            "const:a72:8"
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006717ec",
      "incomplete_value": false,
      "site": "006717f4",
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
            "const:4f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006717ec",
      "incomplete_value": false,
      "site": "006717f4",
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
            "const:457:8"
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
      "00671738",
      "PARAM",
      [
        "storage",
        "002a6a72",
        null,
        "string"
      ]
    ],
    [
      "006717ec",
      "PARAM",
      [
        "storage",
        "002a8457",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00671738",
      "PARAM",
      [
        "storage",
        "002a6b0c",
        null,
        "string"
      ]
    ],
    [
      "006717ec",
      "PARAM",
      [
        "storage",
        "002a84f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671428.md#insn-00671738) · [`006717ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671428.md#insn-006717ec)
- 新版 [`00671738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671428.md#insn-00671738) · [`006717ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671428.md#insn-006717ec)

~~~diff
- 00671738 ["COPY", "tmp:0:8", ["const:a72:8"]]
- 00671738 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00671738 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00671738 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00671738 ["COPY", "tmp:0:8", ["const:b0c:8"]]
+ 00671738 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00671738 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00671738 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00671738 bytes 42c82991
+ 00671738 bytes 42302c91
- 006717ec ["COPY", "tmp:0:8", ["const:457:8"]]
- 006717ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006717ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006717ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006717ec ["COPY", "tmp:0:8", ["const:4f1:8"]]
+ 006717ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006717ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006717ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006717ec bytes 215c1191
+ 006717ec bytes 21c41391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55bd98694b1fad9a88751ffad142c5fa"></a>

### [`00671a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a34.md) → [`00671a34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a34.md) FUN_00671a34

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
      "definition_site": "00671a40",
      "incomplete_value": false,
      "site": "00671a44",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671a40",
      "incomplete_value": false,
      "site": "00671a44",
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
            "const:f08:8"
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
      "00671a44",
      "DATA",
      [
        "storage",
        "00bf7f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671a44",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a34.md#insn-00671a40)
- 新版 [`00671a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a34.md#insn-00671a40)

~~~diff
- 00671a40 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00671a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00671a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00671a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00671a40 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00671a40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00671a40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00671a40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00671a40 bytes 29213c91
+ 00671a40 bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f28f60d7ed845e951f45667e1c56ede"></a>

### [`00671a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a58.md) → [`00671a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a58.md) FUN_00671a58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00671a60",
      "incomplete_value": true,
      "site": "00671a64",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671a60",
      "incomplete_value": true,
      "site": "00671a64",
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
            "const:f08:8"
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
      "00671a64",
      "DATA",
      [
        "storage",
        "00bf7f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671a64",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a58.md#insn-00671a60)
- 新版 [`00671a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a58.md#insn-00671a60)

~~~diff
- 00671a60 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00671a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00671a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00671a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00671a60 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00671a60 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00671a60 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00671a60 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00671a60 bytes 29213c91
+ 00671a60 bytes 29613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46969d9115b94e563c2e215185ce790d"></a>

### [`00671a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a98.md) → [`00671a98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md) FUN_00671a98

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00671ab8",
      "incomplete_value": false,
      "site": "00671ac0",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671ab8",
      "incomplete_value": false,
      "site": "00671ac0",
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
            "const:f08:8"
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
      "00671ac0",
      "DATA",
      [
        "storage",
        "00bf7f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671ac0",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671a98.md#insn-00671ab8)
- 新版 [`00671ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671a98.md#insn-00671ab8)

~~~diff
- 00671ab8 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00671ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671ab8 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00671ab8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671ab8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671ab8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671ab8 bytes 08213c91
+ 00671ab8 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abaff29eb54065c1fffa36559258eea1"></a>

### [`00671b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671b58.md) → [`00671b58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md) FUN_00671b58

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c13c.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0066c13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c13c.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00671b6c",
      "incomplete_value": true,
      "site": "00671b74",
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
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671b6c",
      "incomplete_value": true,
      "site": "00671b74",
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
            "const:f08:8"
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
      "00671b74",
      "DATA",
      [
        "storage",
        "00bf7f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00671b74",
      "DATA",
      [
        "storage",
        "00bf7f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671b58.md#insn-00671b6c)
- 新版 [`00671b6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671b58.md#insn-00671b6c)

~~~diff
- 00671b6c ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00671b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00671b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00671b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00671b6c ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00671b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00671b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00671b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00671b6c bytes 08213c91
+ 00671b6c bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e32ab52ffaf747ab028d9859db22362"></a>

### [`00671c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671c4c.md) → [`00671c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md) FUN_00671c4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 28件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 0件  · 呼出先 28件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 94.89% / 新版 94.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00672058",
      "incomplete_value": true,
      "site": "00672058",
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
      "definition_site": "00672058",
      "incomplete_value": true,
      "site": "00672058",
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
    "ordinal": 16,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00671cd4",
      "incomplete_value": true,
      "site": "00671cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00671cd4",
      "incomplete_value": true,
      "site": "00671cd8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c24000:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00671cc0",
      "incomplete_value": false,
      "site": "00671cd8",
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
      "definition_site": "00671cc0",
      "incomplete_value": false,
      "site": "00671cd8",
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
      "00671cc0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00671cc4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00671ccc",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00671cc0",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00671cc4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00671ccc",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00671cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671c4c.md#insn-00671cc0) · [`00671cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671c4c.md#insn-00671cc4) · [`00671cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00671/00671c4c.md#insn-00671cc8)
- 新版 [`00671cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md#insn-00671cc0) · [`00671cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00671/00671c4c.md#insn-00671cc4)

~~~diff
- 00671cc0 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00671cc0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00671cc0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00671cc0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00671cc0 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00671cc0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00671cc0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00671cc0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00671cc0 bytes 21203991
+ 00671cc0 bytes 21603a91
- 00671cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00671cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00671cc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00671cc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00671cc4 bytes 083d45f9
+ 00671cc4 bytes 085d45f9
- 00671cc8 ["COPY", "register:4010:8", ["const:bf7000:8"]]
- 00671cc8 bytes 222c00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a064eab78f19d96b32b314d94e6a827"></a>

### [`006723a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006723a8.md) → [`006723a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md) FUN_006723a8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "006723c8",
      "incomplete_value": false,
      "site": "006723cc",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006723c8",
      "incomplete_value": false,
      "site": "006723cc",
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
            "const:f88:8"
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
      "006723cc",
      "DATA",
      [
        "storage",
        "00bf7f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006723cc",
      "DATA",
      [
        "storage",
        "00bf7fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006723c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006723a8.md#insn-006723c8)
- 新版 [`006723c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723a8.md#insn-006723c8)

~~~diff
- 006723c8 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 006723c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006723c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006723c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006723c8 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 006723c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006723c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006723c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006723c8 bytes 08213e91
+ 006723c8 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1ef2daf17f5aaef087d9921d071ac09"></a>

### [`006723e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006723e0.md) → [`006723e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723e0.md) FUN_006723e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "006723e4",
      "incomplete_value": false,
      "site": "006723e8",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006723e4",
      "incomplete_value": false,
      "site": "006723e8",
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
            "const:f88:8"
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
      "006723e8",
      "DATA",
      [
        "storage",
        "00bf7f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006723e8",
      "DATA",
      [
        "storage",
        "00bf7fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006723e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006723e0.md#insn-006723e4)
- 新版 [`006723e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006723e0.md#insn-006723e4)

~~~diff
- 006723e4 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 006723e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006723e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006723e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006723e4 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 006723e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006723e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006723e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006723e4 bytes 08213e91
+ 006723e4 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cc218baef9ccb426a908a6cfab48f35"></a>

### [`006724c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006724c4.md) → [`006724c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006724c4.md) FUN_006724c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "006724e4",
      "incomplete_value": false,
      "site": "006724e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006724e4",
      "incomplete_value": false,
      "site": "006724e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006724e8",
      "DATA",
      [
        "storage",
        "00bf8008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006724e8",
      "DATA",
      [
        "storage",
        "00bf8058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006724e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006724c4.md#insn-006724e4)
- 新版 [`006724e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006724c4.md#insn-006724e4)

~~~diff
- 006724e4 ["COPY", "tmp:0:8", ["const:8:8"]]
- 006724e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006724e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006724e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006724e4 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 006724e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006724e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006724e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006724e4 bytes 08210091
+ 006724e4 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ef839ec8545842e30d571f711ebc1e2"></a>

### [`006724fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006724fc.md) → [`006724fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006724fc.md) FUN_006724fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00672500",
      "incomplete_value": false,
      "site": "00672504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672500",
      "incomplete_value": false,
      "site": "00672504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:8:8"
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
      "00672504",
      "DATA",
      [
        "storage",
        "00bf8008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672504",
      "DATA",
      [
        "storage",
        "00bf8058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006724fc.md#insn-00672500)
- 新版 [`00672500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006724fc.md#insn-00672500)

~~~diff
- 00672500 ["COPY", "tmp:0:8", ["const:8:8"]]
- 00672500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672500 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 00672500 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672500 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672500 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672500 bytes 08210091
+ 00672500 bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-932be5c9f08368081780413d612b3ed7"></a>

### [`006725c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006725c0.md) → [`006725c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006725c0.md) FUN_006725c0

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
      "definition_site": "006725e4",
      "incomplete_value": false,
      "site": "006725e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006725e4",
      "incomplete_value": false,
      "site": "006725e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "006725e4",
      "DATA",
      [
        "storage",
        "00bf8088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006725e4",
      "DATA",
      [
        "storage",
        "00bf80d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006725e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006725c0.md#insn-006725e0)
- 新版 [`006725e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006725c0.md#insn-006725e0)

~~~diff
- 006725e0 ["COPY", "tmp:0:8", ["const:88:8"]]
- 006725e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006725e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006725e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006725e0 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 006725e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006725e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006725e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006725e0 bytes 08210291
+ 006725e0 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-faf8274a1be1b28e357ed28d66480f6f"></a>

### [`006725f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006725f4.md) → [`006725f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006725f4.md) FUN_006725f4

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
      "definition_site": "00672600",
      "incomplete_value": false,
      "site": "00672600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672600",
      "incomplete_value": false,
      "site": "00672600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:88:8"
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
      "00672600",
      "DATA",
      [
        "storage",
        "00bf8088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672600",
      "DATA",
      [
        "storage",
        "00bf80d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006725fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006725f4.md#insn-006725fc)
- 新版 [`006725fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006725f4.md#insn-006725fc)

~~~diff
- 006725fc ["COPY", "tmp:0:8", ["const:88:8"]]
- 006725fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006725fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006725fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006725fc ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 006725fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006725fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006725fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006725fc bytes 29210291
+ 006725fc bytes 29610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4356c1ac4cb6e9ac6ec3407b7fce48e4"></a>

### [`00672688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672688.md) → [`00672688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md) FUN_00672688

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
      "definition_site": "006726ac",
      "incomplete_value": false,
      "site": "006726b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006726ac",
      "incomplete_value": false,
      "site": "006726b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "006726b0",
      "DATA",
      [
        "storage",
        "00bf8108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006726b0",
      "DATA",
      [
        "storage",
        "00bf8158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006726ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672688.md#insn-006726ac)
- 新版 [`006726ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672688.md#insn-006726ac)

~~~diff
- 006726ac ["COPY", "tmp:0:8", ["const:108:8"]]
- 006726ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006726ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006726ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006726ac ["COPY", "tmp:0:8", ["const:158:8"]]
+ 006726ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006726ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006726ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006726ac bytes 08210491
+ 006726ac bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f662234a0c36e07f1c262e3fdd67dc9d"></a>

### [`006726c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726c8.md) → [`006726c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726c8.md) FUN_006726c8

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
      "definition_site": "006726cc",
      "incomplete_value": false,
      "site": "006726d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006726cc",
      "incomplete_value": false,
      "site": "006726d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
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
      "006726d0",
      "DATA",
      [
        "storage",
        "00bf8108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006726d0",
      "DATA",
      [
        "storage",
        "00bf8158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006726cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726c8.md#insn-006726cc)
- 新版 [`006726cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726c8.md#insn-006726cc)

~~~diff
- 006726cc ["COPY", "tmp:0:8", ["const:108:8"]]
- 006726cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006726cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006726cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006726cc ["COPY", "tmp:0:8", ["const:158:8"]]
+ 006726cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006726cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006726cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006726cc bytes 08210491
+ 006726cc bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f634d5b7fe06309e06465f675de1937"></a>

### [`006726f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726f0.md) → [`006726f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md) FUN_006726f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)
- 新版 呼出元 0件  · 呼出先 16件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.96% / 新版 93.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00672754",
      "incomplete_value": true,
      "site": "00672754",
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
      "definition_site": "00672754",
      "incomplete_value": true,
      "site": "00672754",
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
      "definition_site": "0067275c",
      "incomplete_value": false,
      "site": "0067276c",
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
      "definition_site": "0067275c",
      "incomplete_value": false,
      "site": "0067276c",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00672764",
      "incomplete_value": false,
      "site": "0067276c",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672764",
      "incomplete_value": false,
      "site": "0067276c",
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
            "const:a60:8"
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
      "00672750",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0067275c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672764",
      "PARAM",
      [
        "storage",
        "00bf7a60",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00672750",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0067275c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00672764",
      "PARAM",
      [
        "storage",
        "00bf7ab0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726f0.md#insn-00672750) · [`0067275c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726f0.md#insn-0067275c) · [`00672764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006726f0.md#insn-00672764)
- 新版 [`00672750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-00672750) · [`0067275c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-0067275c) · [`00672764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006726f0.md#insn-00672764)

~~~diff
- 00672750 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:a78:8"]]
- 00672750 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00672750 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:ab8:8"]]
+ 00672750 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00672750 bytes 403f45f9
+ 00672750 bytes 405f45f9
- 0067275c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0067275c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0067275c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0067275c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0067275c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0067275c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0067275c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0067275c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0067275c bytes 21203991
+ 0067275c bytes 21603a91
- 00672764 ["COPY", "tmp:0:8", ["const:a60:8"]]
- 00672764 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00672764 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00672764 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00672764 ["COPY", "tmp:0:8", ["const:ab0:8"]]
+ 00672764 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00672764 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00672764 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00672764 bytes 42802991
+ 00672764 bytes 42c02a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d2c306aa64cd0f3097abf7e72d75a6a"></a>

### [`006729f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006729f4.md) → [`006729f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md) FUN_006729f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00672a14",
      "incomplete_value": false,
      "site": "00672a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672a14",
      "incomplete_value": false,
      "site": "00672a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00672a18",
      "DATA",
      [
        "storage",
        "00bf8188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672a18",
      "DATA",
      [
        "storage",
        "00bf81d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/006729f4.md#insn-00672a14)
- 新版 [`00672a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/006729f4.md#insn-00672a14)

~~~diff
- 00672a14 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00672a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672a14 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00672a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672a14 bytes 08210691
+ 00672a14 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e58bc9a7f606bff2910cec47e92274f"></a>

### [`00672a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672a2c.md) → [`00672a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a2c.md) FUN_00672a2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00672a30",
      "incomplete_value": false,
      "site": "00672a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672a30",
      "incomplete_value": false,
      "site": "00672a34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:188:8"
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
      "00672a34",
      "DATA",
      [
        "storage",
        "00bf8188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672a34",
      "DATA",
      [
        "storage",
        "00bf81d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672a2c.md#insn-00672a30)
- 新版 [`00672a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672a2c.md#insn-00672a30)

~~~diff
- 00672a30 ["COPY", "tmp:0:8", ["const:188:8"]]
- 00672a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672a30 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 00672a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672a30 bytes 08210691
+ 00672a30 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86006d9f2ad84b9c5e9caa0531a4df13"></a>

### [`00672b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672b78.md) → [`00672b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672b78.md) FUN_00672b78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00672b98",
      "incomplete_value": false,
      "site": "00672b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672b98",
      "incomplete_value": false,
      "site": "00672b9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00672b9c",
      "DATA",
      [
        "storage",
        "00bf8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672b9c",
      "DATA",
      [
        "storage",
        "00bf8258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672b78.md#insn-00672b98)
- 新版 [`00672b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672b78.md#insn-00672b98)

~~~diff
- 00672b98 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00672b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672b98 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00672b98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672b98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672b98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672b98 bytes 08210891
+ 00672b98 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7be17c257e8722ec0d7589a639360499"></a>

### [`00672bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672bb0.md) → [`00672bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bb0.md) FUN_00672bb0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00672bb4",
      "incomplete_value": false,
      "site": "00672bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00672bb4",
      "incomplete_value": false,
      "site": "00672bb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf8000:8"
          ],
          [
            "leaf",
            "const:208:8"
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
      "00672bb8",
      "DATA",
      [
        "storage",
        "00bf8208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00672bb8",
      "DATA",
      [
        "storage",
        "00bf8258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00672bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00672/00672bb0.md#insn-00672bb4)
- 新版 [`00672bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00672/00672bb0.md#insn-00672bb4)

~~~diff
- 00672bb4 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00672bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00672bb4 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 00672bb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00672bb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00672bb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00672bb4 bytes 08210891
+ 00672bb4 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

