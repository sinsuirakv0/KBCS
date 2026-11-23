# v15.7.3 → v15.7.4 · 最優先の変更候補 (46)

[一覧の目次](README.md)

<a id="compare-c40a41f50dd388dbe96c432cc1da66d4"></a>

### [`008aaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md) → [`008aaa18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008aa/008aaa18.md) FUN_008aaa18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 25件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 25件 [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab350",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab350",
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
                "const:c25000:8"
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
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008ab354",
      "incomplete_value": false,
      "site": "008ab354",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ab354",
      "incomplete_value": false,
      "site": "008ab354",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab354",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008ab350",
      "incomplete_value": false,
      "site": "008ab354",
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
                "const:c25000:8"
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
      "008aaa58",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008aaa64",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008aaa78",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008aaa58",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008aaa64",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "008aaa78",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008aaa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md#insn-008aaa44) · [`008aaa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md#insn-008aaa64) · [`008aaa78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008aa/008aaa18.md#insn-008aaa78)
- 新版 `008aaa44`（命令位置の公開資料なし） · `008aaa64`（命令位置の公開資料なし） · `008aaa78`（命令位置の公開資料なし）

~~~diff
- 008aaa44 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008aaa44 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008aaa44 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008aaa44 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008aaa44 bytes f7e20091
+ 008aaa44 bytes f7e20191
- 008aaa64 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:30:8"]]
- 008aaa64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008aaa64 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:70:8"]]
+ 008aaa64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008aaa64 bytes 001b40f9
+ 008aaa64 bytes 003b40f9
- 008aaa78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008aaa78 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008aaa78 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008aaa78 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008aaa78 bytes 003d45f9
+ 008aaa78 bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75e12c190faa310240453e1fa09fb01d"></a>

### [`008ac9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008ac9ec.md) → [`008ac9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac9ec.md) FUN_008ac9ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008ac5b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008ac5b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`008ac5b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008ac5b4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008ac9f8",
      "incomplete_value": false,
      "site": "008ac9fc",
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
      "definition_site": "008ac9f8",
      "incomplete_value": false,
      "site": "008ac9fc",
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
      "008ac9f8",
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
      "008ac9f8",
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

