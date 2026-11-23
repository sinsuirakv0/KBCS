# v15.7.2 → v15.7.3 · 最優先の変更候補 (6)

[一覧の目次](README.md)

<a id="compare-6052a26ef548f7d807de577de1988a60"></a>

### [`00468c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00468/00468c18.md) → [`00468c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00468/00468c18.md) _INIT_20

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00467090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467090.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00b7d194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00467090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467090.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value, unresolved_call_alignment

命令の説明率　旧版 64.47% / 新版 64.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 28件, `store_value` 13件, `unresolved_call_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00468c58",
      "incomplete_value": true,
      "site": "00468c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00468c58",
      "incomplete_value": true,
      "site": "00468c74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "00468c7c",
      "incomplete_value": true,
      "site": "00468c98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00468c7c",
      "incomplete_value": true,
      "site": "00468c98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "00468c9c",
      "incomplete_value": true,
      "site": "00468cb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00468c9c",
      "incomplete_value": true,
      "site": "00468cb8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "00468c58",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00468c7c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00468c9c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00468c58",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00468c7c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00468c9c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00468c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00468/00468c18.md#insn-00468c44) · [`00468c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00468/00468c18.md#insn-00468c48) · [`00468c50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00468/00468c18.md#insn-00468c50)
- 新版 `00468c44`（命令位置の公開資料なし） · `00468c48`（命令位置の公開資料なし）

~~~diff
- 00468c44 ["COPY", "register:4098:8", ["const:c24000:8"]]
+ 00468c44 ["COPY", "register:4098:8", ["const:c25000:8"]]
- 00468c44 bytes f33d0090
+ 00468c44 bytes f33d00b0
- 00468c48 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00468c48 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00468c48 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00468c48 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00468c48 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00468c48 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00468c48 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00468c48 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00468c48 bytes 73423f91
+ 00468c48 bytes 73420291
- 00468c50 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00468c50 bytes e9f1fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55bf6dc0d451a109dd75ef4f1089ce5"></a>

