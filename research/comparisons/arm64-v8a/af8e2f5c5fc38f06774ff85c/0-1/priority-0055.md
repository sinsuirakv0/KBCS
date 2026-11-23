# v15.7.2 → v15.7.3 · 最優先の変更候補 (55)

[一覧の目次](README.md)

<a id="compare-42768b993f1c8b345c92d689411a822e"></a>

### [`00a8c290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c290.md) → [`00a8c290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c290.md) FUN_00a8c290

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac8f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ac8/00ac8f8c.md) · 呼出先 11件 [`00464a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/00465780.md) [`00ab1128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1128.md)
- 新版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 11件 [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`00ab11f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab11f0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 83.81% / 新版 83.81%

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
      "definition_site": "00a8c2c4",
      "incomplete_value": false,
      "site": "00a8c2c8",
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
    "old": {
      "definition_site": "00a8c2c4",
      "incomplete_value": false,
      "site": "00a8c2c8",
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
            "const:c78:8"
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
      "definition_site": "00a8c2e0",
      "incomplete_value": true,
      "site": "00a8c2f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:37c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8c2e0",
      "incomplete_value": true,
      "site": "00a8c2f0",
      "value": [
        "LOAD",
        "16",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:297000:8"
              ],
              [
                "leaf",
                "const:2ef:8"
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
      "definition_site": "00a8c2f4",
      "incomplete_value": true,
      "site": "00a8c2f4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a8c2f4",
      "incomplete_value": true,
      "site": "00a8c2f4",
      "value": [
        "LOAD",
        "8",
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
      "00a8c2c8",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8c2e0",
      "READ",
      [
        "storage",
        "002972ef",
        null,
        "string"
      ]
    ],
    [
      "00a8c2e4",
      "READ",
      [
        "storage",
        "002972fe",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a8c2c8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8c2e0",
      "READ",
      [
        "storage",
        "0029737c",
        null,
        "string"
      ]
    ],
    [
      "00a8c2e4",
      "READ",
      [
        "storage",
        "0029738b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8c2c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c290.md#insn-00a8c2c4) · [`00a8c2d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c290.md#insn-00a8c2d8) · [`00a8c2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c290.md#insn-00a8c2dc)
- 新版 `00a8c2c4`（命令位置の公開資料なし） · `00a8c2d8`（命令位置の公開資料なし）

~~~diff
- 00a8c2c4 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00a8c2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8c2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8c2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2c4 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00a8c2c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8c2c4 bytes 08e13191
+ 00a8c2c4 bytes 08a13491
- 00a8c2d8 ["COPY", "tmp:0:8", ["const:2ef:8"]]
- 00a8c2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8c2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8c2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2d8 ["COPY", "tmp:0:8", ["const:37c:8"]]
+ 00a8c2d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8c2d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8c2d8 bytes 08bd0b91
+ 00a8c2d8 bytes 08f10d91
- 00a8c2dc ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00a8c2dc bytes 29c1ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d734a053b6a57094b48b2dd2e8b276e2"></a>

### [`00a8c478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c478.md) → [`00a8c478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c478.md) FUN_00a8c478

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00a90870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90e28.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063f/0063fa4c.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 2件 [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) [`00a90e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e28.md) · 呼出先 12件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0063fa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.74% / 新版 91.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a8c77c",
      "incomplete_value": false,
      "site": "00a8c77c",
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
    "old": {
      "definition_site": "00a8c77c",
      "incomplete_value": false,
      "site": "00a8c77c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
      "definition_site": "00a8c780",
      "incomplete_value": false,
      "site": "00a8c780",
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
    "old": {
      "definition_site": "00a8c780",
      "incomplete_value": false,
      "site": "00a8c780",
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
            "const:f40:8"
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
      "definition_site": "00a8c77c",
      "incomplete_value": false,
      "site": "00a8c780",
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
    "old": {
      "definition_site": "00a8c77c",
      "incomplete_value": false,
      "site": "00a8c780",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
      "00a8c4b0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c4bc",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8c4c4",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8c4b0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c4bc",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8c4c4",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8c4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c478.md#insn-00a8c4b0) · [`00a8c4bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c478.md#insn-00a8c4bc) · [`00a8c4c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c478.md#insn-00a8c4c4)
- 新版 `00a8c4b0`（命令位置の公開資料なし） · `00a8c4bc`（命令位置の公開資料なし） · `00a8c4c4`（命令位置の公開資料なし）

~~~diff
- 00a8c4b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8c4b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8c4b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8c4b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8c4b0 bytes 08dd44f9
+ 00a8c4b0 bytes 083d45f9
- 00a8c4bc ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8c4bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8c4bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8c4bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8c4bc ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8c4bc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8c4bc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8c4bc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8c4bc bytes 21603691
+ 00a8c4bc bytes 21203991
- 00a8c4c4 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8c4c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8c4c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8c4c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8c4c4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8c4c4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8c4c4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8c4c4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8c4c4 bytes 42c03891
+ 00a8c4c4 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea6abdce2262a3e7f6c2030110125155"></a>

### [`00a8c854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c854.md) → [`00a8c854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8c854.md) FUN_00a8c854

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006d6/006d6d04.md) [`006dd65c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006dd/006dd65c.md) [`008bb9b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/008bb/008bb9b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`0063eaf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0063e/0063eaf8.md) [`00aa3f20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa3/00aa3f20.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 3件 [`006d6d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006d6/006d6d04.md) [`006dd65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006dd/006dd65c.md) [`008bb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008bb/008bb9b0.md) · 呼出先 10件 [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0063eaf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063eaf8.md) [`00aa3f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa3/00aa3f20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.15% / 新版 96.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8ca60",
      "incomplete_value": false,
      "site": "00a8ca70",
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
    "old": {
      "definition_site": "00a8ca60",
      "incomplete_value": false,
      "site": "00a8ca70",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8c98c",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00a8c99c",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c9a0",
      "PARAM",
      [
        "storage",
        "00c25018",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00a8c98c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00a8c99c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8c9a0",
      "PARAM",
      [
        "storage",
        "00c250d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8c8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c854.md#insn-00a8c8d0) · [`00a8c8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8c854.md#insn-00a8c8d8)
- 新版 `00a8c8d0`（命令位置の公開資料なし） · `00a8c8d8`（命令位置の公開資料なし）

~~~diff
- 00a8c8d0 ["COPY", "tmp:0:8", ["const:18:8"]]
- 00a8c8d0 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00a8c8d0 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00a8c8d0 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00a8c8d0 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00a8c8d0 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a8c8d0 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a8c8d0 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00a8c8d0 bytes 18630091
+ 00a8c8d0 bytes 18630391
- 00a8c8d8 ["COPY", "register:40a0:8", ["const:c24000:8"]]
- 00a8c8d8 bytes d40c0090
+ 00a8c8d8 ["COPY", "register:40a0:8", ["const:c25000:8"]]
+ 00a8c8d8 bytes d40c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62de3ce54212583478fd13ebbb6dde38"></a>

### [`00a8cac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cac4.md) → [`00a8cac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cac4.md) FUN_00a8cac4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a8cd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cd44.md) · 呼出先 7件 [`006582c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068b/0068be5c.md) [`00691300`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00691/00691300.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`00a8cd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cd44.md) · 呼出先 7件 [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`0068be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068b/0068be5c.md) [`00691300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691300.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.25% / 新版 96.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8cad8",
      "incomplete_value": false,
      "site": "00a8cae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8cad8",
      "incomplete_value": false,
      "site": "00a8cae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e20:8"
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
      "definition_site": "00a8cc30",
      "incomplete_value": false,
      "site": "00a8cc34",
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
    "old": {
      "definition_site": "00a8cc30",
      "incomplete_value": false,
      "site": "00a8cc34",
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
            "const:d08:8"
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
      "definition_site": "00a8cc6c",
      "incomplete_value": false,
      "site": "00a8cc70",
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
    "old": {
      "definition_site": "00a8cc6c",
      "incomplete_value": false,
      "site": "00a8cc70",
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
            "const:1e8:8"
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
      "00a8cae0",
      "DATA",
      [
        "storage",
        "00c0de20",
        null,
        "pointer"
      ]
    ],
    [
      "00a8cc34",
      "DATA",
      [
        "storage",
        "00bfad08",
        null,
        "pointer"
      ]
    ],
    [
      "00a8cc70",
      "DATA",
      [
        "storage",
        "00bf71e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00a8cae0",
      "DATA",
      [
        "storage",
        "00c0ded0",
        null,
        "pointer"
      ]
    ],
    [
      "00a8cc34",
      "DATA",
      [
        "storage",
        "00bfadb8",
        null,
        "pointer"
      ]
    ],
    [
      "00a8cc70",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8cad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cac4.md#insn-00a8cad8) · [`00a8cc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cac4.md#insn-00a8cc30) · [`00a8cc6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cac4.md#insn-00a8cc6c)
- 新版 `00a8cad8`（命令位置の公開資料なし） · `00a8cc30`（命令位置の公開資料なし） · `00a8cc6c`（命令位置の公開資料なし）

~~~diff
- 00a8cad8 ["COPY", "tmp:0:8", ["const:e20:8"]]
- 00a8cad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8cad8 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00a8cad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8cad8 bytes 08813891
+ 00a8cad8 bytes 08413b91
- 00a8cc30 ["COPY", "tmp:0:8", ["const:d08:8"]]
- 00a8cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc30 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00a8cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8cc30 bytes 08213491
+ 00a8cc30 bytes 08e13691
- 00a8cc6c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 00a8cc6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cc6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cc6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc6c ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00a8cc6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cc6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8cc6c bytes 08a10791
+ 00a8cc6c bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e79104100a750a27365d453b6974f83"></a>

### [`00a8cd6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cd6c.md) → [`00a8cd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cd6c.md) FUN_00a8cd6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8cd90",
      "incomplete_value": false,
      "site": "00a8cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8cd90",
      "incomplete_value": false,
      "site": "00a8cd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00a8cd90",
      "DATA",
      [
        "storage",
        "00c0de58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8cd90",
      "DATA",
      [
        "storage",
        "00c0df08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8cd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cd6c.md#insn-00a8cd8c)
- 新版 `00a8cd8c`（命令位置の公開資料なし）

~~~diff
- 00a8cd8c ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a8cd8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cd8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8cd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8cd8c ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00a8cd8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cd8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8cd8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8cd8c bytes 08613991
+ 00a8cd8c bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af3f22d0ce0612f1c435a3e7ccf1ed53"></a>

### [`00a8cda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cda0.md) → [`00a8cda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8c/00a8cda0.md) FUN_00a8cda0

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
      "definition_site": "00a8cdac",
      "incomplete_value": false,
      "site": "00a8cdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8cdac",
      "incomplete_value": false,
      "site": "00a8cdac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00a8cdac",
      "DATA",
      [
        "storage",
        "00c0de58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8cdac",
      "DATA",
      [
        "storage",
        "00c0df08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8cda8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8c/00a8cda0.md#insn-00a8cda8)
- 新版 `00a8cda8`（命令位置の公開資料なし）

~~~diff
- 00a8cda8 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a8cda8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8cda8 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00a8cda8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8cda8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8cda8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8cda8 bytes 29613991
+ 00a8cda8 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f49ec94300d436ad4d75096ab88a615a"></a>

### [`00a8d128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d128.md) → [`00a8d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d128.md) FUN_00a8d128

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8d14c",
      "incomplete_value": false,
      "site": "00a8d14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8d14c",
      "incomplete_value": false,
      "site": "00a8d14c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00a8d14c",
      "DATA",
      [
        "storage",
        "00c0ded8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8d14c",
      "DATA",
      [
        "storage",
        "00c0df88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8d148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d128.md#insn-00a8d148)
- 新版 `00a8d148`（命令位置の公開資料なし）

~~~diff
- 00a8d148 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00a8d148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8d148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8d148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8d148 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a8d148 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8d148 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8d148 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8d148 bytes 08613b91
+ 00a8d148 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5877a1f8a7ba972a41e99ff5f9a3d3e9"></a>

### [`00a8d15c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d15c.md) → [`00a8d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d15c.md) FUN_00a8d15c

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
      "definition_site": "00a8d168",
      "incomplete_value": false,
      "site": "00a8d168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8d168",
      "incomplete_value": false,
      "site": "00a8d168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00a8d168",
      "DATA",
      [
        "storage",
        "00c0ded8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8d168",
      "DATA",
      [
        "storage",
        "00c0df88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8d164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d15c.md#insn-00a8d164)
- 新版 `00a8d164`（命令位置の公開資料なし）

~~~diff
- 00a8d164 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00a8d164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8d164 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a8d164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8d164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8d164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8d164 bytes 29613b91
+ 00a8d164 bytes 29213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33e1f4acd5ee64fbdc2b54b526a47ebe"></a>

### [`00a8d178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md) → [`00a8d178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8d178.md) FUN_00a8d178

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 26件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 26件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value

命令の説明率　旧版 96.42% / 新版 96.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 7件, `store_condition` 2件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a8d99c",
      "incomplete_value": false,
      "site": "00a8d99c",
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
    "old": {
      "definition_site": "00a8d99c",
      "incomplete_value": false,
      "site": "00a8d99c",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 49,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00a8d9a0",
      "incomplete_value": false,
      "site": "00a8d9a0",
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
    "old": {
      "definition_site": "00a8d9a0",
      "incomplete_value": false,
      "site": "00a8d9a0",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8d99c",
      "incomplete_value": false,
      "site": "00a8d9a0",
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
    "old": {
      "definition_site": "00a8d99c",
      "incomplete_value": false,
      "site": "00a8d9a0",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8d1e8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8d1f8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8d200",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8d1e8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8d1f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8d200",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8d1e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md#insn-00a8d1e8) · [`00a8d1f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md#insn-00a8d1f8) · [`00a8d200`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8d178.md#insn-00a8d200)
- 新版 `00a8d1e8`（命令位置の公開資料なし） · `00a8d1f8`（命令位置の公開資料なし） · `00a8d200`（命令位置の公開資料なし）

~~~diff
- 00a8d1e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8d1e8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8d1e8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8d1e8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8d1e8 bytes 00dd44f9
+ 00a8d1e8 bytes 003d45f9
- 00a8d1f8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8d1f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8d1f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8d1f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8d1f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8d1f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8d1f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8d1f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8d1f8 bytes 21603691
+ 00a8d1f8 bytes 21203991
- 00a8d200 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8d200 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8d200 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8d200 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8d200 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8d200 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8d200 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8d200 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8d200 bytes 42c03891
+ 00a8d200 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-618927de8d45063f2d0655b5340c8f57"></a>

### [`00a8dafc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dafc.md) → [`00a8dafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dafc.md) FUN_00a8dafc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8db20",
      "incomplete_value": false,
      "site": "00a8db20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8db20",
      "incomplete_value": false,
      "site": "00a8db20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
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
      "00a8db20",
      "DATA",
      [
        "storage",
        "00c0df58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8db20",
      "DATA",
      [
        "storage",
        "00c0e008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8db18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dafc.md#insn-00a8db18) · [`00a8db1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dafc.md#insn-00a8db1c)
- 新版 `00a8db18`（命令位置の公開資料なし） · `00a8db1c`（命令位置の公開資料なし）

~~~diff
- 00a8db18 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00a8db18 ["COPY", "register:4040:8", ["const:c0e000:8"]]
- 00a8db18 bytes 080c0090
+ 00a8db18 bytes 080c00b0
- 00a8db1c ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00a8db1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8db1c ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00a8db1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8db1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8db1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8db1c bytes 08613d91
+ 00a8db1c bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc924e604bea8103c43d9551e86e763a"></a>

### [`00a8db4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8db4c.md) → [`00a8db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8db4c.md) FUN_00a8db4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00666298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00666/00666298.md) [`006a8e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006a8/006a8e60.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.32% / 新版 98.32%

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
      "definition_site": "00a8dbfc",
      "incomplete_value": true,
      "site": "00a8dbfc",
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
      "definition_site": "00a8dbfc",
      "incomplete_value": true,
      "site": "00a8dbfc",
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a8dc04",
      "incomplete_value": false,
      "site": "00a8dc14",
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
    "old": {
      "definition_site": "00a8dc04",
      "incomplete_value": false,
      "site": "00a8dc14",
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
            "const:d98:8"
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
      "definition_site": "00a8dc0c",
      "incomplete_value": false,
      "site": "00a8dc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dc0c",
      "incomplete_value": false,
      "site": "00a8dc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a8dbf8",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8dc04",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8dc0c",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8dbf8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8dc04",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8dc0c",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8dbf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8db4c.md#insn-00a8dbf8) · [`00a8dc04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8db4c.md#insn-00a8dc04) · [`00a8dc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8db4c.md#insn-00a8dc0c)
- 新版 `00a8dbf8`（命令位置の公開資料なし） · `00a8dc04`（命令位置の公開資料なし） · `00a8dc0c`（命令位置の公開資料なし）

~~~diff
- 00a8dbf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8dbf8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8dbf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8dbf8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8dbf8 bytes 00dd44f9
+ 00a8dbf8 bytes 003d45f9
- 00a8dc04 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8dc04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8dc04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8dc04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8dc04 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8dc04 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8dc04 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8dc04 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8dc04 bytes 21603691
+ 00a8dc04 bytes 21203991
- 00a8dc0c ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8dc0c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8dc0c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8dc0c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8dc0c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8dc0c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8dc0c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8dc0c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8dc0c bytes 42c03891
+ 00a8dc0c bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f95257580f2cdd83afe1f26ab561ea82"></a>

### [`00a8dd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dd78.md) → [`00a8dd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8dd78.md) FUN_00a8dd78

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
      "definition_site": "00a8dd9c",
      "incomplete_value": false,
      "site": "00a8dda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dd9c",
      "incomplete_value": false,
      "site": "00a8dda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
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
      "00a8dda0",
      "DATA",
      [
        "storage",
        "00c0dfd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8dda0",
      "DATA",
      [
        "storage",
        "00c0e088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8dd98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dd78.md#insn-00a8dd98) · [`00a8dd9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8dd78.md#insn-00a8dd9c)
- 新版 `00a8dd98`（命令位置の公開資料なし） · `00a8dd9c`（命令位置の公開資料なし）

~~~diff
- 00a8dd98 ["COPY", "register:4040:8", ["const:c0d000:8"]]
+ 00a8dd98 ["COPY", "register:4040:8", ["const:c0e000:8"]]
- 00a8dd98 bytes 080c0090
+ 00a8dd98 bytes 080c00b0
- 00a8dd9c ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00a8dd9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8dd9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8dd9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8dd9c ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00a8dd9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8dd9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8dd9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8dd9c bytes 08613f91
+ 00a8dd9c bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-777335d4b15acc5eae5eb295ad69e8a5"></a>

### [`00a8deb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8deb8.md) → [`00a8deb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8d/00a8deb8.md) FUN_00a8deb8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8dedc",
      "incomplete_value": false,
      "site": "00a8dedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8dedc",
      "incomplete_value": false,
      "site": "00a8dedc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a8dedc",
      "DATA",
      [
        "storage",
        "00c0e058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8dedc",
      "DATA",
      [
        "storage",
        "00c0e108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8ded8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8d/00a8deb8.md#insn-00a8ded8)
- 新版 `00a8ded8`（命令位置の公開資料なし）

~~~diff
- 00a8ded8 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00a8ded8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8ded8 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00a8ded8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8ded8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8ded8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8ded8 bytes 08610191
+ 00a8ded8 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-680f339c278b31d70047a73750600b59"></a>

### [`00a8e068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e068.md) → [`00a8e068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e068.md) FUN_00a8e068

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8e08c",
      "incomplete_value": false,
      "site": "00a8e08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e08c",
      "incomplete_value": false,
      "site": "00a8e08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "00a8e08c",
      "DATA",
      [
        "storage",
        "00c0e0d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e08c",
      "DATA",
      [
        "storage",
        "00c0e188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e068.md#insn-00a8e088)
- 新版 `00a8e088`（命令位置の公開資料なし）

~~~diff
- 00a8e088 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00a8e088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8e088 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00a8e088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8e088 bytes 08610391
+ 00a8e088 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fca2dac7879a12301f9b18437e4a7ccf"></a>

### [`00a8e0b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e0b8.md) → [`00a8e0b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e0b8.md) FUN_00a8e0b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 0件  · 呼出先 19件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.01% / 新版 97.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8e19c",
      "incomplete_value": false,
      "site": "00a8e19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e19c",
      "incomplete_value": false,
      "site": "00a8e19c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "definition_site": "00a8e378",
      "incomplete_value": false,
      "site": "00a8e378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e378",
      "incomplete_value": false,
      "site": "00a8e378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:348:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a8e2e8",
      "incomplete_value": true,
      "site": "00a8e2e8",
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
      "definition_site": "00a8e2e8",
      "incomplete_value": true,
      "site": "00a8e2e8",
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
      "00a8e19c",
      "DATA",
      [
        "storage",
        "00c0e148",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8e1f0",
      "READ",
      [
        "storage",
        "00c0e168",
        null,
        "pointer"
      ]
    ],
    [
      "00a8e1f0",
      "READ",
      [
        "storage",
        "00c0e170",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e19c",
      "DATA",
      [
        "storage",
        "00c0e1f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8e1f0",
      "READ",
      [
        "storage",
        "00c0e218",
        null,
        "pointer"
      ]
    ],
    [
      "00a8e1f0",
      "READ",
      [
        "storage",
        "00c0e220",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e0b8.md#insn-00a8e190) · [`00a8e2e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e0b8.md#insn-00a8e2e4) · [`00a8e2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e0b8.md#insn-00a8e2f0)
- 新版 `00a8e190`（命令位置の公開資料なし） · `00a8e2e4`（命令位置の公開資料なし） · `00a8e2f0`（命令位置の公開資料なし）

~~~diff
- 00a8e190 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00a8e190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8e190 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00a8e190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8e190 bytes 08210591
+ 00a8e190 bytes 08e10791
- 00a8e2e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8e2e4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8e2e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8e2e4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8e2e4 bytes 00dd44f9
+ 00a8e2e4 bytes 003d45f9
- 00a8e2f0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8e2f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8e2f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8e2f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8e2f0 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8e2f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8e2f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8e2f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8e2f0 bytes 21603691
+ 00a8e2f0 bytes 21203991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4e1da46a822a882558ac6b229a0ed76"></a>

### [`00a8e4f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e4f8.md) → [`00a8e4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e4f8.md) FUN_00a8e4f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8e51c",
      "incomplete_value": false,
      "site": "00a8e51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e51c",
      "incomplete_value": false,
      "site": "00a8e51c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00a8e51c",
      "DATA",
      [
        "storage",
        "00c0e148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e51c",
      "DATA",
      [
        "storage",
        "00c0e1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e4f8.md#insn-00a8e518)
- 新版 `00a8e518`（命令位置の公開資料なし）

~~~diff
- 00a8e518 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00a8e518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8e518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8e518 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00a8e518 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e518 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8e518 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8e518 bytes 08210591
+ 00a8e518 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51e762a5669ae9c3f34d3526cc2eaaf2"></a>

### [`00a8e52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e52c.md) → [`00a8e52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e52c.md) FUN_00a8e52c

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
      "definition_site": "00a8e538",
      "incomplete_value": false,
      "site": "00a8e538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e538",
      "incomplete_value": false,
      "site": "00a8e538",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:148:8"
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
      "00a8e538",
      "DATA",
      [
        "storage",
        "00c0e148",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8e538",
      "DATA",
      [
        "storage",
        "00c0e1f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e52c.md#insn-00a8e534)
- 新版 `00a8e534`（命令位置の公開資料なし）

~~~diff
- 00a8e534 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00a8e534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8e534 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 00a8e534 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8e534 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8e534 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8e534 bytes 29210591
+ 00a8e534 bytes 29e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88dc38c50f51fde4dbc0682d2ac4e006"></a>

### [`00a8e548`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md) → [`00a8e548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8e548.md) FUN_00a8e548

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 36件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md)
- 新版 呼出元 0件  · 呼出先 36件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8e7a0",
      "incomplete_value": false,
      "site": "00a8e7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e7a0",
      "incomplete_value": false,
      "site": "00a8e7a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
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
      "definition_site": "00a8e938",
      "incomplete_value": false,
      "site": "00a8e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8e938",
      "incomplete_value": false,
      "site": "00a8e938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:238:8"
          ]
        ]
      ]
    },
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8ebf4",
      "incomplete_value": false,
      "site": "00a8ebf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8ebf4",
      "incomplete_value": false,
      "site": "00a8ebf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
          ]
        ]
      ]
    },
    "ordinal": 50,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a8e594",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8e5a0",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8e5a8",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8e594",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8e5a0",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8e5a8",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8e594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md#insn-00a8e594) · [`00a8e5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md#insn-00a8e5a0) · [`00a8e5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8e548.md#insn-00a8e5a8)
- 新版 `00a8e594`（命令位置の公開資料なし） · `00a8e5a0`（命令位置の公開資料なし） · `00a8e5a8`（命令位置の公開資料なし）

~~~diff
- 00a8e594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8e594 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8e594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8e594 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8e594 bytes 00dd44f9
+ 00a8e594 bytes 003d45f9
- 00a8e5a0 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8e5a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8e5a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8e5a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8e5a0 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8e5a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8e5a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8e5a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8e5a0 bytes 21603691
+ 00a8e5a0 bytes 21203991
- 00a8e5a8 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8e5a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8e5a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8e5a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8e5a8 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8e5a8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8e5a8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8e5a8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8e5a8 bytes 42c03891
+ 00a8e5a8 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c2f4026c0037886d2cd363b8ae26ce2"></a>

### [`00a8ef80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8ef80.md) → [`00a8ef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8ef80.md) FUN_00a8ef80

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8efa4",
      "incomplete_value": false,
      "site": "00a8efa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8efa4",
      "incomplete_value": false,
      "site": "00a8efa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a8efa4",
      "DATA",
      [
        "storage",
        "00c0e1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8efa4",
      "DATA",
      [
        "storage",
        "00c0e268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8efa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8ef80.md#insn-00a8efa0)
- 新版 `00a8efa0`（命令位置の公開資料なし）

~~~diff
- 00a8efa0 ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00a8efa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8efa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8efa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8efa0 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00a8efa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8efa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8efa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8efa0 bytes 08e10691
+ 00a8efa0 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-655344896cdaed6e4ac1c3ee549b0703"></a>

### [`00a8efb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8efb4.md) → [`00a8efb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efb4.md) FUN_00a8efb4

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
      "definition_site": "00a8efc0",
      "incomplete_value": false,
      "site": "00a8efc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8efc0",
      "incomplete_value": false,
      "site": "00a8efc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a8efc0",
      "DATA",
      [
        "storage",
        "00c0e1b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8efc0",
      "DATA",
      [
        "storage",
        "00c0e268",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8efbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8efb4.md#insn-00a8efbc)
- 新版 `00a8efbc`（命令位置の公開資料なし）

~~~diff
- 00a8efbc ["COPY", "tmp:0:8", ["const:1b8:8"]]
- 00a8efbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8efbc ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00a8efbc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8efbc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8efbc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8efbc bytes 29e10691
+ 00a8efbc bytes 29a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05244577d9da0299bbf9762c981e57e3"></a>

### [`00a8efd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8efd0.md) → [`00a8efd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8e/00a8efd0.md) FUN_00a8efd0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469e20.md) [`0046f248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046f248.md) [`00885f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00885/00885f80.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`0046f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046f248.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.42% / 新版 93.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8f078",
      "incomplete_value": true,
      "site": "00a8f078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f078",
      "incomplete_value": true,
      "site": "00a8f078",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fb7:8"
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
      "definition_site": "00a8f07c",
      "incomplete_value": true,
      "site": "00a8f07c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00a8f07c",
      "incomplete_value": true,
      "site": "00a8f07c",
      "value": [
        "LOAD",
        "8",
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
      "00a8f068",
      "READ",
      [
        "storage",
        "002a5fb7",
        null,
        "string"
      ]
    ],
    [
      "00a8f070",
      "READ",
      [
        "storage",
        "002a5fbc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a8f068",
      "READ",
      [
        "storage",
        "002a5fb0",
        null,
        "string"
      ]
    ],
    [
      "00a8f070",
      "READ",
      [
        "storage",
        "002a5fb5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8e/00a8efd0.md#insn-00a8f064)
- 新版 `00a8f064`（命令位置の公開資料なし）

~~~diff
- 00a8f064 ["COPY", "tmp:0:8", ["const:fb7:8"]]
- 00a8f064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f064 ["COPY", "tmp:0:8", ["const:fb0:8"]]
+ 00a8f064 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f064 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f064 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f064 bytes 29dd3e91
+ 00a8f064 bytes 29c13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deb05d58436c6fdae239e62467189910"></a>

### [`00a8f168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f168.md) → [`00a8f168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f168.md) FUN_00a8f168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8f18c",
      "incomplete_value": false,
      "site": "00a8f18c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f18c",
      "incomplete_value": false,
      "site": "00a8f18c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "00a8f18c",
      "DATA",
      [
        "storage",
        "00c0e238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f18c",
      "DATA",
      [
        "storage",
        "00c0e2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f168.md#insn-00a8f188)
- 新版 `00a8f188`（命令位置の公開資料なし）

~~~diff
- 00a8f188 ["COPY", "tmp:0:8", ["const:238:8"]]
- 00a8f188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f188 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00a8f188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f188 bytes 08e10891
+ 00a8f188 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e14108edc56d3eb916f7ea7ce9e719d4"></a>

### [`00a8f19c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f19c.md) → [`00a8f19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f19c.md) FUN_00a8f19c

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
      "definition_site": "00a8f1a8",
      "incomplete_value": false,
      "site": "00a8f1a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f1a8",
      "incomplete_value": false,
      "site": "00a8f1a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:238:8"
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
      "00a8f1a8",
      "DATA",
      [
        "storage",
        "00c0e238",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f1a8",
      "DATA",
      [
        "storage",
        "00c0e2e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f19c.md#insn-00a8f1a4)
- 新版 `00a8f1a4`（命令位置の公開資料なし）

~~~diff
- 00a8f1a4 ["COPY", "tmp:0:8", ["const:238:8"]]
- 00a8f1a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1a4 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00a8f1a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f1a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f1a4 bytes 29e10891
+ 00a8f1a4 bytes 29a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e31fa3c224b33ddea4faf59da78e1a4c"></a>

### [`00a8f260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f260.md) → [`00a8f260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f260.md) FUN_00a8f260

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8f274",
      "incomplete_value": false,
      "site": "00a8f278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f274",
      "incomplete_value": false,
      "site": "00a8f278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
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
      "00a8f278",
      "DATA",
      [
        "storage",
        "00c0e2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f278",
      "DATA",
      [
        "storage",
        "00c0e368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f260.md#insn-00a8f274)
- 新版 `00a8f274`（命令位置の公開資料なし）

~~~diff
- 00a8f274 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00a8f274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f274 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00a8f274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f274 bytes 08e10a91
+ 00a8f274 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32967dce3a0269f6566052befc9d0c27"></a>

### [`00a8f284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f284.md) → [`00a8f284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f284.md) FUN_00a8f284

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
      "definition_site": "00a8f288",
      "incomplete_value": false,
      "site": "00a8f28c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f288",
      "incomplete_value": false,
      "site": "00a8f28c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:2b8:8"
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
      "00a8f28c",
      "DATA",
      [
        "storage",
        "00c0e2b8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f28c",
      "DATA",
      [
        "storage",
        "00c0e368",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f284.md#insn-00a8f288)
- 新版 `00a8f288`（命令位置の公開資料なし）

~~~diff
- 00a8f288 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 00a8f288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f288 ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00a8f288 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f288 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f288 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f288 bytes 08e10a91
+ 00a8f288 bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bf5b1c301105830e314d0b6f4d54646"></a>

### [`00a8f308`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f308.md) → [`00a8f308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f308.md) FUN_00a8f308

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a8f32c",
      "incomplete_value": false,
      "site": "00a8f32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f32c",
      "incomplete_value": false,
      "site": "00a8f32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00a8f32c",
      "DATA",
      [
        "storage",
        "00c0e348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f32c",
      "DATA",
      [
        "storage",
        "00c0e3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f308.md#insn-00a8f328)
- 新版 `00a8f328`（命令位置の公開資料なし）

~~~diff
- 00a8f328 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00a8f328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f328 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00a8f328 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f328 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f328 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f328 bytes 08210d91
+ 00a8f328 bytes 08e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56979482ba0a0b30fa6c95135e5d5775"></a>

### [`00a8f33c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f33c.md) → [`00a8f33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f33c.md) FUN_00a8f33c

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
      "definition_site": "00a8f348",
      "incomplete_value": false,
      "site": "00a8f348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f348",
      "incomplete_value": false,
      "site": "00a8f348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:348:8"
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
      "00a8f348",
      "DATA",
      [
        "storage",
        "00c0e348",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f348",
      "DATA",
      [
        "storage",
        "00c0e3f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f33c.md#insn-00a8f344)
- 新版 `00a8f344`（命令位置の公開資料なし）

~~~diff
- 00a8f344 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00a8f344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f344 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00a8f344 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f344 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f344 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f344 bytes 29210d91
+ 00a8f344 bytes 29e10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f22bd4354ba6253e7ddc51258bf4b1c"></a>

### [`00a8f358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f358.md) → [`00a8f358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f358.md) FUN_00a8f358

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 12件 [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`0044ac14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac14.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 12件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0044ac14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac14.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

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
      "definition_site": "00a8f3b0",
      "incomplete_value": true,
      "site": "00a8f3b0",
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
      "definition_site": "00a8f3b0",
      "incomplete_value": true,
      "site": "00a8f3b0",
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
      "definition_site": "00a8f3b8",
      "incomplete_value": false,
      "site": "00a8f3c8",
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
    "old": {
      "definition_site": "00a8f3b8",
      "incomplete_value": false,
      "site": "00a8f3c8",
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
            "const:d98:8"
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
      "definition_site": "00a8f3c0",
      "incomplete_value": false,
      "site": "00a8f3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f3c0",
      "incomplete_value": false,
      "site": "00a8f3c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a8f3ac",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8f3b8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8f3c0",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a8f3ac",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a8f3b8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a8f3c0",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f358.md#insn-00a8f3ac) · [`00a8f3b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f358.md#insn-00a8f3b8) · [`00a8f3c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f358.md#insn-00a8f3c0)
- 新版 `00a8f3ac`（命令位置の公開資料なし） · `00a8f3b8`（命令位置の公開資料なし） · `00a8f3c0`（命令位置の公開資料なし）

~~~diff
- 00a8f3ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a8f3ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a8f3ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a8f3ac ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a8f3ac bytes 00dd44f9
+ 00a8f3ac bytes 003d45f9
- 00a8f3b8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a8f3b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a8f3b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a8f3b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a8f3b8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a8f3b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8f3b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a8f3b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a8f3b8 bytes 21603691
+ 00a8f3b8 bytes 21203991
- 00a8f3c0 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a8f3c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a8f3c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a8f3c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a8f3c0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a8f3c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8f3c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a8f3c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a8f3c0 bytes 42c03891
+ 00a8f3c0 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fed49fe27da315d68551464fc1142f7"></a>

### [`00a8f608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f608.md) → [`00a8f608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f608.md) FUN_00a8f608

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
      "definition_site": "00a8f628",
      "incomplete_value": false,
      "site": "00a8f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f628",
      "incomplete_value": false,
      "site": "00a8f62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00a8f62c",
      "DATA",
      [
        "storage",
        "00c0e3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f62c",
      "DATA",
      [
        "storage",
        "00c0e488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f608.md#insn-00a8f628)
- 新版 `00a8f628`（命令位置の公開資料なし）

~~~diff
- 00a8f628 ["COPY", "tmp:0:8", ["const:3d8:8"]]
- 00a8f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f628 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00a8f628 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f628 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f628 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f628 bytes 08610f91
+ 00a8f628 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-055b606927d495445e838894921abaa0"></a>

### [`00a8f660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f660.md) → [`00a8f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md) FUN_00a8f660

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`006330dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00633/006330dc.md) [`00a8f820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f820.md) [`00a8f824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f824.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`006330dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md) [`00a8f820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f820.md) [`00a8f824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f824.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8f6f0",
      "incomplete_value": false,
      "site": "00a8f6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f6f0",
      "incomplete_value": false,
      "site": "00a8f6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00a8f6f0",
      "DATA",
      [
        "storage",
        "00c0e448",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f72c",
      "READ",
      [
        "storage",
        "00c0e468",
        null,
        "pointer"
      ]
    ],
    [
      "00a8f72c",
      "READ",
      [
        "storage",
        "00c0e470",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f6f0",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f72c",
      "READ",
      [
        "storage",
        "00c0e518",
        null,
        "pointer"
      ]
    ],
    [
      "00a8f72c",
      "READ",
      [
        "storage",
        "00c0e520",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f6e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f660.md#insn-00a8f6e4)
- 新版 `00a8f6e4`（命令位置の公開資料なし）

~~~diff
- 00a8f6e4 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00a8f6e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f6e4 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00a8f6e4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f6e4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f6e4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f6e4 bytes 29211191
+ 00a8f6e4 bytes 29e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85d6c8f6b94b5d96a400f9f4b8f99d08"></a>

### [`00a8f7d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f7d0.md) → [`00a8f7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f7d0.md) FUN_00a8f7d0

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
      "definition_site": "00a8f7f0",
      "incomplete_value": false,
      "site": "00a8f7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f7f0",
      "incomplete_value": false,
      "site": "00a8f7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00a8f7f4",
      "DATA",
      [
        "storage",
        "00c0e448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f7f4",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f7f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f7d0.md#insn-00a8f7f0)
- 新版 `00a8f7f0`（命令位置の公開資料なし）

~~~diff
- 00a8f7f0 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00a8f7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f7f0 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00a8f7f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f7f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f7f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f7f0 bytes 08211191
+ 00a8f7f0 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11faafe8ef9ca1552e6894ad6875d44"></a>

### [`00a8f808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f808.md) → [`00a8f808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f808.md) FUN_00a8f808

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
      "definition_site": "00a8f80c",
      "incomplete_value": false,
      "site": "00a8f810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f80c",
      "incomplete_value": false,
      "site": "00a8f810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:448:8"
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
      "00a8f810",
      "DATA",
      [
        "storage",
        "00c0e448",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f810",
      "DATA",
      [
        "storage",
        "00c0e4f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f808.md#insn-00a8f80c)
- 新版 `00a8f80c`（命令位置の公開資料なし）

~~~diff
- 00a8f80c ["COPY", "tmp:0:8", ["const:448:8"]]
- 00a8f80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f80c ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00a8f80c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f80c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f80c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f80c bytes 08211191
+ 00a8f80c bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c76d0814af43c2821f4d90e14f2fc2a4"></a>

### [`00a8f85c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f85c.md) → [`00a8f85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f85c.md) FUN_00a8f85c

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
      "definition_site": "00a8f87c",
      "incomplete_value": false,
      "site": "00a8f880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:588:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8f87c",
      "incomplete_value": false,
      "site": "00a8f880",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a8f880",
      "DATA",
      [
        "storage",
        "00c0e4d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f880",
      "DATA",
      [
        "storage",
        "00c0e588",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f85c.md#insn-00a8f87c)
- 新版 `00a8f87c`（命令位置の公開資料なし）

~~~diff
- 00a8f87c ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00a8f87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f87c ["COPY", "tmp:0:8", ["const:588:8"]]
+ 00a8f87c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f87c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f87c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f87c bytes 08611391
+ 00a8f87c bytes 08211691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5845e96ea9620ba212f3fe9c6e76d46d"></a>

### [`00a8f8b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f8b4.md) → [`00a8f8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f8b4.md) FUN_00a8f8b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 33件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md)
- 新版 呼出元 0件  · 呼出先 33件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.76% / 新版 97.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a8fd24",
      "incomplete_value": false,
      "site": "00a8fd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a8fd24",
      "incomplete_value": false,
      "site": "00a8fd24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00a8f990",
      "READ",
      [
        "storage",
        "002984b4",
        null,
        "string"
      ]
    ],
    [
      "00a8f9c4",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f9fc",
      "DATA",
      [
        "storage",
        "00c0e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a8f990",
      "READ",
      [
        "storage",
        "00298541",
        null,
        "string"
      ]
    ],
    [
      "00a8f9c4",
      "DATA",
      [
        "storage",
        "00c0e5f8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a8f9fc",
      "DATA",
      [
        "storage",
        "00c0e678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a8f988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f8b4.md#insn-00a8f988) · [`00a8f9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f8b4.md#insn-00a8f9bc) · [`00a8f9f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8f8b4.md#insn-00a8f9f8)
- 新版 `00a8f988`（命令位置の公開資料なし） · `00a8f9bc`（命令位置の公開資料なし） · `00a8f9f8`（命令位置の公開資料なし）

~~~diff
- 00a8f988 ["COPY", "tmp:0:8", ["const:4b4:8"]]
- 00a8f988 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f988 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a8f988 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a8f988 ["COPY", "tmp:0:8", ["const:541:8"]]
+ 00a8f988 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f988 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a8f988 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a8f988 bytes 29d11291
+ 00a8f988 bytes 29051591
- 00a8f9bc ["COPY", "tmp:0:8", ["const:548:8"]]
- 00a8f9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9bc ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00a8f9bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f9bc bytes 08211591
+ 00a8f9bc bytes 08e11791
- 00a8f9f8 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00a8f9f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f9f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a8f9f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9f8 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00a8f9f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a8f9f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a8f9f8 bytes 08211791
+ 00a8f9f8 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c72ddafcb0dd543c14386dc934d583"></a>

### [`00a8ffe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8ffe4.md) → [`00a8ffe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8ffe4.md) FUN_00a8ffe4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90008",
      "incomplete_value": false,
      "site": "00a90008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90008",
      "incomplete_value": false,
      "site": "00a90008",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00a90008",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90008",
      "DATA",
      [
        "storage",
        "00c0e5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8f/00a8ffe4.md#insn-00a90004)
- 新版 `00a90004`（命令位置の公開資料なし）

~~~diff
- 00a90004 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00a90004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90004 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00a90004 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90004 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90004 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90004 bytes 08211591
+ 00a90004 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-870fe21dce4a84d947d75892769c76f2"></a>

### [`00a90018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90018.md) → [`00a90018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90018.md) FUN_00a90018

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
      "definition_site": "00a90024",
      "incomplete_value": false,
      "site": "00a90024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:5f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90024",
      "incomplete_value": false,
      "site": "00a90024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:548:8"
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
      "00a90024",
      "DATA",
      [
        "storage",
        "00c0e548",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90024",
      "DATA",
      [
        "storage",
        "00c0e5f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90018.md#insn-00a90020)
- 新版 `00a90020`（命令位置の公開資料なし）

~~~diff
- 00a90020 ["COPY", "tmp:0:8", ["const:548:8"]]
- 00a90020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90020 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00a90020 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90020 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90020 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90020 bytes 29211591
+ 00a90020 bytes 29e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bba9893f97f76da0e9a5043e4c65218c"></a>

### [`00a90144`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90144.md) → [`00a90144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90144.md) FUN_00a90144

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90168",
      "incomplete_value": false,
      "site": "00a90168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90168",
      "incomplete_value": false,
      "site": "00a90168",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00a90168",
      "DATA",
      [
        "storage",
        "00c0e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90168",
      "DATA",
      [
        "storage",
        "00c0e678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90164`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90144.md#insn-00a90164)
- 新版 `00a90164`（命令位置の公開資料なし）

~~~diff
- 00a90164 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00a90164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90164 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00a90164 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90164 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90164 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90164 bytes 08211791
+ 00a90164 bytes 08e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d61a5f7ce689c7746e96a8358d5a2c89"></a>

### [`00a90178`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90178.md) → [`00a90178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90178.md) FUN_00a90178

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
      "definition_site": "00a90184",
      "incomplete_value": false,
      "site": "00a90184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:678:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90184",
      "incomplete_value": false,
      "site": "00a90184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:5c8:8"
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
      "00a90184",
      "DATA",
      [
        "storage",
        "00c0e5c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90184",
      "DATA",
      [
        "storage",
        "00c0e678",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90178.md#insn-00a90180)
- 新版 `00a90180`（命令位置の公開資料なし）

~~~diff
- 00a90180 ["COPY", "tmp:0:8", ["const:5c8:8"]]
- 00a90180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90180 ["COPY", "tmp:0:8", ["const:678:8"]]
+ 00a90180 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90180 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90180 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90180 bytes 29211791
+ 00a90180 bytes 29e11991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f972dc1d0c17186e8ff2b09c07f1157f"></a>

### [`00a901f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a901f0.md) → [`00a901f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a901f0.md) FUN_00a901f0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90214",
      "incomplete_value": false,
      "site": "00a90214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90214",
      "incomplete_value": false,
      "site": "00a90214",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:648:8"
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
      "00a90214",
      "DATA",
      [
        "storage",
        "00c0e648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90214",
      "DATA",
      [
        "storage",
        "00c0e6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a901f0.md#insn-00a90210)
- 新版 `00a90210`（命令位置の公開資料なし）

~~~diff
- 00a90210 ["COPY", "tmp:0:8", ["const:648:8"]]
- 00a90210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90210 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00a90210 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90210 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90210 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90210 bytes 08211991
+ 00a90210 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e527b564aa56121d9ed7d448bee1824d"></a>

### [`00a90224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90224.md) → [`00a90224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90224.md) FUN_00a90224

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
      "definition_site": "00a90230",
      "incomplete_value": false,
      "site": "00a90230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90230",
      "incomplete_value": false,
      "site": "00a90230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a90230",
      "DATA",
      [
        "storage",
        "00c0e648",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90230",
      "DATA",
      [
        "storage",
        "00c0e6f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9022c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90224.md#insn-00a9022c)
- 新版 `00a9022c`（命令位置の公開資料なし）

~~~diff
- 00a9022c ["COPY", "tmp:0:8", ["const:648:8"]]
- 00a9022c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9022c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9022c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a9022c ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00a9022c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9022c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9022c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9022c bytes 29211991
+ 00a9022c bytes 29e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94c584bd0fd3e55ecaa3fb5e86533f5d"></a>

### [`00a90240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90240.md) → [`00a90240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90240.md) FUN_00a90240

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00467/00467074.md) [`00883bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md) [`008847e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00884/008847e4.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`008847e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00884/008847e4.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.98% / 新版 98.98%

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
      "definition_site": "00a90290",
      "incomplete_value": true,
      "site": "00a90290",
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
      "definition_site": "00a90290",
      "incomplete_value": true,
      "site": "00a90290",
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a90298",
      "incomplete_value": false,
      "site": "00a902a8",
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
    "old": {
      "definition_site": "00a90298",
      "incomplete_value": false,
      "site": "00a902a8",
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
            "const:d98:8"
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
      "definition_site": "00a902a0",
      "incomplete_value": false,
      "site": "00a902a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a902a0",
      "incomplete_value": false,
      "site": "00a902a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a9028c",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a90298",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a902a0",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a9028c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a90298",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a902a0",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9028c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90240.md#insn-00a9028c) · [`00a90298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90240.md#insn-00a90298) · [`00a902a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90240.md#insn-00a902a0)
- 新版 `00a9028c`（命令位置の公開資料なし） · `00a90298`（命令位置の公開資料なし） · `00a902a0`（命令位置の公開資料なし）

~~~diff
- 00a9028c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a9028c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a9028c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a9028c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a9028c bytes 00dd44f9
+ 00a9028c bytes 003d45f9
- 00a90298 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a90298 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a90298 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a90298 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a90298 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a90298 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a90298 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a90298 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a90298 bytes 21603691
+ 00a90298 bytes 21203991
- 00a902a0 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a902a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a902a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a902a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a902a0 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a902a0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a902a0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a902a0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a902a0 bytes 42c03891
+ 00a902a0 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80a66320dd691f4be6239857b7d6c769"></a>

### [`00a9057c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a9057c.md) → [`00a9057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a9057c.md) FUN_00a9057c

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
      "definition_site": "00a9059c",
      "incomplete_value": false,
      "site": "00a905a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9059c",
      "incomplete_value": false,
      "site": "00a905a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00a905a0",
      "DATA",
      [
        "storage",
        "00c0e6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a905a0",
      "DATA",
      [
        "storage",
        "00c0e778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9059c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a9057c.md#insn-00a9059c)
- 新版 `00a9059c`（命令位置の公開資料なし）

~~~diff
- 00a9059c ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00a9059c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9059c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9059c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9059c ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00a9059c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9059c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9059c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9059c bytes 08211b91
+ 00a9059c bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb3ffdabdcdb1be469eff834f89ee458"></a>

### [`00a905b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a905b4.md) → [`00a905b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a905b4.md) FUN_00a905b4

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
      "definition_site": "00a905b8",
      "incomplete_value": false,
      "site": "00a905bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:778:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a905b8",
      "incomplete_value": false,
      "site": "00a905bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:6c8:8"
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
      "00a905bc",
      "DATA",
      [
        "storage",
        "00c0e6c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a905bc",
      "DATA",
      [
        "storage",
        "00c0e778",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a905b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a905b4.md#insn-00a905b8)
- 新版 `00a905b8`（命令位置の公開資料なし）

~~~diff
- 00a905b8 ["COPY", "tmp:0:8", ["const:6c8:8"]]
- 00a905b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a905b8 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00a905b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a905b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a905b8 bytes 08211b91
+ 00a905b8 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7549dbd29e22ed2dba045b8af4657096"></a>

### [`00a906e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a906e8.md) → [`00a906e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a906e8.md) FUN_00a906e8

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
      "definition_site": "00a90708",
      "incomplete_value": false,
      "site": "00a9070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:808:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90708",
      "incomplete_value": false,
      "site": "00a9070c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a9070c",
      "DATA",
      [
        "storage",
        "00c0e758",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9070c",
      "DATA",
      [
        "storage",
        "00c0e808",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a906e8.md#insn-00a90708)
- 新版 `00a90708`（命令位置の公開資料なし）

~~~diff
- 00a90708 ["COPY", "tmp:0:8", ["const:758:8"]]
- 00a90708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90708 ["COPY", "tmp:0:8", ["const:808:8"]]
+ 00a90708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90708 bytes 08611d91
+ 00a90708 bytes 08212091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3ab34bf115af44c2d4e35f8d85fdad7"></a>

### [`00a90820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90820.md) → [`00a90820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90820.md) FUN_00a90820

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90844",
      "incomplete_value": false,
      "site": "00a90844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90844",
      "incomplete_value": false,
      "site": "00a90844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a90844",
      "DATA",
      [
        "storage",
        "00c0e7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90844",
      "DATA",
      [
        "storage",
        "00c0e888",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90820.md#insn-00a90840)
- 新版 `00a90840`（命令位置の公開資料なし）

~~~diff
- 00a90840 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 00a90840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90840 ["COPY", "tmp:0:8", ["const:888:8"]]
+ 00a90840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90840 bytes 08611f91
+ 00a90840 bytes 08212291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c85d5406eb49a92d76d3c69e07086d0a"></a>

### [`00a90870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90870.md) → [`00a90870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90870.md) FUN_00a90870

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`0059815c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00598/0059815c.md) [`0071a0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0071a/0071a0c4.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0059815c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00598/0059815c.md) [`0071a0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071a/0071a0c4.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.30% / 新版 93.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a90a80",
      "incomplete_value": false,
      "site": "00a90a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90a80",
      "incomplete_value": false,
      "site": "00a90a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "definition_site": "00a90b08",
      "incomplete_value": true,
      "site": "00a90b1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:54d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90b08",
      "incomplete_value": true,
      "site": "00a90b1c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4c0:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00a90b3c",
      "incomplete_value": false,
      "site": "00a90b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90b3c",
      "incomplete_value": false,
      "site": "00a90b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00a90a64",
      "PARAM",
      [
        "storage",
        "0029ecc3",
        null,
        "string"
      ]
    ],
    [
      "00a90a64",
      "PARAM",
      [
        "storage",
        "002a4d38",
        null,
        "string"
      ]
    ],
    [
      "00a90a64",
      "PARAM",
      [
        "storage",
        "00293ff7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00a90a64",
      "PARAM",
      [
        "storage",
        "0029ed50",
        null,
        "string"
      ]
    ],
    [
      "00a90a64",
      "PARAM",
      [
        "storage",
        "002a4d31",
        null,
        "string"
      ]
    ],
    [
      "00a90a64",
      "PARAM",
      [
        "storage",
        "00294084",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90a40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90870.md#insn-00a90a40) · [`00a90a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90870.md#insn-00a90a44)
- 新版 `00a90a40`（命令位置の公開資料なし） · `00a90a44`（命令位置の公開資料なし）

~~~diff
- 00a90a40 ["COPY", "tmp:0:8", ["const:cc3:8"]]
- 00a90a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90a40 ["COPY", "tmp:0:8", ["const:d50:8"]]
+ 00a90a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90a40 bytes 080d3391
+ 00a90a40 bytes 08413591
- 00a90a44 ["COPY", "register:4048:8", ["const:293000:8"]]
- 00a90a44 bytes 09c0fff0
+ 00a90a44 ["COPY", "register:4048:8", ["const:294000:8"]]
+ 00a90a44 bytes 29c0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c78de713f8a4e6fd568a81a8592c300"></a>

### [`00a90d28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90d28.md) → [`00a90d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d28.md) FUN_00a90d28

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90d3c",
      "incomplete_value": false,
      "site": "00a90d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90d3c",
      "incomplete_value": false,
      "site": "00a90d40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00a90d40",
      "DATA",
      [
        "storage",
        "00c0e848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90d40",
      "DATA",
      [
        "storage",
        "00c0e8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90d28.md#insn-00a90d3c)
- 新版 `00a90d3c`（命令位置の公開資料なし）

~~~diff
- 00a90d3c ["COPY", "tmp:0:8", ["const:848:8"]]
- 00a90d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90d3c ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00a90d3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90d3c bytes 08212191
+ 00a90d3c bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9320b09bf318b4f8c1e7dd5c1f51ae65"></a>

### [`00a90d4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90d4c.md) → [`00a90d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90d4c.md) FUN_00a90d4c

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
      "definition_site": "00a90d50",
      "incomplete_value": false,
      "site": "00a90d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90d50",
      "incomplete_value": false,
      "site": "00a90d54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:848:8"
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
      "00a90d54",
      "DATA",
      [
        "storage",
        "00c0e848",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90d54",
      "DATA",
      [
        "storage",
        "00c0e8f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90d4c.md#insn-00a90d50)
- 新版 `00a90d50`（命令位置の公開資料なし）

~~~diff
- 00a90d50 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00a90d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90d50 ["COPY", "tmp:0:8", ["const:8f8:8"]]
+ 00a90d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90d50 bytes 08212191
+ 00a90d50 bytes 08e12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40b976b0a83e9c533231ed8fb12e43a3"></a>

### [`00a90dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90dd8.md) → [`00a90dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90dd8.md) FUN_00a90dd8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90dfc",
      "incomplete_value": false,
      "site": "00a90dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90dfc",
      "incomplete_value": false,
      "site": "00a90dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00a90dfc",
      "DATA",
      [
        "storage",
        "00c0e8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90dfc",
      "DATA",
      [
        "storage",
        "00c0e978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90dd8.md#insn-00a90df8)
- 新版 `00a90df8`（命令位置の公開資料なし）

~~~diff
- 00a90df8 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00a90df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90df8 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00a90df8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90df8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90df8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90df8 bytes 08212391
+ 00a90df8 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5370a2b3904b3e24cfda6549496168"></a>

### [`00a90e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90e0c.md) → [`00a90e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90e0c.md) FUN_00a90e0c

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
      "definition_site": "00a90e18",
      "incomplete_value": false,
      "site": "00a90e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90e18",
      "incomplete_value": false,
      "site": "00a90e18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00a90e18",
      "DATA",
      [
        "storage",
        "00c0e8c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90e18",
      "DATA",
      [
        "storage",
        "00c0e978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90e0c.md#insn-00a90e14)
- 新版 `00a90e14`（命令位置の公開資料なし）

~~~diff
- 00a90e14 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00a90e14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90e14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90e14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90e14 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00a90e14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90e14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90e14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90e14 bytes 29212391
+ 00a90e14 bytes 29e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8db6e636bc4782f9305c4a2960ecb5e1"></a>

### [`00a90edc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90edc.md) → [`00a90edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90edc.md) FUN_00a90edc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90ef0",
      "incomplete_value": false,
      "site": "00a90ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90ef0",
      "incomplete_value": false,
      "site": "00a90ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00a90ef4",
      "DATA",
      [
        "storage",
        "00c0e958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90ef4",
      "DATA",
      [
        "storage",
        "00c0ea08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90ef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90edc.md#insn-00a90ef0)
- 新版 `00a90ef0`（命令位置の公開資料なし）

~~~diff
- 00a90ef0 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00a90ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90ef0 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00a90ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90ef0 bytes 08612591
+ 00a90ef0 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d451a1276fa45d0fb81444e60fa700c2"></a>

### [`00a90f00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90f00.md) → [`00a90f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f00.md) FUN_00a90f00

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
      "definition_site": "00a90f04",
      "incomplete_value": false,
      "site": "00a90f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90f04",
      "incomplete_value": false,
      "site": "00a90f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a90f08",
      "DATA",
      [
        "storage",
        "00c0e958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90f08",
      "DATA",
      [
        "storage",
        "00c0ea08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90f00.md#insn-00a90f04)
- 新版 `00a90f04`（命令位置の公開資料なし）

~~~diff
- 00a90f04 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00a90f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90f04 ["COPY", "tmp:0:8", ["const:a08:8"]]
+ 00a90f04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90f04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90f04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90f04 bytes 08612591
+ 00a90f04 bytes 08212891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d57db2f1a0a8a74b6bccf96beb0f9c1"></a>

### [`00a90f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90f90.md) → [`00a90f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90f90.md) FUN_00a90f90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a90fb4",
      "incomplete_value": false,
      "site": "00a90fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90fb4",
      "incomplete_value": false,
      "site": "00a90fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "00a90fb4",
      "DATA",
      [
        "storage",
        "00c0e9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90fb4",
      "DATA",
      [
        "storage",
        "00c0ea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90f90.md#insn-00a90fb0)
- 新版 `00a90fb0`（命令位置の公開資料なし）

~~~diff
- 00a90fb0 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00a90fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a90fb0 ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00a90fb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90fb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a90fb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a90fb0 bytes 08612791
+ 00a90fb0 bytes 08212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16c7ff95d62ecf0e599960567014ae71"></a>

### [`00a90fc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fc4.md) → [`00a90fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90fc4.md) FUN_00a90fc4

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
      "definition_site": "00a90fd0",
      "incomplete_value": false,
      "site": "00a90fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a90fd0",
      "incomplete_value": false,
      "site": "00a90fd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a90fd0",
      "DATA",
      [
        "storage",
        "00c0e9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a90fd0",
      "DATA",
      [
        "storage",
        "00c0ea88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a90fcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fc4.md#insn-00a90fcc)
- 新版 `00a90fcc`（命令位置の公開資料なし）

~~~diff
- 00a90fcc ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 00a90fcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a90fcc ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00a90fcc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90fcc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a90fcc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a90fcc bytes 29612791
+ 00a90fcc bytes 29212a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98c5f3bfe4a2c6a7114ab17af2a89407"></a>

### [`00a90fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fe0.md) → [`00a90fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90fe0.md) FUN_00a90fe0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`00885f80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00885/00885f80.md) [`00886348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00886/00886348.md)
- 新版 呼出元 0件  · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00885f80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00885/00885f80.md) [`00886348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/00886348.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a91060",
      "incomplete_value": true,
      "site": "00a91070",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c4a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91060",
      "incomplete_value": true,
      "site": "00a91070",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bbd:8"
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
      "definition_site": "00a91090",
      "incomplete_value": false,
      "site": "00a91090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91090",
      "incomplete_value": false,
      "site": "00a91090",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "definition_site": "00a910c0",
      "incomplete_value": false,
      "site": "00a910c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a910c0",
      "incomplete_value": false,
      "site": "00a910c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00a91060",
      "READ",
      [
        "storage",
        "0029dbbd",
        null,
        "string"
      ]
    ],
    [
      "00a91090",
      "DATA",
      [
        "storage",
        "00c0ea48",
        null,
        "undefined *"
      ]
    ],
    [
      "00a910c0",
      "DATA",
      [
        "storage",
        "00c0eac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91060",
      "READ",
      [
        "storage",
        "0029dc4a",
        null,
        "string"
      ]
    ],
    [
      "00a91090",
      "DATA",
      [
        "storage",
        "00c0eaf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00a910c0",
      "DATA",
      [
        "storage",
        "00c0eb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fe0.md#insn-00a91058) · [`00a91088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fe0.md#insn-00a91088) · [`00a910bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90fe0.md#insn-00a910bc)
- 新版 `00a91058`（命令位置の公開資料なし） · `00a91088`（命令位置の公開資料なし） · `00a910bc`（命令位置の公開資料なし）

~~~diff
- 00a91058 ["COPY", "tmp:0:8", ["const:bbd:8"]]
- 00a91058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91058 ["COPY", "tmp:0:8", ["const:c4a:8"]]
+ 00a91058 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91058 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91058 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91058 bytes 29f52e91
+ 00a91058 bytes 29293191
- 00a91088 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00a91088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91088 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00a91088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91088 bytes 08212991
+ 00a91088 bytes 08e12b91
- 00a910bc ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00a910bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a910bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a910bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a910bc ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00a910bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a910bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a910bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a910bc bytes 08212b91
+ 00a910bc bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71b5ae8f34aad49369fb03668ae1aeff"></a>

### [`00a912ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a912ec.md) → [`00a912ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a912ec.md) FUN_00a912ec

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91310",
      "incomplete_value": true,
      "site": "00a91310",
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
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91310",
      "incomplete_value": true,
      "site": "00a91310",
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
            "const:a48:8"
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
      "00a91310",
      "DATA",
      [
        "storage",
        "00c0ea48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91310",
      "DATA",
      [
        "storage",
        "00c0eaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9130c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a912ec.md#insn-00a9130c)
- 新版 `00a9130c`（命令位置の公開資料なし）

~~~diff
- 00a9130c ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00a9130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9130c ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00a9130c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9130c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9130c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9130c bytes 08212991
+ 00a9130c bytes 08e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d3404b0897372d8be44473beea783c"></a>

### [`00a91320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91320.md) → [`00a91320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91320.md) FUN_00a91320

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
      "definition_site": "00a9132c",
      "incomplete_value": false,
      "site": "00a9132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:af8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9132c",
      "incomplete_value": false,
      "site": "00a9132c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:a48:8"
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
      "00a9132c",
      "DATA",
      [
        "storage",
        "00c0ea48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9132c",
      "DATA",
      [
        "storage",
        "00c0eaf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91320.md#insn-00a91328)
- 新版 `00a91328`（命令位置の公開資料なし）

~~~diff
- 00a91328 ["COPY", "tmp:0:8", ["const:a48:8"]]
- 00a91328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91328 ["COPY", "tmp:0:8", ["const:af8:8"]]
+ 00a91328 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91328 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91328 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91328 bytes 29212991
+ 00a91328 bytes 29e12b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22c563f9cfb647c5205c19d8de9eae62"></a>

### [`00a913d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a913d0.md) → [`00a913d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a913d0.md) FUN_00a913d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a913f4",
      "incomplete_value": false,
      "site": "00a913f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a913f4",
      "incomplete_value": false,
      "site": "00a913f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00a913f4",
      "DATA",
      [
        "storage",
        "00c0eac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a913f4",
      "DATA",
      [
        "storage",
        "00c0eb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a913f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a913d0.md#insn-00a913f0)
- 新版 `00a913f0`（命令位置の公開資料なし）

~~~diff
- 00a913f0 ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00a913f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a913f0 ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00a913f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a913f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a913f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a913f0 bytes 08212b91
+ 00a913f0 bytes 08e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6635b94ca588f4ad7f77bb7765ca3d3"></a>

### [`00a91404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91404.md) → [`00a91404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91404.md) FUN_00a91404

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
      "definition_site": "00a91410",
      "incomplete_value": false,
      "site": "00a91410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91410",
      "incomplete_value": false,
      "site": "00a91410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00a91410",
      "DATA",
      [
        "storage",
        "00c0eac8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91410",
      "DATA",
      [
        "storage",
        "00c0eb78",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9140c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91404.md#insn-00a9140c)
- 新版 `00a9140c`（命令位置の公開資料なし）

~~~diff
- 00a9140c ["COPY", "tmp:0:8", ["const:ac8:8"]]
- 00a9140c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9140c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9140c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a9140c ["COPY", "tmp:0:8", ["const:b78:8"]]
+ 00a9140c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9140c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9140c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9140c bytes 29212b91
+ 00a9140c bytes 29e12d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86bb048cd71e05ed0cdcf86bc59bb25c"></a>

### [`00a91468`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91468.md) → [`00a91468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91468.md) FUN_00a91468

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a9148c",
      "incomplete_value": false,
      "site": "00a9148c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9148c",
      "incomplete_value": false,
      "site": "00a9148c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00a9148c",
      "DATA",
      [
        "storage",
        "00c0eb48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9148c",
      "DATA",
      [
        "storage",
        "00c0ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91468.md#insn-00a91488)
- 新版 `00a91488`（命令位置の公開資料なし）

~~~diff
- 00a91488 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00a91488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91488 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00a91488 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91488 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91488 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91488 bytes 08212d91
+ 00a91488 bytes 08e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25bcd1c916129275d0f6e24dd8020baa"></a>

### [`00a9149c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a9149c.md) → [`00a9149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9149c.md) FUN_00a9149c

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
      "definition_site": "00a914a8",
      "incomplete_value": false,
      "site": "00a914a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a914a8",
      "incomplete_value": false,
      "site": "00a914a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "00a914a8",
      "DATA",
      [
        "storage",
        "00c0eb48",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a914a8",
      "DATA",
      [
        "storage",
        "00c0ebf8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a914a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a9149c.md#insn-00a914a4)
- 新版 `00a914a4`（命令位置の公開資料なし）

~~~diff
- 00a914a4 ["COPY", "tmp:0:8", ["const:b48:8"]]
- 00a914a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a914a4 ["COPY", "tmp:0:8", ["const:bf8:8"]]
+ 00a914a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a914a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a914a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a914a4 bytes 29212d91
+ 00a914a4 bytes 29e12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-babfbe01989cd11a28859bc13380ad49"></a>

### [`00a914b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a914b8.md) → [`00a914b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a914b8.md) FUN_00a914b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00445d88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/00445d88.md) [`00446d2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/00446d2c.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`00a8b028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a8b/00a8b028.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`00446d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/00446d2c.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`00a8b028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8b/00a8b028.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.98% / 新版 92.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a914f0",
      "incomplete_value": true,
      "site": "00a914f0",
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
      "definition_site": "00a914f0",
      "incomplete_value": true,
      "site": "00a914f0",
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
      "definition_site": "00a914f8",
      "incomplete_value": false,
      "site": "00a91508",
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
    "old": {
      "definition_site": "00a914f8",
      "incomplete_value": false,
      "site": "00a91508",
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
            "const:d98:8"
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
      "definition_site": "00a91500",
      "incomplete_value": false,
      "site": "00a91508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91500",
      "incomplete_value": false,
      "site": "00a91508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a914dc",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a914f8",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91500",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a914dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a914f8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91500",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a914dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a914b8.md#insn-00a914dc) · [`00a914f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a914b8.md#insn-00a914f8) · [`00a91500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a914b8.md#insn-00a91500)
- 新版 `00a914dc`（命令位置の公開資料なし） · `00a914f8`（命令位置の公開資料なし） · `00a91500`（命令位置の公開資料なし）

~~~diff
- 00a914dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9b8:8"]]
- 00a914dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a914dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
+ 00a914dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a914dc bytes 00dd44f9
+ 00a914dc bytes 003d45f9
- 00a914f8 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a914f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a914f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a914f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a914f8 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a914f8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a914f8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a914f8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a914f8 bytes 21603691
+ 00a914f8 bytes 21203991
- 00a91500 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a91500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a91500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a91500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a91500 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a91500 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a91500 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a91500 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a91500 bytes 42c03891
+ 00a91500 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-331ffb2e812b0ce6c9e3f52b2ee9fe4d"></a>

### [`00a915c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a915c8.md) → [`00a915c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915c8.md) FUN_00a915c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a915ec",
      "incomplete_value": false,
      "site": "00a915ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a915ec",
      "incomplete_value": false,
      "site": "00a915ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "00a915ec",
      "DATA",
      [
        "storage",
        "00c0ebd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a915ec",
      "DATA",
      [
        "storage",
        "00c0ec88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a915e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a915c8.md#insn-00a915e8)
- 新版 `00a915e8`（命令位置の公開資料なし）

~~~diff
- 00a915e8 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00a915e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a915e8 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00a915e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a915e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a915e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a915e8 bytes 08612f91
+ 00a915e8 bytes 08213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e541f7d56b1ac3440bb26dc266a08d9"></a>

### [`00a915fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a915fc.md) → [`00a915fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a915fc.md) FUN_00a915fc

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
      "definition_site": "00a91608",
      "incomplete_value": false,
      "site": "00a91608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91608",
      "incomplete_value": false,
      "site": "00a91608",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
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
      "00a91608",
      "DATA",
      [
        "storage",
        "00c0ebd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91608",
      "DATA",
      [
        "storage",
        "00c0ec88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91604`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a915fc.md#insn-00a91604)
- 新版 `00a91604`（命令位置の公開資料なし）

~~~diff
- 00a91604 ["COPY", "tmp:0:8", ["const:bd8:8"]]
- 00a91604 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91604 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91604 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91604 ["COPY", "tmp:0:8", ["const:c88:8"]]
+ 00a91604 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91604 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91604 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91604 bytes 29612f91
+ 00a91604 bytes 29213291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c10e626d3125117c593186984237f36"></a>

### [`00a91660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91660.md) → [`00a91660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91660.md) FUN_00a91660

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91684",
      "incomplete_value": false,
      "site": "00a91684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91684",
      "incomplete_value": false,
      "site": "00a91684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "00a91684",
      "DATA",
      [
        "storage",
        "00c0ec58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91684",
      "DATA",
      [
        "storage",
        "00c0ed08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91660.md#insn-00a91680)
- 新版 `00a91680`（命令位置の公開資料なし）

~~~diff
- 00a91680 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00a91680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91680 ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00a91680 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91680 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91680 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91680 bytes 08613191
+ 00a91680 bytes 08213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de234d5215943f75692856f4e824c5ca"></a>

### [`00a91694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91694.md) → [`00a91694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91694.md) FUN_00a91694

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
      "definition_site": "00a916a0",
      "incomplete_value": false,
      "site": "00a916a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a916a0",
      "incomplete_value": false,
      "site": "00a916a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "00a916a0",
      "DATA",
      [
        "storage",
        "00c0ec58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a916a0",
      "DATA",
      [
        "storage",
        "00c0ed08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9169c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91694.md#insn-00a9169c)
- 新版 `00a9169c`（命令位置の公開資料なし）

~~~diff
- 00a9169c ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00a9169c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a9169c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a9169c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a9169c ["COPY", "tmp:0:8", ["const:d08:8"]]
+ 00a9169c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9169c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a9169c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a9169c bytes 29613191
+ 00a9169c bytes 29213491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72723c409b1b400228353a7e6434e329"></a>

### [`00a916b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a916b0.md) → [`00a916b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a916b0.md) FUN_00a916b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00448c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aad4.md) [`00883bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883c74.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00448c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aad4.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md) [`00883c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883c74.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a916e4",
      "incomplete_value": true,
      "site": "00a916e4",
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
      "definition_site": "00a916e4",
      "incomplete_value": true,
      "site": "00a916e4",
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
      "definition_site": "00a916ec",
      "incomplete_value": false,
      "site": "00a916fc",
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
    "old": {
      "definition_site": "00a916ec",
      "incomplete_value": false,
      "site": "00a916fc",
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
            "const:d98:8"
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
      "definition_site": "00a916f4",
      "incomplete_value": false,
      "site": "00a916fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a916f4",
      "incomplete_value": false,
      "site": "00a916fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a916dc",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a916ec",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a916f4",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a916dc",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a916ec",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a916f4",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a916dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a916b0.md#insn-00a916dc) · [`00a916ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a916b0.md#insn-00a916ec) · [`00a916f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a916b0.md#insn-00a916f4)
- 新版 `00a916dc`（命令位置の公開資料なし） · `00a916ec`（命令位置の公開資料なし） · `00a916f4`（命令位置の公開資料なし）

~~~diff
- 00a916dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 00a916dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a916dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 00a916dc ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a916dc bytes 20dd44f9
+ 00a916dc bytes 203d45f9
- 00a916ec ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a916ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a916ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a916ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a916ec ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a916ec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a916ec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a916ec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a916ec bytes 21603691
+ 00a916ec bytes 21203991
- 00a916f4 ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a916f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a916f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a916f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a916f4 ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a916f4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a916f4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a916f4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a916f4 bytes 42c03891
+ 00a916f4 bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62aa9fd3080f194f4e6c552e28c20b63"></a>

### [`00a91834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91834.md) → [`00a91834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91834.md) FUN_00a91834

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91858",
      "incomplete_value": false,
      "site": "00a91858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91858",
      "incomplete_value": false,
      "site": "00a91858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "00a91858",
      "DATA",
      [
        "storage",
        "00c0ecd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91858",
      "DATA",
      [
        "storage",
        "00c0ed88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91834.md#insn-00a91854)
- 新版 `00a91854`（命令位置の公開資料なし）

~~~diff
- 00a91854 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00a91854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91854 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00a91854 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91854 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91854 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91854 bytes 08613391
+ 00a91854 bytes 08213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3e53d09257e16cae67776ca08f8bfb"></a>

### [`00a91868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91868.md) → [`00a91868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91868.md) FUN_00a91868

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
      "definition_site": "00a91874",
      "incomplete_value": false,
      "site": "00a91874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91874",
      "incomplete_value": false,
      "site": "00a91874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:cd8:8"
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
      "00a91874",
      "DATA",
      [
        "storage",
        "00c0ecd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91874",
      "DATA",
      [
        "storage",
        "00c0ed88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91870`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91868.md#insn-00a91870)
- 新版 `00a91870`（命令位置の公開資料なし）

~~~diff
- 00a91870 ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00a91870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91870 ["COPY", "tmp:0:8", ["const:d88:8"]]
+ 00a91870 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91870 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91870 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91870 bytes 29613391
+ 00a91870 bytes 29213691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-795bb3c5609e71c3f16a88073d324a11"></a>

### [`00a9190c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a9190c.md) → [`00a9190c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a9190c.md) FUN_00a9190c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91930",
      "incomplete_value": false,
      "site": "00a91930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91930",
      "incomplete_value": false,
      "site": "00a91930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "00a91930",
      "DATA",
      [
        "storage",
        "00c0ed58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91930",
      "DATA",
      [
        "storage",
        "00c0ee08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9192c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a9190c.md#insn-00a9192c)
- 新版 `00a9192c`（命令位置の公開資料なし）

~~~diff
- 00a9192c ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00a9192c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9192c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9192c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9192c ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00a9192c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9192c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9192c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9192c bytes 08613591
+ 00a9192c bytes 08213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a963e7f3cdeabc12c55ec73a00430b99"></a>

### [`00a91940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91940.md) → [`00a91940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91940.md) FUN_00a91940

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
      "definition_site": "00a9194c",
      "incomplete_value": false,
      "site": "00a9194c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9194c",
      "incomplete_value": false,
      "site": "00a9194c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:d58:8"
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
      "00a9194c",
      "DATA",
      [
        "storage",
        "00c0ed58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9194c",
      "DATA",
      [
        "storage",
        "00c0ee08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91948`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91940.md#insn-00a91948)
- 新版 `00a91948`（命令位置の公開資料なし）

~~~diff
- 00a91948 ["COPY", "tmp:0:8", ["const:d58:8"]]
- 00a91948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91948 ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00a91948 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91948 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91948 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91948 bytes 29613591
+ 00a91948 bytes 29213891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeb36e27958936ecc2b58bbf2d60695d"></a>

### [`00a91a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91a88.md) → [`00a91a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91a88.md) FUN_00a91a88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91aac",
      "incomplete_value": false,
      "site": "00a91aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91aac",
      "incomplete_value": false,
      "site": "00a91aac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00a91aac",
      "DATA",
      [
        "storage",
        "00c0ee58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91aac",
      "DATA",
      [
        "storage",
        "00c0ef08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91aa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91a88.md#insn-00a91aa8)
- 新版 `00a91aa8`（命令位置の公開資料なし）

~~~diff
- 00a91aa8 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a91aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91aa8 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00a91aa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91aa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91aa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91aa8 bytes 08613991
+ 00a91aa8 bytes 08213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4688994695b5cecee2d33c2052a5e882"></a>

### [`00a91abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91abc.md) → [`00a91abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91abc.md) FUN_00a91abc

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
      "definition_site": "00a91ac8",
      "incomplete_value": false,
      "site": "00a91ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91ac8",
      "incomplete_value": false,
      "site": "00a91ac8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:e58:8"
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
      "00a91ac8",
      "DATA",
      [
        "storage",
        "00c0ee58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91ac8",
      "DATA",
      [
        "storage",
        "00c0ef08",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91abc.md#insn-00a91ac4)
- 新版 `00a91ac4`（命令位置の公開資料なし）

~~~diff
- 00a91ac4 ["COPY", "tmp:0:8", ["const:e58:8"]]
- 00a91ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00a91ac4 ["COPY", "tmp:0:8", ["const:f08:8"]]
+ 00a91ac4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91ac4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00a91ac4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00a91ac4 bytes 29613991
+ 00a91ac4 bytes 29213c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886463c7771f18b3eec104d1067ddaf0"></a>

### [`00a91ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91ad8.md) → [`00a91ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91ad8.md) FUN_00a91ad8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00448c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044aad4.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883bb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883bb8.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00448c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448c90.md) [`0044aa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aa9c.md) [`0044aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044aad4.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883bb8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a91b0c",
      "incomplete_value": true,
      "site": "00a91b0c",
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
      "definition_site": "00a91b0c",
      "incomplete_value": true,
      "site": "00a91b0c",
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
      "definition_site": "00a91b14",
      "incomplete_value": false,
      "site": "00a91b24",
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
    "old": {
      "definition_site": "00a91b14",
      "incomplete_value": false,
      "site": "00a91b24",
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
            "const:d98:8"
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
      "definition_site": "00a91b1c",
      "incomplete_value": false,
      "site": "00a91b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:ee0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91b1c",
      "incomplete_value": false,
      "site": "00a91b24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0d000:8"
          ],
          [
            "leaf",
            "const:e30:8"
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
      "00a91b04",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a91b14",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91b1c",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a91b04",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a91b14",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a91b1c",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91b04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91ad8.md#insn-00a91b04) · [`00a91b14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91ad8.md#insn-00a91b14) · [`00a91b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91ad8.md#insn-00a91b1c)
- 新版 `00a91b04`（命令位置の公開資料なし） · `00a91b14`（命令位置の公開資料なし） · `00a91b1c`（命令位置の公開資料なし）

~~~diff
- 00a91b04 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9b8:8"]]
- 00a91b04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00a91b04 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
+ 00a91b04 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00a91b04 bytes 20dd44f9
+ 00a91b04 bytes 203d45f9
- 00a91b14 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a91b14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00a91b14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00a91b14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00a91b14 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a91b14 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00a91b14 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00a91b14 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00a91b14 bytes 21603691
+ 00a91b14 bytes 21203991
- 00a91b1c ["COPY", "tmp:0:8", ["const:e30:8"]]
- 00a91b1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00a91b1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00a91b1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00a91b1c ["COPY", "tmp:0:8", ["const:ee0:8"]]
+ 00a91b1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00a91b1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00a91b1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00a91b1c bytes 42c03891
+ 00a91b1c bytes 42803b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f6aebc9a6efad97f2d48da1732bd8bd"></a>

### [`00a91c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91c88.md) → [`00a91c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91c88.md) FUN_00a91c88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91c9c",
      "incomplete_value": false,
      "site": "00a91ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91c9c",
      "incomplete_value": false,
      "site": "00a91ca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00a91ca0",
      "DATA",
      [
        "storage",
        "00c0eed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91ca0",
      "DATA",
      [
        "storage",
        "00c0ef88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91c9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91c88.md#insn-00a91c9c)
- 新版 `00a91c9c`（命令位置の公開資料なし）

~~~diff
- 00a91c9c ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00a91c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91c9c ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a91c9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91c9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91c9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91c9c bytes 08613b91
+ 00a91c9c bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd9846a93fc97d1642fa11427e162195"></a>

### [`00a91cac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91cac.md) → [`00a91cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91cac.md) FUN_00a91cac

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
      "definition_site": "00a91cb0",
      "incomplete_value": false,
      "site": "00a91cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91cb0",
      "incomplete_value": false,
      "site": "00a91cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:ed8:8"
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
      "00a91cb4",
      "DATA",
      [
        "storage",
        "00c0eed8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91cb4",
      "DATA",
      [
        "storage",
        "00c0ef88",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91cac.md#insn-00a91cb0)
- 新版 `00a91cb0`（命令位置の公開資料なし）

~~~diff
- 00a91cb0 ["COPY", "tmp:0:8", ["const:ed8:8"]]
- 00a91cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91cb0 ["COPY", "tmp:0:8", ["const:f88:8"]]
+ 00a91cb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91cb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91cb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91cb0 bytes 08613b91
+ 00a91cb0 bytes 08213e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b426ea639249a7118ede5fe3dd8ece2"></a>

### [`00a91d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d30.md) → [`00a91d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d30.md) FUN_00a91d30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91d44",
      "incomplete_value": false,
      "site": "00a91d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91d44",
      "incomplete_value": false,
      "site": "00a91d48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:f58:8"
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
      "00a91d48",
      "DATA",
      [
        "storage",
        "00c0ef58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91d48",
      "DATA",
      [
        "storage",
        "00c0f008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d30.md#insn-00a91d40) · [`00a91d44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d30.md#insn-00a91d44)
- 新版 `00a91d40`（命令位置の公開資料なし） · `00a91d44`（命令位置の公開資料なし）

~~~diff
- 00a91d40 ["COPY", "register:4040:8", ["const:c0e000:8"]]
+ 00a91d40 ["COPY", "register:4040:8", ["const:c0f000:8"]]
- 00a91d40 bytes e80b00b0
+ 00a91d40 bytes e80b00d0
- 00a91d44 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00a91d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91d44 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00a91d44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91d44 bytes 08613d91
+ 00a91d44 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91915e65b0055c5fecd8d1dede3b81e5"></a>

### [`00a91d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d54.md) → [`00a91d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91d54.md) FUN_00a91d54

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
      "definition_site": "00a91d58",
      "incomplete_value": false,
      "site": "00a91d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91d58",
      "incomplete_value": false,
      "site": "00a91d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a91d5c",
      "DATA",
      [
        "storage",
        "00c0ef58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91d5c",
      "DATA",
      [
        "storage",
        "00c0f008",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91d54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d54.md#insn-00a91d54) · [`00a91d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91d54.md#insn-00a91d58)
- 新版 `00a91d54`（命令位置の公開資料なし） · `00a91d58`（命令位置の公開資料なし）

~~~diff
- 00a91d54 ["COPY", "register:4040:8", ["const:c0e000:8"]]
+ 00a91d54 ["COPY", "register:4040:8", ["const:c0f000:8"]]
- 00a91d54 bytes e80b00b0
+ 00a91d54 bytes e80b00d0
- 00a91d58 ["COPY", "tmp:0:8", ["const:f58:8"]]
- 00a91d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91d58 ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00a91d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91d58 bytes 08613d91
+ 00a91d58 bytes 08210091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28f744d650d02d406029fe1051aaa88a"></a>

### [`00a91dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dd8.md) → [`00a91dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dd8.md) FUN_00a91dd8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91dec",
      "incomplete_value": false,
      "site": "00a91df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91dec",
      "incomplete_value": false,
      "site": "00a91df0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
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
      "00a91df0",
      "DATA",
      [
        "storage",
        "00c0efd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91df0",
      "DATA",
      [
        "storage",
        "00c0f088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dd8.md#insn-00a91de8) · [`00a91dec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dd8.md#insn-00a91dec)
- 新版 `00a91de8`（命令位置の公開資料なし） · `00a91dec`（命令位置の公開資料なし）

~~~diff
- 00a91de8 ["COPY", "register:4040:8", ["const:c0e000:8"]]
+ 00a91de8 ["COPY", "register:4040:8", ["const:c0f000:8"]]
- 00a91de8 bytes e80b00b0
+ 00a91de8 bytes e80b00d0
- 00a91dec ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00a91dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91dec ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00a91dec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91dec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91dec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91dec bytes 08613f91
+ 00a91dec bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b5188d7bbcf90296fdee3428f0996b2"></a>

### [`00a91dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dfc.md) → [`00a91dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91dfc.md) FUN_00a91dfc

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
      "definition_site": "00a91e00",
      "incomplete_value": false,
      "site": "00a91e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91e00",
      "incomplete_value": false,
      "site": "00a91e04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0e000:8"
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
      "00a91e04",
      "DATA",
      [
        "storage",
        "00c0efd8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91e04",
      "DATA",
      [
        "storage",
        "00c0f088",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dfc.md#insn-00a91dfc) · [`00a91e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91dfc.md#insn-00a91e00)
- 新版 `00a91dfc`（命令位置の公開資料なし） · `00a91e00`（命令位置の公開資料なし）

~~~diff
- 00a91dfc ["COPY", "register:4040:8", ["const:c0e000:8"]]
+ 00a91dfc ["COPY", "register:4040:8", ["const:c0f000:8"]]
- 00a91dfc bytes e80b00b0
+ 00a91dfc bytes e80b00d0
- 00a91e00 ["COPY", "tmp:0:8", ["const:fd8:8"]]
- 00a91e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91e00 ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00a91e00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91e00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91e00 bytes 08613f91
+ 00a91e00 bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7182a06ea2e7fa977326339cb2a25e27"></a>

### [`00a91f30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91f30.md) → [`00a91f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f30.md) FUN_00a91f30

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a91f44",
      "incomplete_value": false,
      "site": "00a91f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91f44",
      "incomplete_value": false,
      "site": "00a91f48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00a91f48",
      "DATA",
      [
        "storage",
        "00c0f058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91f48",
      "DATA",
      [
        "storage",
        "00c0f108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91f44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91f30.md#insn-00a91f44)
- 新版 `00a91f44`（命令位置の公開資料なし）

~~~diff
- 00a91f44 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00a91f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91f44 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00a91f44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91f44 bytes 08610191
+ 00a91f44 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17b6a3948efc315723dcf4f9e02aae8c"></a>

### [`00a91f54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91f54.md) → [`00a91f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a91/00a91f54.md) FUN_00a91f54

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
      "definition_site": "00a91f58",
      "incomplete_value": false,
      "site": "00a91f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a91f58",
      "incomplete_value": false,
      "site": "00a91f5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
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
      "00a91f5c",
      "DATA",
      [
        "storage",
        "00c0f058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a91f5c",
      "DATA",
      [
        "storage",
        "00c0f108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a91f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a91/00a91f54.md#insn-00a91f58)
- 新版 `00a91f58`（命令位置の公開資料なし）

~~~diff
- 00a91f58 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00a91f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a91f58 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00a91f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a91f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a91f58 bytes 08610191
+ 00a91f58 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16999f44da12750b640046e811de6f3d"></a>

### [`00a9204c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a9204c.md) → [`00a9204c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a9204c.md) FUN_00a9204c

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
      "definition_site": "00a9206c",
      "incomplete_value": false,
      "site": "00a92070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a9206c",
      "incomplete_value": false,
      "site": "00a92070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "00a92070",
      "DATA",
      [
        "storage",
        "00c0f0d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a92070",
      "DATA",
      [
        "storage",
        "00c0f188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a9206c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a9204c.md#insn-00a9206c)
- 新版 `00a9206c`（命令位置の公開資料なし）

~~~diff
- 00a9206c ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00a9206c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a9206c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a9206c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a9206c ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00a9206c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9206c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a9206c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a9206c bytes 08610391
+ 00a9206c bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-010b3eb600dc4eeb0bb9621c20de6160"></a>

### [`00a92084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92084.md) → [`00a92084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92084.md) FUN_00a92084

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
      "definition_site": "00a92088",
      "incomplete_value": false,
      "site": "00a9208c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:188:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92088",
      "incomplete_value": false,
      "site": "00a9208c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "00a9208c",
      "DATA",
      [
        "storage",
        "00c0f0d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9208c",
      "DATA",
      [
        "storage",
        "00c0f188",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92084.md#insn-00a92088)
- 新版 `00a92088`（命令位置の公開資料なし）

~~~diff
- 00a92088 ["COPY", "tmp:0:8", ["const:d8:8"]]
- 00a92088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a92088 ["COPY", "tmp:0:8", ["const:188:8"]]
+ 00a92088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92088 bytes 08610391
+ 00a92088 bytes 08210691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9554501148bac6779b94156a18ab0685"></a>

### [`00a920a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a920a4.md) → [`00a920a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a920a4.md) FUN_00a920a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 19件 [`00444c54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00446/004460b0.md)
- 新版 呼出元 0件  · 呼出先 19件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044507c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044507c.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.19% / 新版 97.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00a923d8",
      "incomplete_value": true,
      "site": "00a923d8",
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
      "definition_site": "00a923d8",
      "incomplete_value": true,
      "site": "00a923d8",
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a922b0",
      "incomplete_value": true,
      "site": "00a922c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a922b0",
      "incomplete_value": true,
      "site": "00a922c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:9b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00a922d4",
      "incomplete_value": true,
      "site": "00a922f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a922d4",
      "incomplete_value": true,
      "site": "00a922f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:9b8:8"
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
      "00a922b0",
      "READ",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00a922b4",
      "PARAM",
      [
        "storage",
        "00be8d98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a922b8",
      "PARAM",
      [
        "storage",
        "00c0de30",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00a922b0",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00a922b4",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00a922b8",
      "PARAM",
      [
        "storage",
        "00c0dee0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a921d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a920a4.md#insn-00a921d4) · [`00a921dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a920a4.md#insn-00a921dc)
- 新版 `00a921d4`（命令位置の公開資料なし） · `00a921dc`（命令位置の公開資料なし）

~~~diff
- 00a921d4 ["COPY", "tmp:0:8", ["const:d98:8"]]
- 00a921d4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00a921d4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00a921d4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00a921d4 ["COPY", "tmp:0:8", ["const:e48:8"]]
+ 00a921d4 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a921d4 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00a921d4 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00a921d4 bytes 18633691
+ 00a921d4 bytes 18233991
- 00a921dc ["COPY", "register:40c8:8", ["const:c0d000:8"]]
- 00a921dc bytes d90b00f0
+ 00a921dc ["COPY", "register:40c8:8", ["const:c0d000:8"]]
+ 00a921dc bytes d90b00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba6bde4512ff0db20837efa4a89943cd"></a>

### [`00a92660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92660.md) → [`00a92660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92660.md) FUN_00a92660

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

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
      "definition_site": "00a92674",
      "incomplete_value": false,
      "site": "00a92678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92674",
      "incomplete_value": false,
      "site": "00a92678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00a92678",
      "DATA",
      [
        "storage",
        "00c0f158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a92678",
      "DATA",
      [
        "storage",
        "00c0f208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92660.md#insn-00a92674)
- 新版 `00a92674`（命令位置の公開資料なし）

~~~diff
- 00a92674 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00a92674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a92674 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00a92674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92674 bytes 08610591
+ 00a92674 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8097850eebf9b0ac1c888b512fb423b3"></a>

### [`00a92684`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92684.md) → [`00a92684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92684.md) FUN_00a92684

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
      "definition_site": "00a92688",
      "incomplete_value": false,
      "site": "00a9268c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:208:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a92688",
      "incomplete_value": false,
      "site": "00a9268c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "00a9268c",
      "DATA",
      [
        "storage",
        "00c0f158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00a9268c",
      "DATA",
      [
        "storage",
        "00c0f208",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00a92688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92684.md#insn-00a92688)
- 新版 `00a92688`（命令位置の公開資料なし）

~~~diff
- 00a92688 ["COPY", "tmp:0:8", ["const:158:8"]]
- 00a92688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00a92688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00a92688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00a92688 ["COPY", "tmp:0:8", ["const:208:8"]]
+ 00a92688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00a92688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00a92688 bytes 08610591
+ 00a92688 bytes 08210891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-696c2d62d5b54db33d4f31a7d15dc77b"></a>

### [`00a92704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92704.md) → [`00a92704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92704.md) _INIT_240

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
      "definition_site": "00a92740",
      "incomplete_value": true,
      "site": "00a9275c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92740",
      "incomplete_value": true,
      "site": "00a9275c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92764",
      "incomplete_value": true,
      "site": "00a92780",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92764",
      "incomplete_value": true,
      "site": "00a92780",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92784",
      "incomplete_value": true,
      "site": "00a927a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92784",
      "incomplete_value": true,
      "site": "00a927a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a92740",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a92764",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a92784",
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
      "00a92740",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a92764",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a92784",
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

- 旧版 [`00a92730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92704.md#insn-00a92730) · [`00a92738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92704.md#insn-00a92738)
- 新版 `00a92730`（命令位置の公開資料なし） · `00a92738`（命令位置の公開資料なし）

~~~diff
- 00a92730 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00a92730 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a92730 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a92730 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a92730 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00a92730 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a92730 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a92730 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a92730 bytes 73422591
+ 00a92730 bytes 73422891
- 00a92738 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a92738 bytes a9c0ffb0
+ 00a92738 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a92738 bytes a9c0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-efa510e3764e1b46baf1c0cc23879a04"></a>

### [`00a92a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92a94.md) → [`00a92a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a92/00a92a94.md) _INIT_241

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
      "definition_site": "00a92ad0",
      "incomplete_value": true,
      "site": "00a92aec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92ad0",
      "incomplete_value": true,
      "site": "00a92aec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92af4",
      "incomplete_value": true,
      "site": "00a92b10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92af4",
      "incomplete_value": true,
      "site": "00a92b10",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92b14",
      "incomplete_value": true,
      "site": "00a92b30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a92b14",
      "incomplete_value": true,
      "site": "00a92b30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a92ad0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a92af4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a92b14",
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
      "00a92ad0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a92af4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a92b14",
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

- 旧版 [`00a92ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92a94.md#insn-00a92ac0) · [`00a92ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a92/00a92a94.md#insn-00a92ac8)
- 新版 `00a92ac0`（命令位置の公開資料なし） · `00a92ac8`（命令位置の公開資料なし）

~~~diff
- 00a92ac0 ["COPY", "tmp:0:8", ["const:968:8"]]
- 00a92ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a92ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a92ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a92ac0 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 00a92ac0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a92ac0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a92ac0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a92ac0 bytes 73a22591
+ 00a92ac0 bytes 73a22891
- 00a92ac8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a92ac8 bytes a9c0ffb0
+ 00a92ac8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a92ac8 bytes a9c0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11c564f29011cd91251ea16a31ce5896"></a>

### [`00a93b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a93/00a93b78.md) → [`00a93b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a93/00a93b78.md) _INIT_242

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.09% / 新版 92.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00a93c34",
      "incomplete_value": true,
      "site": "00a93c50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00a93c34",
      "incomplete_value": true,
      "site": "00a93c50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e1:8"
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
      "definition_site": "00a93da0",
      "incomplete_value": false,
      "site": "00a93dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00a93da0",
      "incomplete_value": false,
      "site": "00a93dac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109f000:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00a93da8",
      "incomplete_value": false,
      "site": "00a93dac",
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
    "old": {
      "definition_site": "00a93da8",
      "incomplete_value": false,
      "site": "00a93dac",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00a93bb4",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a93bd8",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a93bf8",
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
      "00a93bb4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a93bd8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a93bf8",
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

- 旧版 [`00a93ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a93/00a93b78.md#insn-00a93ba4) · [`00a93bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a93/00a93b78.md#insn-00a93bac)
- 新版 `00a93ba4`（命令位置の公開資料なし） · `00a93bac`（命令位置の公開資料なし）

~~~diff
- 00a93ba4 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00a93ba4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a93ba4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a93ba4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a93ba4 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00a93ba4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a93ba4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a93ba4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a93ba4 bytes 73022691
+ 00a93ba4 bytes 73022991
- 00a93bac ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a93bac bytes a9c0ff90
+ 00a93bac ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a93bac bytes a9c0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f4aab284de33708c45988f15fd1be8"></a>

### [`00a9e66c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9e/00a9e66c.md) → [`00a9e66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9e/00a9e66c.md) _INIT_243

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
      "definition_site": "00a9e6a8",
      "incomplete_value": true,
      "site": "00a9e6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a9e6a8",
      "incomplete_value": true,
      "site": "00a9e6c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a9e6cc",
      "incomplete_value": true,
      "site": "00a9e6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a9e6cc",
      "incomplete_value": true,
      "site": "00a9e6e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a9e6ec",
      "incomplete_value": true,
      "site": "00a9e708",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00a9e6ec",
      "incomplete_value": true,
      "site": "00a9e708",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00a9e6a8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00a9e6cc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00a9e6ec",
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
      "00a9e6a8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00a9e6cc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00a9e6ec",
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

- 旧版 [`00a9e698`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9e/00a9e66c.md#insn-00a9e698) · [`00a9e6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9e/00a9e66c.md#insn-00a9e6a0)
- 新版 `00a9e698`（命令位置の公開資料なし） · `00a9e6a0`（命令位置の公開資料なし）

~~~diff
- 00a9e698 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00a9e698 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00a9e698 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00a9e698 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00a9e698 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00a9e698 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00a9e698 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00a9e698 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00a9e698 bytes 73622691
+ 00a9e698 bytes 73622991
- 00a9e6a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00a9e6a0 bytes 49c0ffb0
+ 00a9e6a0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00a9e6a0 bytes 49c0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e391112656ea764285ca099924a0bd0"></a>

### [`00aa76f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa76f4.md) → [`00aa76f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa76f4.md) _INIT_244

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00aa7730",
      "incomplete_value": true,
      "site": "00aa774c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa7730",
      "incomplete_value": true,
      "site": "00aa774c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa7794",
      "incomplete_value": true,
      "site": "00aa77ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:73b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa7794",
      "incomplete_value": true,
      "site": "00aa77ac",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6ae:8"
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
      "definition_site": "00aa77b0",
      "incomplete_value": true,
      "site": "00aa77cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00aa77b0",
      "incomplete_value": true,
      "site": "00aa77cc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2e1:8"
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
      "00aa7730",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00aa7754",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00aa7774",
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
      "00aa7730",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aa7754",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aa7774",
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

- 旧版 [`00aa7720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa76f4.md#insn-00aa7720) · [`00aa7728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa76f4.md#insn-00aa7728)
- 新版 `00aa7720`（命令位置の公開資料なし） · `00aa7728`（命令位置の公開資料なし）

~~~diff
- 00aa7720 ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 00aa7720 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00aa7720 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00aa7720 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00aa7720 ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 00aa7720 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00aa7720 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00aa7720 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00aa7720 bytes 73c22691
+ 00aa7720 bytes 73c22991
- 00aa7728 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00aa7728 bytes 09c0ff90
+ 00aa7728 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00aa7728 bytes 09c0ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2cfe5ff3c8733c13da116d86b5f728"></a>

### [`00aa7ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa7ae4.md) → [`00aa7ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa7/00aa7ae4.md) FUN_00aa7ae4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00abf464`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00abf/00abf464.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`00424230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424230.md)
- 新版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 25件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00424230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424230.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.20% / 新版 98.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 7件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aa7b28",
      "incomplete_value": false,
      "site": "00aa7b30",
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
    "old": {
      "definition_site": "00aa7b28",
      "incomplete_value": false,
      "site": "00aa7b30",
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
            "const:c78:8"
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
      "definition_site": "00aa7b94",
      "incomplete_value": true,
      "site": "00aa7b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d65:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa7b94",
      "incomplete_value": true,
      "site": "00aa7b94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
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
      "definition_site": "00aa7e88",
      "incomplete_value": true,
      "site": "00aa7ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aa7e88",
      "incomplete_value": true,
      "site": "00aa7ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 64,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aa7b30",
      "DATA",
      [
        "storage",
        "00be7c78",
        null,
        "undefined *"
      ]
    ],
    [
      "00aa7b90",
      "READ",
      [
        "storage",
        "0029ecd8",
        null,
        "string"
      ]
    ],
    [
      "00aa7e88",
      "READ",
      [
        "storage",
        "002a1cd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aa7b30",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00aa7b90",
      "READ",
      [
        "storage",
        "0029ed65",
        null,
        "string"
      ]
    ],
    [
      "00aa7e88",
      "READ",
      [
        "storage",
        "002a1d60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aa7b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa7ae4.md#insn-00aa7b28) · [`00aa7b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa7ae4.md#insn-00aa7b8c) · [`00aa7e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa7/00aa7ae4.md#insn-00aa7e84)
- 新版 `00aa7b28`（命令位置の公開資料なし） · `00aa7b8c`（命令位置の公開資料なし） · `00aa7e84`（命令位置の公開資料なし）

~~~diff
- 00aa7b28 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00aa7b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa7b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa7b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b28 ["COPY", "tmp:0:8", ["const:d28:8"]]
+ 00aa7b28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa7b28 bytes 08e13191
+ 00aa7b28 bytes 08a13491
- 00aa7b8c ["COPY", "tmp:0:8", ["const:cd8:8"]]
- 00aa7b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aa7b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aa7b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b8c ["COPY", "tmp:0:8", ["const:d65:8"]]
+ 00aa7b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aa7b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aa7b8c bytes 08613391
+ 00aa7b8c bytes 08953591
- 00aa7e84 ["COPY", "tmp:0:8", ["const:cd3:8"]]
- 00aa7e84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00aa7e84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00aa7e84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00aa7e84 ["COPY", "tmp:0:8", ["const:d60:8"]]
+ 00aa7e84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00aa7e84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00aa7e84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00aa7e84 bytes 4a4d3391
+ 00aa7e84 bytes 4a813591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bebaffc7cbc79bdc87c2c2115d22d7ec"></a>

### [`00aa9390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9390.md) → [`00aa9390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa9390.md) _INIT_245

採用 · 移動量 `+0x0` · 根拠 `relaxed_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

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
      "definition_site": "00aa93cc",
      "incomplete_value": true,
      "site": "00aa93e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa93cc",
      "incomplete_value": true,
      "site": "00aa93e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa93f0",
      "incomplete_value": true,
      "site": "00aa940c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa93f0",
      "incomplete_value": true,
      "site": "00aa940c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa9410",
      "incomplete_value": true,
      "site": "00aa942c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00aa9410",
      "incomplete_value": true,
      "site": "00aa942c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00aa93cc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00aa93f0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00aa9410",
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
      "00aa93cc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00aa93f0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00aa9410",
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

- 旧版 [`00aa93bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9390.md#insn-00aa93bc) · [`00aa93c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa9390.md#insn-00aa93c4)
- 新版 `00aa93bc`（命令位置の公開資料なし） · `00aa93c4`（命令位置の公開資料なし）

~~~diff
- 00aa93bc ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 00aa93bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00aa93bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00aa93bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00aa93bc ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 00aa93bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00aa93bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00aa93bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00aa93bc bytes 73222791
+ 00aa93bc bytes 73222a91
- 00aa93c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00aa93c4 bytes e9bfffd0
+ 00aa93c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00aa93c4 bytes e9bfffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-adf25f5da3c7278699597717267d7070"></a>

### [`00aab67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md) → [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) FUN_00aab744

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`00a90740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a90/00a90740.md) [`00aad110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad110.md) [`00aad22c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad22c.md) · 呼出先 32件 [`0044ac1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00883/00883e08.md)
- 新版 呼出元 4件 [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00a90740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a90/00a90740.md) [`00aad1d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad1d8.md) [`00aad2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad2f4.md) · 呼出先 32件 [`0044ac1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044ac1c.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.32% / 新版 95.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aab7a8",
      "incomplete_value": false,
      "site": "00aab7a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab6e0",
      "incomplete_value": false,
      "site": "00aab6e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "definition_site": "00aab7e0",
      "incomplete_value": false,
      "site": "00aab7e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:408:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab718",
      "incomplete_value": false,
      "site": "00aab718",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:358:8"
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
      "definition_site": "00aab800",
      "incomplete_value": false,
      "site": "00aab800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:488:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aab738",
      "incomplete_value": false,
      "site": "00aab738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "00aab7a8",
      "DATA",
      [
        "storage",
        "00c0f1d8",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab7e0",
      "DATA",
      [
        "storage",
        "00c0f358",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab800",
      "DATA",
      [
        "storage",
        "00c0f3d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aab7a8",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab7e0",
      "DATA",
      [
        "storage",
        "00c0f408",
        null,
        "undefined *"
      ]
    ],
    [
      "00aab800",
      "DATA",
      [
        "storage",
        "00c0f488",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aaba8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md#insn-00aaba8c) · [`00aab6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md#insn-00aab6c8) · [`00aab6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md#insn-00aab6d0)
- 新版 `00aabb54`（命令位置の公開資料なし） · `00aab790`（命令位置の公開資料なし） · `00aab798`（命令位置の公開資料なし）

~~~diff
- 00aaba8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aaba8c ["INT_ADD", "register:40f0:8", ["const:aaba8c:8", "const:4:8"]]
- 00aaba8c ["CALLIND", null, ["register:0:8"]]
+ 00aabb54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aabb54 ["INT_ADD", "register:40f0:8", ["const:aabb54:8", "const:4:8"]]
+ 00aabb54 ["CALLIND", null, ["register:0:8"]]
- 00aaba8c bytes 00013fd6
+ 00aabb54 bytes 00013fd6
- 00aab6c8 ["INT_ADD", "register:40f0:8", ["const:aab6c8:8", "const:4:8"]]
- 00aab6c8 ["CALL", null, ["callee:00aab5e0:8"]]
+ 00aab790 ["INT_ADD", "register:40f0:8", ["const:aab790:8", "const:4:8"]]
+ 00aab790 ["CALL", null, ["callee:00aab5e0:8"]]
- 00aab6c8 bytes 94ffff97
+ 00aab790 bytes 94ffff97
- 00aab6d0 ["INT_ADD", "register:40f0:8", ["const:aab6d0:8", "const:4:8"]]
- 00aab6d0 ["CALL", null, ["callee:0081f580:8"]]
+ 00aab798 ["INT_ADD", "register:40f0:8", ["const:aab798:8", "const:4:8"]]
+ 00aab798 ["CALL", null, ["callee:0081f580:8"]]
- 00aab6d0 bytes accff597
+ 00aab798 bytes 7acff597
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfb2c5c8f633b961d378368aa60ec38"></a>

### [`00aabd3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md) → [`00aabe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md) FUN_00aabe04

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00aab67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aab67c.md) [`00aad8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aad8d8.md) [`00aada14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md) · 呼出先 20件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00469/00469f7c.md)
- 新版 呼出元 3件 [`00aab744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aab744.md) [`00aad9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aad9a0.md) [`00aadadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aad/00aadadc.md) · 呼出先 20件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.75% / 新版 91.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aac0c0",
      "incomplete_value": false,
      "site": "00aac0c0",
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
    "old": {
      "definition_site": "00aabff8",
      "incomplete_value": false,
      "site": "00aabff8",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aac0c4",
      "incomplete_value": false,
      "site": "00aac0c4",
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
    "old": {
      "definition_site": "00aabffc",
      "incomplete_value": false,
      "site": "00aabffc",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00aac0c0",
      "incomplete_value": false,
      "site": "00aac0c4",
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
    "old": {
      "definition_site": "00aabff8",
      "incomplete_value": false,
      "site": "00aabffc",
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
                "const:c24000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
      "00aabf74",
      "READ",
      [
        "storage",
        "002a77c6",
        null,
        "string"
      ]
    ],
    [
      "00aabfa0",
      "READ",
      [
        "storage",
        "00c24f78",
        null,
        "undefined1"
      ]
    ],
    [
      "00aabfe4",
      "PARAM",
      [
        "storage",
        "00c24f40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aabf74",
      "READ",
      [
        "storage",
        "002a7732",
        null,
        "string"
      ]
    ],
    [
      "00aabfa0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00aabfe4",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aabf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md#insn-00aabf24) · [`00aabfd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md#insn-00aabfd4) · [`00aac010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aab/00aabd3c.md#insn-00aac010)
- 新版 `00aabfec`（命令位置の公開資料なし） · `00aac09c`（命令位置の公開資料なし） · `00aac0d8`（命令位置の公開資料なし）

~~~diff
- 00aabf24 ["INT_ADD", "register:40f0:8", ["const:aabf24:8", "const:4:8"]]
- 00aabf24 ["CALL", null, ["callee:0045b734:8"]]
+ 00aabfec ["INT_ADD", "register:40f0:8", ["const:aabfec:8", "const:4:8"]]
+ 00aabfec ["CALL", null, ["callee:0045b734:8"]]
- 00aabf24 bytes 04bee697
+ 00aabfec bytes d2bde697
- 00aabfd4 ["INT_ADD", "register:40f0:8", ["const:aabfd4:8", "const:4:8"]]
- 00aabfd4 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00aac09c ["INT_ADD", "register:40f0:8", ["const:aac09c:8", "const:4:8"]]
+ 00aac09c ["CALL", null, ["callee:00bdafb0:8"]]
- 00aabfd4 bytes cbbb0494
+ 00aac09c bytes c5bb0494
- 00aac010 ["INT_ADD", "register:40f0:8", ["const:aac010:8", "const:4:8"]]
- 00aac010 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00aac0d8 ["INT_ADD", "register:40f0:8", ["const:aac0d8:8", "const:4:8"]]
+ 00aac0d8 ["CALL", null, ["callee:00bdaf90:8"]]
- 00aac010 bytes b4bb0494
+ 00aac0d8 bytes aebb0494
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bb543e2d1955d51490b7ec32d5dcb70"></a>

### [`00aaca64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca64.md) → [`00aacb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb2c.md) FUN_00aacb2c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00aac858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aac858.md) [`00aaca8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca8c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00aac920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aac920.md) [`00aacb54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb54.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00aacb38",
      "incomplete_value": false,
      "site": "00aacb3c",
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
      "definition_site": "00aaca70",
      "incomplete_value": false,
      "site": "00aaca74",
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
      "00aacb38",
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
      "00aacb38",
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

- 旧版 [`00aaca74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca64.md#insn-00aaca74) · [`00aaca70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca64.md#insn-00aaca70)
- 新版 `00aacb3c`（命令位置の公開資料なし） · `00aacb38`（命令位置の公開資料なし）

~~~diff
- 00aaca74 ["INT_ADD", "register:40f0:8", ["const:aaca74:8", "const:4:8"]]
- 00aaca74 ["CALL", null, ["callee:00418c38:8"]]
+ 00aacb3c ["INT_ADD", "register:40f0:8", ["const:aacb3c:8", "const:4:8"]]
+ 00aacb3c ["CALL", null, ["callee:00418c38:8"]]
- 00aaca74 bytes 71b0e597
+ 00aacb3c bytes 3fb0e597
- 00aaca70 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00aaca70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aaca70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aaca70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aacb38 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00aacb38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aaca70 bytes 00280c91
+ 00aacb38 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81a0fa6db9335e628f5918bc44df7e1f"></a>

### [`00aaca78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca78.md) → [`00aacb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacb40.md) FUN_00aacb40

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00aa980c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aa9/00aa980c.md) [`00aaaedc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00aa980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aa9/00aa980c.md) [`00aaafa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00aacb4c",
      "incomplete_value": false,
      "site": "00aacb50",
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
      "definition_site": "00aaca84",
      "incomplete_value": false,
      "site": "00aaca88",
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
      "00aacb4c",
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
      "00aacb4c",
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

- 旧版 [`00aaca88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca78.md#insn-00aaca88) · [`00aaca84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aaca78.md#insn-00aaca84)
- 新版 `00aacb50`（命令位置の公開資料なし） · `00aacb4c`（命令位置の公開資料なし）

~~~diff
- 00aaca88 ["INT_ADD", "register:40f0:8", ["const:aaca88:8", "const:4:8"]]
- 00aaca88 ["CALL", null, ["callee:00418c38:8"]]
+ 00aacb50 ["INT_ADD", "register:40f0:8", ["const:aacb50:8", "const:4:8"]]
+ 00aacb50 ["CALL", null, ["callee:00418c38:8"]]
- 00aaca88 bytes 6cb0e597
+ 00aacb50 bytes 3ab0e597
- 00aaca84 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00aaca84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aaca84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aaca84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aacb4c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00aacb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aacb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aaca84 bytes 00280c91
+ 00aacb4c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27c6bfe84a87915662fff5ca23b99979"></a>

### [`00aacc1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc1c.md) → [`00aacce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacce4.md) FUN_00aacce4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aacd08",
      "incomplete_value": false,
      "site": "00aacd0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aacc40",
      "incomplete_value": false,
      "site": "00aacc44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "00aacd0c",
      "DATA",
      [
        "storage",
        "00c0f1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aacd0c",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aacc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc1c.md#insn-00aacc30) · [`00aacc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc1c.md#insn-00aacc40)
- 新版 `00aaccf8`（命令位置の公開資料なし） · `00aacd08`（命令位置の公開資料なし）

~~~diff
- 00aacc30 ["INT_ADD", "register:40f0:8", ["const:aacc30:8", "const:4:8"]]
- 00aacc30 ["CALL", null, ["callee:00bdaff0:8"]]
+ 00aaccf8 ["INT_ADD", "register:40f0:8", ["const:aaccf8:8", "const:4:8"]]
+ 00aaccf8 ["CALL", null, ["callee:00bdaff0:8"]]
- 00aacc30 bytes c4b80494
+ 00aaccf8 bytes beb80494
- 00aacc40 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00aacc40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aacc40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aacc40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aacd08 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00aacd08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aacc40 bytes 08610791
+ 00aacd08 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9daa53850c7a5056ea8693ac8c51323c"></a>

### [`00aacc5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc5c.md) → [`00aacd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aac/00aacd24.md) FUN_00aacd24

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

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
      "definition_site": "00aacd28",
      "incomplete_value": false,
      "site": "00aacd2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:288:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aacc60",
      "incomplete_value": false,
      "site": "00aacc64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0f000:8"
          ],
          [
            "leaf",
            "const:1d8:8"
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
      "00aacd2c",
      "DATA",
      [
        "storage",
        "00c0f1d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00aacd2c",
      "DATA",
      [
        "storage",
        "00c0f288",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aacc60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc5c.md#insn-00aacc60)
- 新版 `00aacd28`（命令位置の公開資料なし）

~~~diff
- 00aacc60 ["COPY", "tmp:0:8", ["const:1d8:8"]]
- 00aacc60 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aacc60 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aacc60 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aacd28 ["COPY", "tmp:0:8", ["const:288:8"]]
+ 00aacd28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aacd28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aacc60 bytes 08610791
+ 00aacd28 bytes 08210a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