- 旧版 [`008ac9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008ac9ec.md#insn-008ac9f8)
- 新版 `008ac9f8`（命令位置の公開資料なし）

~~~diff
- 008ac9f8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008ac9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008ac9f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008ac9f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008ac9f8 bytes 000c0c91
+ 008ac9f8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35613dbde947945d87e967fe3cdd4cde"></a>

### [`008acbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md) → [`008acbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ac/008acbf0.md) FUN_008acbf0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a9/008a9c80.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00831/00831724.md)
- 新版 呼出元 1件 [`008a9c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a9/008a9c80.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) [`00831724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00831/00831724.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.96% / 新版 88.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_destination` 7件, `store_value` 17件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008acc28",
      "incomplete_value": false,
      "site": "008acc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc28",
      "incomplete_value": false,
      "site": "008acc34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:e98:8"
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
      "definition_site": "008acc70",
      "incomplete_value": true,
      "site": "008acc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc70",
      "incomplete_value": true,
      "site": "008acc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:895:8"
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
      "definition_site": "008acc88",
      "incomplete_value": true,
      "site": "008acc88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008acc88",
      "incomplete_value": true,
      "site": "008acc88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
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
      "008acc34",
      "DATA",
      [
        "storage",
        "00c06e98",
        null,
        "pointer"
      ]
    ],
    [
      "008acc40",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008acc60",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008acc34",
      "DATA",
      [
        "storage",
        "00c06ee8",
        null,
        "pointer"
      ]
    ],
    [
      "008acc40",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008acc60",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008acc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md#insn-008acc28) · [`008acc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ac/008acbf0.md#insn-008acc2c)
- 新版 `008acc28`（命令位置の公開資料なし） · `008acc2c`（命令位置の公開資料なし）

~~~diff
- 008acc28 ["COPY", "tmp:0:8", ["const:e98:8"]]
- 008acc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008acc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008acc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["COPY", "tmp:0:8", ["const:ee8:8"]]
+ 008acc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008acc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008acc28 bytes 08613a91
+ 008acc28 bytes 08a13b91
- 008acc2c ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008acc2c bytes d81b00b0
+ 008acc2c ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 008acc2c bytes d81b00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdf887044dca5893f373e07a4b297952"></a>

### [`008ad8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad8d4.md) → [`008ad8d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad8d4.md) FUN_008ad8d4

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
      "definition_site": "008ad8ec",
      "incomplete_value": false,
      "site": "008ad8f0",
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
      "definition_site": "008ad8ec",
      "incomplete_value": false,
      "site": "008ad8f0",
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
      "definition_site": "008ad928",
      "incomplete_value": false,
      "site": "008ad92c",
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
      "definition_site": "008ad928",
      "incomplete_value": false,
      "site": "008ad92c",
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
      "008ad8f0",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "008ad92c",
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
      "008ad8f0",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "008ad92c",
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

- 旧版 [`008ad8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad8d4.md#insn-008ad8ec) · [`008ad928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad8d4.md#insn-008ad928)
- 新版 `008ad8ec`（命令位置の公開資料なし） · `008ad928`（命令位置の公開資料なし）

~~~diff
- 008ad8ec ["COPY", "tmp:0:8", ["const:db8:8"]]
- 008ad8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 008ad8ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad8ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad8ec bytes 08e13691
+ 008ad8ec bytes 08213891
- 008ad928 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008ad928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ad928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ad928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008ad928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ad928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ad928 bytes 08610a91
+ 008ad928 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3aa151bfdcd25e86a74d8bccc6cedda"></a>

### [`008ad974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad974.md) → [`008ad974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008ad974.md) _INIT_168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008ad9b0",
      "incomplete_value": true,
      "site": "008ad9cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad9b0",
      "incomplete_value": true,
      "site": "008ad9cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "008ad9d4",
      "incomplete_value": true,
      "site": "008ad9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad9d4",
      "incomplete_value": true,
      "site": "008ad9f0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "008ad9f4",
      "incomplete_value": true,
      "site": "008ada10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ad9f4",
      "incomplete_value": true,
      "site": "008ada10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "008ad9b0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008ad9d4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008ad9f4",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ad9b0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008ad9d4",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008ad9f4",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ad9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad974.md#insn-008ad9a0) · [`008ad9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008ad974.md#insn-008ad9a8)
- 新版 `008ad9a0`（命令位置の公開資料なし） · `008ad9a8`（命令位置の公開資料なし）

~~~diff
- 008ad9a0 ["COPY", "tmp:0:8", ["const:718:8"]]
- 008ad9a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 008ad9a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008ad9a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008ad9a0 bytes 73621c91
+ 008ad9a0 bytes 73621d91
- 008ad9a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008ad9a8 bytes c9cfffd0
+ 008ad9a8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008ad9a8 bytes c9cfffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0176a3df1a5e5ecd3cdc143b8383593"></a>

### [`008add04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008add04.md) → [`008add04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ad/008add04.md) FUN_008add04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 89.76% / 新版 89.76%

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
      "definition_site": "008add50",
      "incomplete_value": false,
      "site": "008add58",
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
      "definition_site": "008add50",
      "incomplete_value": false,
      "site": "008add58",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008add7c",
      "incomplete_value": true,
      "site": "008add8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b35:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008add7c",
      "incomplete_value": true,
      "site": "008add8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:aaa:8"
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
      "definition_site": "008add90",
      "incomplete_value": true,
      "site": "008add90",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008add90",
      "incomplete_value": true,
      "site": "008add90",
      "value": [
        "LOAD",
        "8",
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
      "008add58",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008add7c",
      "READ",
      [
        "storage",
        "002a3aaa",
        null,
        "string"
      ]
    ],
    [
      "008add80",
      "READ",
      [
        "storage",
        "002a3ab9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008add58",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008add7c",
      "READ",
      [
        "storage",
        "002a3b35",
        null,
        "string"
      ]
    ],
    [
      "008add80",
      "READ",
      [
        "storage",
        "002a3b44",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008add50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008add04.md#insn-008add50) · [`008add74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008add04.md#insn-008add74) · [`008add78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ad/008add04.md#insn-008add78)
- 新版 `008add50`（命令位置の公開資料なし） · `008add74`（命令位置の公開資料なし）

~~~diff
- 008add50 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 008add50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008add50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 008add50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008add50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008add50 bytes 08a13491
+ 008add50 bytes 08e13591
- 008add74 ["COPY", "tmp:0:8", ["const:aaa:8"]]
- 008add74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008add74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008add74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["COPY", "tmp:0:8", ["const:b35:8"]]
+ 008add74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008add74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008add74 bytes 08a92a91
+ 008add74 bytes 08d52c91
- 008add78 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 008add78 bytes 09d0fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8a188c5a0c5f96cbaff1aeb7b41a7cc"></a>

### [`008ae87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md) → [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) FUN_008ae87c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) · 呼出先 23件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.70% / 新版 93.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008ae8c0",
      "incomplete_value": false,
      "site": "008ae8c8",
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
      "definition_site": "008ae8c0",
      "incomplete_value": false,
      "site": "008ae8c8",
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
      "definition_site": "008ae8e0",
      "incomplete_value": true,
      "site": "008ae8ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b1b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ae8e0",
      "incomplete_value": true,
      "site": "008ae8ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a81:8"
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
      "definition_site": "008aea0c",
      "incomplete_value": true,
      "site": "008aea0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b3d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008aea0c",
      "incomplete_value": true,
      "site": "008aea0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b3f:8"
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
      "008ae8c8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008ae8e0",
      "READ",
      [
        "storage",
        "002a7a81",
        null,
        "string"
      ]
    ],
    [
      "008ae9fc",
      "READ",
      [
        "storage",
        "0029bb3f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008ae8c8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008ae8e0",
      "READ",
      [
        "storage",
        "002a7b1b",
        null,
        "string"
      ]
    ],
    [
      "008ae9fc",
      "READ",
      [
        "storage",
        "0029bb3d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ae8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md#insn-008ae8c0) · [`008ae8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md#insn-008ae8d8) · [`008ae9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md#insn-008ae9f8)
- 新版 `008ae8c0`（命令位置の公開資料なし） · `008ae8d8`（命令位置の公開資料なし） · `008ae9f8`（命令位置の公開資料なし）

~~~diff
- 008ae8c0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 008ae8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 008ae8c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008ae8c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008ae8c0 bytes 08a13491
+ 008ae8c0 bytes 08e13591
- 008ae8d8 ["COPY", "tmp:0:8", ["const:a81:8"]]
- 008ae8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["COPY", "tmp:0:8", ["const:b1b:8"]]
+ 008ae8d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae8d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ae8d8 bytes 29052a91
+ 008ae8d8 bytes 296d2c91
- 008ae9f8 ["COPY", "tmp:0:8", ["const:b3f:8"]]
- 008ae9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["COPY", "tmp:0:8", ["const:b3d:8"]]
+ 008ae9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008ae9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008ae9f8 bytes 29fd2c91
+ 008ae9f8 bytes 29f52c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deadc222e09c4ab5febbea9e93ac9243"></a>

### [`008af36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af36c.md) → [`008af36c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af36c.md) FUN_008af36c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008b266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d4c.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)
- 新版 呼出元 1件 [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) · 呼出先 22件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00883d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d4c.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.46% / 新版 96.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008af634",
      "incomplete_value": false,
      "site": "008af634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008af634",
      "incomplete_value": false,
      "site": "008af634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008af78c",
      "incomplete_value": false,
      "site": "008af78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008af78c",
      "incomplete_value": false,
      "site": "008af78c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008af97c",
      "incomplete_value": true,
      "site": "008af97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "008af97c",
      "incomplete_value": true,
      "site": "008af97c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008af3b0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008af3bc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008af3c4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008af3b0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008af3bc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008af3c4",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008af3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af36c.md#insn-008af3b0) · [`008af3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af36c.md#insn-008af3bc) · [`008af3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af36c.md#insn-008af3c4)
- 新版 `008af3b0`（命令位置の公開資料なし） · `008af3bc`（命令位置の公開資料なし） · `008af3c4`（命令位置の公開資料なし）

~~~diff
- 008af3b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008af3b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008af3b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008af3b0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008af3b0 bytes 003d45f9
+ 008af3b0 bytes 005d45f9
- 008af3bc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008af3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008af3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008af3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008af3bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008af3bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008af3bc bytes 21203991
+ 008af3bc bytes 21603a91
- 008af3c4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008af3c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008af3c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008af3c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008af3c4 bytes 42600a91
+ 008af3c4 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e25d29b4c467915531faa3eb108111ec"></a>

### [`008afd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008afd10.md) → [`008afd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008afd10.md) FUN_008afd10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00447378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447378.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 21件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00447378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447378.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

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
      "definition_site": "008afd5c",
      "incomplete_value": true,
      "site": "008afd5c",
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
      "definition_site": "008afd5c",
      "incomplete_value": true,
      "site": "008afd5c",
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
      "definition_site": "008afd64",
      "incomplete_value": false,
      "site": "008afd74",
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
      "definition_site": "008afd64",
      "incomplete_value": false,
      "site": "008afd74",
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
      "definition_site": "008afd6c",
      "incomplete_value": false,
      "site": "008afd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008afd6c",
      "incomplete_value": false,
      "site": "008afd74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008afd58",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008afd64",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008afd6c",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008afd58",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008afd64",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008afd6c",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008afd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008afd10.md#insn-008afd58) · [`008afd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008afd10.md#insn-008afd64) · [`008afd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008afd10.md#insn-008afd6c)
- 新版 `008afd58`（命令位置の公開資料なし） · `008afd64`（命令位置の公開資料なし） · `008afd6c`（命令位置の公開資料なし）

~~~diff
- 008afd58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008afd58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008afd58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008afd58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008afd58 bytes 003d45f9
+ 008afd58 bytes 005d45f9
- 008afd64 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008afd64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008afd64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008afd64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008afd64 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008afd64 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008afd64 bytes 21203991
+ 008afd64 bytes 21603a91
- 008afd6c ["COPY", "tmp:0:8", ["const:298:8"]]
- 008afd6c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008afd6c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008afd6c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008afd6c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008afd6c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008afd6c bytes 42600a91
+ 008afd6c bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3393ae3f3dea4f5d3236c708dfcc18a9"></a>

### [`008b0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md) → [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) FUN_008b0960

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b5c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5c4c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`008b5c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5c4c.md) · 呼出先 26件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b0ae8",
      "incomplete_value": true,
      "site": "008b0afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:74f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b0ae8",
      "incomplete_value": true,
      "site": "008b0afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6c4:8"
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
      "definition_site": "008b0b00",
      "incomplete_value": true,
      "site": "008b0b00",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b0b00",
      "incomplete_value": true,
      "site": "008b0b00",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 33,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b0f4c",
      "incomplete_value": false,
      "site": "008b0f4c",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008b0f4c",
      "incomplete_value": false,
      "site": "008b0f4c",
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
                "const:c25000:8"
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
    "ordinal": 53,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b0ad4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b0ae8",
      "READ",
      [
        "storage",
        "0029e6c4",
        null,
        "string"
      ]
    ],
    [
      "008b0aec",
      "READ",
      [
        "storage",
        "0029e6d1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b0ad4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008b0ae8",
      "READ",
      [
        "storage",
        "0029e74f",
        null,
        "string"
      ]
    ],
    [
      "008b0aec",
      "READ",
      [
        "storage",
        "0029e75c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b0ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md#insn-008b0ad0) · [`008b0ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md#insn-008b0ae0) · [`008b0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md#insn-008b0b34)
- 新版 `008b0ad0`（命令位置の公開資料なし） · `008b0ae0`（命令位置の公開資料なし） · `008b0b34`（命令位置の公開資料なし）

~~~diff
- 008b0ad0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008b0ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b0ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b0ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b0ad0 bytes 08e10091
+ 008b0ad0 bytes 08e10191
- 008b0ae0 ["COPY", "tmp:0:8", ["const:6c4:8"]]
- 008b0ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["COPY", "tmp:0:8", ["const:74f:8"]]
+ 008b0ae0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b0ae0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b0ae0 bytes 29111b91
+ 008b0ae0 bytes 293d1d91
- 008b0b34 ["COPY", "tmp:0:8", ["const:0:8"]]
- 008b0b34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b0b34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b0b34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b0b34 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 008b0b34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b0b34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b0b34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b0b34 bytes 00000091
+ 008b0b34 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91fd0a85613aaac06366c9b142e81a6d"></a>

### [`008b11a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b11a4.md) → [`008b11a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b11a4.md) FUN_008b11a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008b627c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b627c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`006b5748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b5/006b5748.md)
- 新版 呼出元 1件 [`008b627c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b627c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`006b5748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b5/006b5748.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b1418",
      "incomplete_value": true,
      "site": "008b1434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1418",
      "incomplete_value": true,
      "site": "008b1434",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a92:8"
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
      "definition_site": "008b1534",
      "incomplete_value": true,
      "site": "008b1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1534",
      "incomplete_value": true,
      "site": "008b1550",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:a92:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 55,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b18c4",
      "incomplete_value": true,
      "site": "008b18c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dda:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b18c4",
      "incomplete_value": true,
      "site": "008b18c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e67:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 85,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b1418",
      "READ",
      [
        "storage",
        "002a7a92",
        null,
        "string"
      ]
    ],
    [
      "008b1534",
      "READ",
      [
        "storage",
        "002a7a92",
        null,
        "string"
      ]
    ],
    [
      "008b18b0",
      "READ",
      [
        "storage",
        "00292e67",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b1418",
      "READ",
      [
        "storage",
        "002a7b2c",
        null,
        "string"
      ]
    ],
    [
      "008b1534",
      "READ",
      [
        "storage",
        "002a7b2c",
        null,
        "string"
      ]
    ],
    [
      "008b18b0",
      "READ",
      [
        "storage",
        "00292dda",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b1414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b11a4.md#insn-008b1414) · [`008b1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b11a4.md#insn-008b1530) · [`008b18a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b11a4.md#insn-008b18a8)
- 新版 `008b1414`（命令位置の公開資料なし） · `008b1530`（命令位置の公開資料なし） · `008b18a8`（命令位置の公開資料なし）

~~~diff
- 008b1414 ["COPY", "tmp:0:8", ["const:a92:8"]]
- 008b1414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["COPY", "tmp:0:8", ["const:b2c:8"]]
+ 008b1414 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1414 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1414 bytes 08492a91
+ 008b1414 bytes 08b12c91
- 008b1530 ["COPY", "tmp:0:8", ["const:a92:8"]]
- 008b1530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["COPY", "tmp:0:8", ["const:b2c:8"]]
+ 008b1530 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1530 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1530 bytes 08492a91
+ 008b1530 bytes 08b12c91
- 008b18a8 ["COPY", "tmp:0:8", ["const:e67:8"]]
- 008b18a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b18a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b18a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b18a8 ["COPY", "tmp:0:8", ["const:dda:8"]]
+ 008b18a8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b18a8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b18a8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b18a8 bytes 299d3991
+ 008b18a8 bytes 29693791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52a2dd489bf141a409f0cf0209108e94"></a>

### [`008b1f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md) → [`008b1f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b1/008b1f3c.md) FUN_008b1f3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c620.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`0068c620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c620.md) · 呼出先 24件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.01% / 新版 93.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b1fe8",
      "incomplete_value": true,
      "site": "008b1fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:1ec:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b1fe8",
      "incomplete_value": true,
      "site": "008b1fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:298000:8"
              ],
              [
                "leaf",
                "const:279:8"
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
      "definition_site": "008b1fec",
      "incomplete_value": true,
      "site": "008b1fec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b1fec",
      "incomplete_value": true,
      "site": "008b1fec",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2010",
      "incomplete_value": true,
      "site": "008b2024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ce4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2010",
      "incomplete_value": true,
      "site": "008b2024",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c59:8"
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
      "008b1fc4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b1fd8",
      "READ",
      [
        "storage",
        "00298279",
        null,
        "string"
      ]
    ],
    [
      "008b1fdc",
      "READ",
      [
        "storage",
        "0029827f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b1fc4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008b1fd8",
      "READ",
      [
        "storage",
        "002981ec",
        null,
        "string"
      ]
    ],
    [
      "008b1fdc",
      "READ",
      [
        "storage",
        "002981f2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b1fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md#insn-008b1fc0) · [`008b1fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b1/008b1f3c.md#insn-008b1fcc)
- 新版 `008b1fc0`（命令位置の公開資料なし） · `008b1fcc`（命令位置の公開資料なし）

~~~diff
- 008b1fc0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008b1fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b1fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b1fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b1fc0 bytes 08e10091
+ 008b1fc0 bytes 08e10191
- 008b1fcc ["COPY", "register:4048:8", ["const:298000:8"]]
- 008b1fcc bytes 29cffff0
+ 008b1fcc ["COPY", "register:4048:8", ["const:298000:8"]]
+ 008b1fcc bytes 29cffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4867ea98229e3c369245bd23ad8017ba"></a>

### [`008b266c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md) → [`008b266c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b2/008b266c.md) FUN_008b266c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068c/0068c7d4.md) · 呼出先 42件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0042bab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042b/0042bab0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md)
- 新版 呼出元 1件 [`0068c7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068c/0068c7d4.md) · 呼出先 42件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0042bab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042b/0042bab0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`0044aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044aa9c.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2820",
      "incomplete_value": false,
      "site": "008b2820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2820",
      "incomplete_value": false,
      "site": "008b2820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "definition_site": "008b2924",
      "incomplete_value": false,
      "site": "008b2924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2924",
      "incomplete_value": false,
      "site": "008b2924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b2a74",
      "incomplete_value": false,
      "site": "008b2a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b2a74",
      "incomplete_value": false,
      "site": "008b2a74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "008b2820",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b2924",
      "DATA",
      [
        "storage",
        "00c07538",
        null,
        "undefined *"
      ]
    ],
    [
      "008b2a74",
      "DATA",
      [
        "storage",
        "00c07438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b2820",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ],
    [
      "008b2924",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ],
    [
      "008b2a74",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b281c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md#insn-008b281c) · [`008b2918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md#insn-008b2918) · [`008b291c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b2/008b266c.md#insn-008b291c)
- 新版 `008b281c`（命令位置の公開資料なし） · `008b2918`（命令位置の公開資料なし）

~~~diff
- 008b281c ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 008b281c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b281c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b281c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008b281c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b281c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b281c bytes 08e10e91
+ 008b281c bytes 08211091
- 008b2918 ["COPY", "tmp:0:8", ["const:538:8"]]
- 008b2918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b2918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b2918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b2918 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 008b2918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b2918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b2918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b2918 bytes 08e11491
+ 008b2918 bytes 08211691
- 008b291c ["COPY", "tmp:0:8", ["const:c0:8"]]
- 008b291c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 008b291c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 008b291c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 008b291c bytes f6030391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2aa41bd9cd13bc9ec5bc8605213f1464"></a>

### [`008b3390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3390.md) → [`008b3390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3390.md) FUN_008b3390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00446074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446074.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.58% / 新版 98.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b33d4",
      "incomplete_value": true,
      "site": "008b33d4",
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
      "definition_site": "008b33d4",
      "incomplete_value": true,
      "site": "008b33d4",
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
      "definition_site": "008b33dc",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "definition_site": "008b33dc",
      "incomplete_value": false,
      "site": "008b33ec",
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
      "definition_site": "008b33e4",
      "incomplete_value": false,
      "site": "008b33ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b33e4",
      "incomplete_value": false,
      "site": "008b33ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008b33d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b33dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b33e4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008b33d0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b33dc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b33e4",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b33d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3390.md#insn-008b33d0) · [`008b33dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3390.md#insn-008b33dc) · [`008b33e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3390.md#insn-008b33e4)
- 新版 `008b33d0`（命令位置の公開資料なし） · `008b33dc`（命令位置の公開資料なし） · `008b33e4`（命令位置の公開資料なし）

~~~diff
- 008b33d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008b33d0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b33d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008b33d0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008b33d0 bytes 003d45f9
+ 008b33d0 bytes 005d45f9
- 008b33dc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008b33dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b33dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b33dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008b33dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b33dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b33dc bytes 21203991
+ 008b33dc bytes 21603a91
- 008b33e4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008b33e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008b33e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b33e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b33e4 bytes 42600a91
+ 008b33e4 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c94607079868a604c4034d2e16c9152"></a>

### [`008b3a28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3a28.md) → [`008b3a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b3/008b3a28.md) FUN_008b3a28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d0f8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00447/00447a10.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md)
- 新版 呼出元 1件 [`0068d0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0068d/0068d0f8.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00447a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00447/00447a10.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.61% / 新版 99.61%

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
      "definition_site": "008b4128",
      "incomplete_value": true,
      "site": "008b4128",
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
      "definition_site": "008b4128",
      "incomplete_value": true,
      "site": "008b4128",
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
    "ordinal": 68,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b4130",
      "incomplete_value": false,
      "site": "008b4140",
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
      "definition_site": "008b4130",
      "incomplete_value": false,
      "site": "008b4140",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008b4138",
      "incomplete_value": false,
      "site": "008b4140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b4138",
      "incomplete_value": false,
      "site": "008b4140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b4124",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b4130",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b4138",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008b4124",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b4130",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b4138",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b4124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3a28.md#insn-008b4124) · [`008b4130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3a28.md#insn-008b4130) · [`008b4138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b3/008b3a28.md#insn-008b4138)
- 新版 `008b4124`（命令位置の公開資料なし） · `008b4130`（命令位置の公開資料なし） · `008b4138`（命令位置の公開資料なし）

~~~diff
- 008b4124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008b4124 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b4124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008b4124 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008b4124 bytes 003d45f9
+ 008b4124 bytes 005d45f9
- 008b4130 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008b4130 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b4130 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b4130 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008b4130 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b4130 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b4130 bytes 21203991
+ 008b4130 bytes 21603a91
- 008b4138 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008b4138 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b4138 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b4138 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008b4138 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b4138 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b4138 bytes 42600a91
+ 008b4138 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bb57522bf07ce45d05b5f72501fe29d"></a>

### [`008b4224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4224.md) → [`008b4224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4224.md) FUN_008b4224

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008af0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008af/008af0b4.md) [`008b0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0960.md) [`008b4610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4610.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008af0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008af/008af0b4.md) [`008b0960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0960.md) [`008b4610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4610.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b4230",
      "incomplete_value": false,
      "site": "008b4234",
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
      "definition_site": "008b4230",
      "incomplete_value": false,
      "site": "008b4234",
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
      "008b4230",
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
      "008b4230",
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

- 旧版 [`008b4230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4224.md#insn-008b4230)
- 新版 `008b4230`（命令位置の公開資料なし）

~~~diff
- 008b4230 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b4230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b4230 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4230 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4230 bytes 000c0c91
+ 008b4230 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12d1a5ee03ea4538489c1c86f5677d86"></a>

### [`008b450c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b450c.md) → [`008b450c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b450c.md) FUN_008b450c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b4328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4328.md) [`008b4e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4e00.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b4328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4328.md) [`008b4e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4e00.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b4518",
      "incomplete_value": false,
      "site": "008b451c",
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
      "definition_site": "008b4518",
      "incomplete_value": false,
      "site": "008b451c",
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
      "008b4518",
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
      "008b4518",
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

- 旧版 [`008b4518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b450c.md#insn-008b4518)
- 新版 `008b4518`（命令位置の公開資料なし）

~~~diff
- 008b4518 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b4518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b4518 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4518 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4518 bytes 000c0c91
+ 008b4518 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f074c5782f43b961d01e0ff65cbdd6f1"></a>

### [`008b45fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b45fc.md) → [`008b45fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b45fc.md) FUN_008b45fc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0550.md) [`008b4c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4c78.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) [`008b4c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c78.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b4608",
      "incomplete_value": false,
      "site": "008b460c",
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
      "definition_site": "008b4608",
      "incomplete_value": false,
      "site": "008b460c",
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
      "008b4608",
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
      "008b4608",
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

- 旧版 [`008b4608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b45fc.md#insn-008b4608)
- 新版 `008b4608`（命令位置の公開資料なし）

~~~diff
- 008b4608 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b4608 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4608 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4608 bytes 000c0c91
+ 008b4608 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36672ba0010c1fb88566bd62ceaf3c35"></a>

### [`008b47cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b47cc.md) → [`008b47cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47cc.md) FUN_008b47cc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008ae87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ae/008ae87c.md) [`008b0550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b0/008b0550.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008ae87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ae/008ae87c.md) [`008b0550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b0/008b0550.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b47d8",
      "incomplete_value": false,
      "site": "008b47dc",
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
      "definition_site": "008b47d8",
      "incomplete_value": false,
      "site": "008b47dc",
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
      "008b47d8",
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
      "008b47d8",
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

- 旧版 [`008b47d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b47cc.md#insn-008b47d8)
- 新版 `008b47d8`（命令位置の公開資料なし）

~~~diff
- 008b47d8 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b47d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b47d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b47d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b47d8 bytes 000c0c91
+ 008b47d8 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e806ddcd02e798eebc4637cb7723981e"></a>

### [`008b49c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b49c4.md) → [`008b49c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b49c4.md) FUN_008b49c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008b47e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b47e0.md) [`008b4f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4f48.md) [`008b6558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6558.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008b47e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b47e0.md) [`008b4f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4f48.md) [`008b6558`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6558.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b49d0",
      "incomplete_value": false,
      "site": "008b49d4",
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
      "definition_site": "008b49d0",
      "incomplete_value": false,
      "site": "008b49d4",
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
      "008b49d0",
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
      "008b49d0",
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

- 旧版 [`008b49d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b49c4.md#insn-008b49d0)
- 新版 `008b49d0`（命令位置の公開資料なし）

~~~diff
- 008b49d0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b49d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b49d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b49d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b49d0 bytes 000c0c91
+ 008b49d0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11b20a74dfaf53aa6dfbaf0a2d84626"></a>

### [`008b4c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4c10.md) → [`008b4c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4c10.md) FUN_008b4c10

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`008b4a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4a2c.md) [`008b50f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b50f8.md) [`008b635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b635c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`008b4a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b4/008b4a2c.md) [`008b50f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b50f8.md) [`008b635c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b635c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008b4c1c",
      "incomplete_value": false,
      "site": "008b4c20",
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
      "definition_site": "008b4c1c",
      "incomplete_value": false,
      "site": "008b4c20",
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
      "008b4c1c",
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
      "008b4c1c",
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

- 旧版 [`008b4c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b4/008b4c10.md#insn-008b4c1c)
- 新版 `008b4c1c`（命令位置の公開資料なし）

~~~diff
- 008b4c1c ["COPY", "tmp:0:8", ["const:303:8"]]
- 008b4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008b4c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b4c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b4c1c bytes 000c0c91
+ 008b4c1c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46f65fe8112b5e1b1f3bb34cae950888"></a>

### [`008b52ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52ac.md) → [`008b52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b52ac.md) FUN_008b52ac

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
      "definition_site": "008b52d0",
      "incomplete_value": false,
      "site": "008b52d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b52d0",
      "incomplete_value": false,
      "site": "008b52d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b52d0",
      "DATA",
      [
        "storage",
        "00c06eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b52d0",
      "DATA",
      [
        "storage",
        "00c06f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b52cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52ac.md#insn-008b52cc)
- 新版 `008b52cc`（命令位置の公開資料なし）

~~~diff
- 008b52cc ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 008b52cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b52cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b52cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 008b52cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b52cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b52cc bytes 08e13a91
+ 008b52cc bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0b89ff2fd76295d43d2b11b5af9be88"></a>

### [`008b52e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52e0.md) → [`008b52e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b52e0.md) FUN_008b52e0

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
      "definition_site": "008b52ec",
      "incomplete_value": false,
      "site": "008b52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b52ec",
      "incomplete_value": false,
      "site": "008b52ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
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
      "008b52ec",
      "DATA",
      [
        "storage",
        "00c06eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b52ec",
      "DATA",
      [
        "storage",
        "00c06f08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b52e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b52e0.md#insn-008b52e8)
- 新版 `008b52e8`（命令位置の公開資料なし）

~~~diff
- 008b52e8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 008b52e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 008b52e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b52e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b52e8 bytes 29e13a91
+ 008b52e8 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e51d4e89db8557487bf72acf9afc11ef"></a>

### [`008b542c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b542c.md) → [`008b542c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b542c.md) FUN_008b542c

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
      "definition_site": "008b5450",
      "incomplete_value": false,
      "site": "008b5450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5450",
      "incomplete_value": false,
      "site": "008b5450",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "008b5450",
      "DATA",
      [
        "storage",
        "00c06f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5450",
      "DATA",
      [
        "storage",
        "00c06f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b542c.md#insn-008b544c)
- 新版 `008b544c`（命令位置の公開資料なし）

~~~diff
- 008b544c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008b544c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b544c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b544c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 008b544c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b544c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b544c bytes 08e13c91
+ 008b544c bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe5e98386305f17e66026c3dc42fad2"></a>

### [`008b5460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5460.md) → [`008b5460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5460.md) FUN_008b5460

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
      "definition_site": "008b546c",
      "incomplete_value": false,
      "site": "008b546c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b546c",
      "incomplete_value": false,
      "site": "008b546c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:f38:8"
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
      "008b546c",
      "DATA",
      [
        "storage",
        "00c06f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b546c",
      "DATA",
      [
        "storage",
        "00c06f88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5460.md#insn-008b5468)
- 新版 `008b5468`（命令位置の公開資料なし）

~~~diff
- 008b5468 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 008b5468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 008b5468 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5468 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5468 bytes 29e13c91
+ 008b5468 bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-447b62fbf26e4a5aded848eb95a47761"></a>

### [`008b5528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5528.md) → [`008b5528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5528.md) FUN_008b5528

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
      "definition_site": "008b5548",
      "incomplete_value": false,
      "site": "008b554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5548",
      "incomplete_value": false,
      "site": "008b554c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "008b554c",
      "DATA",
      [
        "storage",
        "00c06fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b554c",
      "DATA",
      [
        "storage",
        "00c07008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5528.md#insn-008b5544) · [`008b5548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5528.md#insn-008b5548)
- 新版 `008b5544`（命令位置の公開資料なし） · `008b5548`（命令位置の公開資料なし）

~~~diff
- 008b5544 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008b5544 ["COPY", "register:4040:8", ["const:c07000:8"]]
- 008b5544 bytes 881a00b0
+ 008b5544 bytes 881a00d0
- 008b5548 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 008b5548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 008b5548 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5548 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5548 bytes 08e13e91
+ 008b5548 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-390b415a9baa87267385f9d5624a8fca"></a>

### [`008b5560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5560.md) → [`008b5560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5560.md) FUN_008b5560

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
      "definition_site": "008b5564",
      "incomplete_value": false,
      "site": "008b5568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5564",
      "incomplete_value": false,
      "site": "008b5568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c06000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
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
      "008b5568",
      "DATA",
      [
        "storage",
        "00c06fb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5568",
      "DATA",
      [
        "storage",
        "00c07008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5560.md#insn-008b5560) · [`008b5564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5560.md#insn-008b5564)
- 新版 `008b5560`（命令位置の公開資料なし） · `008b5564`（命令位置の公開資料なし）

~~~diff
- 008b5560 ["COPY", "register:4040:8", ["const:c06000:8"]]
+ 008b5560 ["COPY", "register:4040:8", ["const:c07000:8"]]
- 008b5560 bytes 881a00b0
+ 008b5560 bytes 881a00d0
- 008b5564 ["COPY", "tmp:0:8", ["const:fb8:8"]]
- 008b5564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 008b5564 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5564 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5564 bytes 08e13e91
+ 008b5564 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97335fc51a76ea764b9d303d514847e1"></a>

### [`008b5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5580.md) → [`008b5580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5580.md) FUN_008b5580

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 17件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.83% / 新版 93.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b56b0",
      "incomplete_value": true,
      "site": "008b56b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b56b0",
      "incomplete_value": true,
      "site": "008b56b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:aa6:8"
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
      "definition_site": "008b5734",
      "incomplete_value": true,
      "site": "008b5734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dea:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5734",
      "incomplete_value": true,
      "site": "008b5734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e77:8"
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
      "definition_site": "008b5758",
      "incomplete_value": false,
      "site": "008b5758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5758",
      "incomplete_value": false,
      "site": "008b5758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:28:8"
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
      "008b5698",
      "READ",
      [
        "storage",
        "002a7aa6",
        null,
        "string"
      ]
    ],
    [
      "008b56d4",
      "DATA",
      [
        "storage",
        "00c070a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b571c",
      "READ",
      [
        "storage",
        "00292e77",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b5698",
      "READ",
      [
        "storage",
        "002a7b40",
        null,
        "string"
      ]
    ],
    [
      "008b56d4",
      "DATA",
      [
        "storage",
        "00c070f8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b571c",
      "READ",
      [
        "storage",
        "00292dea",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5580.md#insn-008b5690) · [`008b56cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5580.md#insn-008b56cc) · [`008b5714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5580.md#insn-008b5714)
- 新版 `008b5690`（命令位置の公開資料なし） · `008b56cc`（命令位置の公開資料なし） · `008b5714`（命令位置の公開資料なし）

~~~diff
- 008b5690 ["COPY", "tmp:0:8", ["const:aa6:8"]]
- 008b5690 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5690 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5690 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["COPY", "tmp:0:8", ["const:b40:8"]]
+ 008b5690 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5690 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5690 bytes 29992a91
+ 008b5690 bytes 29012d91
- 008b56cc ["COPY", "tmp:0:8", ["const:a8:8"]]
- 008b56cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b56cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b56cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 008b56cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b56cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b56cc bytes 29a10291
+ 008b56cc bytes 29e10391
- 008b5714 ["COPY", "tmp:0:8", ["const:e77:8"]]
- 008b5714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5714 ["COPY", "tmp:0:8", ["const:dea:8"]]
+ 008b5714 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5714 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5714 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5714 bytes 29dd3991
+ 008b5714 bytes 29a93791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4f992bfd50c3d1e476b8c84aaa68028"></a>

### [`008b5a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5a6c.md) → [`008b5a6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5a6c.md) FUN_008b5a6c

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
      "definition_site": "008b5a8c",
      "incomplete_value": false,
      "site": "008b5a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5a8c",
      "incomplete_value": false,
      "site": "008b5a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b5a90",
      "DATA",
      [
        "storage",
        "00c07028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5a90",
      "DATA",
      [
        "storage",
        "00c07078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5a6c.md#insn-008b5a8c)
- 新版 `008b5a8c`（命令位置の公開資料なし）

~~~diff
- 008b5a8c ["COPY", "tmp:0:8", ["const:28:8"]]
- 008b5a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b5a8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5a8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5a8c bytes 08a10091
+ 008b5a8c bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96671c06df319837d39a1f3c731bd4a2"></a>

### [`008b5aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5aa4.md) → [`008b5aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5aa4.md) FUN_008b5aa4

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
      "definition_site": "008b5aa8",
      "incomplete_value": false,
      "site": "008b5aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5aa8",
      "incomplete_value": false,
      "site": "008b5aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b5aac",
      "DATA",
      [
        "storage",
        "00c07028",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5aac",
      "DATA",
      [
        "storage",
        "00c07078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5aa4.md#insn-008b5aa8)
- 新版 `008b5aa8`（命令位置の公開資料なし）

~~~diff
- 008b5aa8 ["COPY", "tmp:0:8", ["const:28:8"]]
- 008b5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b5aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5aa8 bytes 08a10091
+ 008b5aa8 bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-863b79495f21d4eca5daaf09ecc755e9"></a>

### [`008b5b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5b68.md) → [`008b5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5b68.md) FUN_008b5b68

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
      "definition_site": "008b5b6c",
      "incomplete_value": false,
      "site": "008b5b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5b6c",
      "incomplete_value": false,
      "site": "008b5b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a8:8"
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
      "008b5b70",
      "DATA",
      [
        "storage",
        "00c070a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5b70",
      "DATA",
      [
        "storage",
        "00c070f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5b68.md#insn-008b5b6c)
- 新版 `008b5b6c`（命令位置の公開資料なし）

~~~diff
- 008b5b6c ["COPY", "tmp:0:8", ["const:a8:8"]]
- 008b5b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 008b5b6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5b6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5b6c bytes 08a10291
+ 008b5b6c bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015578e923a7dd8feaa4488d812f98d0"></a>

### [`008b5bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5bf4.md) → [`008b5bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5bf4.md) FUN_008b5bf4

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
      "definition_site": "008b5c14",
      "incomplete_value": false,
      "site": "008b5c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5c14",
      "incomplete_value": false,
      "site": "008b5c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "008b5c18",
      "DATA",
      [
        "storage",
        "00c07128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5c18",
      "DATA",
      [
        "storage",
        "00c07178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5bf4.md#insn-008b5c14)
- 新版 `008b5c14`（命令位置の公開資料なし）

~~~diff
- 008b5c14 ["COPY", "tmp:0:8", ["const:128:8"]]
- 008b5c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 008b5c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5c14 bytes 08a10491
+ 008b5c14 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35eafeb130506a26c5ecf182c78cab0d"></a>

### [`008b5c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5c2c.md) → [`008b5c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5c2c.md) FUN_008b5c2c

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
      "definition_site": "008b5c30",
      "incomplete_value": false,
      "site": "008b5c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5c30",
      "incomplete_value": false,
      "site": "008b5c34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:128:8"
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
      "008b5c34",
      "DATA",
      [
        "storage",
        "00c07128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5c34",
      "DATA",
      [
        "storage",
        "00c07178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5c2c.md#insn-008b5c30)
- 新版 `008b5c30`（命令位置の公開資料なし）

~~~diff
- 008b5c30 ["COPY", "tmp:0:8", ["const:128:8"]]
- 008b5c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 008b5c30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5c30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5c30 bytes 08a10491
+ 008b5c30 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67dd318431ef7b5bda8f57b01acfb5fe"></a>

### [`008b5d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d18.md) → [`008b5d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d18.md) FUN_008b5d18

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
      "definition_site": "008b5d3c",
      "incomplete_value": false,
      "site": "008b5d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d3c",
      "incomplete_value": false,
      "site": "008b5d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "008b5d3c",
      "DATA",
      [
        "storage",
        "00c071b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5d3c",
      "DATA",
      [
        "storage",
        "00c07208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d18.md#insn-008b5d38)
- 新版 `008b5d38`（命令位置の公開資料なし）

~~~diff
- 008b5d38 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 008b5d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 008b5d38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5d38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5d38 bytes 08e10691
+ 008b5d38 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2165049f682802bf791df177df64c24e"></a>

### [`008b5d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d4c.md) → [`008b5d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d4c.md) FUN_008b5d4c

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
      "definition_site": "008b5d58",
      "incomplete_value": false,
      "site": "008b5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5d58",
      "incomplete_value": false,
      "site": "008b5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "008b5d58",
      "DATA",
      [
        "storage",
        "00c071b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b5d58",
      "DATA",
      [
        "storage",
        "00c07208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d4c.md#insn-008b5d54)
- 新版 `008b5d54`（命令位置の公開資料なし）

~~~diff
- 008b5d54 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 008b5d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 008b5d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5d54 bytes 29e10691
+ 008b5d54 bytes 29210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-689c7038b38017fcc55a54c4db872439"></a>

### [`008b5d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d68.md) → [`008b5d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b5/008b5d68.md) FUN_008b5d68

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.80% / 新版 85.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b5e44",
      "incomplete_value": true,
      "site": "008b5e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c72:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5e44",
      "incomplete_value": true,
      "site": "008b5e44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c63:8"
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
      "definition_site": "008b5e48",
      "incomplete_value": true,
      "site": "008b5e48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b5e48",
      "incomplete_value": true,
      "site": "008b5e48",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 10,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b5e60",
      "incomplete_value": false,
      "site": "008b5e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b5e60",
      "incomplete_value": false,
      "site": "008b5e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "008b5e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b5e98"
      ]
    ],
    [
      "008b5e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:008b5f0c"
      ]
    ],
    [
      "008b5e34",
      "READ",
      [
        "storage",
        "002a9c63",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b5e04",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b5e98"
      ]
    ],
    [
      "008b5e24",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "008b5f0c"
      ]
    ],
    [
      "008b5e34",
      "READ",
      [
        "storage",
        "002a9c72",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b5e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d68.md#insn-008b5e2c) · [`008b5e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d68.md#insn-008b5e5c) · [`008b5e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b5/008b5d68.md#insn-008b5e98)
- 新版 `008b5e2c`（命令位置の公開資料なし） · `008b5e5c`（命令位置の公開資料なし）

~~~diff
- 008b5e2c ["COPY", "tmp:0:8", ["const:c63:8"]]
- 008b5e2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["COPY", "tmp:0:8", ["const:c72:8"]]
+ 008b5e2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b5e2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b5e2c bytes 298d3191
+ 008b5e2c bytes 29c93191
- 008b5e5c ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 008b5e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 008b5e5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b5e5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b5e5c bytes 08a10a91
+ 008b5e5c bytes 08e10b91
- 008b5e98 ["COPY", "register:4048:8", ["const:299000:8"]]
- 008b5e98 bytes 29cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09df8394a2a4482241fa42005ba26564"></a>

### [`008b60b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60b4.md) → [`008b60b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60b4.md) FUN_008b60b4

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
      "definition_site": "008b60d8",
      "incomplete_value": false,
      "site": "008b60d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b60d8",
      "incomplete_value": false,
      "site": "008b60d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b60d8",
      "DATA",
      [
        "storage",
        "00c07228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b60d8",
      "DATA",
      [
        "storage",
        "00c07278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b60d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60b4.md#insn-008b60d4)
- 新版 `008b60d4`（命令位置の公開資料なし）

~~~diff
- 008b60d4 ["COPY", "tmp:0:8", ["const:228:8"]]
- 008b60d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 008b60d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b60d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b60d4 bytes 08a10891
+ 008b60d4 bytes 08e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46bd04f66d9c5a375decfdfe2ad0d539"></a>

### [`008b60e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60e8.md) → [`008b60e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b60e8.md) FUN_008b60e8

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
      "definition_site": "008b60f4",
      "incomplete_value": false,
      "site": "008b60f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:278:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b60f4",
      "incomplete_value": false,
      "site": "008b60f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b60f4",
      "DATA",
      [
        "storage",
        "00c07228",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b60f4",
      "DATA",
      [
        "storage",
        "00c07278",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b60f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b60e8.md#insn-008b60f0)
- 新版 `008b60f0`（命令位置の公開資料なし）

~~~diff
- 008b60f0 ["COPY", "tmp:0:8", ["const:228:8"]]
- 008b60f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["COPY", "tmp:0:8", ["const:278:8"]]
+ 008b60f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b60f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b60f0 bytes 29a10891
+ 008b60f0 bytes 29e10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-110aec6cf72c7f9b22c4b1a18b0d04ad"></a>

### [`008b6170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6170.md) → [`008b6170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6170.md) FUN_008b6170

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
      "definition_site": "008b6194",
      "incomplete_value": false,
      "site": "008b6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6194",
      "incomplete_value": false,
      "site": "008b6194",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2a8:8"
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
      "008b6194",
      "DATA",
      [
        "storage",
        "00c072a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6194",
      "DATA",
      [
        "storage",
        "00c072f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6170.md#insn-008b6190)
- 新版 `008b6190`（命令位置の公開資料なし）

~~~diff
- 008b6190 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 008b6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 008b6190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6190 bytes 08a10a91
+ 008b6190 bytes 08e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cebe92d3dc56abe2a99ee5b97e7da5e3"></a>

### [`008b61a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b61a4.md) → [`008b61a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b61a4.md) FUN_008b61a4

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
      "definition_site": "008b61b0",
      "incomplete_value": false,
      "site": "008b61b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b61b0",
      "incomplete_value": false,
      "site": "008b61b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b61b0",
      "DATA",
      [
        "storage",
        "00c072a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b61b0",
      "DATA",
      [
        "storage",
        "00c072f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b61ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b61a4.md#insn-008b61ac)
- 新版 `008b61ac`（命令位置の公開資料なし）

~~~diff
- 008b61ac ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 008b61ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b61ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b61ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["COPY", "tmp:0:8", ["const:2f8:8"]]
+ 008b61ac ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b61ac ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b61ac bytes 29a10a91
+ 008b61ac bytes 29e10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9bfe2cb292f7c6e702306c3f46bc608"></a>

### [`008b622c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b622c.md) → [`008b622c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b622c.md) FUN_008b622c

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
      "definition_site": "008b6250",
      "incomplete_value": false,
      "site": "008b6250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6250",
      "incomplete_value": false,
      "site": "008b6250",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "008b6250",
      "DATA",
      [
        "storage",
        "00c07328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6250",
      "DATA",
      [
        "storage",
        "00c07378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b624c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b622c.md#insn-008b624c)
- 新版 `008b624c`（命令位置の公開資料なし）

~~~diff
- 008b624c ["COPY", "tmp:0:8", ["const:328:8"]]
- 008b624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["COPY", "tmp:0:8", ["const:378:8"]]
+ 008b624c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b624c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b624c bytes 08a10c91
+ 008b624c bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f13ba039c684b52d4ac1efce5a56c3c"></a>

### [`008b6260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6260.md) → [`008b6260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6260.md) FUN_008b6260

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
      "definition_site": "008b626c",
      "incomplete_value": false,
      "site": "008b626c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b626c",
      "incomplete_value": false,
      "site": "008b626c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b626c",
      "DATA",
      [
        "storage",
        "00c07328",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b626c",
      "DATA",
      [
        "storage",
        "00c07378",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6260.md#insn-008b6268)
- 新版 `008b6268`（命令位置の公開資料なし）

~~~diff
- 008b6268 ["COPY", "tmp:0:8", ["const:328:8"]]
- 008b6268 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6268 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6268 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["COPY", "tmp:0:8", ["const:378:8"]]
+ 008b6268 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6268 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6268 bytes 29a10c91
+ 008b6268 bytes 29e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a2ebf26b64285804c14ce0df9a6c25e"></a>

### [`008b6750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6750.md) → [`008b6750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6750.md) FUN_008b6750

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
      "definition_site": "008b6774",
      "incomplete_value": false,
      "site": "008b6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6774",
      "incomplete_value": false,
      "site": "008b6774",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "008b6774",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6774",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6750.md#insn-008b6770)
- 新版 `008b6770`（命令位置の公開資料なし）

~~~diff
- 008b6770 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 008b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008b6770 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6770 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6770 bytes 08e10e91
+ 008b6770 bytes 08211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44092b3f04dd5f86d2ae0c5c0264ef28"></a>

### [`008b6784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6784.md) → [`008b6784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6784.md) FUN_008b6784

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
      "definition_site": "008b6790",
      "incomplete_value": false,
      "site": "008b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6790",
      "incomplete_value": false,
      "site": "008b6790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "008b6790",
      "DATA",
      [
        "storage",
        "00c073b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6790",
      "DATA",
      [
        "storage",
        "00c07408",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b678c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6784.md#insn-008b678c)
- 新版 `008b678c`（命令位置の公開資料なし）

~~~diff
- 008b678c ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 008b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["COPY", "tmp:0:8", ["const:408:8"]]
+ 008b678c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b678c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b678c bytes 29e10e91
+ 008b678c bytes 29211091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbbc6cc0cb5f5c481a800a8a04f103ed"></a>

### [`008b6814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6814.md) → [`008b6814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6814.md) FUN_008b6814

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
      "definition_site": "008b6838",
      "incomplete_value": false,
      "site": "008b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6838",
      "incomplete_value": false,
      "site": "008b6838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "008b6838",
      "DATA",
      [
        "storage",
        "00c07438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6838",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6814.md#insn-008b6834)
- 新版 `008b6834`（命令位置の公開資料なし）

~~~diff
- 008b6834 ["COPY", "tmp:0:8", ["const:438:8"]]
- 008b6834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 008b6834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6834 bytes 08e11091
+ 008b6834 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba5f12e69eea1f694d3b40e5a0e989f4"></a>

### [`008b6848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6848.md) → [`008b6848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6848.md) FUN_008b6848

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
      "definition_site": "008b6854",
      "incomplete_value": false,
      "site": "008b6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6854",
      "incomplete_value": false,
      "site": "008b6854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:438:8"
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
      "008b6854",
      "DATA",
      [
        "storage",
        "00c07438",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6854",
      "DATA",
      [
        "storage",
        "00c07488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6848.md#insn-008b6850)
- 新版 `008b6850`（命令位置の公開資料なし）

~~~diff
- 008b6850 ["COPY", "tmp:0:8", ["const:438:8"]]
- 008b6850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 008b6850 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6850 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6850 bytes 29e11091
+ 008b6850 bytes 29211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdc9c87e801e196be04fc44002af463c"></a>

### [`008b6908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6908.md) → [`008b6908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6908.md) FUN_008b6908

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
      "definition_site": "008b692c",
      "incomplete_value": false,
      "site": "008b692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b692c",
      "incomplete_value": false,
      "site": "008b692c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "008b692c",
      "DATA",
      [
        "storage",
        "00c074b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b692c",
      "DATA",
      [
        "storage",
        "00c07508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6908.md#insn-008b6928)
- 新版 `008b6928`（命令位置の公開資料なし）

~~~diff
- 008b6928 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 008b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 008b6928 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6928 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6928 bytes 08e11291
+ 008b6928 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed2cf4bbc673fad71317f136b2a9b658"></a>

### [`008b693c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b693c.md) → [`008b693c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b693c.md) FUN_008b693c

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
      "definition_site": "008b6948",
      "incomplete_value": false,
      "site": "008b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6948",
      "incomplete_value": false,
      "site": "008b6948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:4b8:8"
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
      "008b6948",
      "DATA",
      [
        "storage",
        "00c074b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6948",
      "DATA",
      [
        "storage",
        "00c07508",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b693c.md#insn-008b6944)
- 新版 `008b6944`（命令位置の公開資料なし）

~~~diff
- 008b6944 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 008b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 008b6944 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6944 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6944 bytes 29e11291
+ 008b6944 bytes 29211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a29ab255f964b14f25d7c6f526b62669"></a>

### [`008b69b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69b8.md) → [`008b69b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69b8.md) FUN_008b69b8

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
      "definition_site": "008b69dc",
      "incomplete_value": false,
      "site": "008b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69dc",
      "incomplete_value": false,
      "site": "008b69dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "008b69dc",
      "DATA",
      [
        "storage",
        "00c07538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b69dc",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69b8.md#insn-008b69d8)
- 新版 `008b69d8`（命令位置の公開資料なし）

~~~diff
- 008b69d8 ["COPY", "tmp:0:8", ["const:538:8"]]
- 008b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 008b69d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b69d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b69d8 bytes 08e11491
+ 008b69d8 bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-859c4ddfa8b4e1772552415b1c12c961"></a>

### [`008b69ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69ec.md) → [`008b69ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b69ec.md) FUN_008b69ec

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
      "definition_site": "008b69f8",
      "incomplete_value": false,
      "site": "008b69f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b69f8",
      "incomplete_value": false,
      "site": "008b69f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:538:8"
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
      "008b69f8",
      "DATA",
      [
        "storage",
        "00c07538",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b69f8",
      "DATA",
      [
        "storage",
        "00c07588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b69f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b69ec.md#insn-008b69f4)
- 新版 `008b69f4`（命令位置の公開資料なし）

~~~diff
- 008b69f4 ["COPY", "tmp:0:8", ["const:538:8"]]
- 008b69f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["COPY", "tmp:0:8", ["const:588:8"]]
+ 008b69f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b69f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b69f4 bytes 29e11491
+ 008b69f4 bytes 29211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c48e6d9520c1e74a8549a9438d025efa"></a>

### [`008b6a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6a08.md) → [`008b6a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6a08.md) FUN_008b6a08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md)
- 新版 呼出元 0件  · 呼出先 15件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.58% / 新版 97.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b6af0",
      "incomplete_value": true,
      "site": "008b6b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:93d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6af0",
      "incomplete_value": true,
      "site": "008b6b08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8a3:8"
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
      "definition_site": "008b6be0",
      "incomplete_value": false,
      "site": "008b6be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6be0",
      "incomplete_value": false,
      "site": "008b6be0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "008b6af0",
      "READ",
      [
        "storage",
        "002a88a3",
        null,
        "string"
      ]
    ],
    [
      "008b6be0",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b6c2c",
      "READ",
      [
        "storage",
        "00c075c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b6af0",
      "READ",
      [
        "storage",
        "002a893d",
        null,
        "string"
      ]
    ],
    [
      "008b6be0",
      "DATA",
      [
        "storage",
        "00c075f8",
        null,
        "undefined *"
      ]
    ],
    [
      "008b6c2c",
      "READ",
      [
        "storage",
        "00c07618",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6a08.md#insn-008b6ae8) · [`008b6bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6a08.md#insn-008b6bd8)
- 新版 `008b6ae8`（命令位置の公開資料なし） · `008b6bd8`（命令位置の公開資料なし）

~~~diff
- 008b6ae8 ["COPY", "tmp:0:8", ["const:8a3:8"]]
- 008b6ae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["COPY", "tmp:0:8", ["const:93d:8"]]
+ 008b6ae8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ae8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6ae8 bytes 298d2291
+ 008b6ae8 bytes 29f52491
- 008b6bd8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 008b6bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 008b6bd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6bd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6bd8 bytes 08a11691
+ 008b6bd8 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c385c96cad90836a660d293935d2046d"></a>

### [`008b6e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6e8c.md) → [`008b6e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6e8c.md) FUN_008b6e8c

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
      "definition_site": "008b6eb0",
      "incomplete_value": false,
      "site": "008b6eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6eb0",
      "incomplete_value": false,
      "site": "008b6eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "008b6eb0",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6eb0",
      "DATA",
      [
        "storage",
        "00c075f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6e8c.md#insn-008b6eac)
- 新版 `008b6eac`（命令位置の公開資料なし）

~~~diff
- 008b6eac ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 008b6eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 008b6eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6eac bytes 08a11691
+ 008b6eac bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7741b7d3185a510ddd0f6878301f50f6"></a>

### [`008b6ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6ec0.md) → [`008b6ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6ec0.md) FUN_008b6ec0

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
      "definition_site": "008b6ecc",
      "incomplete_value": false,
      "site": "008b6ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6ecc",
      "incomplete_value": false,
      "site": "008b6ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
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
      "008b6ecc",
      "DATA",
      [
        "storage",
        "00c075a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6ecc",
      "DATA",
      [
        "storage",
        "00c075f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6ec0.md#insn-008b6ec8)
- 新版 `008b6ec8`（命令位置の公開資料なし）

~~~diff
- 008b6ec8 ["COPY", "tmp:0:8", ["const:5a8:8"]]
- 008b6ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 008b6ec8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6ec8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6ec8 bytes 29a11691
+ 008b6ec8 bytes 29e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e0d931c7ae6492584f9e5d1b991b83e"></a>

### [`008b6f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f3c.md) → [`008b6f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f3c.md) FUN_008b6f3c

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
      "definition_site": "008b6f60",
      "incomplete_value": false,
      "site": "008b6f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6f60",
      "incomplete_value": false,
      "site": "008b6f60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "008b6f60",
      "DATA",
      [
        "storage",
        "00c07638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6f60",
      "DATA",
      [
        "storage",
        "00c07688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f3c.md#insn-008b6f5c)
- 新版 `008b6f5c`（命令位置の公開資料なし）

~~~diff
- 008b6f5c ["COPY", "tmp:0:8", ["const:638:8"]]
- 008b6f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["COPY", "tmp:0:8", ["const:688:8"]]
+ 008b6f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b6f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b6f5c bytes 08e11891
+ 008b6f5c bytes 08211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6dcbbf463e1ac919a5ae3da858f649"></a>

### [`008b6f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f70.md) → [`008b6f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f70.md) FUN_008b6f70

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
      "definition_site": "008b6f7c",
      "incomplete_value": false,
      "site": "008b6f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:688:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6f7c",
      "incomplete_value": false,
      "site": "008b6f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:638:8"
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
      "008b6f7c",
      "DATA",
      [
        "storage",
        "00c07638",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008b6f7c",
      "DATA",
      [
        "storage",
        "00c07688",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f70.md#insn-008b6f78)
- 新版 `008b6f78`（命令位置の公開資料なし）

~~~diff
- 008b6f78 ["COPY", "tmp:0:8", ["const:638:8"]]
- 008b6f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["COPY", "tmp:0:8", ["const:688:8"]]
+ 008b6f78 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b6f78 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b6f78 bytes 29e11891
+ 008b6f78 bytes 29211a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c312be538b575917da870da8bf588778"></a>

### [`008b6f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f8c.md) → [`008b6f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b6/008b6f8c.md) FUN_008b6f8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/0088600c.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`0088600c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/0088600c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b6fc4",
      "incomplete_value": true,
      "site": "008b6fc4",
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
      "definition_site": "008b6fc4",
      "incomplete_value": true,
      "site": "008b6fc4",
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
      "definition_site": "008b6fcc",
      "incomplete_value": false,
      "site": "008b6fe0",
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
      "definition_site": "008b6fcc",
      "incomplete_value": false,
      "site": "008b6fe0",
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
      "definition_site": "008b6fd4",
      "incomplete_value": false,
      "site": "008b6fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b6fd4",
      "incomplete_value": false,
      "site": "008b6fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:bf6000:8"
          ],
          [
            "leaf",
            "const:298:8"
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
      "008b6fc0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b6fcc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b6fd4",
      "PARAM",
      [
        "storage",
        "00bf6298",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008b6fc0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b6fcc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b6fd4",
      "PARAM",
      [
        "storage",
        "00bf62e8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b6fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f8c.md#insn-008b6fc0) · [`008b6fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f8c.md#insn-008b6fcc) · [`008b6fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b6/008b6f8c.md#insn-008b6fd4)
- 新版 `008b6fc0`（命令位置の公開資料なし） · `008b6fcc`（命令位置の公開資料なし） · `008b6fd4`（命令位置の公開資料なし）

~~~diff
- 008b6fc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008b6fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b6fc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008b6fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008b6fc0 bytes 083d45f9
+ 008b6fc0 bytes 085d45f9
- 008b6fcc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008b6fcc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008b6fcc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b6fcc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b6fcc bytes 21203991
+ 008b6fcc bytes 21603a91
- 008b6fd4 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008b6fd4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008b6fd4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b6fd4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b6fd4 bytes 42600a91
+ 008b6fd4 bytes 42a00b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a45ea313a0ec6217009c3409c98c0c3d"></a>

### [`008b70b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md) → [`008b70b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b70b8.md) _INIT_169

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b70f4",
      "incomplete_value": true,
      "site": "008b7110",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b70f4",
      "incomplete_value": true,
      "site": "008b7110",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "008b7138",
      "incomplete_value": true,
      "site": "008b7154",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7138",
      "incomplete_value": true,
      "site": "008b7154",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "definition_site": "008b7174",
      "incomplete_value": true,
      "site": "008b7190",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7174",
      "incomplete_value": true,
      "site": "008b7190",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29c000:8"
              ],
              [
                "leaf",
                "const:36e:8"
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
      "008b70f4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008b7118",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008b7138",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b70f4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008b7118",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008b7138",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b70e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md#insn-008b70e4) · [`008b70ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b70b8.md#insn-008b70ec)
- 新版 `008b70e4`（命令位置の公開資料なし） · `008b70ec`（命令位置の公開資料なし）

~~~diff
- 008b70e4 ["COPY", "tmp:0:8", ["const:730:8"]]
- 008b70e4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 008b70e4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008b70e4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008b70e4 bytes 73c21c91
+ 008b70e4 bytes 73c21d91
- 008b70ec ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008b70ec bytes 89cfff90
+ 008b70ec ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008b70ec bytes 89cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de791019b6a172780a115ae040013e1a"></a>

### [`008b7448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md) → [`008b7448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md) FUN_008b7448

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006ae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae96c.md) · 呼出先 2件 [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) [`008b7948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7948.md)
- 新版 呼出元 1件 [`006ae96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae96c.md) · 呼出先 2件 [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) [`008b7948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7948.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b74a4",
      "incomplete_value": true,
      "site": "008b74a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b74a4",
      "incomplete_value": true,
      "site": "008b74a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b74cc",
      "incomplete_value": true,
      "site": "008b74cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:72c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b74cc",
      "incomplete_value": true,
      "site": "008b74cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6dc:8"
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
      "008b7484",
      "READ",
      [
        "storage",
        "00c246d8",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74a4",
      "WRITE",
      [
        "storage",
        "00c246d8",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74ac",
      "READ",
      [
        "storage",
        "00c246dc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008b7484",
      "READ",
      [
        "storage",
        "00c24728",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74a4",
      "WRITE",
      [
        "storage",
        "00c24728",
        null,
        "undefined4"
      ]
    ],
    [
      "008b74ac",
      "READ",
      [
        "storage",
        "00c2472c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b74a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b74a4) · [`008b74cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b74cc) · [`008b7484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md#insn-008b7484)
- 新版 `008b74a4`（命令位置の公開資料なし） · `008b74cc`（命令位置の公開資料なし） · `008b7484`（命令位置の公開資料なし）

~~~diff
- 008b74a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 008b74a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b74a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 008b74a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74a4 bytes 68da06b9
+ 008b74a4 bytes 682a07b9
- 008b74cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6dc:8"]]
- 008b74cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b74cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:72c:8"]]
+ 008b74cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b74cc bytes 68de06b9
+ 008b74cc bytes 682e07b9
- 008b7484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 008b7484 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 008b7484 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 008b7484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 008b7484 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 008b7484 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 008b7484 bytes 68da46b9
+ 008b7484 bytes 682a47b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf234f203f2307014b3f7714e8398ed8"></a>

### [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) → [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) FUN_008b74dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`008b7448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7448.md) [`008b8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md) [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060dcac.md) [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md)
- 新版 呼出元 4件 [`008b7448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7448.md) [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 13件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060dcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060dcac.md) [`008be334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.20% / 新版 93.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7890",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7890",
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
                "const:c25000:8"
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
    "ordinal": 28,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b7894",
      "incomplete_value": false,
      "site": "008b7894",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7894",
      "incomplete_value": false,
      "site": "008b7894",
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
            "const:0:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7894",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008b7890",
      "incomplete_value": false,
      "site": "008b7894",
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
                "const:c25000:8"
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
      "008b7704",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b774c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "008b7750",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b7704",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008b774c",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "008b7750",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b7700) · [`008b774c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b774c) · [`008b7750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md#insn-008b7750)
- 新版 `008b7700`（命令位置の公開資料なし） · `008b774c`（命令位置の公開資料なし） · `008b7750`（命令位置の公開資料なし）

~~~diff
- 008b7700 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008b7700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b7700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b7700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b7700 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7700 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b7700 bytes 08e10091
+ 008b7700 bytes 08e10191
- 008b774c ["COPY", "tmp:0:8", ["const:0:8"]]
- 008b774c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008b774c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008b774c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008b774c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 008b774c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008b774c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008b774c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008b774c bytes 00000091
+ 008b774c bytes 00000191
- 008b7750 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:e60:8"]]
- 008b7750 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b7750 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:eb0:8"]]
+ 008b7750 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 008b7750 bytes 423047f9
+ 008b7750 bytes 425847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a096f2b8376a18dccd0554ac36c4d07c"></a>

### [`008b7b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md) → [`008b7b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md) FUN_008b7b38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 14件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.23% / 新版 91.23%

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
      "definition_site": "008b7b8c",
      "incomplete_value": false,
      "site": "008b7b94",
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
      "definition_site": "008b7b8c",
      "incomplete_value": false,
      "site": "008b7b94",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:46:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:295000:8"
              ],
              [
                "leaf",
                "const:d3:8"
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
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008b7bb0",
      "incomplete_value": true,
      "site": "008b7bc8",
      "value": [
        "LOAD",
        "16",
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
      "008b7b94",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "002950d3",
        null,
        "string"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "002950e3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b7b94",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "00295046",
        null,
        "string"
      ]
    ],
    [
      "008b7bb0",
      "READ",
      [
        "storage",
        "00295056",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md#insn-008b7b8c) · [`008b7ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md#insn-008b7ba8) · [`008b7bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md#insn-008b7bac)
- 新版 `008b7b8c`（命令位置の公開資料なし） · `008b7ba8`（命令位置の公開資料なし）

~~~diff
- 008b7b8c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 008b7b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 008b7b8c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008b7b8c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008b7b8c bytes 29a13491
+ 008b7b8c bytes 29e13591
- 008b7ba8 ["COPY", "tmp:0:8", ["const:d3:8"]]
- 008b7ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["COPY", "tmp:0:8", ["const:46:8"]]
+ 008b7ba8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 008b7ba8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 008b7ba8 bytes 4a4d0391
+ 008b7ba8 bytes 4a190191
- 008b7bac ["COPY", "register:4040:8", ["const:2b1000:8"]]
- 008b7bac bytes c8cfffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91418f786413855005897cf09ac9f801"></a>

### [`008b7f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md) → [`008b7f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7f70.md) FUN_008b7f70

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a8/005a83e4.md) [`0063e588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e588.md)
- 新版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) · 呼出先 8件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0050ae28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0050a/0050ae28.md) [`005a83e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005a8/005a83e4.md) [`0063e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e588.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b7fac",
      "incomplete_value": true,
      "site": "008b7fbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:125:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b7fac",
      "incomplete_value": true,
      "site": "008b7fbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1b2:8"
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
      "definition_site": "008b7fc0",
      "incomplete_value": true,
      "site": "008b7fc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b7fc0",
      "incomplete_value": true,
      "site": "008b7fc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008b8010",
      "incomplete_value": true,
      "site": "008b8010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:764:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b8010",
      "incomplete_value": true,
      "site": "008b8010",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6d9:8"
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
      "008b7fac",
      "READ",
      [
        "storage",
        "002961b2",
        null,
        "string"
      ]
    ],
    [
      "008b7fb0",
      "READ",
      [
        "storage",
        "002961c1",
        null,
        "string"
      ]
    ],
    [
      "008b8000",
      "READ",
      [
        "storage",
        "002a46d9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b7fac",
      "READ",
      [
        "storage",
        "00296125",
        null,
        "string"
      ]
    ],
    [
      "008b7fb0",
      "READ",
      [
        "storage",
        "00296134",
        null,
        "string"
      ]
    ],
    [
      "008b8000",
      "READ",
      [
        "storage",
        "002a4764",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b7fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md#insn-008b7fa4) · [`008b7fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7f70.md#insn-008b7fa8)
- 新版 `008b7fa4`（命令位置の公開資料なし） · `008b7fa8`（命令位置の公開資料なし）

~~~diff
- 008b7fa4 ["COPY", "tmp:0:8", ["const:1b2:8"]]
- 008b7fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["COPY", "tmp:0:8", ["const:125:8"]]
+ 008b7fa4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b7fa4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b7fa4 bytes 08c90691
+ 008b7fa4 bytes 08950491
- 008b7fa8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 008b7fa8 bytes c9cfffb0
+ 008b7fa8 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 008b7fa8 bytes c9cfffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e519a0c5b6ea76754700e0c51ea4a4bf"></a>

### [`008b8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md) → [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) FUN_008b8260

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md)
- 新版 呼出元 1件 [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.30% / 新版 93.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_destination` 7件, `store_value` 4件

アドレスに依存する影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008b834c",
      "incomplete_value": true,
      "site": "008b834c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b4d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b834c",
      "incomplete_value": true,
      "site": "008b834c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b4f:8"
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
      "definition_site": "008b84e4",
      "incomplete_value": true,
      "site": "008b84e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b5a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b84e4",
      "incomplete_value": true,
      "site": "008b84e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:29b000:8"
              ],
              [
                "leaf",
                "const:b5c:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b87fc",
      "incomplete_value": false,
      "site": "008b87fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b87fc",
      "incomplete_value": false,
      "site": "008b87fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 35,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b8324",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008b8338",
      "READ",
      [
        "storage",
        "0029bb4f",
        null,
        "string"
      ]
    ],
    [
      "008b83c0",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "008b8324",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008b8338",
      "READ",
      [
        "storage",
        "0029bb4d",
        null,
        "string"
      ]
    ],
    [
      "008b83c0",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b87fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b87fc) · [`008b881c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b881c) · [`008b8320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md#insn-008b8320)
- 新版 `008b87fc`（命令位置の公開資料なし） · `008b881c`（命令位置の公開資料なし） · `008b8320`（命令位置の公開資料なし）

~~~diff
- 008b87fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
- 008b87fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b87fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 008b87fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b87fc bytes 28d906b9
+ 008b87fc bytes 282907b9
- 008b881c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6dc:8"]]
- 008b881c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008b881c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:72c:8"]]
+ 008b881c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008b881c bytes 28dd06b9
+ 008b881c bytes 282d07b9
- 008b8320 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008b8320 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 008b8320 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 008b8320 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 008b8320 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008b8320 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 008b8320 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 008b8320 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 008b8320 bytes 5ae30091
+ 008b8320 bytes 5ae30191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac819cf8cfd2d738ff582efcfb015ddb"></a>

### [`008b89f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md) → [`008b89f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b89f8.md) FUN_008b89f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c3/008c3e08.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.49% / 新版 98.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008b8a14",
      "incomplete_value": true,
      "site": "008b8a14",
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
      "definition_site": "008b8a14",
      "incomplete_value": true,
      "site": "008b8a14",
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
      "definition_site": "008b8a1c",
      "incomplete_value": false,
      "site": "008b8a30",
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
      "definition_site": "008b8a1c",
      "incomplete_value": false,
      "site": "008b8a30",
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
      "definition_site": "008b8a24",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b8a24",
      "incomplete_value": false,
      "site": "008b8a30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008b8a10",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008b8a1c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b8a24",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008b8a10",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008b8a1c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008b8a24",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b8a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a10) · [`008b8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a1c) · [`008b8a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b89f8.md#insn-008b8a24)
- 新版 `008b8a10`（命令位置の公開資料なし） · `008b8a1c`（命令位置の公開資料なし） · `008b8a24`（命令位置の公開資料なし）

~~~diff
- 008b8a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008b8a10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008b8a10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008b8a10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008b8a10 bytes 083d45f9
+ 008b8a10 bytes 085d45f9
- 008b8a1c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008b8a1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008b8a1c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008b8a1c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008b8a1c bytes 21203991
+ 008b8a1c bytes 21603a91
- 008b8a24 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008b8a24 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008b8a24 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008b8a24 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008b8a24 bytes 42a01a91
+ 008b8a24 bytes 42e01b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93df04b316fd34f4af0b57d3998b80f7"></a>

### [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) → [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) FUN_008b9174

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) [`008bf000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf000.md) [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 53件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 3件 [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) [`008bf000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf000.md) [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) · 呼出先 53件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.27% / 新版 94.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 31件, `store_destination` 50件, `store_value` 18件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b9864",
      "incomplete_value": false,
      "site": "008b9864",
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
      "definition_site": "008b9864",
      "incomplete_value": false,
      "site": "008b9864",
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
    "ordinal": 52,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008b9890",
      "incomplete_value": false,
      "site": "008b9890",
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
            "const:20c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b9890",
      "incomplete_value": false,
      "site": "008b9890",
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
            "const:299:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008b9e84",
      "incomplete_value": false,
      "site": "008b9e84",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008b9e84",
      "incomplete_value": false,
      "site": "008b9e84",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:28:8"
          ]
        ]
      ]
    },
    "ordinal": 112,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008b9864",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ],
    [
      "008b9890",
      "DATA",
      [
        "storage",
        "00298299",
        null,
        "string"
      ]
    ],
    [
      "008b9980",
      "DATA",
      [
        "storage",
        "00298ff9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008b9864",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ],
    [
      "008b9890",
      "DATA",
      [
        "storage",
        "0029820c",
        null,
        "string"
      ]
    ],
    [
      "008b9980",
      "DATA",
      [
        "storage",
        "00298f6c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008b985c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md#insn-008b985c) · [`008b9884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md#insn-008b9884) · [`008b988c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md#insn-008b988c)
- 新版 `008b985c`（命令位置の公開資料なし） · `008b9884`（命令位置の公開資料なし）

~~~diff
- 008b985c ["COPY", "tmp:0:8", ["const:ff9:8"]]
- 008b985c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b985c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b985c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["COPY", "tmp:0:8", ["const:f6c:8"]]
+ 008b985c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b985c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b985c bytes 08e53f91
+ 008b985c bytes 08b13d91
- 008b9884 ["COPY", "tmp:0:8", ["const:299:8"]]
- 008b9884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008b9884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008b9884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["COPY", "tmp:0:8", ["const:20c:8"]]
+ 008b9884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008b9884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008b9884 bytes 08650a91
+ 008b9884 bytes 08310891
- 008b988c ["INT_SUB", "register:4008:8", ["register:40e8:8", "const:80:8"]]
- 008b988c bytes a10302d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e92ba61fa135c71f1e5d0f2cefb5408"></a>

### [`008bb8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md) → [`008bb8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md) FUN_008bb8c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0069ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab88.md) [`0069bb8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069b/0069bb8c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)
- 新版 呼出元 1件 [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) · 呼出先 5件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0069ab88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab88.md) [`0069bb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069bb8c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7c0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bb8e4",
      "incomplete_value": true,
      "site": "008bb8e4",
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
      "definition_site": "008bb8e4",
      "incomplete_value": true,
      "site": "008bb8e4",
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
      "definition_site": "008bb8ec",
      "incomplete_value": false,
      "site": "008bb900",
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
      "definition_site": "008bb8ec",
      "incomplete_value": false,
      "site": "008bb900",
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
      "definition_site": "008bb8f4",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bb8f4",
      "incomplete_value": false,
      "site": "008bb900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008bb8e0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bb8ec",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bb8f4",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bb8e0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bb8ec",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bb8f4",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8e0) · [`008bb8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8ec) · [`008bb8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md#insn-008bb8f4)
- 新版 `008bb8e0`（命令位置の公開資料なし） · `008bb8ec`（命令位置の公開資料なし） · `008bb8f4`（命令位置の公開資料なし）

~~~diff
- 008bb8e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008bb8e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bb8e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008bb8e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bb8e0 bytes 083d45f9
+ 008bb8e0 bytes 085d45f9
- 008bb8ec ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008bb8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008bb8ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bb8ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bb8ec bytes 21203991
+ 008bb8ec bytes 21603a91
- 008bb8f4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008bb8f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008bb8f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bb8f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bb8f4 bytes 42a01a91
+ 008bb8f4 bytes 42e01b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe848d92200fae054cd6c4a5a17da011"></a>

### [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) → [`008bb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb9b0.md) FUN_008bb9b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c26e0.md) · 呼出先 41件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044bf2c.md)
- 新版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c26e0.md) · 呼出先 41件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008bbf50",
      "incomplete_value": false,
      "site": "008bbf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bbf50",
      "incomplete_value": false,
      "site": "008bbf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
          ]
        ]
      ]
    },
    "ordinal": 43,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bc5bc",
      "incomplete_value": true,
      "site": "008bc5d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc5bc",
      "incomplete_value": true,
      "site": "008bc5d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 95,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008bc64c",
      "incomplete_value": false,
      "site": "008bc650",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc64c",
      "incomplete_value": false,
      "site": "008bc650",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 102,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008bbb14",
      "READ",
      [
        "storage",
        "00c1b6e0",
        null,
        "pointer"
      ]
    ],
    [
      "008bbb20",
      "DATA",
      [
        "storage",
        "00c24074",
        null,
        null
      ]
    ],
    [
      "008bbf50",
      "DATA",
      [
        "storage",
        "00c076d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008bbb14",
      "READ",
      [
        "storage",
        "00c1b730",
        null,
        "pointer"
      ]
    ],
    [
      "008bbb20",
      "DATA",
      [
        "storage",
        "00c240c4",
        null,
        null
      ]
    ],
    [
      "008bbf50",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bbb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bbb14) · [`008bbf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bbf4c) · [`008bc51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md#insn-008bc51c)
- 新版 `008bbb14`（命令位置の公開資料なし） · `008bbf4c`（命令位置の公開資料なし） · `008bc51c`（命令位置の公開資料なし）

~~~diff
- 008bbb14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6e0:8"]]
- 008bbb14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bbb14 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:730:8"]]
+ 008bbb14 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 008bbb14 bytes 297143f9
+ 008bbb14 bytes 299943f9
- 008bbf4c ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 008bbf4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008bbf4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008bbf4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008bbf4c bytes 08411b91
+ 008bbf4c bytes 08811c91
- 008bc51c ["COPY", "tmp:0:8", ["const:0:8"]]
- 008bc51c ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
- 008bc51c ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
- 008bc51c ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
+ 008bc51c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 008bc51c ["INT_CARRY", "register:105:1", ["register:40d8:8", "tmp:0:8"]]
+ 008bc51c ["INT_SCARRY", "register:106:1", ["register:40d8:8", "tmp:0:8"]]
+ 008bc51c ["INT_ADD", "tmp:1:8", ["register:40d8:8", "tmp:0:8"]]
- 008bc51c bytes 7b030091
+ 008bc51c bytes 7b030191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91455f80c9dc1c2d2d7d8e413d0a9036"></a>

### [`008bc990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md) → [`008bc990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bc/008bc990.md) FUN_008bc990

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md)
- 新版 呼出元 1件 [`008c3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c3/008c3e08.md) · 呼出先 41件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 99.62% / 新版 99.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bc9d4",
      "incomplete_value": true,
      "site": "008bc9d4",
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
      "definition_site": "008bc9d4",
      "incomplete_value": true,
      "site": "008bc9d4",
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
      "definition_site": "008bc9dc",
      "incomplete_value": false,
      "site": "008bc9f0",
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
      "definition_site": "008bc9dc",
      "incomplete_value": false,
      "site": "008bc9f0",
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
      "definition_site": "008bc9e4",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bc9e4",
      "incomplete_value": false,
      "site": "008bc9f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008bc9d0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bc9dc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bc9e4",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bc9d0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bc9dc",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bc9e4",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bc9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9d0) · [`008bc9dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9dc) · [`008bc9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bc/008bc990.md#insn-008bc9e4)
- 新版 `008bc9d0`（命令位置の公開資料なし） · `008bc9dc`（命令位置の公開資料なし） · `008bc9e4`（命令位置の公開資料なし）

~~~diff
- 008bc9d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008bc9d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bc9d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008bc9d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bc9d0 bytes 083d45f9
+ 008bc9d0 bytes 085d45f9
- 008bc9dc ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008bc9dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008bc9dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bc9dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bc9dc bytes 21203991
+ 008bc9dc bytes 21603a91
- 008bc9e4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008bc9e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008bc9e4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bc9e4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bc9e4 bytes 42a01a91
+ 008bc9e4 bytes 42e01b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59130991ed550d4c68735358c829fd32"></a>

### [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md) → [`008be334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md) FUN_008be334

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008b74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b74dc.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`00640008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md)
- 新版 呼出元 1件 [`008b74dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b74dc.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`008c4a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4a54.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.96% / 新版 85.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008be458",
      "incomplete_value": true,
      "site": "008be46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008be458",
      "incomplete_value": true,
      "site": "008be46c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:859:8"
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
      "definition_site": "008be4ac",
      "incomplete_value": true,
      "site": "008be4ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008be4ac",
      "incomplete_value": true,
      "site": "008be4ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:732:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008be5b0",
      "incomplete_value": false,
      "site": "008be5b0",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008be5b0",
      "incomplete_value": false,
      "site": "008be5b0",
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
                "const:c25000:8"
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
    "ordinal": 20,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008be444",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008be458",
      "READ",
      [
        "storage",
        "002a5859",
        null,
        "string"
      ]
    ],
    [
      "008be478",
      "PARAM",
      [
        "storage",
        "002a9c72",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "008be444",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008be458",
      "READ",
      [
        "storage",
        "002a58e4",
        null,
        "string"
      ]
    ],
    [
      "008be478",
      "PARAM",
      [
        "storage",
        "002a9c81",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008be440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md#insn-008be440) · [`008be44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md#insn-008be44c)
- 新版 `008be440`（命令位置の公開資料なし） · `008be44c`（命令位置の公開資料なし）

~~~diff
- 008be440 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008be440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008be440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008be440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008be440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008be440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008be440 bytes 08e10091
+ 008be440 bytes 08e10191
- 008be44c ["COPY", "register:4048:8", ["const:2a5000:8"]]
- 008be44c bytes 29cffff0
+ 008be44c ["COPY", "register:4048:8", ["const:2a5000:8"]]
+ 008be44c bytes 29cffff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5355e2ccc364a332bba9569a20f5cfc1"></a>

### [`008bf204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md) → [`008bf204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf204.md) FUN_008bf204

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2284.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445e30.md)
- 新版 呼出元 1件 [`008c2284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2284.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445e30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445e30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008bf238",
      "incomplete_value": true,
      "site": "008bf238",
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
      "definition_site": "008bf238",
      "incomplete_value": true,
      "site": "008bf238",
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
      "definition_site": "008bf240",
      "incomplete_value": false,
      "site": "008bf254",
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
      "definition_site": "008bf240",
      "incomplete_value": false,
      "site": "008bf254",
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
      "definition_site": "008bf248",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008bf248",
      "incomplete_value": false,
      "site": "008bf254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008bf230",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008bf240",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bf248",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008bf230",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008bf240",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008bf248",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008bf230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf230) · [`008bf240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf240) · [`008bf248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf204.md#insn-008bf248)
- 新版 `008bf230`（命令位置の公開資料なし） · `008bf240`（命令位置の公開資料なし） · `008bf248`（命令位置の公開資料なし）

~~~diff
- 008bf230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008bf230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008bf230 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008bf230 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008bf230 bytes 083d45f9
+ 008bf230 bytes 085d45f9
- 008bf240 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008bf240 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008bf240 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008bf240 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008bf240 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008bf240 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008bf240 bytes 21203991
+ 008bf240 bytes 21603a91
- 008bf248 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008bf248 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008bf248 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008bf248 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008bf248 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008bf248 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008bf248 bytes 42a01a91
+ 008bf248 bytes 42e01b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b4cd833c7b2a3057664c808107ba07c"></a>

### [`008bf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md) → [`008bf94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf94c.md) FUN_008bf94c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`006ae96c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ae/006ae96c.md) [`008bf94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md) [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md)
- 新版 呼出元 4件 [`006ae96c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ae/006ae96c.md) [`008bf94c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bf/008bf94c.md) [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) · 呼出先 30件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00450668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00450/00450668.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.22% / 新版 99.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0794",
      "incomplete_value": false,
      "site": "008c0794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c0794",
      "incomplete_value": false,
      "site": "008c0794",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
          ]
        ]
      ]
    },
    "ordinal": 163,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0840",
      "incomplete_value": true,
      "site": "008c085c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:de6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c0840",
      "incomplete_value": true,
      "site": "008c085c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d5b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 167,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c0860",
      "incomplete_value": true,
      "site": "008c0860",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "008c0860",
      "incomplete_value": true,
      "site": "008c0860",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 168,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c0794",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ],
    [
      "008c07ec",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c07f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c0794",
      "DATA",
      [
        "storage",
        "00c077a0",
        null,
        "undefined *"
      ]
    ],
    [
      "008c07ec",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c07f8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c0788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c0788) · [`008c07ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c07ec) · [`008c07f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bf/008bf94c.md#insn-008c07f8)
- 新版 `008c0788`（命令位置の公開資料なし） · `008c07ec`（命令位置の公開資料なし） · `008c07f8`（命令位置の公開資料なし）

~~~diff
- 008c0788 ["COPY", "tmp:0:8", ["const:750:8"]]
- 008c0788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c0788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c0788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008c0788 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c0788 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c0788 bytes 08411d91
+ 008c0788 bytes 08811e91
- 008c07ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008c07ec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c07ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008c07ec ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008c07ec bytes 003d45f9
+ 008c07ec bytes 005d45f9
- 008c07f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008c07f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008c07f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c07f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c07f8 bytes 21203991
+ 008c07f8 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a57665931d8ca23dc447e5812d103382"></a>

### [`008c1354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md) → [`008c1354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1354.md) FUN_008c1354

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) · 呼出先 27件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0063e4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e4a8.md)
- 新版 呼出元 1件 [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) · 呼出先 27件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0063e4a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e4a8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c1960",
      "incomplete_value": false,
      "site": "008c1960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c1960",
      "incomplete_value": false,
      "site": "008c1960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 109,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c1980",
      "incomplete_value": false,
      "site": "008c1980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:72c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c1980",
      "incomplete_value": false,
      "site": "008c1980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:6dc:8"
          ]
        ]
      ]
    },
    "ordinal": 110,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008c1390",
      "incomplete_value": true,
      "site": "008c1390",
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
      "definition_site": "008c1390",
      "incomplete_value": true,
      "site": "008c1390",
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
      "008c138c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c1398",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c13a0",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c138c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c1398",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c13a0",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c1960) · [`008c1980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c1980) · [`008c138c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1354.md#insn-008c138c)
- 新版 `008c1960`（命令位置の公開資料なし） · `008c1980`（命令位置の公開資料なし） · `008c138c`（命令位置の公開資料なし）

~~~diff
- 008c1960 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
- 008c1960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c1960 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 008c1960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c1960 bytes 28d906b9
+ 008c1960 bytes 282907b9
- 008c1980 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6dc:8"]]
- 008c1980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c1980 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:72c:8"]]
+ 008c1980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c1980 bytes 28dd06b9
+ 008c1980 bytes 282d07b9
- 008c138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008c138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c138c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008c138c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008c138c bytes 083d45f9
+ 008c138c bytes 085d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0521e1735e03bb58dad1ffbf5c91775"></a>

### [`008c1b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md) → [`008c1b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c1/008c1b84.md) FUN_008c1b84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c26e0.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00650740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650740.md) [`0069ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069a/0069ab94.md) [`0069bc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069b/0069bc74.md)
- 新版 呼出元 1件 [`008c26e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c26e0.md) · 呼出先 17件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00650740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650740.md) [`0069ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069a/0069ab94.md) [`0069bc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069b/0069bc74.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.99% / 新版 98.99%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c6b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 59,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008c20c0",
      "incomplete_value": true,
      "site": "008c20d0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 60,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fc6b",
        null,
        "string"
      ]
    ],
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fc7b",
        null,
        "string"
      ]
    ],
    [
      "008c20ec",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fcf6",
        null,
        "string"
      ]
    ],
    [
      "008c20c0",
      "READ",
      [
        "storage",
        "0029fd06",
        null,
        "string"
      ]
    ],
    [
      "008c20ec",
      "DATA",
      [
        "storage",
        "00c07820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c20bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md#insn-008c20bc) · [`008c20e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c1/008c1b84.md#insn-008c20e4)
- 新版 `008c20bc`（命令位置の公開資料なし） · `008c20e4`（命令位置の公開資料なし）

~~~diff
- 008c20bc ["COPY", "tmp:0:8", ["const:c6b:8"]]
- 008c20bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c20bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c20bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["COPY", "tmp:0:8", ["const:cf6:8"]]
+ 008c20bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c20bc bytes 08ad3191
+ 008c20bc bytes 08d93391
- 008c20e4 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 008c20e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 008c20e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c20e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c20e4 bytes 08411f91
+ 008c20e4 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b89732cbb609382adb2f3b9c370e59c2"></a>

### [`008c2634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md) → [`008c2634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2634.md) FUN_008c2634

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 7件 [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`0069de18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0069d/0069de18.md) [`006a86c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a86c4.md) [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) [`008bb8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb8c4.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 7件 [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`0069de18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0069d/0069de18.md) [`006a86c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006a8/006a86c4.md) [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) [`008bb8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008bb/008bb8c4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.70% / 新版 90.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "008c264c",
      "incomplete_value": true,
      "site": "008c264c",
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
      "definition_site": "008c264c",
      "incomplete_value": true,
      "site": "008c264c",
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
      "definition_site": "008c2654",
      "incomplete_value": false,
      "site": "008c2668",
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
      "definition_site": "008c2654",
      "incomplete_value": false,
      "site": "008c2668",
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
      "definition_site": "008c265c",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c265c",
      "incomplete_value": false,
      "site": "008c2668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "008c2648",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2654",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c265c",
      "PARAM",
      [
        "storage",
        "00c076a8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c2648",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2654",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008c265c",
      "PARAM",
      [
        "storage",
        "00c076f8",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c2648) · [`008c2654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c2654) · [`008c265c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2634.md#insn-008c265c)
- 新版 `008c2648`（命令位置の公開資料なし） · `008c2654`（命令位置の公開資料なし） · `008c265c`（命令位置の公開資料なし）

~~~diff
- 008c2648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008c2648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c2648 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008c2648 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008c2648 bytes 083d45f9
+ 008c2648 bytes 085d45f9
- 008c2654 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008c2654 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c2654 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c2654 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008c2654 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c2654 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c2654 bytes 21203991
+ 008c2654 bytes 21603a91
- 008c265c ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 008c265c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008c265c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008c265c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 008c265c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008c265c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008c265c bytes 42a01a91
+ 008c265c bytes 42e01b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18029694cf54fde1b2dbf4847253d530"></a>

### [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) → [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) FUN_008c2704

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 16件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`007f96a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96a4.md) [`007f96d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96d8.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 16件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`007f96a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96a4.md) [`007f96d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96d8.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 3件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2738",
      "incomplete_value": false,
      "site": "008c2738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2738",
      "incomplete_value": false,
      "site": "008c2738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c272c",
      "incomplete_value": true,
      "site": "008c2738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008c272c",
      "incomplete_value": true,
      "site": "008c2738",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c273c",
      "incomplete_value": false,
      "site": "008c273c",
      "value": [
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
    },
    "old": {
      "definition_site": "008c273c",
      "incomplete_value": false,
      "site": "008c273c",
      "value": [
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
    },
    "ordinal": 13,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c272c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2730",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2738",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008c272c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2730",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2738",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c2738) · [`008c273c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c273c) · [`008c278c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md#insn-008c278c)
- 新版 `008c2738`（命令位置の公開資料なし） · `008c273c`（命令位置の公開資料なし） · `008c278c`（命令位置の公開資料なし）

~~~diff
- 008c2738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 008c2738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008c2738 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 008c2738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008c2738 bytes 093505f9
+ 008c2738 bytes 095505f9
- 008c273c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
- 008c273c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008c273c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:ab8:8"]]
+ 008c273c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008c273c bytes 8a3f05f9
+ 008c273c bytes 8a5f05f9
- 008c278c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:a78:8"]]
- 008c278c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008c278c ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:ab8:8"]]
+ 008c278c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008c278c bytes 943f05f9
+ 008c278c bytes 945f05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-863f7c3e71cce45b8d729051ca8a7381"></a>

### [`008c2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md) → [`008c2a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2a7c.md) FUN_008c2a7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 44件 [`00429060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429060.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 44件 [`00429060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00429/00429060.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 96.66% / 新版 96.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 8件, `store_destination` 17件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2d54",
      "incomplete_value": true,
      "site": "008c2d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2d54",
      "incomplete_value": true,
      "site": "008c2d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2ed4",
      "incomplete_value": true,
      "site": "008c2ed4",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2ed4",
      "incomplete_value": true,
      "site": "008c2ed4",
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
            "const:6d8:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c2fb0",
      "incomplete_value": true,
      "site": "008c2fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:72c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c2fb0",
      "incomplete_value": true,
      "site": "008c2fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6dc:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c2c78",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c2c80",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2d38",
      "READ",
      [
        "storage",
        "00c246d8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "008c2c78",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008c2c80",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "008c2d38",
      "READ",
      [
        "storage",
        "00c24728",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c2d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2d54) · [`008c2ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2ed4) · [`008c2fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2a7c.md#insn-008c2fb0)
- 新版 `008c2d54`（命令位置の公開資料なし） · `008c2ed4`（命令位置の公開資料なし） · `008c2fb0`（命令位置の公開資料なし）

~~~diff
- 008c2d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6d8:8"]]
- 008c2d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2d54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:728:8"]]
+ 008c2d54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2d54 bytes 68da06b9
+ 008c2d54 bytes 682a07b9
- 008c2ed4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:6d8:8"]]
- 008c2ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2ed4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
+ 008c2ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2ed4 bytes 28d906b9
+ 008c2ed4 bytes 282907b9
- 008c2fb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6dc:8"]]
- 008c2fb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 008c2fb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:72c:8"]]
+ 008c2fb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 008c2fb0 bytes 68de06b9
+ 008c2fb0 bytes 682e07b9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc2a5a7a6c582022a4da1003c2a1c023"></a>

### [`008c3e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md) → [`008c3e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c3/008c3e08.md) FUN_008c3e08

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 32件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 32件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.82% / 新版 94.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f4",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f4",
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
                "const:c25000:8"
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
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008c48f8",
      "incomplete_value": false,
      "site": "008c48f8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c48f8",
      "incomplete_value": false,
      "site": "008c48f8",
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
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f8",
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
                "const:c25000:8"
              ],
              [
                "leaf",
                "const:40:8"
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
      "definition_site": "008c48f4",
      "incomplete_value": false,
      "site": "008c48f8",
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
                "const:c25000:8"
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
      "008c3e48",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c3e54",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "008c3e6c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008c3e48",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008c3e54",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "008c3e6c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c3e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e34) · [`008c3e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e54) · [`008c3e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c3/008c3e08.md#insn-008c3e6c)
- 新版 `008c3e34`（命令位置の公開資料なし） · `008c3e54`（命令位置の公開資料なし） · `008c3e6c`（命令位置の公開資料なし）

~~~diff
- 008c3e34 ["COPY", "tmp:0:8", ["const:38:8"]]
- 008c3e34 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 008c3e34 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 008c3e34 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 008c3e34 bytes f7e20091
+ 008c3e34 bytes f7e20191
- 008c3e54 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:30:8"]]
- 008c3e54 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c3e54 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:70:8"]]
+ 008c3e54 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008c3e54 bytes 001b40f9
+ 008c3e54 bytes 003b40f9
- 008c3e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008c3e6c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 008c3e6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008c3e6c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 008c3e6c bytes 003d45f9
+ 008c3e6c bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba4d93d36eb763645f83c0b383fcadca"></a>

### [`008c497c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c497c.md) → [`008c497c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c497c.md) FUN_008c497c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008b7b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7b38.md) [`008b7e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b7/008b7e34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`008b7b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7b38.md) [`008b7e34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b7/008b7e34.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "008c4988",
      "incomplete_value": false,
      "site": "008c498c",
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
      "definition_site": "008c4988",
      "incomplete_value": false,
      "site": "008c498c",
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
      "008c4988",
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
      "008c4988",
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

- 旧版 [`008c4988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c497c.md#insn-008c4988)
- 新版 `008c4988`（命令位置の公開資料なし）

~~~diff
- 008c4988 ["COPY", "tmp:0:8", ["const:303:8"]]
- 008c4988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 008c4988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 008c4988 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 008c4988 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 008c4988 bytes 000c0c91
+ 008c4988 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-235757d0f6811a147235b23eea2bb174"></a>

### [`008c4994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4994.md) → [`008c4994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4994.md) FUN_008c4994

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
      "definition_site": "008c49b8",
      "incomplete_value": false,
      "site": "008c49b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c49b8",
      "incomplete_value": false,
      "site": "008c49b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "008c49b8",
      "DATA",
      [
        "storage",
        "00c076d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c49b8",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c49b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4994.md#insn-008c49b4)
- 新版 `008c49b4`（命令位置の公開資料なし）

~~~diff
- 008c49b4 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 008c49b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008c49b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c49b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c49b4 bytes 08411b91
+ 008c49b4 bytes 08811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1716e8f454b02dd0048521d227fe947"></a>

### [`008c49c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c49c8.md) → [`008c49c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c49c8.md) FUN_008c49c8

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
      "definition_site": "008c49d4",
      "incomplete_value": false,
      "site": "008c49d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c49d4",
      "incomplete_value": false,
      "site": "008c49d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:6d0:8"
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
      "008c49d4",
      "DATA",
      [
        "storage",
        "00c076d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c49d4",
      "DATA",
      [
        "storage",
        "00c07720",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c49d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c49c8.md#insn-008c49d0)
- 新版 `008c49d0`（命令位置の公開資料なし）

~~~diff
- 008c49d0 ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 008c49d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["COPY", "tmp:0:8", ["const:720:8"]]
+ 008c49d0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008c49d0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008c49d0 bytes 29411b91
+ 008c49d0 bytes 29811c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e18e29732f09c79072edbcc9c7cd7ed2"></a>

### [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) → [`008c4a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4a54.md) FUN_008c4a54

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008be334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008be/008be334.md) [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008be334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008be/008be334.md) [`008c4a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4a54.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "008c4bb0",
      "incomplete_value": false,
      "site": "008c4bb8",
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
      "definition_site": "008c4bb0",
      "incomplete_value": false,
      "site": "008c4bb8",
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
      "definition_site": "008c4d08",
      "incomplete_value": false,
      "site": "008c4d10",
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
      "definition_site": "008c4d08",
      "incomplete_value": false,
      "site": "008c4d10",
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
      "definition_site": "008c4d20",
      "incomplete_value": false,
      "site": "008c4d2c",
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
      "definition_site": "008c4d20",
      "incomplete_value": false,
      "site": "008c4d2c",
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
      "008c4bb0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008c4bd4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "008c4d08",
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
      "008c4bb0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "008c4bd4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "008c4d08",
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

- 旧版 [`008c4bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4bb0) · [`008c4bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4bd4) · [`008c4d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md#insn-008c4d08)
- 新版 `008c4bb0`（命令位置の公開資料なし） · `008c4bd4`（命令位置の公開資料なし） · `008c4d08`（命令位置の公開資料なし）

~~~diff
- 008c4bb0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008c4bb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008c4bb0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bb0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4bb0 bytes 21280c91
+ 008c4bb0 bytes 21900e91
- 008c4bd4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 008c4bd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4bd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4bd4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 008c4bd4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bd4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4bd4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4bd4 bytes 21642491
+ 008c4bd4 bytes 21142291
- 008c4d08 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 008c4d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 008c4d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c4d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c4d08 bytes 21b80b91
+ 008c4d08 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61041e066982cacea22913beb23c12de"></a>

### [`008c526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md) → [`008c526c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c5/008c526c.md) FUN_008c526c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`008c4a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c4/008c4a54.md) [`008c526c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`008c4a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c4/008c4a54.md) [`008c526c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c5/008c526c.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.69% / 新版 98.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c53c4",
      "incomplete_value": false,
      "site": "008c53cc",
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
      "definition_site": "008c53c4",
      "incomplete_value": false,
      "site": "008c53cc",
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
      "definition_site": "008c5498",
      "incomplete_value": false,
      "site": "008c54a4",
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
      "definition_site": "008c5498",
      "incomplete_value": false,
      "site": "008c54a4",
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008c5594",
      "incomplete_value": false,
      "site": "008c55a0",
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
      "definition_site": "008c5594",
      "incomplete_value": false,
      "site": "008c55a0",
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
      "008c53c4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "008c5480",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "008c5498",
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
      "008c53c4",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "008c5480",
      "PARAM",
      [
        "storage",
        "002a5379",
        null,
        null
      ]
    ],
    [
      "008c5498",
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

- 旧版 [`008c53c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c53c4) · [`008c5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c5480) · [`008c5498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c526c.md#insn-008c5498)
- 新版 `008c53c4`（命令位置の公開資料なし） · `008c5480`（命令位置の公開資料なし） · `008c5498`（命令位置の公開資料なし）

~~~diff
- 008c53c4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 008c53c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 008c53c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c53c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c53c4 bytes 21280c91
+ 008c53c4 bytes 21900e91
- 008c5480 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 008c5480 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c5480 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c5480 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 008c5480 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5480 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c5480 bytes 21b80b91
+ 008c5480 bytes 21e40d91
- 008c5498 ["COPY", "tmp:0:8", ["const:919:8"]]
- 008c5498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c5498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c5498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c5498 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 008c5498 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5498 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c5498 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c5498 bytes 21642491
+ 008c5498 bytes 21142291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dc45ce3e992969efa3d704b126b9034"></a>

### [`008c5d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d2c.md) → [`008c5d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c5/008c5d2c.md) FUN_008c5d2c

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
      "definition_site": "008c5d40",
      "incomplete_value": false,
      "site": "008c5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c5d40",
      "incomplete_value": false,
      "site": "008c5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "008c5d44",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c5d44",
      "DATA",
      [
        "storage",
        "00c077a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c5d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d2c.md#insn-008c5d40)
- 新版 `008c5d40`（命令位置の公開資料なし）

~~~diff
- 008c5d40 ["COPY", "tmp:0:8", ["const:750:8"]]
- 008c5d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008c5d40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c5d40 bytes 08411d91
+ 008c5d40 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6775a9ada35af5964d08a50f75e40db7"></a>

### [`008c5d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d50.md) → [`008c5d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c5/008c5d50.md) FUN_008c5d50

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
      "definition_site": "008c5d54",
      "incomplete_value": false,
      "site": "008c5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c5d54",
      "incomplete_value": false,
      "site": "008c5d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:750:8"
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
      "008c5d58",
      "DATA",
      [
        "storage",
        "00c07750",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c5d58",
      "DATA",
      [
        "storage",
        "00c077a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c5d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c5/008c5d50.md#insn-008c5d54)
- 新版 `008c5d54`（命令位置の公開資料なし）

~~~diff
- 008c5d54 ["COPY", "tmp:0:8", ["const:750:8"]]
- 008c5d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008c5d54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c5d54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c5d54 bytes 08411d91
+ 008c5d54 bytes 08811e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40c514a9b3ee420e84dfd20ac6ff0d79"></a>

### [`008c6ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6ae4.md) → [`008c6ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6ae4.md) FUN_008c6ae4

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
      "definition_site": "008c6af8",
      "incomplete_value": false,
      "site": "008c6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6af8",
      "incomplete_value": false,
      "site": "008c6afc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "008c6afc",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6afc",
      "DATA",
      [
        "storage",
        "00c07820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6ae4.md#insn-008c6af8)
- 新版 `008c6af8`（命令位置の公開資料なし）

~~~diff
- 008c6af8 ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 008c6af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["COPY", "tmp:0:8", ["const:820:8"]]
+ 008c6af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6af8 bytes 08411f91
+ 008c6af8 bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4cc60a113cb60f8fe2adf4e67f43c11"></a>

### [`008c6b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b08.md) → [`008c6b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6b08.md) FUN_008c6b08

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
      "definition_site": "008c6b0c",
      "incomplete_value": false,
      "site": "008c6b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:820:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6b0c",
      "incomplete_value": false,
      "site": "008c6b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:7d0:8"
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
      "008c6b10",
      "DATA",
      [
        "storage",
        "00c077d0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6b10",
      "DATA",
      [
        "storage",
        "00c07820",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b08.md#insn-008c6b0c)
- 新版 `008c6b0c`（命令位置の公開資料なし）

~~~diff
- 008c6b0c ["COPY", "tmp:0:8", ["const:7d0:8"]]
- 008c6b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["COPY", "tmp:0:8", ["const:820:8"]]
+ 008c6b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6b0c bytes 08411f91
+ 008c6b0c bytes 08812091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d66e9d289a1193f41e64315b9e66699b"></a>

### [`008c6b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md) → [`008c6b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6b20.md) FUN_008c6b20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00885f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00885/00885f80.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3ad:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3af:8"
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
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "008c6bc0",
      "incomplete_value": true,
      "site": "008c6bd0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6be4",
      "incomplete_value": false,
      "site": "008c6bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6be4",
      "incomplete_value": false,
      "site": "008c6bec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3af",
        null,
        "string"
      ]
    ],
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3bf",
        null,
        "string"
      ]
    ],
    [
      "008c6bec",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3ad",
        null,
        "string"
      ]
    ],
    [
      "008c6bc0",
      "READ",
      [
        "storage",
        "0029a3bd",
        null,
        "string"
      ]
    ],
    [
      "008c6bec",
      "DATA",
      [
        "storage",
        "00c07890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md#insn-008c6bbc) · [`008c6be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md#insn-008c6be4) · [`008c6be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6b20.md#insn-008c6be8)
- 新版 `008c6bbc`（命令位置の公開資料なし） · `008c6be4`（命令位置の公開資料なし）

~~~diff
- 008c6bbc ["COPY", "tmp:0:8", ["const:3af:8"]]
- 008c6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["COPY", "tmp:0:8", ["const:3ad:8"]]
+ 008c6bbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6bbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6bbc bytes 08bd0e91
+ 008c6bbc bytes 08b50e91
- 008c6be4 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008c6be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 008c6be4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6be4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6be4 bytes 08012191
+ 008c6be4 bytes 08412291
- 008c6be8 ["COPY", "tmp:0:8", ["const:30:8"]]
- 008c6be8 ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 008c6be8 ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 008c6be8 ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 008c6be8 bytes f5c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0018d1f6268c6863673d15fd622d02fc"></a>

### [`008c6d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d50.md) → [`008c6d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6d50.md) FUN_008c6d50

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
      "definition_site": "008c6d64",
      "incomplete_value": false,
      "site": "008c6d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6d64",
      "incomplete_value": false,
      "site": "008c6d68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "008c6d68",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6d68",
      "DATA",
      [
        "storage",
        "00c07890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d50.md#insn-008c6d64)
- 新版 `008c6d64`（命令位置の公開資料なし）

~~~diff
- 008c6d64 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008c6d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 008c6d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6d64 bytes 08012191
+ 008c6d64 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-422b6c7e86ea233766db716ea2dfbddc"></a>

### [`008c6d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d74.md) → [`008c6d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6d74.md) FUN_008c6d74

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
      "definition_site": "008c6d78",
      "incomplete_value": false,
      "site": "008c6d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6d78",
      "incomplete_value": false,
      "site": "008c6d7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:840:8"
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
      "008c6d7c",
      "DATA",
      [
        "storage",
        "00c07840",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008c6d7c",
      "DATA",
      [
        "storage",
        "00c07890",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6d74.md#insn-008c6d78)
- 新版 `008c6d78`（命令位置の公開資料なし）

~~~diff
- 008c6d78 ["COPY", "tmp:0:8", ["const:840:8"]]
- 008c6d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["COPY", "tmp:0:8", ["const:890:8"]]
+ 008c6d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6d78 bytes 08012191
+ 008c6d78 bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f23b306e5b32afe53a254e71599096a6"></a>

### [`008c6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md) → [`008c6e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c6/008c6e18.md) FUN_008c6e18

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c2704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c2/008c2704.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) [`00830c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00832/00832580.md)
- 新版 呼出元 1件 [`008c2704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c2/008c2704.md) · 呼出先 12件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) [`00830c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00830/00830c98.md) [`00832580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00832/00832580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.46% / 新版 88.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 28件, `store_destination` 7件, `store_value` 18件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c6e50",
      "incomplete_value": false,
      "site": "008c6e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6e50",
      "incomplete_value": false,
      "site": "008c6e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "definition_site": "008c6e98",
      "incomplete_value": true,
      "site": "008c6e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6e98",
      "incomplete_value": true,
      "site": "008c6e98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:895:8"
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
      "definition_site": "008c6eb0",
      "incomplete_value": true,
      "site": "008c6eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c6eb0",
      "incomplete_value": true,
      "site": "008c6eb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7ff:8"
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
      "008c6e5c",
      "DATA",
      [
        "storage",
        "00c078d0",
        null,
        "pointer"
      ]
    ],
    [
      "008c6e68",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "008c6e88",
      "READ",
      [
        "storage",
        "002a5895",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c6e5c",
      "DATA",
      [
        "storage",
        "00c07920",
        null,
        "pointer"
      ]
    ],
    [
      "008c6e68",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "008c6e88",
      "READ",
      [
        "storage",
        "002a5920",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md#insn-008c6e50) · [`008c6e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c6/008c6e18.md#insn-008c6e54)
- 新版 `008c6e50`（命令位置の公開資料なし） · `008c6e54`（命令位置の公開資料なし）

~~~diff
- 008c6e50 ["COPY", "tmp:0:8", ["const:8d0:8"]]
- 008c6e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 008c6e50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c6e50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c6e50 bytes 08412391
+ 008c6e50 bytes 08812491
- 008c6e54 ["COPY", "register:40c0:8", ["const:c25000:8"]]
- 008c6e54 bytes f81a00f0
+ 008c6e54 ["COPY", "register:40c0:8", ["const:c25000:8"]]
+ 008c6e54 bytes f81a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-032e21972e2209ecda1bf80e241eb633"></a>

### [`008c7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md) → [`008c7afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c7/008c7afc.md) FUN_008c7afc

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
      "definition_site": "008c7b14",
      "incomplete_value": false,
      "site": "008c7b18",
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
      "definition_site": "008c7b14",
      "incomplete_value": false,
      "site": "008c7b18",
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
      "definition_site": "008c7b50",
      "incomplete_value": false,
      "site": "008c7b54",
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
      "definition_site": "008c7b50",
      "incomplete_value": false,
      "site": "008c7b54",
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
      "008c7b18",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "008c7b54",
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
      "008c7b18",
      "DATA",
      [
        "storage",
        "00bfae08",
        null,
        "pointer"
      ]
    ],
    [
      "008c7b54",
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

- 旧版 [`008c7b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md#insn-008c7b14) · [`008c7b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7afc.md#insn-008c7b50)
- 新版 `008c7b14`（命令位置の公開資料なし） · `008c7b50`（命令位置の公開資料なし）

~~~diff
- 008c7b14 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 008c7b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 008c7b14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c7b14 bytes 08e13691
+ 008c7b14 bytes 08213891
- 008c7b50 ["COPY", "tmp:0:8", ["const:298:8"]]
- 008c7b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 008c7b50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c7b50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c7b50 bytes 08610a91
+ 008c7b50 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b623191d2b626cf8bc905490b79735f"></a>

### [`008c7b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md) → [`008c7b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c7/008c7b9c.md) _INIT_170

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.27% / 新版 89.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7bd8",
      "incomplete_value": true,
      "site": "008c7bf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7bd8",
      "incomplete_value": true,
      "site": "008c7bf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "008c7bfc",
      "incomplete_value": true,
      "site": "008c7c18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7bfc",
      "incomplete_value": true,
      "site": "008c7c18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "008c7c1c",
      "incomplete_value": true,
      "site": "008c7c38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7c1c",
      "incomplete_value": true,
      "site": "008c7c38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "008c7bd8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008c7bfc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008c7c1c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c7bd8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008c7bfc",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008c7c1c",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c7bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md#insn-008c7bc8) · [`008c7bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7b9c.md#insn-008c7bd0)
- 新版 `008c7bc8`（命令位置の公開資料なし） · `008c7bd0`（命令位置の公開資料なし）

~~~diff
- 008c7bc8 ["COPY", "tmp:0:8", ["const:748:8"]]
- 008c7bc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["COPY", "tmp:0:8", ["const:788:8"]]
+ 008c7bc8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7bc8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008c7bc8 bytes 73221d91
+ 008c7bc8 bytes 73221e91
- 008c7bd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008c7bd0 bytes 09cfff90
+ 008c7bd0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008c7bd0 bytes 09cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8544b3a13e281082de4c5c0efb3c900d"></a>

### [`008c7f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md) → [`008c7f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c7/008c7f2c.md) _INIT_171

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008c7f68",
      "incomplete_value": true,
      "site": "008c7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:377:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7f68",
      "incomplete_value": true,
      "site": "008c7f84",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2dd:8"
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
      "definition_site": "008c7f8c",
      "incomplete_value": true,
      "site": "008c7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:38a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7f8c",
      "incomplete_value": true,
      "site": "008c7fa8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f0:8"
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
      "definition_site": "008c7fac",
      "incomplete_value": true,
      "site": "008c7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c7fac",
      "incomplete_value": true,
      "site": "008c7fc8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:46:8"
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
      "008c7f68",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "008c7f8c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "008c7fac",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "008c7f68",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "008c7f8c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "008c7fac",
      "READ",
      [
        "storage",
        "002a80e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c7f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md#insn-008c7f58) · [`008c7f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c7/008c7f2c.md#insn-008c7f60)
- 新版 `008c7f58`（命令位置の公開資料なし） · `008c7f60`（命令位置の公開資料なし）

~~~diff
- 008c7f58 ["COPY", "tmp:0:8", ["const:760:8"]]
- 008c7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 008c7f58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 008c7f58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 008c7f58 bytes 73821d91
+ 008c7f58 bytes 73821e91
- 008c7f60 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 008c7f60 bytes 09cfff90
+ 008c7f60 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 008c7f60 bytes 09cfff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca243bef3004357d24dcef685f98940e"></a>

### [`008c8b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8b30.md) → [`008c8b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8b30.md) FUN_008c8b30

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008c8580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8580.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`008c8580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8580.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 comparison, comparison_count, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 96.04% / 新版 96.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c8b9c",
      "incomplete_value": false,
      "site": "008c8ba0",
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
      "definition_site": "008c8b9c",
      "incomplete_value": false,
      "site": "008c8ba0",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8d0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "008c8d10"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c8ba0",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "unmatched:008c8cfc",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:008c8d00",
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
      "008c8ba0",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "008c8cfc",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "008c8d00",
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

- 旧版 [`008c8d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8b30.md#insn-008c8d0c) · [`008c8d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8b30.md#insn-008c8d10)
- 新版 `008c8d0c`（命令位置の公開資料なし）

~~~diff
- 008c8d0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
- 008c8d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 008c8d0c bytes e80f00f9
+ 008c8d0c ["INT_ADD", "tmp:0:8", ["register:8:8", "const:18:8"]]
+ 008c8d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 008c8d0c bytes e80f00f9
- 008c8d10 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:60:8"]]
- 008c8d10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008c8d10 bytes e93300f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51f1e2370f13299f2dc78c932246d1e3"></a>

### [`008c9490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md) → [`008c9490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c9/008c9490.md) FUN_008c9490

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cacc4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8b0.md)
- 新版 呼出元 1件 [`008cacc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cacc4.md) · 呼出先 43件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a0.md) [`0044b8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008c9624",
      "incomplete_value": false,
      "site": "008c9624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c9624",
      "incomplete_value": false,
      "site": "008c9624",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "definition_site": "008c96a4",
      "incomplete_value": false,
      "site": "008c96a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c96a4",
      "incomplete_value": false,
      "site": "008c96a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "definition_site": "008c9eb0",
      "incomplete_value": false,
      "site": "008c9eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008c9eb0",
      "incomplete_value": false,
      "site": "008c9eb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "ordinal": 76,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008c9624",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ],
    [
      "008c96a4",
      "DATA",
      [
        "storage",
        "00c07a08",
        null,
        "undefined *"
      ]
    ],
    [
      "008c9844",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008c9624",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ],
    [
      "008c96a4",
      "DATA",
      [
        "storage",
        "00c07a58",
        null,
        "undefined *"
      ]
    ],
    [
      "008c9844",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008c9620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c9620) · [`008c96a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c96a0) · [`008c9844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c9/008c9490.md#insn-008c9844)
- 新版 `008c9620`（命令位置の公開資料なし） · `008c96a0`（命令位置の公開資料なし） · `008c9844`（命令位置の公開資料なし）

~~~diff
- 008c9620 ["COPY", "tmp:0:8", ["const:908:8"]]
- 008c9620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c9620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c9620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 008c9620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c9620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c9620 bytes 08212491
+ 008c9620 bytes 08612591
- 008c96a0 ["COPY", "tmp:0:8", ["const:a08:8"]]
- 008c96a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 008c96a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008c96a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008c96a0 bytes 08212891
+ 008c96a0 bytes 08612991
- 008c9844 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008c9844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008c9844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008c9844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008c9844 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008c9844 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008c9844 bytes 21203991
+ 008c9844 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2748a90d2b3af812d56395cd30630c8c"></a>

### [`008ca5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md) → [`008ca5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008ca5c0.md) FUN_008ca5c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`008cafd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`0044626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/0044626c.md) [`00448e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md)
- 新版 呼出元 1件 [`008cafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cafd4.md) · 呼出先 12件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`0044626c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/0044626c.md) [`00448e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448e7c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "008ca608",
      "incomplete_value": true,
      "site": "008ca614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ca608",
      "incomplete_value": true,
      "site": "008ca614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4010:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "definition_site": "008ca698",
      "incomplete_value": false,
      "site": "008ca6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008ca698",
      "incomplete_value": false,
      "site": "008ca6ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "008ca5f4",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008ca600",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ca608",
      "PARAM",
      [
        "storage",
        "00c078e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008ca5f4",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008ca600",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008ca608",
      "PARAM",
      [
        "storage",
        "00c07930",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008ca5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca5f4) · [`008ca600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca600) · [`008ca608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca5c0.md#insn-008ca608)
- 新版 `008ca5f4`（命令位置の公開資料なし） · `008ca600`（命令位置の公開資料なし） · `008ca608`（命令位置の公開資料なし）

~~~diff
- 008ca5f4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 008ca5f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008ca5f4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 008ca5f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008ca5f4 bytes c83e45f9
+ 008ca5f4 bytes c85e45f9
- 008ca600 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008ca600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008ca600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008ca600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008ca600 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008ca600 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008ca600 bytes 21203991
+ 008ca600 bytes 21603a91
- 008ca608 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 008ca608 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008ca608 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008ca608 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 008ca608 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008ca608 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008ca608 bytes 42802391
+ 008ca608 bytes 42c02491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e097d1820af9fa2385c15bf80287b4ce"></a>

### [`008ca974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md) → [`008ca974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008ca974.md) FUN_008ca974

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 19件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00646dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646dc4.md) [`008381ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/008381ac.md) [`008c8580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008c8/008c8580.md) [`008cb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb860.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 19件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00646dc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646dc4.md) [`008381ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00838/008381ac.md) [`008c8580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008c8/008c8580.md) [`008cb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb860.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 92.02% / 新版 92.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008caae8",
      "incomplete_value": false,
      "site": "008caae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008caae8",
      "incomplete_value": false,
      "site": "008caae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c24000:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "008caae0",
      "incomplete_value": true,
      "site": "008caae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "008caae0",
      "incomplete_value": true,
      "site": "008caae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "008caaec",
      "incomplete_value": false,
      "site": "008caaec",
      "value": [
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
    },
    "old": {
      "definition_site": "008caaec",
      "incomplete_value": false,
      "site": "008caaec",
      "value": [
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
    },
    "ordinal": 37,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "008caae0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae4",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae8",
      "WRITE",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "008caae0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae4",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "008caae8",
      "WRITE",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008caae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008caae8) · [`008caaec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008caaec) · [`008cab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008ca974.md#insn-008cab04)
- 新版 `008caae8`（命令位置の公開資料なし） · `008caaec`（命令位置の公開資料なし） · `008cab04`（命令位置の公開資料なし）

~~~diff
- 008caae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 008caae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 008caae8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 008caae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 008caae8 bytes 093505f9
+ 008caae8 bytes 095505f9
- 008caaec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 008caaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 008caaec ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 008caaec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 008caaec bytes ca3e05f9
+ 008caaec bytes ca5e05f9
- 008cab04 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 008cab04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 008cab04 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 008cab04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 008cab04 bytes d43e05f9
+ 008cab04 bytes d45e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5db29cbfb0413de90f8df0d2b04ad7d"></a>

### [`008cafd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md) → [`008cafd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008ca/008cafd4.md) FUN_008cafd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 15件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044507c.md) [`00446d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/00446d2c.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

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
      "definition_site": "008caff4",
      "incomplete_value": true,
      "site": "008caff4",
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
      "definition_site": "008caff4",
      "incomplete_value": true,
      "site": "008caff4",
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
      "definition_site": "008cb004",
      "incomplete_value": false,
      "site": "008cb018",
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
      "definition_site": "008cb004",
      "incomplete_value": false,
      "site": "008cb018",
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
      "definition_site": "008cb00c",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:930:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb00c",
      "incomplete_value": false,
      "site": "008cb018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:8e0:8"
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
      "008caff0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb004",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008cb00c",
      "PARAM",
      [
        "storage",
        "00c078e0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "008caff0",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "008cb004",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "008cb00c",
      "PARAM",
      [
        "storage",
        "00c07930",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008caff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008caff0) · [`008cb004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008cb004) · [`008cb00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008ca/008cafd4.md#insn-008cb00c)
- 新版 `008caff0`（命令位置の公開資料なし） · `008cb004`（命令位置の公開資料なし） · `008cb00c`（命令位置の公開資料なし）

~~~diff
- 008caff0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 008caff0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 008caff0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 008caff0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 008caff0 bytes 083d45f9
+ 008caff0 bytes 085d45f9
- 008cb004 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 008cb004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 008cb004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 008cb004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 008cb004 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 008cb004 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 008cb004 bytes 21203991
+ 008cb004 bytes 21603a91
- 008cb00c ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 008cb00c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 008cb00c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 008cb00c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["COPY", "tmp:0:8", ["const:930:8"]]
+ 008cb00c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 008cb00c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 008cb00c bytes 42802391
+ 008cb00c bytes 42c02491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e6a108176e4fa770878010f26597a57"></a>

### [`008cb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb190.md) → [`008cb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb190.md) FUN_008cb190

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
      "definition_site": "008cb1b4",
      "incomplete_value": false,
      "site": "008cb1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb1b4",
      "incomplete_value": false,
      "site": "008cb1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "008cb1b4",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb1b4",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb190.md#insn-008cb1b0)
- 新版 `008cb1b0`（命令位置の公開資料なし）

~~~diff
- 008cb1b0 ["COPY", "tmp:0:8", ["const:908:8"]]
- 008cb1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 008cb1b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb1b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb1b0 bytes 08212491
+ 008cb1b0 bytes 08612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1110ac144e1b15b6ca9385e3b627331b"></a>

### [`008cb1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb1c4.md) → [`008cb1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb1c4.md) FUN_008cb1c4

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
      "definition_site": "008cb1d0",
      "incomplete_value": false,
      "site": "008cb1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb1d0",
      "incomplete_value": false,
      "site": "008cb1d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:908:8"
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
      "008cb1d0",
      "DATA",
      [
        "storage",
        "00c07908",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb1d0",
      "DATA",
      [
        "storage",
        "00c07958",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb1c4.md#insn-008cb1cc)
- 新版 `008cb1cc`（命令位置の公開資料なし）

~~~diff
- 008cb1cc ["COPY", "tmp:0:8", ["const:908:8"]]
- 008cb1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["COPY", "tmp:0:8", ["const:958:8"]]
+ 008cb1cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 008cb1cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 008cb1cc bytes 29212491
+ 008cb1cc bytes 29612591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84df13bab60457a75ef9945b6edef2cf"></a>

### [`008cb258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb258.md) → [`008cb258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008cb/008cb258.md) FUN_008cb258

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059d/0059d12c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0059d12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0059d/0059d12c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "008cb274",
      "incomplete_value": false,
      "site": "008cb274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "008cb274",
      "incomplete_value": false,
      "site": "008cb274",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c07000:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "008cb274",
      "DATA",
      [
        "storage",
        "00c07988",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "008cb274",
      "DATA",
      [
        "storage",
        "00c079d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`008cb26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008cb/008cb258.md#insn-008cb26c)
- 新版 `008cb26c`（命令位置の公開資料なし）

~~~diff
- 008cb26c ["COPY", "tmp:0:8", ["const:988:8"]]
- 008cb26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 008cb26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 008cb26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 008cb26c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 008cb26c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 008cb26c bytes 08212691
+ 008cb26c bytes 08612791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