### [`00469128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md) → [`00469128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469128.md) FUN_00469128

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00469128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md) [`008818a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00881/008818a8.md) [`0090f708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0090f/0090f708.md) [`00971a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0097a/0097a888.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 5件 [`00469128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469128.md) [`008818a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00881/008818a8.md) [`0090f708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0090f/0090f708.md) [`00971a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00971/00971a68.md) [`0097a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.07% / 新版 99.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00469280",
      "incomplete_value": false,
      "site": "00469288",
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
    "old": {
      "definition_site": "00469280",
      "incomplete_value": false,
      "site": "00469288",
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
            "const:311:8"
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
      "definition_site": "0046933c",
      "incomplete_value": false,
      "site": "00469344",
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
    "old": {
      "definition_site": "0046933c",
      "incomplete_value": false,
      "site": "00469344",
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
            "const:2f5:8"
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
      "definition_site": "004696ac",
      "incomplete_value": false,
      "site": "004696bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:672:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004696ac",
      "incomplete_value": false,
      "site": "004696bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:292000:8"
          ],
          [
            "leaf",
            "const:5e5:8"
          ]
        ]
      ]
    },
    "ordinal": 26,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00469280",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0046933c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "004696ac",
      "PARAM",
      [
        "storage",
        "002925e5",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00469280",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0046933c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "004696ac",
      "PARAM",
      [
        "storage",
        "00292672",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00469280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md#insn-00469280) · [`0046933c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md#insn-0046933c) · [`004696ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469128.md#insn-004696ac)
- 新版 `00469280`（命令位置の公開資料なし） · `0046933c`（命令位置の公開資料なし） · `004696ac`（命令位置の公開資料なし）

~~~diff
- 00469280 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00469280 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00469280 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00469280 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00469280 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00469280 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00469280 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00469280 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00469280 bytes 21440c91
+ 00469280 bytes 21280c91
- 0046933c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0046933c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046933c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046933c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046933c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0046933c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046933c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046933c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046933c bytes 21d40b91
+ 0046933c bytes 21b80b91
- 004696ac ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 004696ac ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004696ac ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004696ac ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004696ac ["COPY", "tmp:0:8", ["const:672:8"]]
+ 004696ac ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004696ac ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004696ac ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004696ac bytes 63941791
+ 004696ac bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615f72cd8a08680f1af25ffa47f1d65c"></a>

### [`00469a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469a60.md) → [`00469a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469a60.md) _INIT_21

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "00469a9c",
      "incomplete_value": true,
      "site": "00469ab8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469a9c",
      "incomplete_value": true,
      "site": "00469ab8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "00469ac0",
      "incomplete_value": true,
      "site": "00469adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469ac0",
      "incomplete_value": true,
      "site": "00469adc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "00469ae0",
      "incomplete_value": true,
      "site": "00469afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00469ae0",
      "incomplete_value": true,
      "site": "00469afc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "00469a9c",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00469ac0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00469ae0",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00469a9c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00469ac0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00469ae0",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00469a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469a60.md#insn-00469a8c) · [`00469a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469a60.md#insn-00469a94)
- 新版 `00469a8c`（命令位置の公開資料なし） · `00469a94`（命令位置の公開資料なし）

~~~diff
- 00469a8c ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00469a8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00469a8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00469a8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00469a8c ["COPY", "tmp:0:8", ["const:178:8"]]
+ 00469a8c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00469a8c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00469a8c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00469a8c bytes 73e20291
+ 00469a8c bytes 73e20591
- 00469a94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00469a94 bytes e9f1ffd0
+ 00469a94 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00469a94 bytes e9f1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ef3571c96423eb5a6bb93debf0dba39"></a>

### [`00469df0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469df0.md) → [`00469df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469df0.md) FUN_00469df0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080dd1c.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0080dd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080dd1c.md) · 呼出先 0件 

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
      "definition_site": "00469df4",
      "incomplete_value": false,
      "site": "00469dfc",
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
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00469df4",
      "incomplete_value": false,
      "site": "00469dfc",
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
      "00469dfc",
      "DATA",
      [
        "storage",
        "00be8858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00469dfc",
      "DATA",
      [
        "storage",
        "00be8908",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00469df4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469df0.md#insn-00469df4)
- 新版 `00469df4`（命令位置の公開資料なし）

~~~diff
- 00469df4 ["COPY", "tmp:0:8", ["const:858:8"]]
- 00469df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00469df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00469df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00469df4 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00469df4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00469df4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00469df4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00469df4 bytes 08612191
+ 00469df4 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4f44a819c162637dfad96766061d0bc"></a>

### [`0046a090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a090.md) → [`0046a090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a090.md) FUN_0046a090

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0046a08c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a08c.md) · 呼出先 12件 [`004365f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/004365f8.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md)
- 新版 呼出元 1件 [`0046a08c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046a08c.md) · 呼出先 12件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046a0f8",
      "incomplete_value": true,
      "site": "0046a0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0046a0f8",
      "incomplete_value": true,
      "site": "0046a0fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046a0f4",
      "incomplete_value": true,
      "site": "0046a100",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0046a0f4",
      "incomplete_value": true,
      "site": "0046a100",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046a108",
      "incomplete_value": true,
      "site": "0046a108",
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
                "const:10:8"
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
      "definition_site": "0046a108",
      "incomplete_value": true,
      "site": "0046a108",
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
                "const:10:8"
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
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046a0e4",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ],
    [
      "0046a0e8",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0046a0f4",
      "READ",
      [
        "storage",
        "00c13360",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0046a0e4",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "0046a0e8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0046a0f4",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046a0e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a090.md#insn-0046a0e4) · [`0046a0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a090.md#insn-0046a0e8) · [`0046a150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046a090.md#insn-0046a150)
- 新版 `0046a0e4`（命令位置の公開資料なし） · `0046a0e8`（命令位置の公開資料なし） · `0046a150`（命令位置の公開資料なし）

~~~diff
- 0046a0e4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d98:8"]]
- 0046a0e4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046a0e4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e48:8"]]
+ 0046a0e4 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0046a0e4 bytes 39cf46f9
+ 0046a0e4 bytes 392747f9
- 0046a0e8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:cc8:8"]]
- 0046a0e8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046a0e8 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d78:8"]]
+ 0046a0e8 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 0046a0e8 bytes 186746f9
+ 0046a0e8 bytes 18bf46f9
- 0046a150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:cd0:8"]]
- 0046a150 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046a150 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d80:8"]]
+ 0046a150 ["LOAD", "register:40c8:8", ["const:1b1:8", "tmp:0:8"]]
- 0046a150 bytes 396b46f9
+ 0046a150 bytes 39c346f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a846596b10962ac64fc26ea508e640c"></a>

### [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) → [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) FUN_0046c018

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 22件 [`005a2308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a2/005a2308.md) [`006091c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00609/006091c4.md) [`00629194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00629/00629194.md) [`00632468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00632/00632468.md) [`006833dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00683/006833dc.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md)
- 新版 呼出元 22件 [`005a2308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a2/005a2308.md) [`006091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md) [`00629194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00629/00629194.md) [`00632468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632468.md) [`006833dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00683/006833dc.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `call_target` 1件, `store_destination` 1件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046c0cc",
      "incomplete_value": false,
      "site": "0046c0cc",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c0cc",
      "incomplete_value": false,
      "site": "0046c0cc",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046c19c",
      "incomplete_value": true,
      "site": "0046c19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046c19c",
      "incomplete_value": true,
      "site": "0046c19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046c2e8",
      "incomplete_value": true,
      "site": "0046c2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046c2e8",
      "incomplete_value": true,
      "site": "0046c2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0046c0c4",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c0cc",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c138",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046c0c4",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c0cc",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c138",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c0bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md#insn-0046c0bc) · [`0046c138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md#insn-0046c138) · [`0046c180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md#insn-0046c180)
- 新版 `0046c0bc`（命令位置の公開資料なし） · `0046c138`（命令位置の公開資料なし） · `0046c180`（命令位置の公開資料なし）

~~~diff
- 0046c0bc ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046c0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046c0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046c0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046c0bc ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046c0bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046c0bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046c0bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046c0bc bytes 08410591
+ 0046c0bc bytes 08410891
- 0046c138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c78:8"]]
- 0046c138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046c138 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
+ 0046c138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046c138 bytes 083d46f9
+ 0046c138 bytes 089546f9
- 0046c180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0046c180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046c180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
+ 0046c180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046c180 bytes 08e946f9
+ 0046c180 bytes 084147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6bbaeb5e5f5c7e89235155c7bf7baf9"></a>

### [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md) → [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md) FUN_0046c4c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md) [`0046ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046ede4.md) [`0046f248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db24.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 9件 [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d7c4.md) [`0046ede4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046ede4.md) [`0046f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f248.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db24.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
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
                "const:210:8"
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
      "definition_site": "0046c4dc",
      "incomplete_value": false,
      "site": "0046c4dc",
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
                "const:150:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0046c4e0",
      "incomplete_value": true,
      "site": "0046c4e0",
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
      "definition_site": "0046c4e0",
      "incomplete_value": true,
      "site": "0046c4e0",
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
      "0046c4d8",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c4dc",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c4dc",
      "WRITE",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046c4d8",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c4dc",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c4dc",
      "WRITE",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md#insn-0046c4d4) · [`0046c510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md#insn-0046c510)
- 新版 `0046c4d4`（命令位置の公開資料なし） · `0046c510`（命令位置の公開資料なし）

~~~diff
- 0046c4d4 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046c4d4 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046c4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046c4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046c4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046c4d4 bytes 08410591
+ 0046c4d4 bytes 08410891
- 0046c510 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 0046c510 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046c510 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 0046c510 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046c510 bytes 00a140f9
+ 0046c510 bytes 000141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1bf429c1b71f9c36ed545641122f97b"></a>

### [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md) → [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) FUN_0046c588

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 8件 [`0046c018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md) [`0046dc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046dc5c.md) [`0046e4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046e4f8.md) · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`00423878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423878.md) [`00426cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426cec.md) [`00426e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md) [`0052db30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db30.md)
- 新版 呼出元 8件 [`0046c018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c018.md) [`0046d29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d29c.md) [`0046d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d7c4.md) [`0046dc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046dc5c.md) [`0046e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046e4f8.md) · 呼出先 17件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00423878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423878.md) [`00426cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426cec.md) [`00426e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) [`0052db30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db30.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.72% / 新版 95.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_value` 13件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046c8ec",
      "incomplete_value": true,
      "site": "0046c900",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:255:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046c8ec",
      "incomplete_value": true,
      "site": "0046c900",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1c8:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0046c8f0",
      "incomplete_value": true,
      "site": "0046c904",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0046c8f0",
      "incomplete_value": true,
      "site": "0046c904",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046c938",
      "incomplete_value": true,
      "site": "0046c948",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0046c938",
      "incomplete_value": true,
      "site": "0046c948",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046c6a0",
      "READ",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c76c",
      "PARAM",
      [
        "storage",
        "0029e1b6",
        null,
        "string"
      ]
    ],
    [
      "0046c828",
      "READ",
      [
        "storage",
        "0029aac2",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0046c6a0",
      "READ",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046c76c",
      "PARAM",
      [
        "storage",
        "0029e243",
        null,
        "string"
      ]
    ],
    [
      "0046c828",
      "READ",
      [
        "storage",
        "0029ab4f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046c6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md#insn-0046c6a0) · [`0046c76c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md#insn-0046c76c) · [`0046c804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md#insn-0046c804)
- 新版 `0046c6a0`（命令位置の公開資料なし） · `0046c76c`（命令位置の公開資料なし） · `0046c804`（命令位置の公開資料なし）

~~~diff
- 0046c6a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:150:8"]]
- 0046c6a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046c6a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:210:8"]]
+ 0046c6a0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046c6a0 bytes 00a940f9
+ 0046c6a0 bytes 000941f9
- 0046c76c ["COPY", "tmp:0:8", ["const:1b6:8"]]
- 0046c76c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0046c76c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0046c76c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0046c76c ["COPY", "tmp:0:8", ["const:243:8"]]
+ 0046c76c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0046c76c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0046c76c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0046c76c bytes 21d80691
+ 0046c76c bytes 210c0991
- 0046c804 ["COPY", "tmp:0:8", ["const:ac2:8"]]
- 0046c804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046c804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046c804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046c804 ["COPY", "tmp:0:8", ["const:b4f:8"]]
+ 0046c804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046c804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046c804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046c804 bytes 29092b91
+ 0046c804 bytes 293d2d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de4b5f972ee9f50bef86460200361329"></a>

### [`0046d29c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md) → [`0046d29c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d29c.md) FUN_0046d29c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) · 呼出先 21件 [`00449c2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c2c.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 21件 [`00449c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c2c.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.07% / 新版 90.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d300",
      "incomplete_value": true,
      "site": "0046d314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5fb:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d300",
      "incomplete_value": true,
      "site": "0046d314",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:602:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d3d8",
      "incomplete_value": false,
      "site": "0046d3d8",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d3d8",
      "incomplete_value": false,
      "site": "0046d3d8",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046d480",
      "incomplete_value": true,
      "site": "0046d480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d480",
      "incomplete_value": true,
      "site": "0046d480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0046d300",
      "READ",
      [
        "storage",
        "002a6602",
        null,
        "string"
      ]
    ],
    [
      "0046d34c",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "0046d350",
      "PARAM",
      [
        "storage",
        "00c24cb0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046d300",
      "READ",
      [
        "storage",
        "002a65fb",
        null,
        "string"
      ]
    ],
    [
      "0046d34c",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0046d350",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md#insn-0046d2f8) · [`0046d34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md#insn-0046d34c) · [`0046d3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d29c.md#insn-0046d3c8)
- 新版 `0046d2f8`（命令位置の公開資料なし） · `0046d34c`（命令位置の公開資料なし） · `0046d3c8`（命令位置の公開資料なし）

~~~diff
- 0046d2f8 ["COPY", "tmp:0:8", ["const:602:8"]]
- 0046d2f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0046d2f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0046d2f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0046d2f8 ["COPY", "tmp:0:8", ["const:5fb:8"]]
+ 0046d2f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0046d2f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0046d2f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0046d2f8 bytes 29091891
+ 0046d2f8 bytes 29ed1791
- 0046d34c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:c78:8"]]
- 0046d34c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d34c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d28:8"]]
+ 0046d34c ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d34c bytes f73e46f9
+ 0046d34c bytes f79646f9
- 0046d3c8 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046d3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046d3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046d3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046d3c8 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046d3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046d3c8 bytes 08410591
+ 0046d3c8 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edab48cecac0989e44e3c2d6bb8c22e2"></a>

### [`0046d7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md) → [`0046d7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046d7c4.md) FUN_0046d7c4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0094ac20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0094a/0094ac20.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md)
- 新版 呼出元 1件 [`0094ac20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094a/0094ac20.md) · 呼出先 17件 [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046d8a8",
      "incomplete_value": false,
      "site": "0046d8a8",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046d8a8",
      "incomplete_value": false,
      "site": "0046d8a8",
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
            "const:150:8"
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
      "definition_site": "0046d93c",
      "incomplete_value": true,
      "site": "0046d93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046d93c",
      "incomplete_value": true,
      "site": "0046d93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046da84",
      "incomplete_value": true,
      "site": "0046da84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046da84",
      "incomplete_value": true,
      "site": "0046da84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046d834",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "0046d83c",
      "READ",
      [
        "storage",
        "00c24cd4",
        null,
        "undefined4"
      ]
    ],
    [
      "0046d8a0",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046d834",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0046d83c",
      "READ",
      [
        "storage",
        "00c24d94",
        null,
        "undefined4"
      ]
    ],
    [
      "0046d8a0",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046d834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md#insn-0046d834) · [`0046d898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md#insn-0046d898) · [`0046d91c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046d7c4.md#insn-0046d91c)
- 新版 `0046d834`（命令位置の公開資料なし） · `0046d898`（命令位置の公開資料なし） · `0046d91c`（命令位置の公開資料なし）

~~~diff
- 0046d834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c78:8"]]
- 0046d834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d834 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
+ 0046d834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d834 bytes 083d46f9
+ 0046d834 bytes 089546f9
- 0046d898 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046d898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046d898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046d898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046d898 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046d898 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d898 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046d898 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046d898 bytes 08410591
+ 0046d898 bytes 08410891
- 0046d91c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd0:8"]]
- 0046d91c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046d91c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
+ 0046d91c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046d91c bytes 08e946f9
+ 0046d91c bytes 084147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b8d9bca224c20492742296f15b3cc98"></a>

### [`0046dc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046dc5c.md) → [`0046dc5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046d/0046dc5c.md) FUN_0046dc5c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`008594d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/008594d4.md) · 呼出先 21件 [`00449c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c34.md) [`00449c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c84.md) [`0046ae68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b618.md)
- 新版 呼出元 3件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`008594d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/008594d4.md) · 呼出先 21件 [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`00449c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c84.md) [`0046ae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b618.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.87% / 新版 88.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046dce4",
      "incomplete_value": false,
      "site": "0046dce4",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046dce4",
      "incomplete_value": false,
      "site": "0046dce4",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046e028",
      "incomplete_value": false,
      "site": "0046e028",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e028",
      "incomplete_value": false,
      "site": "0046e028",
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
            "const:a98:8"
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
      "definition_site": "0046e0e8",
      "incomplete_value": true,
      "site": "0046e0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e0e8",
      "incomplete_value": true,
      "site": "0046e0fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a1:8"
              ]
            ]
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
      "0046dcdc",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046dce4",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046dd88",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046dcdc",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046dce4",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046dd88",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046dcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046dc5c.md#insn-0046dcd4) · [`0046dd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046dc5c.md#insn-0046dd70) · [`0046dd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046d/0046dc5c.md#insn-0046dd78)
- 新版 `0046dcd4`（命令位置の公開資料なし） · `0046dd70`（命令位置の公開資料なし）

~~~diff
- 0046dcd4 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046dcd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046dcd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046dcd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046dcd4 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046dcd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046dcd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046dcd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046dcd4 bytes 08410591
+ 0046dcd4 bytes 08410891
- 0046dd70 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0046dd70 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
- 0046dd70 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
- 0046dd70 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
+ 0046dd70 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 0046dd70 ["INT_CARRY", "register:105:1", ["register:40e0:8", "tmp:0:8"]]
+ 0046dd70 ["INT_SCARRY", "register:106:1", ["register:40e0:8", "tmp:0:8"]]
+ 0046dd70 ["INT_ADD", "tmp:1:8", ["register:40e0:8", "tmp:0:8"]]
- 0046dd70 bytes 9c830591
+ 0046dd70 bytes 9c830891
- 0046dd78 ["COPY", "register:40d0:8", ["const:c25000:8"]]
- 0046dd78 bytes da3d0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98fbad9294642a7e2b0246837cebe49c"></a>

### [`0046e4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046e4f8.md) → [`0046e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046e4f8.md) FUN_0046e4f8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`0080d900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0080d/0080d900.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`0083d5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md) · 呼出先 20件 [`0046ae68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004710d8.md)
- 新版 呼出元 3件 [`0080d900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0080d/0080d900.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`0083d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md) · 呼出先 20件 [`0046ae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004710d8.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.43% / 新版 88.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046e5ac",
      "incomplete_value": false,
      "site": "0046e5ac",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e5ac",
      "incomplete_value": false,
      "site": "0046e5ac",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0046e924",
      "incomplete_value": false,
      "site": "0046e924",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e924",
      "incomplete_value": false,
      "site": "0046e924",
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
            "const:b98:8"
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
      "definition_site": "0046e9d0",
      "incomplete_value": true,
      "site": "0046e9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046e9d0",
      "incomplete_value": true,
      "site": "0046e9ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a1:8"
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
      "0046e5a4",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046e5ac",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046e6b4",
      "READ",
      [
        "storage",
        "00c25160",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0046e5a4",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046e5ac",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046e6b4",
      "READ",
      [
        "storage",
        "00c25220",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046e59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046e4f8.md#insn-0046e59c) · [`0046e654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046e4f8.md#insn-0046e654) · [`0046e65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046e4f8.md#insn-0046e65c)
- 新版 `0046e59c`（命令位置の公開資料なし） · `0046e654`（命令位置の公開資料なし）

~~~diff
- 0046e59c ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046e59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046e59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046e59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046e59c ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046e59c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046e59c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046e59c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046e59c bytes 08410591
+ 0046e59c bytes 08410891
- 0046e654 ["COPY", "tmp:0:8", ["const:160:8"]]
- 0046e654 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 0046e654 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 0046e654 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 0046e654 ["COPY", "tmp:0:8", ["const:220:8"]]
+ 0046e654 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 0046e654 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 0046e654 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 0046e654 bytes 5a830591
+ 0046e654 bytes 5a830891
- 0046e65c ["COPY", "register:40e0:8", ["const:c25000:8"]]
- 0046e65c bytes bc3d00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b145b9019f4d3393b51ecac9e014138"></a>

### [`0046ede4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046ede4.md) → [`0046ede4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046e/0046ede4.md) FUN_0046ede4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00605bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00605/00605bdc.md) · 呼出先 17件 [`00449c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c84.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md)
- 新版 呼出元 1件 [`00605bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md) · 呼出先 17件 [`00449c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c84.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.15% / 新版 86.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046ee68",
      "incomplete_value": false,
      "site": "0046ee68",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046ee68",
      "incomplete_value": false,
      "site": "0046ee68",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046ef2c",
      "incomplete_value": true,
      "site": "0046ef2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046ef2c",
      "incomplete_value": true,
      "site": "0046ef2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0046f054",
      "incomplete_value": true,
      "site": "0046f054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046f054",
      "incomplete_value": true,
      "site": "0046f054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0046ee60",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046ee68",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046eed4",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046ee60",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046ee68",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046eed4",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046ee58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046ede4.md#insn-0046ee58) · [`0046eed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046ede4.md#insn-0046eed4) · [`0046eee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046e/0046ede4.md#insn-0046eee4)
- 新版 `0046ee58`（命令位置の公開資料なし） · `0046eed4`（命令位置の公開資料なし） · `0046eee4`（命令位置の公開資料なし）

~~~diff
- 0046ee58 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046ee58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046ee58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046ee58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046ee58 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046ee58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046ee58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046ee58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046ee58 bytes 08410591
+ 0046ee58 bytes 08410891
- 0046eed4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c78:8"]]
- 0046eed4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046eed4 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
+ 0046eed4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046eed4 bytes 003c46f9
+ 0046eed4 bytes 009446f9
- 0046eee4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:150:8"]]
- 0046eee4 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046eee4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:210:8"]]
+ 0046eee4 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0046eee4 bytes 16ab40f9
+ 0046eee4 bytes 160b41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54b81773f29f4677b0a9a9add972c465"></a>

### [`0046f248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md) → [`0046f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f248.md) FUN_0046f248

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`006b0874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006b0/006b0874.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008a5/008a5bd0.md) · 呼出先 17件 [`00449c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c34.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c4c0.md)
- 新版 呼出元 6件 [`006b0874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b0/006b0874.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) [`008a5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a5/008a5bd0.md) · 呼出先 17件 [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046ba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046ba28.md) [`0046bd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046bd30.md) [`0046c4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c4c0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.22% / 新版 86.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046f2c0",
      "incomplete_value": false,
      "site": "0046f2c0",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f2c0",
      "incomplete_value": false,
      "site": "0046f2c0",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046f378",
      "incomplete_value": true,
      "site": "0046f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046f378",
      "incomplete_value": true,
      "site": "0046f378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046f4a4",
      "incomplete_value": true,
      "site": "0046f4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046f4a4",
      "incomplete_value": true,
      "site": "0046f4a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046f2b8",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f2c0",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f32c",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0046f2b8",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f2c0",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f32c",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f2b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md#insn-0046f2b0) · [`0046f32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md#insn-0046f32c) · [`0046f338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md#insn-0046f338)
- 新版 `0046f2b0`（命令位置の公開資料なし） · `0046f32c`（命令位置の公開資料なし） · `0046f338`（命令位置の公開資料なし）

~~~diff
- 0046f2b0 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046f2b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046f2b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046f2b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046f2b0 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046f2b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046f2b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046f2b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046f2b0 bytes 08410591
+ 0046f2b0 bytes 08410891
- 0046f32c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:c78:8"]]
- 0046f32c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046f32c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d28:8"]]
+ 0046f32c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046f32c bytes 003c46f9
+ 0046f32c bytes 009446f9
- 0046f338 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:150:8"]]
- 0046f338 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046f338 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:210:8"]]
+ 0046f338 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0046f338 bytes 16ab40f9
+ 0046f338 bytes 160b41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecca128458b502d031649b9dcfbf4846"></a>

### [`0046f694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f694.md) → [`0046f694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f694.md) FUN_0046f694

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00acce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md) · 呼出先 1件 [`00449c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00449/00449c34.md)
- 新版 呼出元 1件 [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md) · 呼出先 1件 [`00449c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449c34.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `call_target` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0046f6b4",
      "incomplete_value": true,
      "site": "0046f6b4",
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
      "definition_site": "0046f6b4",
      "incomplete_value": true,
      "site": "0046f6b4",
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
      "definition_site": "0046f774",
      "incomplete_value": false,
      "site": "0046f778",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f774",
      "incomplete_value": false,
      "site": "0046f778",
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
            "const:cb0:8"
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
      "definition_site": "0046f7b0",
      "incomplete_value": false,
      "site": "0046f7b4",
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
            "const:d70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046f7b0",
      "incomplete_value": false,
      "site": "0046f7b4",
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
            "const:cb0:8"
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
      "0046f6b0",
      "READ",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f6c0",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "0046f6c8",
      "READ",
      [
        "storage",
        "00c24cdc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0046f6b0",
      "READ",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046f6c0",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "0046f6c8",
      "READ",
      [
        "storage",
        "00c24d9c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046f6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f694.md#insn-0046f6b0) · [`0046f6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f694.md#insn-0046f6c0) · [`0046f774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f694.md#insn-0046f774)
- 新版 `0046f6b0`（命令位置の公開資料なし） · `0046f6c0`（命令位置の公開資料なし） · `0046f774`（命令位置の公開資料なし）

~~~diff
- 0046f6b0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:150:8"]]
- 0046f6b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046f6b0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:210:8"]]
+ 0046f6b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046f6b0 bytes 28ab40f9
+ 0046f6b0 bytes 280b41f9
- 0046f6c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
- 0046f6c0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046f6c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 0046f6c0 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 0046f6c0 bytes 733e46f9
+ 0046f6c0 bytes 739646f9
- 0046f774 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 0046f774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0046f774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0046f774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0046f774 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 0046f774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0046f774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0046f774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0046f774 bytes 00c03291
+ 0046f774 bytes 00c03591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67902f6a5dc8a96c712ddadcec730863"></a>

### [`0046f9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md) → [`0046f9d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f9d4.md) FUN_0046f9d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 28件 [`00833158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00833/00833158.md) [`0083fcf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083fcf4.md) [`0083ff24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083f/0083ff24.md) [`0084c134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c134.md) [`0084c290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c290.md) · 呼出先 9件 [`0046ae68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004710d8.md)
- 新版 呼出元 28件 [`00833158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00833/00833158.md) [`0083fcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083fcf4.md) [`0083ff24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083f/0083ff24.md) [`0084c134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c134.md) [`0084c290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c290.md) · 呼出先 9件 [`0046ae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ae68.md) [`0046b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b1e0.md) [`0046b618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046b/0046b618.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`004710d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004710d8.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.64% / 新版 82.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0046fa90",
      "incomplete_value": true,
      "site": "0046fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046fa90",
      "incomplete_value": true,
      "site": "0046fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046faa8",
      "incomplete_value": true,
      "site": "0046faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046faa8",
      "incomplete_value": true,
      "site": "0046faa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046fb10",
      "incomplete_value": true,
      "site": "0046fb10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0046fb10",
      "incomplete_value": true,
      "site": "0046fb10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0046fa74",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "0046fa78",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "0046fa90",
      "DATA",
      [
        "storage",
        "00be8938",
        null,
        "undefined1[88]"
      ]
    ]
  ],
  "added": [
    [
      "0046fa74",
      "READ",
      [
        "storage",
        "00c1ae88",
        null,
        "pointer"
      ]
    ],
    [
      "0046fa78",
      "READ",
      [
        "storage",
        "00c1ae90",
        null,
        "pointer"
      ]
    ],
    [
      "0046fa90",
      "DATA",
      [
        "storage",
        "00be89e8",
        null,
        "undefined1[88]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fa74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md#insn-0046fa74) · [`0046fa78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md#insn-0046fa78) · [`0046fa94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f9d4.md#insn-0046fa94)
- 新版 `0046fa74`（命令位置の公開資料なし） · `0046fa78`（命令位置の公開資料なし）

~~~diff
- 0046fa74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 0046fa74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046fa74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e88:8"]]
+ 0046fa74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fa74 bytes 08ed46f9
+ 0046fa74 bytes 084547f9
- 0046fa78 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:de0:8"]]
- 0046fa78 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046fa78 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:e90:8"]]
+ 0046fa78 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fa78 bytes 4af146f9
+ 0046fa78 bytes 4a4947f9
- 0046fa94 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 0046fa94 bytes a83d00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34721e5bd88688d83579d3efa44e9fab"></a>

### [`0046fc48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fc48.md) → [`0046fc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fc48.md) FUN_0046fc48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00860ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/00860ba8.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db24.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 1件 [`00860ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/00860ba8.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db24.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.93% / 新版 83.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
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
                "const:210:8"
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
      "definition_site": "0046fc98",
      "incomplete_value": false,
      "site": "0046fc98",
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
                "const:150:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0046fc60",
      "incomplete_value": true,
      "site": "0046fc60",
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
      "definition_site": "0046fc60",
      "incomplete_value": true,
      "site": "0046fc60",
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
      "0046fc5c",
      "READ",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fc78",
      "READ",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fc94",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046fc5c",
      "READ",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fc78",
      "READ",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fc94",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fc48.md#insn-0046fc5c) · [`0046fc78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fc48.md#insn-0046fc78) · [`0046fc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fc48.md#insn-0046fc90)
- 新版 `0046fc5c`（命令位置の公開資料なし） · `0046fc78`（命令位置の公開資料なし） · `0046fc90`（命令位置の公開資料なし）

~~~diff
- 0046fc5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
- 0046fc5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046fc5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:210:8"]]
+ 0046fc5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fc5c bytes 88aa40f9
+ 0046fc5c bytes 880a41f9
- 0046fc78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:150:8"]]
- 0046fc78 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046fc78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:210:8"]]
+ 0046fc78 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fc78 bytes 80aa40f9
+ 0046fc78 bytes 800a41f9
- 0046fc90 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046fc90 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046fc90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046fc90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046fc90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046fc90 bytes 08410591
+ 0046fc90 bytes 08410891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6e3ea700c3491296f595601e9e33b52"></a>

### [`0046fd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fd28.md) → [`0046fd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fd28.md) FUN_0046fd28

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 10件 [`0084c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c390.md) [`0084d1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084d/0084d1b4.md) [`0084e780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084e/0084e780.md) [`00859898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00859/00859898.md) [`008609f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00860/008609f4.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db24.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 10件 [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) [`0084d1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084d/0084d1b4.md) [`0084e780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084e/0084e780.md) [`00859898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00859/00859898.md) [`008609f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00860/008609f4.md) · 呼出先 3件 [`0052db24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db24.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
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
            "const:150:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
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
                "const:210:8"
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
      "definition_site": "0046fd48",
      "incomplete_value": false,
      "site": "0046fd48",
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
                "const:150:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0046fd4c",
      "incomplete_value": true,
      "site": "0046fd4c",
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
      "definition_site": "0046fd4c",
      "incomplete_value": true,
      "site": "0046fd4c",
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
      "0046fd44",
      "READ",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fd48",
      "WRITE",
      [
        "storage",
        "00c25150",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fd48",
      "WRITE",
      [
        "storage",
        "00c25158",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0046fd44",
      "READ",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fd48",
      "WRITE",
      [
        "storage",
        "00c25210",
        null,
        "undefined8"
      ]
    ],
    [
      "0046fd48",
      "WRITE",
      [
        "storage",
        "00c25218",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0046fd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fd28.md#insn-0046fd40) · [`0046fdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046fd28.md#insn-0046fdb0)
- 新版 `0046fd40`（命令位置の公開資料なし） · `0046fdb0`（命令位置の公開資料なし）

~~~diff
- 0046fd40 ["COPY", "tmp:0:8", ["const:150:8"]]
- 0046fd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0046fd40 ["COPY", "tmp:0:8", ["const:210:8"]]
+ 0046fd40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0046fd40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0046fd40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0046fd40 bytes 08410591
+ 0046fd40 bytes 08410891
- 0046fdb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
- 0046fdb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0046fdb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
+ 0046fdb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0046fdb0 bytes 00a140f9
+ 0046fdb0 bytes 000141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba23f706dd05bd2227855a42b2ee8c06"></a>

### [`00470130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470130.md) → [`00470130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470130.md) FUN_00470130

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00470050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470050.md) [`0073fa38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073f/0073fa38.md) [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`00844bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/00844bd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/004703fc.md) [`004715ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004715ac.md) [`004715b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004715b0.md) [`0052db38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db38.md)
- 新版 呼出元 5件 [`00470050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470050.md) [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00844bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004703fc.md) [`004715ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004715ac.md) [`004715b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004715b0.md) [`0052db38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db38.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 86.54% / 新版 86.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00470180",
      "incomplete_value": false,
      "site": "00470180",
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
            "const:280:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470180",
      "incomplete_value": false,
      "site": "00470180",
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
            "const:1c0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047019c",
      "incomplete_value": false,
      "site": "0047019c",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047019c",
      "incomplete_value": false,
      "site": "0047019c",
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
            "const:c98:8"
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
      "definition_site": "00470268",
      "incomplete_value": true,
      "site": "00470268",
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
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470268",
      "incomplete_value": true,
      "site": "00470268",
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
            "const:1c8:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0047016c",
      "READ",
      [
        "storage",
        "00c251e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00470178",
      "READ",
      [
        "storage",
        "00c251c0",
        null,
        "undefined4"
      ]
    ],
    [
      "00470180",
      "WRITE",
      [
        "storage",
        "00c251c0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "0047016c",
      "READ",
      [
        "storage",
        "00c252a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00470178",
      "READ",
      [
        "storage",
        "00c25280",
        null,
        "undefined4"
      ]
    ],
    [
      "00470180",
      "WRITE",
      [
        "storage",
        "00c25280",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00470180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470130.md#insn-00470180) · [`00470268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470130.md#insn-00470268) · [`00470168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470130.md#insn-00470168)
- 新版 `00470180`（命令位置の公開資料なし） · `00470268`（命令位置の公開資料なし） · `00470168`（命令位置の公開資料なし）

~~~diff
- 00470180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c0:8"]]
- 00470180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
+ 00470180 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:280:8"]]
+ 00470180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:4"]]
- 00470180 bytes 15c101b9
+ 00470180 bytes 158102b9
- 00470268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1c8:8"]]
- 00470268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00470268 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:288:8"]]
+ 00470268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00470268 bytes 09e500f9
+ 00470268 bytes 094501f9
- 00470168 ["COPY", "tmp:0:8", ["const:1e0:8"]]
- 00470168 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00470168 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00470168 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00470168 ["COPY", "tmp:0:8", ["const:2a0:8"]]
+ 00470168 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00470168 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00470168 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00470168 bytes 4a810791
+ 00470168 bytes 4a810a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ca9e24719e1da5f5364b9a8740e3c7e"></a>

### [`00470404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470404.md) → [`00470404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/00470404.md) FUN_00470404

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`0083d5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0083d/0083d5f0.md) [`00850180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00850/00850180.md) [`008e0bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008e0/008e0bc0.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/004703fc.md) [`00471ca4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471ca4.md) [`0052db38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052db38.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 4件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`0083d5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0083d/0083d5f0.md) [`00850180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00850/00850180.md) [`008e0bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008e0/008e0bc0.md) · 呼出先 12件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004703fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00470/004703fc.md) [`00471ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471ca4.md) [`0052db38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052db38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 89.45% / 新版 89.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 5件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0047045c",
      "incomplete_value": false,
      "site": "0047045c",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047045c",
      "incomplete_value": false,
      "site": "0047045c",
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
            "const:1e8:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004704c4",
      "incomplete_value": false,
      "site": "004704c4",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004704c4",
      "incomplete_value": false,
      "site": "004704c4",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00470614",
      "incomplete_value": true,
      "site": "00470614",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00470614",
      "incomplete_value": true,
      "site": "00470614",
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
            "const:1f0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00470444",
      "READ",
      [
        "storage",
        "00c25208",
        null,
        "undefined1"
      ]
    ],
    [
      "00470454",
      "READ",
      [
        "storage",
        "00c251e8",
        null,
        "undefined4"
      ]
    ],
    [
      "0047045c",
      "WRITE",
      [
        "storage",
        "00c251e8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00470444",
      "READ",
      [
        "storage",
        "00c252c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00470454",
      "READ",
      [
        "storage",
        "00c252a8",
        null,
        "undefined4"
      ]
    ],
    [
      "0047045c",
      "WRITE",
      [
        "storage",
        "00c252a8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047045c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470404.md#insn-0047045c) · [`00470614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470404.md#insn-00470614) · [`00470440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00470/00470404.md#insn-00470440)
- 新版 `0047045c`（命令位置の公開資料なし） · `00470614`（命令位置の公開資料なし） · `00470440`（命令位置の公開資料なし）

~~~diff
- 0047045c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
- 0047045c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
+ 0047045c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2a8:8"]]
+ 0047045c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40c0:4"]]
- 0047045c bytes 18e901b9
+ 0047045c bytes 18a902b9
- 00470614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1f0:8"]]
- 00470614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00470614 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2b0:8"]]
+ 00470614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00470614 bytes 09f900f9
+ 00470614 bytes 095901f9
- 00470440 ["COPY", "tmp:0:8", ["const:208:8"]]
- 00470440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00470440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00470440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00470440 ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00470440 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00470440 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00470440 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00470440 bytes 29210891
+ 00470440 bytes 29210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cd94cd6ee01495e1e1fc8d00350f8af"></a>

### [`004711b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004711b4.md) → [`004711b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004711b4.md) FUN_004711b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "004711d4",
      "incomplete_value": false,
      "site": "004711d8",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004711d4",
      "incomplete_value": false,
      "site": "004711d8",
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
      "004711d8",
      "DATA",
      [
        "storage",
        "00be8a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004711d8",
      "DATA",
      [
        "storage",
        "00be8b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004711d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004711b4.md#insn-004711d4)
- 新版 `004711d4`（命令位置の公開資料なし）

~~~diff
- 004711d4 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 004711d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004711d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004711d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004711d4 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004711d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004711d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004711d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004711d4 bytes 08612a91
+ 004711d4 bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebd479b6e8faf986c732c44815480669"></a>

### [`004711ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004711ec.md) → [`004711ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004711ec.md) FUN_004711ec

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
      "definition_site": "004711f0",
      "incomplete_value": false,
      "site": "004711f4",
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
            "const:b48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004711f0",
      "incomplete_value": false,
      "site": "004711f4",
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
      "004711f4",
      "DATA",
      [
        "storage",
        "00be8a98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004711f4",
      "DATA",
      [
        "storage",
        "00be8b48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004711f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004711ec.md#insn-004711f0)
- 新版 `004711f0`（命令位置の公開資料なし）

~~~diff
- 004711f0 ["COPY", "tmp:0:8", ["const:a98:8"]]
- 004711f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004711f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004711f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004711f0 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004711f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004711f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004711f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004711f0 bytes 08612a91
+ 004711f0 bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e3b10be07131a0052fcaf0ebdc772d4"></a>

### [`00471254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471254.md) → [`00471254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471254.md) FUN_00471254

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00471274",
      "incomplete_value": false,
      "site": "00471278",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471274",
      "incomplete_value": false,
      "site": "00471278",
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
      "00471278",
      "DATA",
      [
        "storage",
        "00be8b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471278",
      "DATA",
      [
        "storage",
        "00be8bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471254.md#insn-00471274)
- 新版 `00471274`（命令位置の公開資料なし）

~~~diff
- 00471274 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00471274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471274 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00471274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471274 bytes 08612c91
+ 00471274 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0d03918e2a0019d9c23cbe0783b3933"></a>

### [`0047128c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047128c.md) → [`0047128c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/0047128c.md) FUN_0047128c

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
      "definition_site": "00471290",
      "incomplete_value": false,
      "site": "00471294",
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
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471290",
      "incomplete_value": false,
      "site": "00471294",
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
      "00471294",
      "DATA",
      [
        "storage",
        "00be8b18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471294",
      "DATA",
      [
        "storage",
        "00be8bc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047128c.md#insn-00471290)
- 新版 `00471290`（命令位置の公開資料なし）

~~~diff
- 00471290 ["COPY", "tmp:0:8", ["const:b18:8"]]
- 00471290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471290 ["COPY", "tmp:0:8", ["const:bc8:8"]]
+ 00471290 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471290 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471290 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471290 bytes 08612c91
+ 00471290 bytes 08212f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e6fec9f8622609e86a2c35de4563546"></a>

### [`004712f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004712f4.md) → [`004712f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004712f4.md) FUN_004712f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00471314",
      "incomplete_value": false,
      "site": "00471318",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471314",
      "incomplete_value": false,
      "site": "00471318",
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
            "const:b98:8"
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
      "00471318",
      "DATA",
      [
        "storage",
        "00be8b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471318",
      "DATA",
      [
        "storage",
        "00be8c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004712f4.md#insn-00471314)
- 新版 `00471314`（命令位置の公開資料なし）

~~~diff
- 00471314 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00471314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471314 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00471314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471314 bytes 08612e91
+ 00471314 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ed2fc09e66e8761752fa76a40c1d10b"></a>

### [`0047132c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047132c.md) → [`0047132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/0047132c.md) FUN_0047132c

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
      "definition_site": "00471330",
      "incomplete_value": false,
      "site": "00471334",
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
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471330",
      "incomplete_value": false,
      "site": "00471334",
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
            "const:b98:8"
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
      "00471334",
      "DATA",
      [
        "storage",
        "00be8b98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471334",
      "DATA",
      [
        "storage",
        "00be8c48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047132c.md#insn-00471330)
- 新版 `00471330`（命令位置の公開資料なし）

~~~diff
- 00471330 ["COPY", "tmp:0:8", ["const:b98:8"]]
- 00471330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471330 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00471330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471330 bytes 08612e91
+ 00471330 bytes 08213191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a452d8a0ab94fe4b7f8db2933f193cd1"></a>

### [`00471394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471394.md) → [`00471394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471394.md) FUN_00471394

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "004713b4",
      "incomplete_value": false,
      "site": "004713b8",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004713b4",
      "incomplete_value": false,
      "site": "004713b8",
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
            "const:c18:8"
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
      "004713b8",
      "DATA",
      [
        "storage",
        "00be8c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004713b8",
      "DATA",
      [
        "storage",
        "00be8cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004713b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471394.md#insn-004713b4)
- 新版 `004713b4`（命令位置の公開資料なし）

~~~diff
- 004713b4 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 004713b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004713b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004713b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004713b4 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 004713b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004713b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004713b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004713b4 bytes 08613091
+ 004713b4 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-882fc54d775eeb8b777275f665396832"></a>

### [`004713cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004713cc.md) → [`004713cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/004713cc.md) FUN_004713cc

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
      "definition_site": "004713d0",
      "incomplete_value": false,
      "site": "004713d4",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004713d0",
      "incomplete_value": false,
      "site": "004713d4",
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
            "const:c18:8"
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
      "004713d4",
      "DATA",
      [
        "storage",
        "00be8c18",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004713d4",
      "DATA",
      [
        "storage",
        "00be8cc8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004713d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/004713cc.md#insn-004713d0)
- 新版 `004713d0`（命令位置の公開資料なし）

~~~diff
- 004713d0 ["COPY", "tmp:0:8", ["const:c18:8"]]
- 004713d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004713d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004713d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004713d0 ["COPY", "tmp:0:8", ["const:cc8:8"]]
+ 004713d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004713d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004713d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004713d0 bytes 08613091
+ 004713d0 bytes 08213391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de50bf82e7e626889c0d62386bd701af"></a>

### [`0047155c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047155c.md) → [`0047155c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/0047155c.md) FUN_0047155c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "0047157c",
      "incomplete_value": false,
      "site": "00471580",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047157c",
      "incomplete_value": false,
      "site": "00471580",
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
            "const:c98:8"
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
      "00471580",
      "DATA",
      [
        "storage",
        "00be8c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471580",
      "DATA",
      [
        "storage",
        "00be8d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047157c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047155c.md#insn-0047157c)
- 新版 `0047157c`（命令位置の公開資料なし）

~~~diff
- 0047157c ["COPY", "tmp:0:8", ["const:c98:8"]]
- 0047157c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047157c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047157c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047157c ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 0047157c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047157c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047157c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047157c bytes 08613291
+ 0047157c bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db04a989e264c9727b1c8955790fe9d3"></a>

### [`00471594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471594.md) → [`00471594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471594.md) FUN_00471594

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
      "definition_site": "00471598",
      "incomplete_value": false,
      "site": "0047159c",
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
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471598",
      "incomplete_value": false,
      "site": "0047159c",
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
            "const:c98:8"
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
      "0047159c",
      "DATA",
      [
        "storage",
        "00be8c98",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047159c",
      "DATA",
      [
        "storage",
        "00be8d48",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471594.md#insn-00471598)
- 新版 `00471598`（命令位置の公開資料なし）

~~~diff
- 00471598 ["COPY", "tmp:0:8", ["const:c98:8"]]
- 00471598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471598 ["COPY", "tmp:0:8", ["const:d48:8"]]
+ 00471598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471598 bytes 08613291
+ 00471598 bytes 08213591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d23e2984f7ad5b9fad75c97cb643b94c"></a>

### [`00471ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471ac4.md) → [`00471ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471ac4.md) FUN_00471ac4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00471ad0",
      "incomplete_value": false,
      "site": "00471adc",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471ad0",
      "incomplete_value": false,
      "site": "00471adc",
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
            "const:d28:8"
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
      "00471adc",
      "DATA",
      [
        "storage",
        "00be8d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471adc",
      "DATA",
      [
        "storage",
        "00be8dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471ac4.md#insn-00471ad0)
- 新版 `00471ad0`（命令位置の公開資料なし）

~~~diff
- 00471ad0 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00471ad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00471ad0 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00471ad0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00471ad0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00471ad0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00471ad0 bytes 4aa13491
+ 00471ad0 bytes 4a613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde72b212f21f15841ce1189387cf3b9"></a>

### [`00471b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471b08.md) → [`00471b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471b08.md) FUN_00471b08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00471b20",
      "incomplete_value": false,
      "site": "00471b2c",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471b20",
      "incomplete_value": false,
      "site": "00471b2c",
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
            "const:d28:8"
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
      "00471b2c",
      "DATA",
      [
        "storage",
        "00be8d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471b2c",
      "DATA",
      [
        "storage",
        "00be8dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471b08.md#insn-00471b20)
- 新版 `00471b20`（命令位置の公開資料なし）

~~~diff
- 00471b20 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00471b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471b20 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00471b20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471b20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471b20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471b20 bytes 08a13491
+ 00471b20 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef462a1298e5852e2e230c1263b20233"></a>

### [`00471b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471b64.md) → [`00471b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471b64.md) FUN_00471b64

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00471b90",
      "incomplete_value": false,
      "site": "00471b90",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471b90",
      "incomplete_value": false,
      "site": "00471b90",
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
            "const:d28:8"
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
      "00471b90",
      "DATA",
      [
        "storage",
        "00be8d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471b90",
      "DATA",
      [
        "storage",
        "00be8dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471b64.md#insn-00471b88)
- 新版 `00471b88`（命令位置の公開資料なし）

~~~diff
- 00471b88 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00471b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471b88 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00471b88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471b88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471b88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471b88 bytes 08a13491
+ 00471b88 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a73cb10194696fbf2068651f76c2b29"></a>

### [`00471bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471bf4.md) → [`00471bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471bf4.md) FUN_00471bf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00471c14",
      "incomplete_value": false,
      "site": "00471c14",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471c14",
      "incomplete_value": false,
      "site": "00471c14",
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
            "const:d28:8"
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
      "00471c14",
      "DATA",
      [
        "storage",
        "00be8d28",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00471c14",
      "DATA",
      [
        "storage",
        "00be8dd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471bf4.md#insn-00471c10)
- 新版 `00471c10`（命令位置の公開資料なし）

~~~diff
- 00471c10 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00471c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00471c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00471c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00471c10 ["COPY", "tmp:0:8", ["const:dd8:8"]]
+ 00471c10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00471c10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00471c10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00471c10 bytes 08a13491
+ 00471c10 bytes 08613791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6d43aca85b37d94e4cdf49247f62a0"></a>

### [`00471cf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471cf4.md) → [`00471cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471cf4.md) FUN_00471cf4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00436e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436e9c.md) [`0047163c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/0047163c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0047163c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/0047163c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.06% / 新版 97.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00471d38",
      "incomplete_value": false,
      "site": "00471d40",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00471d38",
      "incomplete_value": false,
      "site": "00471d40",
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
            "const:1f0:8"
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
      "00471d38",
      "PARAM",
      [
        "storage",
        "00c251f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00471d38",
      "PARAM",
      [
        "storage",
        "00c252b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471cf4.md#insn-00471d38)
- 新版 `00471d38`（命令位置の公開資料なし）

~~~diff
- 00471d38 ["COPY", "tmp:0:8", ["const:1f0:8"]]
- 00471d38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00471d38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00471d38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00471d38 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00471d38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00471d38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00471d38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00471d38 bytes 00c00791
+ 00471d38 bytes 00c00a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b23847d1e80d1cb89a34629c361d721d"></a>

### [`00471f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471f30.md) → [`00471f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00471/00471f30.md) _INIT_22

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`0046ad90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046a/0046ad90.md) [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`0046ad90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046a/0046ad90.md) [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 79.06% / 新版 79.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 15件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00471f70",
      "incomplete_value": true,
      "site": "00471f8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00471f70",
      "incomplete_value": true,
      "site": "00471f8c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "00471f94",
      "incomplete_value": true,
      "site": "00471fb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00471f94",
      "incomplete_value": true,
      "site": "00471fb0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "00471fb4",
      "incomplete_value": true,
      "site": "00471fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00471fb4",
      "incomplete_value": true,
      "site": "00471fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "00471f70",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00471f94",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00471fb4",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00471f70",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00471f94",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00471fb4",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00471f60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471f30.md#insn-00471f60) · [`00471f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00471/00471f30.md#insn-00471f68)
- 新版 `00471f60`（命令位置の公開資料なし） · `00471f68`（命令位置の公開資料なし）

~~~diff
- 00471f60 ["COPY", "tmp:0:8", ["const:d0:8"]]
- 00471f60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00471f60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00471f60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00471f60 ["COPY", "tmp:0:8", ["const:190:8"]]
+ 00471f60 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00471f60 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00471f60 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00471f60 bytes 73420391
+ 00471f60 bytes 73420691
- 00471f68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00471f68 bytes a9f1ffd0
+ 00471f68 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00471f68 bytes a9f1ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba176904ac992777bfe4a6963934c05"></a>

### [`004724fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004724fc.md) → [`004724fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004724fc.md) FUN_004724fc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/00821350.md) [`00821cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/00821cbc.md) [`00829478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/008443c8.md) · 呼出先 2件 [`00472e6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/00472e6c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 5件 [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md) [`00821cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821cbc.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) [`008443c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/008443c8.md) · 呼出先 2件 [`00472e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/00472e6c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004725b8",
      "incomplete_value": true,
      "site": "004725b8",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004725b8",
      "incomplete_value": true,
      "site": "004725b8",
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
            "const:250:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00472518",
      "incomplete_value": true,
      "site": "00472518",
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
      "definition_site": "00472518",
      "incomplete_value": true,
      "site": "00472518",
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
      "definition_site": "00472570",
      "incomplete_value": false,
      "site": "00472574",
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
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472570",
      "incomplete_value": false,
      "site": "00472574",
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
            "const:228:8"
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
      "00472514",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "0047252c",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "00472538",
      "READ",
      [
        "storage",
        "00c25230",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00472514",
      "READ",
      [
        "storage",
        "00c25310",
        null,
        "undefined8"
      ]
    ],
    [
      "0047252c",
      "READ",
      [
        "storage",
        "00c25310",
        null,
        "undefined8"
      ]
    ],
    [
      "00472538",
      "READ",
      [
        "storage",
        "00c252f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004725b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004724fc.md#insn-004725b8) · [`00472514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004724fc.md#insn-00472514) · [`0047252c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004724fc.md#insn-0047252c)
- 新版 `004725b8`（命令位置の公開資料なし） · `00472514`（命令位置の公開資料なし） · `0047252c`（命令位置の公開資料なし）

~~~diff
- 004725b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:250:8"]]
- 004725b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 004725b8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:310:8"]]
+ 004725b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 004725b8 bytes a82a01f9
+ 004725b8 bytes a88a01f9
- 00472514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:250:8"]]
- 00472514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00472514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:310:8"]]
+ 00472514 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00472514 bytes a82a41f9
+ 00472514 bytes a88a41f9
- 0047252c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:250:8"]]
- 0047252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047252c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:310:8"]]
+ 0047252c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047252c bytes a82a41f9
+ 0047252c bytes a88a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-740bbaedfaddc1bc81f512aa15af4845"></a>

### [`004725e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004725e0.md) → [`004725e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004725e0.md) FUN_004725e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) [`00829478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00829/00829478.md) · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 2件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) [`00829478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00829/00829478.md) · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047260c",
      "incomplete_value": true,
      "site": "00472614",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047260c",
      "incomplete_value": true,
      "site": "00472614",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "004725e8",
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
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "004725e8",
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
    "guard": [
      [
        "FALL_THROUGH",
        "004725e8"
      ],
      [
        "FALL_THROUGH",
        "004725e8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "00472614",
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
      "definition_site": "004725e8",
      "incomplete_value": true,
      "site": "00472614",
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
      "004725e4",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "004725f4",
      "READ",
      [
        "storage",
        "00c25248",
        null,
        "undefined8"
      ]
    ],
    [
      "004725f8",
      "READ",
      [
        "storage",
        "00c25230",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004725e4",
      "READ",
      [
        "storage",
        "00c25310",
        null,
        "undefined8"
      ]
    ],
    [
      "004725f4",
      "READ",
      [
        "storage",
        "00c25308",
        null,
        "undefined8"
      ]
    ],
    [
      "004725f8",
      "READ",
      [
        "storage",
        "00c252f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004725e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004725e0.md#insn-004725e4) · [`004725f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004725e0.md#insn-004725f0)
- 新版 `004725e4`（命令位置の公開資料なし） · `004725f0`（命令位置の公開資料なし）

~~~diff
- 004725e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:250:8"]]
- 004725e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004725e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:310:8"]]
+ 004725e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004725e4 bytes 292941f9
+ 004725e4 bytes 298941f9
- 004725f0 ["COPY", "tmp:0:8", ["const:230:8"]]
- 004725f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004725f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004725f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004725f0 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 004725f0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004725f0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004725f0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004725f0 bytes 29c10891
+ 004725f0 bytes 29c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5e260923ff9eb2ea4bda7b354a4546c"></a>

### [`00472640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/00472640.md) → [`00472640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/00472640.md) FUN_00472640

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00827/00827ba0.md) · 呼出先 19件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`00445ae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445ae8.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 19件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445ae8.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 95.85% / 新版 95.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004726b0",
      "incomplete_value": true,
      "site": "004726b8",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004726b0",
      "incomplete_value": true,
      "site": "004726b8",
      "value": [
        "LOAD",
        "16",
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
              "INT_LEFT"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00472b94",
      "incomplete_value": false,
      "site": "00472b94",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00472b94",
      "incomplete_value": false,
      "site": "00472b94",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0047267c",
      "incomplete_value": true,
      "site": "0047267c",
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
      "definition_site": "0047267c",
      "incomplete_value": true,
      "site": "0047267c",
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
      "00472678",
      "READ",
      [
        "storage",
        "00c25250",
        null,
        "undefined8"
      ]
    ],
    [
      "0047268c",
      "READ",
      [
        "storage",
        "00c25248",
        null,
        "undefined8"
      ]
    ],
    [
      "00472690",
      "READ",
      [
        "storage",
        "00c25230",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00472678",
      "READ",
      [
        "storage",
        "00c25310",
        null,
        "undefined8"
      ]
    ],
    [
      "0047268c",
      "READ",
      [
        "storage",
        "00c25308",
        null,
        "undefined8"
      ]
    ],
    [
      "00472690",
      "READ",
      [
        "storage",
        "00c252f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00472b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/00472640.md#insn-00472b94) · [`00472678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/00472640.md#insn-00472678) · [`00472684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/00472640.md#insn-00472684)
- 新版 `00472b94`（命令位置の公開資料なし） · `00472678`（命令位置の公開資料なし） · `00472684`（命令位置の公開資料なし）

~~~diff
- 00472b94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:258:8"]]
- 00472b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00472b94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:318:8"]]
+ 00472b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00472b94 bytes 095902b9
+ 00472b94 bytes 091903b9
- 00472678 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:250:8"]]
- 00472678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00472678 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
+ 00472678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00472678 bytes 082941f9
+ 00472678 bytes 088941f9
- 00472684 ["COPY", "tmp:0:8", ["const:230:8"]]
- 00472684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00472684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00472684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00472684 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00472684 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00472684 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00472684 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00472684 bytes 08c10891
+ 00472684 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-906f23d7b3703d2ca679ea2f6b08d8d7"></a>

### [`004737cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/004737cc.md) → [`004737cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/004737cc.md) _INIT_23

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`004723a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00472/004723a4.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`004723a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00472/004723a4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.42% / 新版 83.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 6件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00473808",
      "incomplete_value": true,
      "site": "00473824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00473808",
      "incomplete_value": true,
      "site": "00473824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "0047382c",
      "incomplete_value": true,
      "site": "00473848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0047382c",
      "incomplete_value": true,
      "site": "00473848",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "0047384c",
      "incomplete_value": true,
      "site": "00473868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0047384c",
      "incomplete_value": true,
      "site": "00473868",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "00473808",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "0047382c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "0047384c",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00473808",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0047382c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0047384c",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004737f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/004737cc.md#insn-004737f8) · [`00473800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/004737cc.md#insn-00473800)
- 新版 `004737f8`（命令位置の公開資料なし） · `00473800`（命令位置の公開資料なし）

~~~diff
- 004737f8 ["COPY", "tmp:0:8", ["const:210:8"]]
- 004737f8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004737f8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004737f8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004737f8 ["COPY", "tmp:0:8", ["const:2d0:8"]]
+ 004737f8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004737f8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004737f8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004737f8 bytes 73420891
+ 004737f8 bytes 73420b91
- 00473800 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00473800 bytes a9f1ff90
+ 00473800 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00473800 bytes a9f1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789c529691fccc420496560e7b8ea48a"></a>

### [`00473b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473b84.md) → [`00473b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/00473b84.md) FUN_00473b84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`0073ab94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073a/0073ab94.md) [`0073e258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e258.md) [`0073e4a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e4a4.md) [`0073e6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073eb44.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0052dd54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd54.md) [`00574144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574144.md)
- 新版 呼出元 6件 [`0073ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073ab94.md) [`0073e258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e258.md) [`0073e4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e4a4.md) [`0073e6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e6dc.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md) · 呼出先 12件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0052dd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd54.md) [`00574144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574144.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00473c94",
      "incomplete_value": false,
      "site": "00473c9c",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473c94",
      "incomplete_value": false,
      "site": "00473c9c",
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
            "const:dd0:8"
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
      "definition_site": "00473cb4",
      "incomplete_value": false,
      "site": "00473cb4",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473cb4",
      "incomplete_value": false,
      "site": "00473cb4",
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
            "const:e20:8"
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
      "definition_site": "00473d38",
      "incomplete_value": false,
      "site": "00473d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473d38",
      "incomplete_value": false,
      "site": "00473d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9d0:8"
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
      "00473c9c",
      "DATA",
      [
        "storage",
        "00be8dd0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473cb4",
      "DATA",
      [
        "storage",
        "00be8e20",
        null,
        "undefined *"
      ]
    ],
    [
      "00473d40",
      "DATA",
      [
        "storage",
        "00be69d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00473c9c",
      "DATA",
      [
        "storage",
        "00be8e80",
        null,
        "undefined *"
      ]
    ],
    [
      "00473cb4",
      "DATA",
      [
        "storage",
        "00be8ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "00473d40",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473b84.md#insn-00473c94) · [`00473c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473b84.md#insn-00473c98)
- 新版 `00473c94`（命令位置の公開資料なし） · `00473c98`（命令位置の公開資料なし）

~~~diff
- 00473c94 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00473c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00473c94 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00473c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00473c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00473c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473c94 bytes 08413791
+ 00473c94 bytes 08013a91
- 00473c98 ["COPY", "register:40a0:8", ["register:4000:8"]]
- 00473c98 bytes f40300aa
+ 00473c98 ["COPY", "register:40a0:8", ["register:4000:8"]]
+ 00473c98 bytes f40300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6ae2353ce1f17e3627ae01614647057"></a>

### [`00473ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473ee0.md) → [`00473ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/00473ee0.md) FUN_00473ee0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00473ee4",
      "incomplete_value": false,
      "site": "00473ee8",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473ee4",
      "incomplete_value": false,
      "site": "00473ee8",
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
      "00473ee8",
      "DATA",
      [
        "storage",
        "00be8dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00473ee8",
      "DATA",
      [
        "storage",
        "00be8e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473ee0.md#insn-00473ee4)
- 新版 `00473ee4`（命令位置の公開資料なし）

~~~diff
- 00473ee4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00473ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00473ee4 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00473ee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00473ee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00473ee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473ee4 bytes 08413791
+ 00473ee4 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16423e7a2a561365a4aac11703756a8b"></a>

### [`00473ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473ef0.md) → [`00473ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/00473ef0.md) FUN_00473ef0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00473f00",
      "incomplete_value": false,
      "site": "00473f08",
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
            "const:e80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473f00",
      "incomplete_value": false,
      "site": "00473f08",
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
            "const:dd0:8"
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
      "00473f08",
      "DATA",
      [
        "storage",
        "00be8dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00473f08",
      "DATA",
      [
        "storage",
        "00be8e80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473ef0.md#insn-00473f00)
- 新版 `00473f00`（命令位置の公開資料なし）

~~~diff
- 00473f00 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00473f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00473f00 ["COPY", "tmp:0:8", ["const:e80:8"]]
+ 00473f00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00473f00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00473f00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473f00 bytes 08413791
+ 00473f00 bytes 08013a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb8bae276d0b0e974136cdad6a6cafce"></a>

### [`00473f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473f20.md) → [`00473f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00473/00473f20.md) FUN_00473f20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00473f38",
      "incomplete_value": false,
      "site": "00473f3c",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00473f38",
      "incomplete_value": false,
      "site": "00473f3c",
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
            "const:e20:8"
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
      "00473f3c",
      "DATA",
      [
        "storage",
        "00be8e20",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00473f3c",
      "DATA",
      [
        "storage",
        "00be8ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00473f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00473/00473f20.md#insn-00473f38)
- 新版 `00473f38`（命令位置の公開資料なし）

~~~diff
- 00473f38 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00473f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00473f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00473f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00473f38 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00473f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00473f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00473f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00473f38 bytes 08813891
+ 00473f38 bytes 08413b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-518fe6e3ffc3a3641d0d702009e5b6ca"></a>

### [`00474160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474160.md) → [`00474160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474160.md) FUN_00474160

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574238.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "004741a8",
      "incomplete_value": true,
      "site": "004741b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "004741a8",
      "incomplete_value": true,
      "site": "004741b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0047419c",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "004741b0",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "004741d8",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047419c",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "004741b0",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "004741d8",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047419c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474160.md#insn-0047419c)
- 新版 `0047419c`（命令位置の公開資料なし）

~~~diff
- 0047419c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
- 0047419c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047419c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 0047419c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0047419c bytes 299946f9
+ 0047419c bytes 29f146f9
~~~


<a id="compare-ef14dae9b3cbedbdcfa1d593174ec401"></a>

### [`0047423c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047423c.md) → [`0047423c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047423c.md) FUN_0047423c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574238.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.33% / 新版 93.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047428c",
      "incomplete_value": true,
      "site": "00474294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047428c",
      "incomplete_value": true,
      "site": "00474294",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00474280",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00474294",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "004742bc",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474280",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00474294",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "004742bc",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047423c.md#insn-00474280)
- 新版 `00474280`（命令位置の公開資料なし）

~~~diff
- 00474280 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
- 00474280 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00474280 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 00474280 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474280 bytes 299946f9
+ 00474280 bytes 29f146f9
~~~


<a id="compare-d1a6f32ac0a0a32e83775fdc5668e96a"></a>

### [`00474324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474324.md) → [`00474324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474324.md) FUN_00474324

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574238.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "00474370",
      "incomplete_value": true,
      "site": "00474378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00474370",
      "incomplete_value": true,
      "site": "00474378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00474364",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00474378",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "004743a0",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474364",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00474378",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "004743a0",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474364`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474324.md#insn-00474364)
- 新版 `00474364`（命令位置の公開資料なし）

~~~diff
- 00474364 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
- 00474364 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00474364 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 00474364 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474364 bytes 299946f9
+ 00474364 bytes 29f146f9
~~~


<a id="compare-eb5b439a01be2510cbf548e26f98ccad"></a>

### [`00474404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474404.md) → [`00474404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474404.md) FUN_00474404

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574238.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00436954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436954.md) [`00574238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574238.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0047444c",
      "incomplete_value": true,
      "site": "00474454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0047444c",
      "incomplete_value": true,
      "site": "00474454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00474440",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00474454",
      "DATA",
      [
        "storage",
        "00bf0548",
        null,
        "pointer"
      ]
    ],
    [
      "0047447c",
      "READ",
      [
        "storage",
        "00bf0550",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474440",
      "READ",
      [
        "storage",
        "00c1ade0",
        null,
        "pointer"
      ]
    ],
    [
      "00474454",
      "DATA",
      [
        "storage",
        "00bf05f8",
        null,
        "pointer"
      ]
    ],
    [
      "0047447c",
      "READ",
      [
        "storage",
        "00bf0600",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474404.md#insn-00474440)
- 新版 `00474440`（命令位置の公開資料なし）

~~~diff
- 00474440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
- 00474440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00474440 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:de0:8"]]
+ 00474440 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00474440 bytes 299946f9
+ 00474440 bytes 29f146f9
~~~


<a id="compare-4841e920d9b0d25d64e0c8db6d7fdca1"></a>

### [`004744e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004744e8.md) → [`004744e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004744e8.md) FUN_004744e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0042e9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042e/0042eb00.md) [`0052de60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052de60.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`0042eb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eb00.md) [`0052de60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052de60.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.71% / 新版 88.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00474560",
      "incomplete_value": true,
      "site": "00474568",
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
      "definition_site": "00474560",
      "incomplete_value": true,
      "site": "00474568",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
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
                "const:20:8"
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
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
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
                "const:20:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00474570",
      "incomplete_value": true,
      "site": "00474570",
      "value": [
        "LOAD",
        "8",
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
      "0047455c",
      "READ",
      [
        "storage",
        "00c1ad20",
        null,
        "pointer"
      ]
    ],
    [
      "00474560",
      "READ",
      [
        "storage",
        "00c13240",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00474564",
      "READ",
      [
        "storage",
        "00c13280",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ],
  "added": [
    [
      "0047455c",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00474560",
      "READ",
      [
        "storage",
        "00c132f0",
        "_ZTTNSt6__ndk118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ],
    [
      "00474564",
      "READ",
      [
        "storage",
        "00c13330",
        null,
        "pointer __((offset(0x68)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047455c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004744e8.md#insn-0047455c) · [`00474578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004744e8.md#insn-00474578)
- 新版 `0047455c`（命令位置の公開資料なし） · `00474578`（命令位置の公開資料なし）

~~~diff
- 0047455c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d20:8"]]
- 0047455c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047455c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dd0:8"]]
+ 0047455c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0047455c bytes d69246f9
+ 0047455c bytes d6ea46f9
- 00474578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00474578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00474578 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 00474578 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00474578 bytes 086946f9
+ 00474578 bytes 08c146f9
~~~


<a id="compare-67ffbbbe0ad3ddb25fbb7392d1cd416b"></a>

### [`004747cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004747cc.md) → [`004747cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004747cc.md) FUN_004747cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00469fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469fa8.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00469fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fa8.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00474808",
      "incomplete_value": true,
      "site": "00474820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:322:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474808",
      "incomplete_value": true,
      "site": "00474820",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:295:8"
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
      "00474808",
      "READ",
      [
        "storage",
        "002a0295",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00474808",
      "READ",
      [
        "storage",
        "002a0322",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004747cc.md#insn-00474804)
- 新版 `00474804`（命令位置の公開資料なし）

~~~diff
- 00474804 ["COPY", "tmp:0:8", ["const:295:8"]]
- 00474804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00474804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00474804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00474804 ["COPY", "tmp:0:8", ["const:322:8"]]
+ 00474804 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00474804 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00474804 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00474804 bytes 29550a91
+ 00474804 bytes 29890c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d789cb4d92cab0dd16941dbbfb7a7b6d"></a>

### [`004749f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004749f8.md) → [`004749f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/004749f8.md) FUN_004749f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00469f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f78.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/00566448.md)
- 新版 呼出元 1件 [`00469f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f78.md) · 呼出先 8件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00565f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00565/00565f94.md) [`0056626c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056626c.md) [`00566284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566284.md) [`00566448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/00566448.md)

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
      "definition_site": "00474a38",
      "incomplete_value": true,
      "site": "00474a50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:273:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474a38",
      "incomplete_value": true,
      "site": "00474a50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:1e6:8"
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
      "00474a38",
      "READ",
      [
        "storage",
        "0029b1e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00474a38",
      "READ",
      [
        "storage",
        "0029b273",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/004749f8.md#insn-00474a2c)
- 新版 `00474a2c`（命令位置の公開資料なし）

~~~diff
- 00474a2c ["COPY", "tmp:0:8", ["const:1e6:8"]]
- 00474a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00474a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00474a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00474a2c ["COPY", "tmp:0:8", ["const:273:8"]]
+ 00474a2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00474a2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00474a2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00474a2c bytes 29990791
+ 00474a2c bytes 29cd0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10c2e65e7d4b8d39b8cf8f197f172d91"></a>

### [`00474c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474c0c.md) → [`00474c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474c0c.md) FUN_00474c0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060f/0060f9b8.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060f9b8.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00474c4c",
      "incomplete_value": false,
      "site": "00474c50",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c4c",
      "incomplete_value": false,
      "site": "00474c50",
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
            "const:eb8:8"
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
      "definition_site": "00474c94",
      "incomplete_value": false,
      "site": "00474c98",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474c94",
      "incomplete_value": false,
      "site": "00474c98",
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
            "const:f08:8"
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
      "00474c50",
      "DATA",
      [
        "storage",
        "00be8eb8",
        null,
        "undefined *"
      ]
    ],
    [
      "00474c98",
      "DATA",
      [
        "storage",
        "00be8f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00474c50",
      "DATA",
      [
        "storage",
        "00be8f68",
        null,
        "undefined *"
      ]
    ],
    [
      "00474c98",
      "DATA",
      [
        "storage",
        "00be8fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474c4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474c0c.md#insn-00474c4c) · [`00474c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474c0c.md#insn-00474c94)
- 新版 `00474c4c`（命令位置の公開資料なし） · `00474c94`（命令位置の公開資料なし）

~~~diff
- 00474c4c ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00474c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474c4c ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00474c4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474c4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474c4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474c4c bytes 08e13a91
+ 00474c4c bytes 08a13d91
- 00474c94 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00474c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00474c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00474c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00474c94 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00474c94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00474c94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00474c94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00474c94 bytes 08213c91
+ 00474c94 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-900400bb1287ab55ac3ce9aeb982840f"></a>

### [`00474da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474da4.md) → [`00474da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474da4.md) FUN_00474da4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0060f9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060f/0060f9b8.md) · 呼出先 7件 [`004751fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004751fc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb220.md)
- 新版 呼出元 2件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060f9b8.md) · 呼出先 7件 [`004751fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004751fc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00474dd8",
      "incomplete_value": false,
      "site": "00474ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:334:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474dd8",
      "incomplete_value": false,
      "site": "00474ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:2a7:8"
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
      "00474dd8",
      "PARAM",
      [
        "storage",
        "0029d2a7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00474dd8",
      "PARAM",
      [
        "storage",
        "0029d334",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474da4.md#insn-00474dd8)
- 新版 `00474dd8`（命令位置の公開資料なし）

~~~diff
- 00474dd8 ["COPY", "tmp:0:8", ["const:2a7:8"]]
- 00474dd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00474dd8 ["COPY", "tmp:0:8", ["const:334:8"]]
+ 00474dd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00474dd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00474dd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00474dd8 bytes 009c0a91
+ 00474dd8 bytes 00d00c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91fa071fd68c2dda386b168ef8d4bc5d"></a>

### [`00474f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md) → [`00474f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474f1c.md) FUN_00474f1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060f/0060f9b8.md) · 呼出先 11件 [`004751fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/004751fc.md) [`00475e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475e24.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`0060f9b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060f9b8.md) · 呼出先 11件 [`004751fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004751fc.md) [`00475e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475e24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00474f58",
      "incomplete_value": false,
      "site": "00474f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:334:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00474f58",
      "incomplete_value": false,
      "site": "00474f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:2a7:8"
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
      "definition_site": "0047511c",
      "incomplete_value": false,
      "site": "00475120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:5d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047511c",
      "incomplete_value": false,
      "site": "00475120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:544:8"
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
      "00474f58",
      "PARAM",
      [
        "storage",
        "0029d2a7",
        null,
        "string"
      ]
    ],
    [
      "0047511c",
      "PARAM",
      [
        "storage",
        "00294544",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00474f58",
      "PARAM",
      [
        "storage",
        "0029d334",
        null,
        "string"
      ]
    ],
    [
      "0047511c",
      "PARAM",
      [
        "storage",
        "002945d1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00474f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md#insn-00474f58) · [`0047511c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md#insn-0047511c)
- 新版 `00474f58`（命令位置の公開資料なし） · `0047511c`（命令位置の公開資料なし）

~~~diff
- 00474f58 ["COPY", "tmp:0:8", ["const:2a7:8"]]
- 00474f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00474f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00474f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00474f58 ["COPY", "tmp:0:8", ["const:334:8"]]
+ 00474f58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00474f58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00474f58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00474f58 bytes 009c0a91
+ 00474f58 bytes 00d00c91
- 0047511c ["COPY", "tmp:0:8", ["const:544:8"]]
- 0047511c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0047511c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0047511c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0047511c ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 0047511c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0047511c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0047511c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0047511c bytes 21101591
+ 0047511c bytes 21441791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9eb90d657774481787c6acd17f2df842"></a>

### [`0047580c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/0047580c.md) → [`0047580c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/0047580c.md) FUN_0047580c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 4件 [`0060ffa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0060f/0060ffa8.md) [`00610540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00610/00610540.md) [`00838c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838c74.md) [`00838ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00838/00838ef4.md) · 呼出先 6件 [`00475470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475470.md) [`00477e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477e0c.md) [`00477e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477e1c.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 4件 [`0060ffa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060f/0060ffa8.md) [`00610540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00610/00610540.md) [`00838c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838c74.md) [`00838ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00838/00838ef4.md) · 呼出先 6件 [`00475470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475470.md) [`00477e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477e0c.md) [`00477e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477e1c.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00475860",
      "incomplete_value": false,
      "site": "00475860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475860",
      "incomplete_value": false,
      "site": "00475860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00475860",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ],
    [
      "00475898",
      "READ",
      [
        "storage",
        "00be9078",
        null,
        "pointer"
      ]
    ],
    [
      "00475898",
      "READ",
      [
        "storage",
        "00be9080",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475860",
      "DATA",
      [
        "storage",
        "00be9108",
        null,
        "undefined *"
      ]
    ],
    [
      "00475898",
      "READ",
      [
        "storage",
        "00be9128",
        null,
        "pointer"
      ]
    ],
    [
      "00475898",
      "READ",
      [
        "storage",
        "00be9130",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/0047580c.md#insn-00475858)
- 新版 `00475858`（命令位置の公開資料なし）

~~~diff
- 00475858 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00475858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475858 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00475858 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475858 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475858 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475858 bytes 08610191
+ 00475858 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e4c7c7a7035d22d046402b39a7cb95e"></a>

### [`00475a04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475a04.md) → [`00475a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475a04.md) FUN_00475a04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00475a08",
      "incomplete_value": false,
      "site": "00475a0c",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475a08",
      "incomplete_value": false,
      "site": "00475a0c",
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
      "00475a0c",
      "DATA",
      [
        "storage",
        "00be8eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475a0c",
      "DATA",
      [
        "storage",
        "00be8f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475a08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475a04.md#insn-00475a08)
- 新版 `00475a08`（命令位置の公開資料なし）

~~~diff
- 00475a08 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00475a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475a08 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00475a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475a08 bytes 08e13a91
+ 00475a08 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7695bec3ef09a3537ccfb64cd28350a"></a>

### [`00475a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475a14.md) → [`00475a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475a14.md) FUN_00475a14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00475a24",
      "incomplete_value": false,
      "site": "00475a2c",
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
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475a24",
      "incomplete_value": false,
      "site": "00475a2c",
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
      "00475a2c",
      "DATA",
      [
        "storage",
        "00be8eb8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475a2c",
      "DATA",
      [
        "storage",
        "00be8f68",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475a14.md#insn-00475a24)
- 新版 `00475a24`（命令位置の公開資料なし）

~~~diff
- 00475a24 ["COPY", "tmp:0:8", ["const:eb8:8"]]
- 00475a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475a24 ["COPY", "tmp:0:8", ["const:f68:8"]]
+ 00475a24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475a24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475a24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475a24 bytes 08e13a91
+ 00475a24 bytes 08a13d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-688ce04f61be4672029cffc242ce164b"></a>

### [`00475c14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475c14.md) → [`00475c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475c14.md) FUN_00475c14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md)

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
      "definition_site": "00475c18",
      "incomplete_value": false,
      "site": "00475c1c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475c18",
      "incomplete_value": false,
      "site": "00475c1c",
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
      "00475c1c",
      "DATA",
      [
        "storage",
        "00be8f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475c1c",
      "DATA",
      [
        "storage",
        "00be8fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475c14.md#insn-00475c18)
- 新版 `00475c18`（命令位置の公開資料なし）

~~~diff
- 00475c18 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00475c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475c18 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00475c18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475c18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475c18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475c18 bytes 08213c91
+ 00475c18 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87e3f35855159d8501bd2dcc6dd6106f"></a>

### [`00475c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475c24.md) → [`00475c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475c24.md) FUN_00475c24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf50.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

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
      "definition_site": "00475c34",
      "incomplete_value": false,
      "site": "00475c3c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475c34",
      "incomplete_value": false,
      "site": "00475c3c",
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
            "const:f08:8"
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
      "00475c3c",
      "DATA",
      [
        "storage",
        "00be8f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475c3c",
      "DATA",
      [
        "storage",
        "00be8fb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475c34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475c24.md#insn-00475c34)
- 新版 `00475c34`（命令位置の公開資料なし）

~~~diff
- 00475c34 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 00475c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00475c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00475c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00475c34 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00475c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00475c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00475c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00475c34 bytes 08213c91
+ 00475c34 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7337fe54cb04d94866f6db7b12df0549"></a>

### [`00475e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475e24.md) → [`00475e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/00475e24.md) FUN_00475e24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00474f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474f1c.md) · 呼出先 15件 [`004763f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/004763f8.md) [`00476598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476598.md) [`00476868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476868.md) [`0047686c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/0047686c.md) [`00574778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574778.md)
- 新版 呼出元 1件 [`00474f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474f1c.md) · 呼出先 15件 [`004763f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/004763f8.md) [`00476598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476598.md) [`00476868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476868.md) [`0047686c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/0047686c.md) [`00574778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.54% / 新版 96.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047608c",
      "incomplete_value": false,
      "site": "0047608c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047608c",
      "incomplete_value": false,
      "site": "0047608c",
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
            "const:fd8:8"
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
      "definition_site": "00475e78",
      "incomplete_value": false,
      "site": "00475e7c",
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
            "const:2af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00475e78",
      "incomplete_value": false,
      "site": "00475e7c",
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
            "const:222:8"
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
      "definition_site": "0047612c",
      "incomplete_value": false,
      "site": "00476130",
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
            "const:40d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047612c",
      "incomplete_value": false,
      "site": "00476130",
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
            "const:414:8"
          ]
        ]
      ]
    },
    "ordinal": 25,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00475e78",
      "PARAM",
      [
        "storage",
        "0029e222",
        null,
        "string"
      ]
    ],
    [
      "00476070",
      "PARAM",
      [
        "storage",
        "002a937e",
        null,
        "string"
      ]
    ],
    [
      "0047608c",
      "DATA",
      [
        "storage",
        "00be8fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00475e78",
      "PARAM",
      [
        "storage",
        "0029e2af",
        null,
        "string"
      ]
    ],
    [
      "00476070",
      "PARAM",
      [
        "storage",
        "002a92ea",
        null,
        "string"
      ]
    ],
    [
      "0047608c",
      "DATA",
      [
        "storage",
        "00be9088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00475e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475e24.md#insn-00475e78) · [`00475e94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475e24.md#insn-00475e94) · [`00475e9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00475/00475e24.md#insn-00475e9c)
- 新版 `00475e78`（命令位置の公開資料なし） · `00475e94`（命令位置の公開資料なし）

~~~diff
- 00475e78 ["COPY", "tmp:0:8", ["const:222:8"]]
- 00475e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00475e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00475e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00475e78 ["COPY", "tmp:0:8", ["const:2af:8"]]
+ 00475e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00475e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00475e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00475e78 bytes 00880891
+ 00475e78 bytes 00bc0a91
- 00475e94 ["COPY", "tmp:0:8", ["const:3fa:8"]]
- 00475e94 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00475e94 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00475e94 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00475e94 ["COPY", "tmp:0:8", ["const:3f3:8"]]
+ 00475e94 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00475e94 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00475e94 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00475e94 bytes d6ea0f91
+ 00475e94 bytes d6ce0f91
- 00475e9c ["COPY", "register:40e0:8", ["const:be8000:8"]]
- 00475e9c bytes 9c3b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3881a04ec5bbeae06037663f3046f28"></a>

### [`00476704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476704.md) → [`00476704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476704.md) FUN_00476704

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00476728",
      "incomplete_value": false,
      "site": "0047672c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476728",
      "incomplete_value": false,
      "site": "0047672c",
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
            "const:f58:8"
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
      "0047672c",
      "DATA",
      [
        "storage",
        "00be8f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047672c",
      "DATA",
      [
        "storage",
        "00be9008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476724`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476704.md#insn-00476724) · [`00476728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476704.md#insn-00476728)
- 新版 `00476724`（命令位置の公開資料なし） · `00476728`（命令位置の公開資料なし）

~~~diff
- 00476724 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00476724 ["COPY", "register:4040:8", ["const:be9000:8"]]
- 00476724 bytes 883b00d0
+ 00476724 bytes 883b00f0
- 00476728 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00476728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00476728 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00476728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00476728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00476728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476728 bytes 08613d91
+ 00476728 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd8fe99c3e6f091b256e0c4847817fb1"></a>

### [`00476744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476744.md) → [`00476744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476744.md) FUN_00476744

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
      "definition_site": "00476748",
      "incomplete_value": false,
      "site": "0047674c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476748",
      "incomplete_value": false,
      "site": "0047674c",
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
            "const:f58:8"
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
      "0047674c",
      "DATA",
      [
        "storage",
        "00be8f58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047674c",
      "DATA",
      [
        "storage",
        "00be9008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476744.md#insn-00476744) · [`00476748`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476744.md#insn-00476748)
- 新版 `00476744`（命令位置の公開資料なし） · `00476748`（命令位置の公開資料なし）

~~~diff
- 00476744 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00476744 ["COPY", "register:4040:8", ["const:be9000:8"]]
- 00476744 bytes 883b00d0
+ 00476744 bytes 883b00f0
- 00476748 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00476748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00476748 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00476748 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00476748 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00476748 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476748 bytes 08613d91
+ 00476748 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f19fb9a31004b3503fa0327f790f00d"></a>

### [`00476818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476818.md) → [`00476818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476818.md) FUN_00476818

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00476838",
      "incomplete_value": false,
      "site": "0047683c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476838",
      "incomplete_value": false,
      "site": "0047683c",
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
            "const:fd8:8"
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
      "0047683c",
      "DATA",
      [
        "storage",
        "00be8fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0047683c",
      "DATA",
      [
        "storage",
        "00be9088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476818.md#insn-00476834) · [`00476838`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476818.md#insn-00476838)
- 新版 `00476834`（命令位置の公開資料なし） · `00476838`（命令位置の公開資料なし）

~~~diff
- 00476834 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00476834 ["COPY", "register:4040:8", ["const:be9000:8"]]
- 00476834 bytes 883b00d0
+ 00476834 bytes 883b00f0
- 00476838 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00476838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00476838 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00476838 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00476838 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00476838 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476838 bytes 08613f91
+ 00476838 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-353dda87eef2b83f7589a4b0c7fec815"></a>

### [`00476850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476850.md) → [`00476850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00476/00476850.md) FUN_00476850

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
      "definition_site": "00476854",
      "incomplete_value": false,
      "site": "00476858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00476854",
      "incomplete_value": false,
      "site": "00476858",
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
            "const:fd8:8"
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
      "00476858",
      "DATA",
      [
        "storage",
        "00be8fd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00476858",
      "DATA",
      [
        "storage",
        "00be9088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00476850`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476850.md#insn-00476850) · [`00476854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00476/00476850.md#insn-00476854)
- 新版 `00476850`（命令位置の公開資料なし） · `00476854`（命令位置の公開資料なし）

~~~diff
- 00476850 ["COPY", "register:4040:8", ["const:be8000:8"]]
+ 00476850 ["COPY", "register:4040:8", ["const:be9000:8"]]
- 00476850 bytes 883b00d0
+ 00476850 bytes 883b00f0
- 00476854 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00476854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00476854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00476854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00476854 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00476854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00476854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00476854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00476854 bytes 08613f91
+ 00476854 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94349c1aea34e7e7bc03ca0d4c002f09"></a>

### [`00477d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d2c.md) → [`00477d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477d2c.md) FUN_00477d2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

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
      "definition_site": "00477d38",
      "incomplete_value": false,
      "site": "00477d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477d38",
      "incomplete_value": false,
      "site": "00477d3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00477d3c",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00477d3c",
      "DATA",
      [
        "storage",
        "00be9108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477d38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d2c.md#insn-00477d38)
- 新版 `00477d38`（命令位置の公開資料なし）

~~~diff
- 00477d38 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00477d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00477d38 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00477d38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00477d38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00477d38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477d38 bytes 29610191
+ 00477d38 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71a6dbbf671faa246d42921884116adf"></a>

### [`00477d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d4c.md) → [`00477d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477d4c.md) FUN_00477d4c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00477d54",
      "incomplete_value": false,
      "site": "00477d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477d54",
      "incomplete_value": false,
      "site": "00477d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00477d58",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00477d58",
      "DATA",
      [
        "storage",
        "00be9108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d4c.md#insn-00477d54)
- 新版 `00477d54`（命令位置の公開資料なし）

~~~diff
- 00477d54 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00477d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00477d54 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00477d54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00477d54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00477d54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477d54 bytes 29610191
+ 00477d54 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fe866e82ec1815214da3fd6da50afa"></a>

### [`00477d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d88.md) → [`00477d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477d88.md) FUN_00477d88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00477dac",
      "incomplete_value": false,
      "site": "00477dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477dac",
      "incomplete_value": false,
      "site": "00477dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00477dac",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00477dac",
      "DATA",
      [
        "storage",
        "00be9108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477da8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477d88.md#insn-00477da8)
- 新版 `00477da8`（命令位置の公開資料なし）

~~~diff
- 00477da8 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00477da8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477da8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477da8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00477da8 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00477da8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00477da8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00477da8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477da8 bytes 29610191
+ 00477da8 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ae3bac41bef976d657d85c7e73983f"></a>

### [`00477dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477dd8.md) → [`00477dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477dd8.md) FUN_00477dd8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)

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
      "definition_site": "00477de4",
      "incomplete_value": false,
      "site": "00477de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00477de4",
      "incomplete_value": false,
      "site": "00477de4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be9000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00477de4",
      "DATA",
      [
        "storage",
        "00be9058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00477de4",
      "DATA",
      [
        "storage",
        "00be9108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477dd8.md#insn-00477de0)
- 新版 `00477de0`（命令位置の公開資料なし）

~~~diff
- 00477de0 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00477de0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00477de0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00477de0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00477de0 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00477de0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00477de0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00477de0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00477de0 bytes 29610191
+ 00477de0 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cad3ffe8d7d7da92411e048db7eaeb65"></a>

### [`00477f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477f54.md) → [`00477f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00477/00477f54.md) _INIT_24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "00477f90",
      "incomplete_value": true,
      "site": "00477fac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00477f90",
      "incomplete_value": true,
      "site": "00477fac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e4:8"
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
      "definition_site": "00477fb4",
      "incomplete_value": true,
      "site": "00477fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00477fb4",
      "incomplete_value": true,
      "site": "00477fd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2f7:8"
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
      "definition_site": "00477fd4",
      "incomplete_value": true,
      "site": "00477ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00477fd4",
      "incomplete_value": true,
      "site": "00477ff0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:da:8"
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
      "00477f90",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00477fb4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00477fd4",
      "READ",
      [
        "storage",
        "002a80da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00477f90",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00477fb4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00477fd4",
      "READ",
      [
        "storage",
        "002a8046",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00477f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477f54.md#insn-00477f80) · [`00477f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00477/00477f54.md#insn-00477f88)
- 新版 `00477f80`（命令位置の公開資料なし） · `00477f88`（命令位置の公開資料なし）

~~~diff
- 00477f80 ["COPY", "tmp:0:8", ["const:260:8"]]
- 00477f80 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00477f80 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00477f80 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00477f80 ["COPY", "tmp:0:8", ["const:320:8"]]
+ 00477f80 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00477f80 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00477f80 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00477f80 bytes 73820991
+ 00477f80 bytes 73820c91
- 00477f88 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00477f88 bytes 89f1ff90
+ 00477f88 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00477f88 bytes 89f1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-066a3a7b56ccd1a2e6b183898c6f155f"></a>

### [`004785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md) → [`004785c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004785c8.md) FUN_004785c8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004787b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md) [`0047cc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cc18.md) [`0047cd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cd90.md) [`0047cef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cef8.md) · 呼出先 4件 [`0045a6dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a7e0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 4件 [`004787b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004787b4.md) [`0047cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cc18.md) [`0047cd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cd90.md) [`0047cef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cef8.md) · 呼出先 4件 [`0045a6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a6dc.md) [`0045a7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a7e0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.52% / 新版 95.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004786bc",
      "incomplete_value": false,
      "site": "004786c4",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004786bc",
      "incomplete_value": false,
      "site": "004786c4",
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
            "const:c53:8"
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
      "definition_site": "004786cc",
      "incomplete_value": true,
      "site": "004786d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004786cc",
      "incomplete_value": true,
      "site": "004786d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004786c4",
      "DATA",
      [
        "storage",
        "00298c53",
        null,
        "string"
      ]
    ],
    [
      "004786cc",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "004786cc",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "004786c4",
      "DATA",
      [
        "storage",
        "00298ce0",
        null,
        "string"
      ]
    ],
    [
      "004786cc",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "004786cc",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004786bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md#insn-004786bc) · [`004786cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md#insn-004786cc)
- 新版 `004786bc`（命令位置の公開資料なし） · `004786cc`（命令位置の公開資料なし）

~~~diff
- 004786bc ["COPY", "tmp:0:8", ["const:c53:8"]]
- 004786bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004786bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004786bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004786bc ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 004786bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004786bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004786bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004786bc bytes 084d3191
+ 004786bc bytes 08813391
- 004786cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 004786cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004786cc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 004786cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004786cc bytes 210c47f9
+ 004786cc bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d02474a4ac4781de2ee1a5db8e36e41d"></a>

### [`004787b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md) → [`004787b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004787b4.md) FUN_004787b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004786d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004786d4.md) · 呼出先 15件 [`004784f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004784f0.md) [`004784fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004784fc.md) [`004785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md) [`00478d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md) [`0047bdcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047bdcc.md)
- 新版 呼出元 1件 [`004786d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004786d4.md) · 呼出先 15件 [`004784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004784f0.md) [`004784fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004784fc.md) [`004785c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004785c8.md) [`00478d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/00478d84.md) [`0047bdcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047bdcc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.77% / 新版 97.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00478c6c",
      "incomplete_value": false,
      "site": "00478c70",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c6c",
      "incomplete_value": false,
      "site": "00478c70",
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
            "const:c66:8"
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
      "definition_site": "00478c30",
      "incomplete_value": true,
      "site": "00478c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c30",
      "incomplete_value": true,
      "site": "00478c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00478c90",
      "incomplete_value": true,
      "site": "00478c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00478c90",
      "incomplete_value": true,
      "site": "00478c94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00478c24",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "00478c24",
      "DATA",
      [
        "storage",
        "002a742b",
        null,
        "string"
      ]
    ],
    [
      "00478c24",
      "DATA",
      [
        "storage",
        "002a9391",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00478c24",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "00478c24",
      "DATA",
      [
        "storage",
        "002a7424",
        null,
        "string"
      ]
    ],
    [
      "00478c24",
      "DATA",
      [
        "storage",
        "002a92fd",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00478930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md#insn-00478930) · [`00478c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md#insn-00478c20) · [`00478c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md#insn-00478c30)
- 新版 `00478930`（命令位置の公開資料なし） · `00478c20`（命令位置の公開資料なし） · `00478c30`（命令位置の公開資料なし）

~~~diff
- 00478930 ["COPY", "tmp:0:8", ["const:164:8"]]
- 00478930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478930 ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 00478930 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478930 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478930 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478930 bytes 08910591
+ 00478930 bytes 08c50791
- 00478c20 ["COPY", "tmp:0:8", ["const:42b:8"]]
- 00478c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00478c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00478c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00478c20 ["COPY", "tmp:0:8", ["const:424:8"]]
+ 00478c20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00478c20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00478c20 bytes 08ad1091
+ 00478c20 bytes 08911091
- 00478c30 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 00478c30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00478c30 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 00478c30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00478c30 bytes 210c47f9
+ 00478c30 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-284eb74f1bd086fd3403d4d7cfcd174b"></a>

### [`00478d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md) → [`00478d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/00478d84.md) FUN_00478d84

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md) · 呼出先 15件 [`0045a7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a7e0.md) [`0047914c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/0047914c.md) [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md) [`00479f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md)
- 新版 呼出元 1件 [`004787b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004787b4.md) · 呼出先 15件 [`0045a7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a7e0.md) [`0047914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/0047914c.md) [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479c04.md) [`00479f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479f48.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.62% / 新版 98.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479058",
      "incomplete_value": false,
      "site": "0047905c",
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
            "const:ce0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479058",
      "incomplete_value": false,
      "site": "0047905c",
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
            "const:c53:8"
          ]
        ]
      ]
    },
    "ordinal": 56,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047907c",
      "incomplete_value": true,
      "site": "00479080",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047907c",
      "incomplete_value": true,
      "site": "00479080",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047905c",
      "DATA",
      [
        "storage",
        "00298c53",
        null,
        "string"
      ]
    ],
    [
      "0047907c",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047907c",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047905c",
      "DATA",
      [
        "storage",
        "00298ce0",
        null,
        "string"
      ]
    ],
    [
      "0047907c",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047907c",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md#insn-00479058) · [`0047907c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md#insn-0047907c)
- 新版 `00479058`（命令位置の公開資料なし） · `0047907c`（命令位置の公開資料なし）

~~~diff
- 00479058 ["COPY", "tmp:0:8", ["const:c53:8"]]
- 00479058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479058 ["COPY", "tmp:0:8", ["const:ce0:8"]]
+ 00479058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479058 bytes 084d3191
+ 00479058 bytes 08813391
- 0047907c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047907c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047907c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047907c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047907c bytes 210c47f9
+ 0047907c bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c11af98d7b23b1814cb4b92a28191d5"></a>

### [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) → [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) FUN_004794a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md) · 呼出先 14件 [`0047ab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md) [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) [`0047c568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c568.md) [`0047c854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c854.md)
- 新版 呼出元 1件 [`00478d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/00478d84.md) · 呼出先 14件 [`0047ab48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047ba2c.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`0047c568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c568.md) [`0047c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c854.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.59% / 新版 98.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00479b1c",
      "incomplete_value": false,
      "site": "00479b20",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b1c",
      "incomplete_value": false,
      "site": "00479b20",
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
            "const:c66:8"
          ]
        ]
      ]
    },
    "ordinal": 62,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00479b08",
      "incomplete_value": true,
      "site": "00479b0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b08",
      "incomplete_value": true,
      "site": "00479b0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 24,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00479b40",
      "incomplete_value": true,
      "site": "00479b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479b40",
      "incomplete_value": true,
      "site": "00479b44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00479afc",
      "DATA",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "00479afc",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "00479b08",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00479afc",
      "DATA",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "00479afc",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "00479b08",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md#insn-00479ad0) · [`00479af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md#insn-00479af8) · [`00479b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md#insn-00479b08)
- 新版 `00479ad0`（命令位置の公開資料なし） · `00479af8`（命令位置の公開資料なし） · `00479b08`（命令位置の公開資料なし）

~~~diff
- 00479ad0 ["COPY", "tmp:0:8", ["const:164:8"]]
- 00479ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479ad0 ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 00479ad0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479ad0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479ad0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479ad0 bytes 08910591
+ 00479ad0 bytes 08c50791
- 00479af8 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 00479af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479af8 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 00479af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479af8 bytes 08f52091
+ 00479af8 bytes 08292391
- 00479b08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 00479b08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00479b08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 00479b08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00479b08 bytes 210c47f9
+ 00479b08 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a3af29f76cd79b5b23158bf68462dbd"></a>

### [`00479c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md) → [`00479c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479c04.md) FUN_00479c04

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md) · 呼出先 5件 [`0047c52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c540.md) [`0047ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047ca08.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00478d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/00478d84.md) · 呼出先 5件 [`0047c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c540.md) [`0047ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047ca08.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.09% / 新版 98.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00479f40",
      "incomplete_value": true,
      "site": "00479f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00479f40",
      "incomplete_value": true,
      "site": "00479f44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00479f34",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "00479f34",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "00479f34",
      "DATA",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00479f34",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "00479f34",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "00479f34",
      "DATA",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00479f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md#insn-00479f08) · [`00479f1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md#insn-00479f1c) · [`00479f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md#insn-00479f30)
- 新版 `00479f08`（命令位置の公開資料なし） · `00479f1c`（命令位置の公開資料なし） · `00479f30`（命令位置の公開資料なし）

~~~diff
- 00479f08 ["COPY", "tmp:0:8", ["const:164:8"]]
- 00479f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479f08 ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 00479f08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479f08 bytes 08910591
+ 00479f08 bytes 08c50791
- 00479f1c ["COPY", "tmp:0:8", ["const:83d:8"]]
- 00479f1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479f1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479f1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479f1c ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 00479f1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479f1c bytes 08f52091
+ 00479f1c bytes 08292391
- 00479f30 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 00479f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00479f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00479f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00479f30 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 00479f30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00479f30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00479f30 bytes 08993191
+ 00479f30 bytes 08cd3391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf5b8fa36bac265068be45fc7cd2530"></a>

### [`00479f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md) → [`00479f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479f48.md) FUN_00479f48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00478d84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/00478d84.md) · 呼出先 5件 [`0047a5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a5ec.md) [`0047adfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047b068.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00478d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/00478d84.md) · 呼出先 5件 [`0047a5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a5ec.md) [`0047adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047b068.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.05% / 新版 98.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a198",
      "incomplete_value": false,
      "site": "0047a1a0",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a198",
      "incomplete_value": false,
      "site": "0047a1a0",
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
            "const:c66:8"
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
      "definition_site": "0047a1a8",
      "incomplete_value": true,
      "site": "0047a1ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a1a8",
      "incomplete_value": true,
      "site": "0047a1ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047a1a0",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0047a1a8",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047a1a8",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047a1a0",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "0047a1a8",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047a1a8",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md#insn-0047a198) · [`0047a1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md#insn-0047a1a8)
- 新版 `0047a198`（命令位置の公開資料なし） · `0047a1a8`（命令位置の公開資料なし）

~~~diff
- 0047a198 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 0047a198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 0047a198 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a198 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a198 bytes 08993191
+ 0047a198 bytes 08cd3391
- 0047a1a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047a1a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047a1a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047a1a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047a1a8 bytes 210c47f9
+ 0047a1a8 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f4fb017f706de0db22b1636e4bf54c"></a>

### [`0047a39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a39c.md) → [`0047a39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a39c.md) FUN_0047a39c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047914c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/0047914c.md) · 呼出先 5件 [`0047b5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047b5ec.md) [`0047b7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047b7fc.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`0047914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/0047914c.md) · 呼出先 5件 [`0047b5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047b5ec.md) [`0047b7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047b7fc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.47% / 新版 96.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a4d4",
      "incomplete_value": false,
      "site": "0047a4dc",
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
            "const:1f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a4d4",
      "incomplete_value": false,
      "site": "0047a4dc",
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
            "const:164:8"
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
      "definition_site": "0047a4e4",
      "incomplete_value": true,
      "site": "0047a4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a4e4",
      "incomplete_value": true,
      "site": "0047a4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047a4dc",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "0047a4e4",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047a4e4",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047a4dc",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "0047a4e4",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047a4e4",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a4d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a39c.md#insn-0047a4d4) · [`0047a4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a39c.md#insn-0047a4e4)
- 新版 `0047a4d4`（命令位置の公開資料なし） · `0047a4e4`（命令位置の公開資料なし）

~~~diff
- 0047a4d4 ["COPY", "tmp:0:8", ["const:164:8"]]
- 0047a4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a4d4 ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 0047a4d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a4d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a4d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a4d4 bytes 08910591
+ 0047a4d4 bytes 08c50791
- 0047a4e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047a4e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047a4e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047a4e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047a4e4 bytes 210c47f9
+ 0047a4e4 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4d8a603b1a8d42b106a2303e46034d"></a>

### [`0047a5ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a5ec.md) → [`0047a5ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a5ec.md) FUN_0047a5ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0047914c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/0047914c.md) [`00479f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a2c0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 2件 [`0047914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/0047914c.md) [`00479f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479f48.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a2c0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.81% / 新版 98.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047a9c8",
      "incomplete_value": false,
      "site": "0047a9d0",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9c8",
      "incomplete_value": false,
      "site": "0047a9d0",
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
            "const:c66:8"
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
      "definition_site": "0047a9d8",
      "incomplete_value": true,
      "site": "0047a9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047a9d8",
      "incomplete_value": true,
      "site": "0047a9dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047a9d0",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0047a9d8",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047a9d8",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047a9d0",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "0047a9d8",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047a9d8",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047a9c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a5ec.md#insn-0047a9c8) · [`0047a9d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a5ec.md#insn-0047a9d8)
- 新版 `0047a9c8`（命令位置の公開資料なし） · `0047a9d8`（命令位置の公開資料なし）

~~~diff
- 0047a9c8 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 0047a9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047a9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047a9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047a9c8 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 0047a9c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a9c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047a9c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047a9c8 bytes 08993191
+ 0047a9c8 bytes 08cd3391
- 0047a9d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047a9d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047a9d8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047a9d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047a9d8 bytes 210c47f9
+ 0047a9d8 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c12707cfa5a5dc7e4a2b47df1058650"></a>

### [`0047a9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a9e0.md) → [`0047a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a9e0.md) FUN_0047a9e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047914c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/0047914c.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a2c0.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`0047914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/0047914c.md) · 呼出先 3件 [`0047a2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a2c0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ab30",
      "incomplete_value": false,
      "site": "0047ab38",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ab30",
      "incomplete_value": false,
      "site": "0047ab38",
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
            "const:c66:8"
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
      "definition_site": "0047ab40",
      "incomplete_value": true,
      "site": "0047ab44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ab40",
      "incomplete_value": true,
      "site": "0047ab44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047ab38",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0047ab40",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047ab40",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047ab38",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "0047ab40",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047ab40",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ab30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a9e0.md#insn-0047ab30) · [`0047ab40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a9e0.md#insn-0047ab40)
- 新版 `0047ab30`（命令位置の公開資料なし） · `0047ab40`（命令位置の公開資料なし）

~~~diff
- 0047ab30 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 0047ab30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047ab30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047ab30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047ab30 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 0047ab30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047ab30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047ab30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047ab30 bytes 08993191
+ 0047ab30 bytes 08cd3391
- 0047ab40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047ab40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047ab40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047ab40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047ab40 bytes 210c47f9
+ 0047ab40 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d40e070ff5a21d731115a0928f445ec7"></a>

### [`0047adfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md) → [`0047adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047adfc.md) FUN_0047adfc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00479f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479f48.md) · 呼出先 4件 [`0047c52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c540.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`00479f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479f48.md) · 呼出先 4件 [`0047c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c540.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.06% / 新版 98.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047b050",
      "incomplete_value": false,
      "site": "0047b058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:b45:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b050",
      "incomplete_value": false,
      "site": "0047b058",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:299000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "definition_site": "0047b060",
      "incomplete_value": true,
      "site": "0047b064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047b060",
      "incomplete_value": true,
      "site": "0047b064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047b058",
      "DATA",
      [
        "storage",
        "00299ab8",
        null,
        "string"
      ]
    ],
    [
      "0047b060",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047b060",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047b058",
      "DATA",
      [
        "storage",
        "00299b45",
        null,
        "string"
      ]
    ],
    [
      "0047b060",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047b060",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047b050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md#insn-0047b050) · [`0047b060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md#insn-0047b060)
- 新版 `0047b050`（命令位置の公開資料なし） · `0047b060`（命令位置の公開資料なし）

~~~diff
- 0047b050 ["COPY", "tmp:0:8", ["const:ab8:8"]]
- 0047b050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047b050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047b050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047b050 ["COPY", "tmp:0:8", ["const:b45:8"]]
+ 0047b050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047b050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047b050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047b050 bytes 08e12a91
+ 0047b050 bytes 08152d91
- 0047b060 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047b060 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047b060 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047b060 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047b060 bytes 210c47f9
+ 0047b060 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-733b3252c9ecbf2508eb5e682c68b957"></a>

### [`0047ba2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md) → [`0047ba2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047ba2c.md) FUN_0047ba2c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) · 呼出先 8件 [`0047bbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047bbd4.md) [`0047ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047ca08.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) · 呼出先 8件 [`0047bbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047bbd4.md) [`0047ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047ca08.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.23% / 新版 94.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047bb64",
      "incomplete_value": false,
      "site": "0047bb68",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb64",
      "incomplete_value": false,
      "site": "0047bb68",
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
            "const:c66:8"
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
      "definition_site": "0047bb88",
      "incomplete_value": false,
      "site": "0047bb8c",
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
            "const:d03:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb88",
      "incomplete_value": false,
      "site": "0047bb8c",
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
            "const:c76:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047bb74",
      "incomplete_value": true,
      "site": "0047bb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bb74",
      "incomplete_value": true,
      "site": "0047bb78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047bb68",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0047bb74",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047bb74",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047bb68",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "0047bb74",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047bb74",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bb64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md#insn-0047bb64) · [`0047bb74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md#insn-0047bb74) · [`0047bb88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md#insn-0047bb88)
- 新版 `0047bb64`（命令位置の公開資料なし） · `0047bb74`（命令位置の公開資料なし） · `0047bb88`（命令位置の公開資料なし）

~~~diff
- 0047bb64 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 0047bb64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047bb64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047bb64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047bb64 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 0047bb64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bb64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bb64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047bb64 bytes 08993191
+ 0047bb64 bytes 08cd3391
- 0047bb74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047bb74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047bb74 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047bb74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047bb74 bytes 210c47f9
+ 0047bb74 bytes 216447f9
- 0047bb88 ["COPY", "tmp:0:8", ["const:c76:8"]]
- 0047bb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047bb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047bb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047bb88 ["COPY", "tmp:0:8", ["const:d03:8"]]
+ 0047bb88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bb88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bb88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047bb88 bytes 08d93191
+ 0047bb88 bytes 080d3491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-392db613303d18e8382e17cbe43090bf"></a>

### [`0047bbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047bbd4.md) → [`0047bbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047bbd4.md) FUN_0047bbd4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0047ab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md) · 呼出先 2件 [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 2件 [`0047ab48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047ba2c.md) · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.08% / 新版 95.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047bcb0",
      "incomplete_value": false,
      "site": "0047bcb8",
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
            "const:cf3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bcb0",
      "incomplete_value": false,
      "site": "0047bcb8",
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
            "const:c66:8"
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
      "definition_site": "0047bcc0",
      "incomplete_value": true,
      "site": "0047bcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047bcc0",
      "incomplete_value": true,
      "site": "0047bcc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047bcb8",
      "DATA",
      [
        "storage",
        "00298c66",
        null,
        "string"
      ]
    ],
    [
      "0047bcc0",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047bcc0",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047bcb8",
      "DATA",
      [
        "storage",
        "00298cf3",
        null,
        "string"
      ]
    ],
    [
      "0047bcc0",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047bcc0",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047bcb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047bbd4.md#insn-0047bcb0) · [`0047bcc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047bbd4.md#insn-0047bcc0)
- 新版 `0047bcb0`（命令位置の公開資料なし） · `0047bcc0`（命令位置の公開資料なし）

~~~diff
- 0047bcb0 ["COPY", "tmp:0:8", ["const:c66:8"]]
- 0047bcb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047bcb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047bcb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047bcb0 ["COPY", "tmp:0:8", ["const:cf3:8"]]
+ 0047bcb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bcb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047bcb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047bcb0 bytes 08993191
+ 0047bcb0 bytes 08cd3391
- 0047bcc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047bcc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047bcc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047bcc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047bcc0 bytes 210c47f9
+ 0047bcc0 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00359b1d51623c356abe75d1c48d0126"></a>

### [`0047c518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c518.md) → [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) FUN_0047c518

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 65件 [`0047914c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/0047914c.md) [`0058c05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0058c/0058c05c.md) [`005b8a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b8/005b8a40.md) [`005be130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005be/005be130.md) [`005c27f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005c2/005c27f4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 65件 [`0047914c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/0047914c.md) [`0058c05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0058c/0058c05c.md) [`005b8a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b8/005b8a40.md) [`005be130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be130.md) [`005c27f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005c2/005c27f4.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0047c524",
      "incomplete_value": false,
      "site": "0047c528",
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
    "old": {
      "definition_site": "0047c524",
      "incomplete_value": false,
      "site": "0047c528",
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
      "0047c524",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047c524",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c518.md#insn-0047c524)
- 新版 `0047c524`（命令位置の公開資料なし）

~~~diff
- 0047c524 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047c524 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c524 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c524 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c524 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047c524 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c524 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c524 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c524 bytes 00280c91
+ 0047c524 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fbae1125deef361daa842593cfb610a"></a>

### [`0047c52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c52c.md) → [`0047c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c52c.md) FUN_0047c52c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00479c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 5件 [`00479c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0047c538",
      "incomplete_value": false,
      "site": "0047c53c",
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
    "old": {
      "definition_site": "0047c538",
      "incomplete_value": false,
      "site": "0047c53c",
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
      "0047c538",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047c538",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c52c.md#insn-0047c538)
- 新版 `0047c538`（命令位置の公開資料なし）

~~~diff
- 0047c538 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047c538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c538 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047c538 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c538 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c538 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c538 bytes 00280c91
+ 0047c538 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4fa07ca0e2d47a8d8c55247190a74b5"></a>

### [`0047c540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c540.md) → [`0047c540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c540.md) FUN_0047c540

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`00479c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 6件 [`00479c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479c04.md) [`0047a228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a228.md) [`0047a2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047a2c0.md) [`0047adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047adfc.md) [`0047b068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047b068.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0047c54c",
      "incomplete_value": false,
      "site": "0047c550",
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
    "old": {
      "definition_site": "0047c54c",
      "incomplete_value": false,
      "site": "0047c550",
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
      "0047c54c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047c54c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c540.md#insn-0047c54c)
- 新版 `0047c54c`（命令位置の公開資料なし）

~~~diff
- 0047c54c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047c54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c54c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047c54c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c54c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c54c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c54c bytes 00280c91
+ 0047c54c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70ec12fe719bed882ccfcf5b438c32c3"></a>

### [`0047c554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md) → [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) FUN_0047c554

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 77件 [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) [`0047ab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047ab48.md) [`0047c568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c568.md) [`0047d078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d078.md) [`0047f2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047f/0047f2d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 77件 [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) [`0047ab48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047ab48.md) [`0047c568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c568.md) [`0047d078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d078.md) [`0047f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f2d0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0047c560",
      "incomplete_value": false,
      "site": "0047c564",
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
    "old": {
      "definition_site": "0047c560",
      "incomplete_value": false,
      "site": "0047c564",
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
      "0047c560",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047c560",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c554.md#insn-0047c560)
- 新版 `0047c560`（命令位置の公開資料なし）

~~~diff
- 0047c560 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047c560 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c560 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c560 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c560 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047c560 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c560 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c560 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c560 bytes 00280c91
+ 0047c560 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e20522853ca907b0b2d7d9ff37c0063b"></a>

### [`0047c9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c9e0.md) → [`0047c9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c9e0.md) FUN_0047c9e0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047c854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c854.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0047c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c854.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0047c9ec",
      "incomplete_value": false,
      "site": "0047c9f0",
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
    "old": {
      "definition_site": "0047c9ec",
      "incomplete_value": false,
      "site": "0047c9f0",
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
      "0047c9ec",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047c9ec",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047c9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c9e0.md#insn-0047c9ec)
- 新版 `0047c9ec`（命令位置の公開資料なし）

~~~diff
- 0047c9ec ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047c9ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047c9ec ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047c9ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c9ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047c9ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047c9ec bytes 00280c91
+ 0047c9ec bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3fd20402fd5145516d24ba3c7cca786d"></a>

### [`0047c9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c9f4.md) → [`0047c9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c9f4.md) FUN_0047c9f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0047ca00",
      "incomplete_value": false,
      "site": "0047ca04",
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
    "old": {
      "definition_site": "0047ca00",
      "incomplete_value": false,
      "site": "0047ca04",
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
      "0047ca00",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047ca00",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ca00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c9f4.md#insn-0047ca00)
- 新版 `0047ca00`（命令位置の公開資料なし）

~~~diff
- 0047ca00 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047ca00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047ca00 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047ca00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047ca00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047ca00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047ca00 bytes 00280c91
+ 0047ca00 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cf096c95ca9ca01afc87a7193d41920"></a>

### [`0047ca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047ca08.md) → [`0047ca08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047ca08.md) FUN_0047ca08

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004794a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00479/00479c04.md) [`0047ab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047b/0047ba2c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 4件 [`004794a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/004794a0.md) [`00479c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00479/00479c04.md) [`0047ab48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047a/0047ab48.md) [`0047ba2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047b/0047ba2c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0047ca14",
      "incomplete_value": false,
      "site": "0047ca18",
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
    "old": {
      "definition_site": "0047ca14",
      "incomplete_value": false,
      "site": "0047ca18",
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
      "0047ca14",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047ca14",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ca14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047ca08.md#insn-0047ca14)
- 新版 `0047ca14`（命令位置の公開資料なし）

~~~diff
- 0047ca14 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047ca14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047ca14 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047ca14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047ca14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047ca14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047ca14 bytes 00280c91
+ 0047ca14 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f399f0606bc321800f859038028b5936"></a>

### [`0047cba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cba4.md) → [`0047cba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cba4.md) FUN_0047cba4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md) · 呼出先 2件 [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`004787b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004787b4.md) · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
      "definition_site": "0047cc00",
      "incomplete_value": false,
      "site": "0047cc08",
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
            "const:1f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cc00",
      "incomplete_value": false,
      "site": "0047cc08",
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
            "const:164:8"
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
      "definition_site": "0047cc10",
      "incomplete_value": true,
      "site": "0047cc14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cc10",
      "incomplete_value": true,
      "site": "0047cc14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047cc08",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "0047cc10",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047cc10",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047cc08",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "0047cc10",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047cc10",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cba4.md#insn-0047cc00) · [`0047cc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cba4.md#insn-0047cc10)
- 新版 `0047cc00`（命令位置の公開資料なし） · `0047cc10`（命令位置の公開資料なし）

~~~diff
- 0047cc00 ["COPY", "tmp:0:8", ["const:164:8"]]
- 0047cc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047cc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047cc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047cc00 ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 0047cc00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cc00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cc00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047cc00 bytes 08910591
+ 0047cc00 bytes 08c50791
- 0047cc10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047cc10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047cc10 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047cc10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047cc10 bytes 210c47f9
+ 0047cc10 bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c4b3556cb3214accb718fa809c38d87"></a>

### [`0047cc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cc18.md) → [`0047cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cc18.md) FUN_0047cc18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`0047d078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004785c8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.41% / 新版 92.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047cd04",
      "incomplete_value": false,
      "site": "0047cd0c",
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
            "const:424:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cd04",
      "incomplete_value": false,
      "site": "0047cd0c",
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
            "const:42b:8"
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
      "definition_site": "0047cd28",
      "incomplete_value": false,
      "site": "0047cd2c",
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
            "const:2fd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cd28",
      "incomplete_value": false,
      "site": "0047cd2c",
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
            "const:391:8"
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
      "definition_site": "0047cd14",
      "incomplete_value": true,
      "site": "0047cd18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cd14",
      "incomplete_value": true,
      "site": "0047cd18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047cd0c",
      "DATA",
      [
        "storage",
        "002a742b",
        null,
        "string"
      ]
    ],
    [
      "0047cd14",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047cd14",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047cd0c",
      "DATA",
      [
        "storage",
        "002a7424",
        null,
        "string"
      ]
    ],
    [
      "0047cd14",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047cd14",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cc18.md#insn-0047cd04) · [`0047cd14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cc18.md#insn-0047cd14) · [`0047cd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cc18.md#insn-0047cd28)
- 新版 `0047cd04`（命令位置の公開資料なし） · `0047cd14`（命令位置の公開資料なし） · `0047cd28`（命令位置の公開資料なし）

~~~diff
- 0047cd04 ["COPY", "tmp:0:8", ["const:42b:8"]]
- 0047cd04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047cd04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047cd04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047cd04 ["COPY", "tmp:0:8", ["const:424:8"]]
+ 0047cd04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cd04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cd04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047cd04 bytes 08ad1091
+ 0047cd04 bytes 08911091
- 0047cd14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047cd14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047cd14 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047cd14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047cd14 bytes 210c47f9
+ 0047cd14 bytes 216447f9
- 0047cd28 ["COPY", "tmp:0:8", ["const:391:8"]]
- 0047cd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047cd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047cd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047cd28 ["COPY", "tmp:0:8", ["const:2fd:8"]]
+ 0047cd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047cd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047cd28 bytes 08450e91
+ 0047cd28 bytes 08f50b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-253febb96d8882fa6e4ba5736c8b9d15"></a>

### [`0047cd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cd90.md) → [`0047cd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cd90.md) FUN_0047cd90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`0047d078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d078.md) · 呼出先 5件 [`004784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004785c8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047ce9c",
      "incomplete_value": false,
      "site": "0047cea0",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ce9c",
      "incomplete_value": false,
      "site": "0047cea0",
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
            "const:19f:8"
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
      "definition_site": "0047cebc",
      "incomplete_value": true,
      "site": "0047cec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cebc",
      "incomplete_value": true,
      "site": "0047cec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047cea0",
      "DATA",
      [
        "storage",
        "002a319f",
        null,
        "string"
      ]
    ],
    [
      "0047cebc",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047cebc",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047cea0",
      "DATA",
      [
        "storage",
        "002a3198",
        null,
        "string"
      ]
    ],
    [
      "0047cebc",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047cebc",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ce9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cd90.md#insn-0047ce9c) · [`0047cebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cd90.md#insn-0047cebc)
- 新版 `0047ce9c`（命令位置の公開資料なし） · `0047cebc`（命令位置の公開資料なし）

~~~diff
- 0047ce9c ["COPY", "tmp:0:8", ["const:19f:8"]]
- 0047ce9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047ce9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047ce9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047ce9c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0047ce9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047ce9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047ce9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047ce9c bytes 087d0691
+ 0047ce9c bytes 08610691
- 0047cebc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047cebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047cebc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047cebc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047cebc bytes 210c47f9
+ 0047cebc bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afdc532cb8775c0f7d0b06bc454e77a3"></a>

### [`0047cef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cef8.md) → [`0047cef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047cef8.md) FUN_0047cef8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d078`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d078.md) · 呼出先 6件 [`004784f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004785c8.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`0047d078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d078.md) · 呼出先 6件 [`004784f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004784f0.md) [`004785c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004785c8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.05% / 新版 94.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0047d01c",
      "incomplete_value": false,
      "site": "0047d020",
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
            "const:6b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d01c",
      "incomplete_value": false,
      "site": "0047d020",
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
            "const:74c:8"
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
      "definition_site": "0047cf64",
      "incomplete_value": true,
      "site": "0047cf6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:858:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047cf64",
      "incomplete_value": true,
      "site": "0047cf6c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7a8:8"
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
      "definition_site": "0047d03c",
      "incomplete_value": true,
      "site": "0047d040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d03c",
      "incomplete_value": true,
      "site": "0047d040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047cf64",
      "READ",
      [
        "storage",
        "00c237a8",
        null,
        "pointer"
      ]
    ],
    [
      "0047cf64",
      "PARAM",
      [
        "storage",
        "002ab4ab",
        null,
        "string"
      ]
    ],
    [
      "0047cf74",
      "READ",
      [
        "storage",
        "00c237a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0047cf64",
      "READ",
      [
        "storage",
        "00c23858",
        null,
        "pointer"
      ]
    ],
    [
      "0047cf64",
      "PARAM",
      [
        "storage",
        "002ab4b1",
        null,
        "string"
      ]
    ],
    [
      "0047cf74",
      "READ",
      [
        "storage",
        "00c23858",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047cf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cef8.md#insn-0047cf64) · [`0047cf74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cef8.md#insn-0047cf74) · [`0047d01c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047cef8.md#insn-0047d01c)
- 新版 `0047cf64`（命令位置の公開資料なし） · `0047cf74`（命令位置の公開資料なし） · `0047d01c`（命令位置の公開資料なし）

~~~diff
- 0047cf64 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:7a8:8"]]
- 0047cf64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047cf64 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:858:8"]]
+ 0047cf64 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0047cf64 bytes 00d743f9
+ 0047cf64 bytes 002f44f9
- 0047cf74 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:7a8:8"]]
- 0047cf74 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 0047cf74 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 0047cf74 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:858:8"]]
+ 0047cf74 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 0047cf74 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 0047cf74 bytes 08ab47b9
+ 0047cf74 bytes 085b48b9
- 0047d01c ["COPY", "tmp:0:8", ["const:74c:8"]]
- 0047d01c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d01c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d01c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d01c ["COPY", "tmp:0:8", ["const:6b8:8"]]
+ 0047d01c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d01c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d01c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d01c bytes 08311d91
+ 0047d01c bytes 08e11a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dbdcebfef12155d8a9384155eeec487"></a>

### [`0047d3a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d3a0.md) → [`0047d3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d3a0.md) FUN_0047d3a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`004787b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004787b4.md) · 呼出先 2件 [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 1件 [`004787b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004787b4.md) · 呼出先 2件 [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

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
      "definition_site": "0047d45c",
      "incomplete_value": false,
      "site": "0047d464",
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
            "const:1f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d45c",
      "incomplete_value": false,
      "site": "0047d464",
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
            "const:164:8"
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
      "definition_site": "0047d46c",
      "incomplete_value": true,
      "site": "0047d470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d46c",
      "incomplete_value": true,
      "site": "0047d470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047d464",
      "DATA",
      [
        "storage",
        "002a2164",
        null,
        "string"
      ]
    ],
    [
      "0047d46c",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0047d46c",
      "PARAM",
      [
        "storage",
        "00c16d98",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047d464",
      "DATA",
      [
        "storage",
        "002a21f1",
        null,
        "string"
      ]
    ],
    [
      "0047d46c",
      "READ",
      [
        "storage",
        "00c1aec8",
        null,
        "pointer"
      ]
    ],
    [
      "0047d46c",
      "PARAM",
      [
        "storage",
        "00c16e48",
        "_ZTIPKc",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d3a0.md#insn-0047d45c) · [`0047d46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d3a0.md#insn-0047d46c)
- 新版 `0047d45c`（命令位置の公開資料なし） · `0047d46c`（命令位置の公開資料なし）

~~~diff
- 0047d45c ["COPY", "tmp:0:8", ["const:164:8"]]
- 0047d45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d45c ["COPY", "tmp:0:8", ["const:1f1:8"]]
+ 0047d45c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d45c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d45c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d45c bytes 08910591
+ 0047d45c bytes 08c50791
- 0047d46c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0047d46c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047d46c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ec8:8"]]
+ 0047d46c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047d46c bytes 210c47f9
+ 0047d46c bytes 216447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec1182ddbff4b45e58e8bac9df1b6bbe"></a>

### [`0047d610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d610.md) → [`0047d610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d610.md) FUN_0047d610

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0047d490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d490.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0047d490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d490.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0047d61c",
      "incomplete_value": false,
      "site": "0047d620",
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
    "old": {
      "definition_site": "0047d61c",
      "incomplete_value": false,
      "site": "0047d620",
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
      "0047d61c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047d61c",
      "PARAM",
      [
        "storage",
        "002a7303",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d610.md#insn-0047d61c)
- 新版 `0047d61c`（命令位置の公開資料なし）

~~~diff
- 0047d61c ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0047d61c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0047d61c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0047d61c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0047d61c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0047d61c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d61c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0047d61c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0047d61c bytes 00280c91
+ 0047d61c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c18ea617100248071b9e97c2c6598a82"></a>

### [`0047d690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d690.md) → [`0047d690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d690.md) _ZNK5Botan7AES_1289encrypt_nEPKhPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047d750",
      "incomplete_value": true,
      "site": "0047d75c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047d750",
      "incomplete_value": true,
      "site": "0047d75c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
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
      "0047d750",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0047d750",
      "PARAM",
      [
        "storage",
        "00beca98",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047d750",
      "READ",
      [
        "storage",
        "00c1aed0",
        null,
        "pointer"
      ]
    ],
    [
      "0047d750",
      "PARAM",
      [
        "storage",
        "00becb48",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d690.md#insn-0047d750)
- 新版 `0047d750`（命令位置の公開資料なし）

~~~diff
- 0047d750 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e20:8"]]
- 0047d750 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047d750 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed0:8"]]
+ 0047d750 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047d750 bytes 211047f9
+ 0047d750 bytes 216847f9
~~~


<a id="compare-f534b9a11f8f93bb6b5e2352b0fb4a27"></a>

### [`0047d7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md) → [`0047d7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d7b0.md) FUN_0047d7b0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0047d690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d690.md) [`0047ec98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047ec98.md) [`0047efb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047efb4.md) · 呼出先 4件 [`00512a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512a64.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md)
- 新版 呼出元 3件 [`0047d690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d690.md) [`0047ec98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047ec98.md) [`0047efb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047efb4.md) · 呼出先 4件 [`00512a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512a64.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.28% / 新版 97.28%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0047d7f0",
      "incomplete_value": true,
      "site": "0047d7f0",
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
      "definition_site": "0047d7f0",
      "incomplete_value": true,
      "site": "0047d7f0",
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
      "definition_site": "0047dcfc",
      "incomplete_value": false,
      "site": "0047dd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:4f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047dcfc",
      "incomplete_value": false,
      "site": "0047dd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29b000:8"
          ],
          [
            "leaf",
            "const:467:8"
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
      "definition_site": "0047dd04",
      "incomplete_value": false,
      "site": "0047dd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:bde:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047dd04",
      "incomplete_value": false,
      "site": "0047dd1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b51:8"
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
      "0047d7e8",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "0047d7ec",
      "READ",
      [
        "storage",
        "00c25278",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0047d7f8",
      "WRITE",
      [
        "storage",
        "00c25278",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0047d7e8",
      "READ",
      [
        "storage",
        "00c1aed8",
        null,
        "pointer"
      ]
    ],
    [
      "0047d7ec",
      "READ",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0047d7f8",
      "WRITE",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047d7e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md#insn-0047d7e8) · [`0047d800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md#insn-0047d800) · [`0047d80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md#insn-0047d80c)
- 新版 `0047d7e8`（命令位置の公開資料なし） · `0047d800`（命令位置の公開資料なし） · `0047d80c`（命令位置の公開資料なし）

~~~diff
- 0047d7e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
- 0047d7e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047d7e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed8:8"]]
+ 0047d7e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047d7e8 bytes 081547f9
+ 0047d7e8 bytes 086d47f9
- 0047d800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 0047d800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047d800 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 0047d800 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047d800 bytes 081947f9
+ 0047d800 bytes 087147f9
- 0047d80c ["COPY", "tmp:0:8", ["const:800:8"]]
- 0047d80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047d80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047d80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047d80c ["COPY", "tmp:0:8", ["const:8c0:8"]]
+ 0047d80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047d80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047d80c bytes 08012091
+ 0047d80c bytes 08012391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62f47fa5f14a0bb413ec5346fc73cac3"></a>

### [`0047dd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047dd70.md) → [`0047dd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047dd70.md) _ZNK5Botan7AES_1289decrypt_nEPKhPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047de90.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047de90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047de90.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047de30",
      "incomplete_value": true,
      "site": "0047de3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047de30",
      "incomplete_value": true,
      "site": "0047de3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
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
      "0047de30",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0047de30",
      "PARAM",
      [
        "storage",
        "00beca98",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047de30",
      "READ",
      [
        "storage",
        "00c1aed0",
        null,
        "pointer"
      ]
    ],
    [
      "0047de30",
      "PARAM",
      [
        "storage",
        "00becb48",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047de30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047dd70.md#insn-0047de30)
- 新版 `0047de30`（命令位置の公開資料なし）

~~~diff
- 0047de30 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e20:8"]]
- 0047de30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047de30 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed0:8"]]
+ 0047de30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047de30 bytes 211047f9
+ 0047de30 bytes 216847f9
~~~


<a id="compare-a8ea3dc6ceeb610bc2ff03900cfbfbf7"></a>

### [`0047de90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047de90.md) → [`0047de90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047de90.md) FUN_0047de90

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0047dd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047dd70.md) [`0047edb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047edb8.md) [`0047f0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047f/0047f0d4.md) · 呼出先 4件 [`00512b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512b5c.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb700.md)
- 新版 呼出元 3件 [`0047dd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047dd70.md) [`0047edb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047edb8.md) [`0047f0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f0d4.md) · 呼出先 4件 [`00512b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512b5c.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0047ded0",
      "incomplete_value": true,
      "site": "0047ded0",
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
      "definition_site": "0047ded0",
      "incomplete_value": true,
      "site": "0047ded0",
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
      "definition_site": "0047e3e8",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:a06:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e3e8",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:293000:8"
          ],
          [
            "leaf",
            "const:979:8"
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
      "definition_site": "0047e3f0",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:bde:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047e3f0",
      "incomplete_value": false,
      "site": "0047e408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:291000:8"
          ],
          [
            "leaf",
            "const:b51:8"
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
      "0047dec8",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "0047decc",
      "READ",
      [
        "storage",
        "00c25278",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0047ded8",
      "WRITE",
      [
        "storage",
        "00c25278",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0047dec8",
      "READ",
      [
        "storage",
        "00c1aed8",
        null,
        "pointer"
      ]
    ],
    [
      "0047decc",
      "READ",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ],
    [
      "0047ded8",
      "WRITE",
      [
        "storage",
        "00c25338",
        "_ZN5Botan5CPUID20g_processor_featuresE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047dec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047de90.md#insn-0047dec8) · [`0047dee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047de90.md#insn-0047dee0) · [`0047deec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047de90.md#insn-0047deec)
- 新版 `0047dec8`（命令位置の公開資料なし） · `0047dee0`（命令位置の公開資料なし） · `0047deec`（命令位置の公開資料なし）

~~~diff
- 0047dec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
- 0047dec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047dec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed8:8"]]
+ 0047dec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047dec8 bytes 081547f9
+ 0047dec8 bytes 086d47f9
- 0047dee0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e30:8"]]
- 0047dee0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047dee0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ee0:8"]]
+ 0047dee0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047dee0 bytes 081947f9
+ 0047dee0 bytes 087147f9
- 0047deec ["COPY", "tmp:0:8", ["const:c40:8"]]
- 0047deec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0047deec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0047deec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0047deec ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0047deec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0047deec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0047deec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0047deec bytes 08013191
+ 0047deec bytes 08013491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eac30597d8b48d8a82faffeb0d381875"></a>

### [`0047e47c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047e47c.md) → [`0047e47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047e47c.md) FUN_0047e47c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0047e45c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047e45c.md) [`0047eed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047eed8.md) [`0047f1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047f/0047f1f4.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00495/00495978.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00512b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512b5c.md) [`0051d614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0051d/0051d614.md)
- 新版 呼出元 3件 [`0047e45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047e45c.md) [`0047eed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047eed8.md) [`0047f1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f1f4.md) · 呼出先 15件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512b5c.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0047ea9c",
      "incomplete_value": true,
      "site": "0047ea9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ea9c",
      "incomplete_value": true,
      "site": "0047ea9c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0047eac8",
      "incomplete_value": true,
      "site": "0047eac8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:728:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047eac8",
      "incomplete_value": true,
      "site": "0047eac8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:678:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047eb54",
      "incomplete_value": true,
      "site": "0047eb60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047eb54",
      "incomplete_value": true,
      "site": "0047eb60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0047e7e0",
      "READ",
      [
        "storage",
        "00c25c40",
        null,
        "undefined1"
      ]
    ],
    [
      "0047e7f4",
      "DATA",
      [
        "storage",
        "00c25840",
        null,
        "undefined4"
      ]
    ],
    [
      "0047e7f8",
      "READ",
      [
        "storage",
        "00c25c40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0047e7e0",
      "READ",
      [
        "storage",
        "00c25d00",
        null,
        "undefined1"
      ]
    ],
    [
      "0047e7f4",
      "DATA",
      [
        "storage",
        "00c25900",
        null,
        "undefined4"
      ]
    ],
    [
      "0047e7f8",
      "READ",
      [
        "storage",
        "00c25d00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047e788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047e47c.md#insn-0047e788) · [`0047e7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047e47c.md#insn-0047e7a0) · [`0047ea8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047e47c.md#insn-0047ea8c)
- 新版 `0047e788`（命令位置の公開資料なし） · `0047e7a0`（命令位置の公開資料なし） · `0047ea8c`（命令位置の公開資料なし）

~~~diff
- 0047e788 ["COPY", "tmp:0:8", ["const:c40:8"]]
- 0047e788 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0047e788 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0047e788 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0047e788 ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 0047e788 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0047e788 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0047e788 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0047e788 bytes 18033191
+ 0047e788 bytes 18033491
- 0047e7a0 ["COPY", "tmp:0:8", ["const:840:8"]]
- 0047e7a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0047e7a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0047e7a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0047e7a0 ["COPY", "tmp:0:8", ["const:900:8"]]
+ 0047e7a0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0047e7a0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0047e7a0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0047e7a0 bytes 73022191
+ 0047e7a0 bytes 73022491
- 0047ea8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:678:8"]]
- 0047ea8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047ea8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:728:8"]]
+ 0047ea8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0047ea8c bytes 893e43f9
+ 0047ea8c bytes 899643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e74cc2f8f4b4c646b66191fdb0b723ba"></a>

### [`0047ec98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047ec98.md) → [`0047ec98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047ec98.md) _ZNK5Botan7AES_1929encrypt_nEPKhPhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00512/00512990.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0047d7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047d/0047d7b0.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0047ed58",
      "incomplete_value": true,
      "site": "0047ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047ed58",
      "incomplete_value": true,
      "site": "0047ed64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e20:8"
              ]
            ]
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
      "0047ed58",
      "READ",
      [
        "storage",
        "00c1ae20",
        null,
        "pointer"
      ]
    ],
    [
      "0047ed58",
      "PARAM",
      [
        "storage",
        "00beca98",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0047ed58",
      "READ",
      [
        "storage",
        "00c1aed0",
        null,
        "pointer"
      ]
    ],
    [
      "0047ed58",
      "PARAM",
      [
        "storage",
        "00becb48",
        "_ZTIN5Botan11Key_Not_SetE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047ed58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047e/0047ec98.md#insn-0047ed58)
- 新版 `0047ed58`（命令位置の公開資料なし）

~~~diff
- 0047ed58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e20:8"]]
- 0047ed58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047ed58 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed0:8"]]
+ 0047ed58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0047ed58 bytes 211047f9
+ 0047ed58 bytes 216847f9
~~~


