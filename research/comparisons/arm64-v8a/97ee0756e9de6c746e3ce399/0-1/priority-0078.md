# v15.7.2 → v15.7.3 · 最優先の変更候補 (78)

[一覧の目次](README.md)

<a id="compare-0c00618870eee04a297e6d4bbe09df11"></a>

### [`00bab284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab284.md) → [`00bab34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bdd920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd920.md) [`00be1700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1700.md) · 呼出先 3件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 2件 [`00bdd9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9d0.md) [`00be17b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17b0.md) · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 62.86% / 新版 62.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bab374",
      "incomplete_value": true,
      "site": "00bab374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bab2ac",
      "incomplete_value": true,
      "site": "00bab2ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bab388",
      "incomplete_value": true,
      "site": "00bab38c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab2c0",
      "incomplete_value": true,
      "site": "00bab2c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bab3c4",
      "incomplete_value": true,
      "site": "00bab3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab2fc",
      "incomplete_value": true,
      "site": "00bab2fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bab368",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bab374",
      "DATA",
      [
        "storage",
        "00c13a18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab380",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bab368",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bab374",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab380",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab284.md#insn-00bab2e0) · [`00bab2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab284.md#insn-00bab2f8) · [`00bab2fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab284.md#insn-00bab2fc)
- 新版 [`00bab3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab3a8) · [`00bab3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab3c0) · [`00bab3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab3c4)

~~~diff
- 00bab2e0 ["INT_ADD", "register:40f0:8", ["const:bab2e0:8", "const:4:8"]]
- 00bab2e0 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bab3a8 ["INT_ADD", "register:40f0:8", ["const:bab3a8:8", "const:4:8"]]
+ 00bab3a8 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bab2e0 bytes 08bf0094
+ 00bab3a8 bytes 02bf0094
- 00bab2f8 ["INT_ADD", "register:40f0:8", ["const:bab2f8:8", "const:4:8"]]
- 00bab2f8 ["CALL", null, ["callee:00be1520:8"]]
+ 00bab3c0 ["INT_ADD", "register:40f0:8", ["const:bab3c0:8", "const:4:8"]]
+ 00bab3c0 ["CALL", null, ["callee:00be1520:8"]]
- 00bab2f8 bytes 5ed80094
+ 00bab3c0 bytes 58d80094
- 00bab2fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:890:8"]]
- 00bab2fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bab3c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00bab3c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bab2fc bytes 804a04f9
+ 00bab3c4 bytes 80aa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-786de0e495fceb467e996b727a7783d5"></a>

### [`00bab330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab330.md) → [`00bab3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC2EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1770.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00be1820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1820.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bab424",
      "incomplete_value": true,
      "site": "00bab424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bab35c",
      "incomplete_value": true,
      "site": "00bab35c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bab460",
      "incomplete_value": false,
      "site": "00bab470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:267:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab398",
      "incomplete_value": false,
      "site": "00bab3a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:1da:8"
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
      "00bab418",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bab424",
      "DATA",
      [
        "storage",
        "00c13a18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab460",
      "PARAM",
      [
        "storage",
        "0029c1da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bab418",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bab424",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab460",
      "PARAM",
      [
        "storage",
        "0029c267",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab330.md#insn-00bab3a8) · [`00bab350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab330.md#insn-00bab350) · [`00bab368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bab/00bab330.md#insn-00bab368)
- 新版 [`00bab470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab470) · [`00bab418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab418) · [`00bab430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab430)

~~~diff
- 00bab3a8 ["INT_ADD", "register:40f0:8", ["const:bab3a8:8", "const:4:8"]]
- 00bab3a8 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bab470 ["INT_ADD", "register:40f0:8", ["const:bab470:8", "const:4:8"]]
+ 00bab470 ["CALL", null, ["callee:00ba8a80:8"]]
- 00bab3a8 bytes 84f5ff97
+ 00bab470 bytes 84f5ff97
- 00bab350 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb0:8"]]
- 00bab350 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bab418 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
+ 00bab418 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bab350 bytes 085947f9
+ 00bab418 bytes 08b147f9
- 00bab368 ["INT_ADD", "register:40f0:8", ["const:bab368:8", "const:4:8"]]
- 00bab368 ["CALL", null, ["callee:00be1520:8"]]
+ 00bab430 ["INT_ADD", "register:40f0:8", ["const:bab430:8", "const:4:8"]]
+ 00bab430 ["CALL", null, ["callee:00be1520:8"]]
- 00bab368 bytes 42d80094
+ 00bab430 bytes 3cd80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13f503b96f9a6f65ff90ffece5b7255a"></a>

### [`00baeef0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baeef0.md) → [`00baefb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md) _ZNSt6__ndk18numpunctIcEC2Em

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1710.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be17c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17c0.md) · 呼出先 0件 

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
      "definition_site": "00baefdc",
      "incomplete_value": true,
      "site": "00baefdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00baef14",
      "incomplete_value": true,
      "site": "00baef14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00baefc4",
      "READ",
      [
        "storage",
        "00c1beb8",
        null,
        "pointer"
      ]
    ],
    [
      "00baefdc",
      "DATA",
      [
        "storage",
        "00c13a78",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baefc4",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00baefdc",
      "DATA",
      [
        "storage",
        "00c13b28",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baeefc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baeef0.md#insn-00baeefc)
- 新版 [`00baefc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md#insn-00baefc4)

~~~diff
- 00baeefc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:eb8:8"]]
- 00baeefc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baefc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f68:8"]]
+ 00baefc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baeefc bytes 295d47f9
+ 00baefc4 bytes 29b547f9
~~~


<a id="compare-14d07852d06e763fa0478f0bbe72669d"></a>

### [`00baef1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baef1c.md) → [`00baefe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefe4.md) _ZNSt6__ndk18numpunctIwEC2Em

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1720.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be17d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17d0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baf00c",
      "incomplete_value": true,
      "site": "00baf00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00baef44",
      "incomplete_value": true,
      "site": "00baef44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00baeff4",
      "READ",
      [
        "storage",
        "00c1bec0",
        null,
        "pointer"
      ]
    ],
    [
      "00baf00c",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baeff4",
      "READ",
      [
        "storage",
        "00c1bf70",
        null,
        "pointer"
      ]
    ],
    [
      "00baf00c",
      "DATA",
      [
        "storage",
        "00c13b78",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baef2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bae/00baef1c.md#insn-00baef2c)
- 新版 [`00baeff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefe4.md#insn-00baeff4)

~~~diff
- 00baef2c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec0:8"]]
- 00baef2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baeff4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f70:8"]]
+ 00baeff4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baef2c bytes 296147f9
+ 00baeff4 bytes 29b947f9
~~~


<a id="compare-a5789d0502ff4472ef5b369ba374c6b5"></a>

### [`00baf24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf24c.md) → [`00baf314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baf348",
      "incomplete_value": true,
      "site": "00baf348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00baf280",
      "incomplete_value": true,
      "site": "00baf280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00baf33c",
      "READ",
      [
        "storage",
        "00c1bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00baf348",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf33c",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00baf348",
      "DATA",
      [
        "storage",
        "00c13bc8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf274`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf24c.md#insn-00baf274) · [`00baf284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf24c.md#insn-00baf284)
- 新版 [`00baf33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md#insn-00baf33c) · [`00baf34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md#insn-00baf34c)

~~~diff
- 00baf274 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
- 00baf274 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf33c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 00baf33c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baf274 bytes 086547f9
+ 00baf33c bytes 08bd47f9
- 00baf284 ["INT_ADD", "register:40f0:8", ["const:baf284:8", "const:4:8"]]
- 00baf284 ["CALL", null, ["callee:00be1c20:8"]]
+ 00baf34c ["INT_ADD", "register:40f0:8", ["const:baf34c:8", "const:4:8"]]
+ 00baf34c ["CALL", null, ["callee:00be1c20:8"]]
- 00baf284 bytes 3bca0094
+ 00baf34c bytes 35ca0094
~~~


<a id="compare-c9d4f414c076ad8b1ed1afa5d15a08f3"></a>

### [`00baf2ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf2ac.md) → [`00baf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md) _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b70.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baf39c",
      "incomplete_value": false,
      "site": "00baf3a4",
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
            "const:683:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baf2d4",
      "incomplete_value": false,
      "site": "00baf2dc",
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
            "const:68a:8"
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
      "00baf39c",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ],
    [
      "00baf5a0",
      "PARAM",
      [
        "storage",
        "0029999a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baf39c",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "00baf5a0",
      "PARAM",
      [
        "storage",
        "00299a27",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf2dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf2ac.md#insn-00baf2dc) · [`00baf2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf2ac.md#insn-00baf2d4) · [`00baf2f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf2ac.md#insn-00baf2f0)
- 新版 [`00baf3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf3a4) · [`00baf39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf39c) · [`00baf3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf3b8)

~~~diff
- 00baf2dc ["INT_ADD", "register:40f0:8", ["const:baf2dc:8", "const:4:8"]]
- 00baf2dc ["CALL", null, ["callee:00bde980:8"]]
+ 00baf3a4 ["INT_ADD", "register:40f0:8", ["const:baf3a4:8", "const:4:8"]]
+ 00baf3a4 ["CALL", null, ["callee:00bde980:8"]]
- 00baf2dc bytes 7dbd0094
+ 00baf3a4 bytes 77bd0094
- 00baf2d4 ["COPY", "tmp:0:8", ["const:68a:8"]]
- 00baf2d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00baf2d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00baf2d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00baf39c ["COPY", "tmp:0:8", ["const:683:8"]]
+ 00baf39c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf39c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf39c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00baf2d4 bytes 21281a91
+ 00baf39c bytes 210c1a91
- 00baf2f0 ["INT_ADD", "register:40f0:8", ["const:baf2f0:8", "const:4:8"]]
- 00baf2f0 ["CALL", null, ["callee:00be1520:8"]]
+ 00baf3b8 ["INT_ADD", "register:40f0:8", ["const:baf3b8:8", "const:4:8"]]
+ 00baf3b8 ["CALL", null, ["callee:00be1520:8"]]
- 00baf2f0 bytes 60c80094
+ 00baf3b8 bytes 5ac80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17f27b99f5e32b75bbcf1f9384539816"></a>

### [`00baf580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf580.md) → [`00baf648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md) _ZNSt6__ndk115numpunct_bynameIcEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1780.md) · 呼出先 1件 [`00be1b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1b70.md)
- 新版 呼出元 1件 [`00be1830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1830.md) · 呼出先 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baf67c",
      "incomplete_value": true,
      "site": "00baf67c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00baf5b4",
      "incomplete_value": true,
      "site": "00baf5b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00baf670",
      "READ",
      [
        "storage",
        "00c1bec8",
        null,
        "pointer"
      ]
    ],
    [
      "00baf67c",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf670",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00baf67c",
      "DATA",
      [
        "storage",
        "00c13bc8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf5a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf580.md#insn-00baf5a8) · [`00baf5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf580.md#insn-00baf5c8)
- 新版 [`00baf670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md#insn-00baf670) · [`00baf690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md#insn-00baf690)

~~~diff
- 00baf5a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec8:8"]]
- 00baf5a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 00baf670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baf5a8 bytes 086547f9
+ 00baf670 bytes 08bd47f9
- 00baf5c8 ["INT_ADD", "register:40f0:8", ["const:baf5c8:8", "const:4:8"]]
- 00baf5c8 ["CALL", null, ["callee:00be1c20:8"]]
+ 00baf690 ["INT_ADD", "register:40f0:8", ["const:baf690:8", "const:4:8"]]
+ 00baf690 ["CALL", null, ["callee:00be1c20:8"]]
- 00baf5c8 bytes 6ac90094
+ 00baf690 bytes 64c90094
~~~


<a id="compare-5634a922ac52b4a044010f94aa392883"></a>

### [`00baf6a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf6a8.md) → [`00baf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md) _ZNSt6__ndk115numpunct_bynameIwE6__initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ba0.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00baf61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf61c.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md)
- 新版 呼出元 1件 [`00be1c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c50.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baf8e4",
      "incomplete_value": false,
      "site": "00baf8f4",
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
            "const:9f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baf81c",
      "incomplete_value": false,
      "site": "00baf82c",
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
            "const:12:8"
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
      "00baf798",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ],
    [
      "00baf8e4",
      "PARAM",
      [
        "storage",
        "002a1012",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baf798",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "00baf8e4",
      "PARAM",
      [
        "storage",
        "002a109f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf6a8.md#insn-00baf82c) · [`00baf6d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf6a8.md#insn-00baf6d0) · [`00baf6d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf6a8.md#insn-00baf6d8)
- 新版 [`00baf8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf8f4) · [`00baf798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf798) · [`00baf7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf7a0)

~~~diff
- 00baf82c ["INT_ADD", "register:40f0:8", ["const:baf82c:8", "const:4:8"]]
- 00baf82c ["CALL", null, ["callee:00ba8a80:8"]]
+ 00baf8f4 ["INT_ADD", "register:40f0:8", ["const:baf8f4:8", "const:4:8"]]
+ 00baf8f4 ["CALL", null, ["callee:00ba8a80:8"]]
- 00baf82c bytes 63e4ff97
+ 00baf8f4 bytes 63e4ff97
- 00baf6d0 ["COPY", "tmp:0:8", ["const:68a:8"]]
- 00baf6d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00baf6d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00baf6d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00baf798 ["COPY", "tmp:0:8", ["const:683:8"]]
+ 00baf798 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf798 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf798 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00baf6d0 bytes 21281a91
+ 00baf798 bytes 210c1a91
- 00baf6d8 ["INT_ADD", "register:40f0:8", ["const:baf6d8:8", "const:4:8"]]
- 00baf6d8 ["CALL", null, ["callee:00bde980:8"]]
+ 00baf7a0 ["INT_ADD", "register:40f0:8", ["const:baf7a0:8", "const:4:8"]]
+ 00baf7a0 ["CALL", null, ["callee:00bde980:8"]]
- 00baf6d8 bytes 7ebc0094
+ 00baf7a0 bytes 78bc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3443b2096fbdb04f33987723463bd0bb"></a>

### [`00bafaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md) → [`00bafbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bafb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafc18",
      "incomplete_value": false,
      "site": "00bafc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafb50",
      "incomplete_value": false,
      "site": "00bafb50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bafc08",
      "incomplete_value": false,
      "site": "00bafc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafb40",
      "incomplete_value": false,
      "site": "00bafb50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
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
      "definition_site": "00bafbf0",
      "incomplete_value": false,
      "site": "00bafbf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafb28",
      "incomplete_value": false,
      "site": "00bafb2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "00bafbd0",
      "READ",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafbdc",
      "READ",
      [
        "storage",
        "010a2aa0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bafbdc",
      "DATA",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bafbd0",
      "READ",
      [
        "storage",
        "010a2b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafbdc",
      "READ",
      [
        "storage",
        "010a2b60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bafbdc",
      "DATA",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md#insn-00bafb2c) · [`00bafb50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md#insn-00bafb50) · [`00bafb54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md#insn-00bafb54)
- 新版 [`00bafbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md#insn-00bafbf4) · [`00bafc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md#insn-00bafc18) · [`00bafc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md#insn-00bafc1c)

~~~diff
- 00bafb2c ["INT_ADD", "register:40f0:8", ["const:bafb2c:8", "const:4:8"]]
- 00bafb2c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bafbf4 ["INT_ADD", "register:40f0:8", ["const:bafbf4:8", "const:4:8"]]
+ 00bafbf4 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bafb2c bytes f5ac0094
+ 00bafbf4 bytes efac0094
- 00bafb50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa0:8"]]
- 00bafb50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bafc18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
+ 00bafc18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bafb50 bytes 095105f9
+ 00bafc18 bytes 09b105f9
- 00bafb54 ["INT_ADD", "register:40f0:8", ["const:bafb54:8", "const:4:8"]]
- 00bafb54 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bafc1c ["INT_ADD", "register:40f0:8", ["const:bafc1c:8", "const:4:8"]]
+ 00bafc1c ["CALL", null, ["callee:00bdafd0:8"]]
- 00bafb54 bytes f3ac0094
+ 00bafc1c bytes edac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a01776ba3a0480958baf1ea24cebea32"></a>

### [`00bafb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md) → [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) FUN_00bafc28

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bafaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafaf4.md) · 呼出先 4件 [`00bb8c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bafbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md) · 呼出先 4件 [`00bb8cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 26件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafc5c",
      "incomplete_value": false,
      "site": "00bafc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafb94",
      "incomplete_value": false,
      "site": "00bafb94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafc74",
      "incomplete_value": false,
      "site": "00bafc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafbac",
      "incomplete_value": false,
      "site": "00bafbac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "definition_site": "00bafca8",
      "incomplete_value": false,
      "site": "00bafca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafbe0",
      "incomplete_value": false,
      "site": "00bafbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bafc3c",
      "READ",
      [
        "storage",
        "010a2cf0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc48",
      "READ",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc5c",
      "WRITE",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bafc3c",
      "READ",
      [
        "storage",
        "010a2db0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc48",
      "READ",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc5c",
      "WRITE",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md#insn-00bafbcc) · [`00bafc18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md#insn-00bafc18) · [`00bafc74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md#insn-00bafc74)
- 新版 [`00bafc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafc94) · [`00bafce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafce0) · [`00bafd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafd3c)

~~~diff
- 00bafbcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bb8:8"]]
- 00bafbcc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bafbcc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bafc94 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c78:8"]]
+ 00bafc94 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bafc94 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bafbcc bytes 28e16e39
+ 00bafc94 bytes 28e17139
- 00bafc18 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:bd0:8"]]
- 00bafc18 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bafc18 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bafce0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c90:8"]]
+ 00bafce0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bafce0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bafc18 bytes 28416f39
+ 00bafce0 bytes 28417239
- 00bafc74 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00bafc74 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bafc74 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bafc74 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bafd3c ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 00bafd3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafd3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafd3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bafc74 bytes 08a12f91
+ 00bafd3c bytes 08a13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c3f616d05078f80f65c1693d0ee47e5"></a>

### [`00baff98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baff98.md) → [`00bb0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb0018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0018.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb00e0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb00bc",
      "incomplete_value": true,
      "site": "00bb00bc",
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
            "const:b70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafff4",
      "incomplete_value": true,
      "site": "00bafff4",
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
            "const:ab0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb00b0",
      "incomplete_value": false,
      "site": "00bb00bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baffe8",
      "incomplete_value": false,
      "site": "00bafff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:cf8:8"
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
      "definition_site": "00bb009c",
      "incomplete_value": false,
      "site": "00bb00a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baffd4",
      "incomplete_value": false,
      "site": "00baffd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab8:8"
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
      "00bb007c",
      "READ",
      [
        "storage",
        "010a2ab8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0084",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0084",
      "DATA",
      [
        "storage",
        "010a2cf8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb007c",
      "READ",
      [
        "storage",
        "010a2b78",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0084",
      "READ",
      [
        "storage",
        "010a2b70",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0084",
      "DATA",
      [
        "storage",
        "010a2db8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baffd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baff98.md#insn-00baffd8) · [`00baffe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baff98.md#insn-00baffe0) · [`00bafff4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baff98.md#insn-00bafff4)
- 新版 [`00bb00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00a0) · [`00bb00a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00a8) · [`00bb00bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00bc)

~~~diff
- 00baffd8 ["INT_ADD", "register:40f0:8", ["const:baffd8:8", "const:4:8"]]
- 00baffd8 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb00a0 ["INT_ADD", "register:40f0:8", ["const:bb00a0:8", "const:4:8"]]
+ 00bb00a0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00baffd8 bytes caab0094
+ 00bb00a0 bytes c4ab0094
- 00baffe0 ["INT_ADD", "register:40f0:8", ["const:baffe0:8", "const:4:8"]]
- 00baffe0 ["CALL", null, ["ram:bb0018:8"]]
+ 00bb00a8 ["INT_ADD", "register:40f0:8", ["const:bb00a8:8", "const:4:8"]]
+ 00bb00a8 ["CALL", null, ["ram:bb00e0:8"]]
- 00baffe0 bytes 0e000094
+ 00bb00a8 bytes 0e000094
- 00bafff4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab0:8"]]
- 00bafff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb00bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b70:8"]]
+ 00bb00bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bafff4 bytes 685a05f9
+ 00bb00bc bytes 68ba05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7140325df8c290a936d68bd645c507c1"></a>

### [`00bb02ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb02ec.md) → [`00bb03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md) _ZNKSt6__ndk120__time_get_c_storageIcE8__monthsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb0358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0358.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0410",
      "incomplete_value": false,
      "site": "00bb0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0348",
      "incomplete_value": false,
      "site": "00bb0348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ac0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb0400",
      "incomplete_value": false,
      "site": "00bb0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0338",
      "incomplete_value": false,
      "site": "00bb0348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:e50:8"
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
      "definition_site": "00bb03e8",
      "incomplete_value": false,
      "site": "00bb03ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0320",
      "incomplete_value": false,
      "site": "00bb0324",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ac8:8"
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
      "00bb03c8",
      "READ",
      [
        "storage",
        "010a2ac8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb03d4",
      "READ",
      [
        "storage",
        "010a2ac0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb03d4",
      "DATA",
      [
        "storage",
        "010a2e50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb03c8",
      "READ",
      [
        "storage",
        "010a2b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb03d4",
      "READ",
      [
        "storage",
        "010a2b80",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb03d4",
      "DATA",
      [
        "storage",
        "010a2f10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb02ec.md#insn-00bb0324) · [`00bb0348`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb02ec.md#insn-00bb0348) · [`00bb034c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb02ec.md#insn-00bb034c)
- 新版 [`00bb03ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md#insn-00bb03ec) · [`00bb0410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md#insn-00bb0410) · [`00bb0414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md#insn-00bb0414)

~~~diff
- 00bb0324 ["INT_ADD", "register:40f0:8", ["const:bb0324:8", "const:4:8"]]
- 00bb0324 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb03ec ["INT_ADD", "register:40f0:8", ["const:bb03ec:8", "const:4:8"]]
+ 00bb03ec ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb0324 bytes f7aa0094
+ 00bb03ec bytes f1aa0094
- 00bb0348 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ac0:8"]]
- 00bb0348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb0410 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
+ 00bb0410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb0348 bytes 096105f9
+ 00bb0410 bytes 09c105f9
- 00bb034c ["INT_ADD", "register:40f0:8", ["const:bb034c:8", "const:4:8"]]
- 00bb034c ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb0414 ["INT_ADD", "register:40f0:8", ["const:bb0414:8", "const:4:8"]]
+ 00bb0414 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb034c bytes f5aa0094
+ 00bb0414 bytes efaa0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9cbf927769920f23aba97ad5576c44"></a>

### [`00bb0358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0358.md) → [`00bb0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md) FUN_00bb0420

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb02ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb02ec.md) · 呼出先 4件 [`00bb8f04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8f04.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bb03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md) · 呼出先 4件 [`00bb8fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8fcc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.39% / 新版 63.39%

CFGの説明率　旧版 3.81% / 新版 3.81%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 6件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 29件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb038c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb03a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00bb03dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00bb036c",
      "READ",
      [
        "storage",
        "010a3090",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0440",
      "READ",
      [
        "storage",
        "010a2e50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00bb0394"
      ]
    ]
  ],
  "added": [
    [
      "00bb0434",
      "READ",
      [
        "storage",
        "010a3150",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0440",
      "READ",
      [
        "storage",
        "010a2f10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0444",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00bb045c"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0358.md#insn-00bb0378) · [`00bb038c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0358.md#insn-00bb038c) · [`00bb03a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0358.md#insn-00bb03a4)
- 新版 [`00bb0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md#insn-00bb0440)

~~~diff
- 00bb0378 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e50:8"]]
- 00bb0378 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bb0378 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bb0440 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f10:8"]]
+ 00bb0440 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bb0440 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bb0378 bytes 08417939
+ 00bb0440 bytes 08417c39
- 00bb038c ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00bb038c ["COPY", "tmp:1:8", ["register:4040:8"]]
- 00bb038c ["INT_ADD", "register:4040:8", ["register:4040:8", "const:1:8"]]
- 00bb038c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00bb038c bytes 09150038
- 00bb03a4 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00bb03a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00bb03a4 bytes 2a0100f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f412e92c5ea702f1df78b28ee0ec6869"></a>

### [`00bb0a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0a2c.md) → [`00bb0af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md) _ZNKSt6__ndk120__time_get_c_storageIwE8__monthsEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb0aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0aac.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0b74.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0b50",
      "incomplete_value": true,
      "site": "00bb0b50",
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
            "const:b90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0a88",
      "incomplete_value": true,
      "site": "00bb0a88",
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
            "const:ad0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb0b44",
      "incomplete_value": false,
      "site": "00bb0b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0a7c",
      "incomplete_value": false,
      "site": "00bb0a88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:98:8"
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
      "definition_site": "00bb0b30",
      "incomplete_value": false,
      "site": "00bb0b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0a68",
      "incomplete_value": false,
      "site": "00bb0a6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "00bb0b10",
      "READ",
      [
        "storage",
        "010a2ad8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0b18",
      "READ",
      [
        "storage",
        "010a2ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0b18",
      "DATA",
      [
        "storage",
        "010a3098",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb0b10",
      "READ",
      [
        "storage",
        "010a2b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0b18",
      "READ",
      [
        "storage",
        "010a2b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0b18",
      "DATA",
      [
        "storage",
        "010a3158",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0a2c.md#insn-00bb0a6c) · [`00bb0a74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0a2c.md#insn-00bb0a74) · [`00bb0a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0a2c.md#insn-00bb0a88)
- 新版 [`00bb0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b34) · [`00bb0b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b3c) · [`00bb0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b50)

~~~diff
- 00bb0a6c ["INT_ADD", "register:40f0:8", ["const:bb0a6c:8", "const:4:8"]]
- 00bb0a6c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb0b34 ["INT_ADD", "register:40f0:8", ["const:bb0b34:8", "const:4:8"]]
+ 00bb0b34 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb0a6c bytes 25a90094
+ 00bb0b34 bytes 1fa90094
- 00bb0a74 ["INT_ADD", "register:40f0:8", ["const:bb0a74:8", "const:4:8"]]
- 00bb0a74 ["CALL", null, ["ram:bb0aac:8"]]
+ 00bb0b3c ["INT_ADD", "register:40f0:8", ["const:bb0b3c:8", "const:4:8"]]
+ 00bb0b3c ["CALL", null, ["ram:bb0b74:8"]]
- 00bb0a74 bytes 0e000094
+ 00bb0b3c bytes 0e000094
- 00bb0a88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
- 00bb0a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb0b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
+ 00bb0b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb0a88 bytes 686a05f9
+ 00bb0b50 bytes 68ca05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-015047c7824850a991c7a9191a63a7c1"></a>

### [`00bb0fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0fd4.md) → [`00bb109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb1040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1040.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb1108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb10f8",
      "incomplete_value": false,
      "site": "00bb10f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1030",
      "incomplete_value": false,
      "site": "00bb1030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ae0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb10e8",
      "incomplete_value": false,
      "site": "00bb10f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1020",
      "incomplete_value": false,
      "site": "00bb1030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
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
      "definition_site": "00bb10d0",
      "incomplete_value": false,
      "site": "00bb10d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1008",
      "incomplete_value": false,
      "site": "00bb100c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00bb10b0",
      "READ",
      [
        "storage",
        "010a2ae8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb10bc",
      "READ",
      [
        "storage",
        "010a2ae0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb10bc",
      "DATA",
      [
        "storage",
        "010a32e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb10b0",
      "READ",
      [
        "storage",
        "010a2ba8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb10bc",
      "READ",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb10bc",
      "DATA",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb100c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0fd4.md#insn-00bb100c) · [`00bb1030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0fd4.md#insn-00bb1030) · [`00bb1034`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0fd4.md#insn-00bb1034)
- 新版 [`00bb10d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md#insn-00bb10d4) · [`00bb10f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md#insn-00bb10f8) · [`00bb10fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md#insn-00bb10fc)

~~~diff
- 00bb100c ["INT_ADD", "register:40f0:8", ["const:bb100c:8", "const:4:8"]]
- 00bb100c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb10d4 ["INT_ADD", "register:40f0:8", ["const:bb10d4:8", "const:4:8"]]
+ 00bb10d4 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb100c bytes bda70094
+ 00bb10d4 bytes b7a70094
- 00bb1030 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ae0:8"]]
- 00bb1030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb10f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba0:8"]]
+ 00bb10f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb1030 bytes 097105f9
+ 00bb10f8 bytes 09d105f9
- 00bb1034 ["INT_ADD", "register:40f0:8", ["const:bb1034:8", "const:4:8"]]
- 00bb1034 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb10fc ["INT_ADD", "register:40f0:8", ["const:bb10fc:8", "const:4:8"]]
+ 00bb10fc ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb1034 bytes bba70094
+ 00bb10fc bytes b5a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-987063eead0a70b9e6b811a2797a588b"></a>

### [`00bb1040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1040.md) → [`00bb1108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md) FUN_00bb1108

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb0fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb0/00bb0fd4.md) · 呼出先 4件 [`00bb8fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8fa4.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bb109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md) · 呼出先 4件 [`00bb906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb906c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb113c",
      "incomplete_value": false,
      "site": "00bb113c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1074",
      "incomplete_value": false,
      "site": "00bb1074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:2e0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1154",
      "incomplete_value": false,
      "site": "00bb1154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb108c",
      "incomplete_value": false,
      "site": "00bb108c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:2e8:8"
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
      "definition_site": "00bb117c",
      "incomplete_value": false,
      "site": "00bb117c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb10b4",
      "incomplete_value": false,
      "site": "00bb10b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:2f8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb111c",
      "READ",
      [
        "storage",
        "010a3310",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1128",
      "READ",
      [
        "storage",
        "010a32e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb113c",
      "WRITE",
      [
        "storage",
        "010a32e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb111c",
      "READ",
      [
        "storage",
        "010a33d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1128",
      "READ",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb113c",
      "WRITE",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1040.md#insn-00bb1050) · [`00bb10f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1040.md#insn-00bb10f0) · [`00bb110c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1040.md#insn-00bb110c)
- 新版 [`00bb1118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb1118) · [`00bb11b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb11b8) · [`00bb11d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb11d4)

~~~diff
- 00bb1050 ["COPY", "tmp:0:8", ["const:310:8"]]
- 00bb1050 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1050 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1050 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb1118 ["COPY", "tmp:0:8", ["const:3d0:8"]]
+ 00bb1118 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1118 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1118 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb1050 bytes 08410c91
+ 00bb1118 bytes 08410f91
- 00bb10f0 ["INT_ADD", "register:40f0:8", ["const:bb10f0:8", "const:4:8"]]
- 00bb10f0 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb11b8 ["INT_ADD", "register:40f0:8", ["const:bb11b8:8", "const:4:8"]]
+ 00bb11b8 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb10f0 bytes 84a70094
+ 00bb11b8 bytes 7ea70094
- 00bb110c ["INT_ADD", "register:40f0:8", ["const:bb110c:8", "const:4:8"]]
- 00bb110c ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb11d4 ["INT_ADD", "register:40f0:8", ["const:bb11d4:8", "const:4:8"]]
+ 00bb11d4 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb110c bytes 75a70094
+ 00bb11d4 bytes 6fa70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d570e7cd2f1f0f52ea7bdad6a4d5ac1"></a>

### [`00bb1120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1120.md) → [`00bb11e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__am_pmEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb118c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb118c.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb1254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1244",
      "incomplete_value": false,
      "site": "00bb1244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb117c",
      "incomplete_value": false,
      "site": "00bb117c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb1234",
      "incomplete_value": true,
      "site": "00bb1244",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb116c",
      "incomplete_value": true,
      "site": "00bb117c",
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
            "const:318:8"
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
      "definition_site": "00bb121c",
      "incomplete_value": false,
      "site": "00bb1220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1154",
      "incomplete_value": false,
      "site": "00bb1158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af8:8"
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
      "00bb11fc",
      "READ",
      [
        "storage",
        "010a2af8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1208",
      "READ",
      [
        "storage",
        "010a2af0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb1208",
      "DATA",
      [
        "storage",
        "010a3318",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb11fc",
      "READ",
      [
        "storage",
        "010a2bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1208",
      "READ",
      [
        "storage",
        "010a2bb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb1208",
      "DATA",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1120.md#insn-00bb1158) · [`00bb117c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1120.md#insn-00bb117c) · [`00bb1130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1120.md#insn-00bb1130)
- 新版 [`00bb1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md#insn-00bb1220) · [`00bb1244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md#insn-00bb1244) · [`00bb11f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md#insn-00bb11f8)

~~~diff
- 00bb1158 ["INT_ADD", "register:40f0:8", ["const:bb1158:8", "const:4:8"]]
- 00bb1158 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1220 ["INT_ADD", "register:40f0:8", ["const:bb1220:8", "const:4:8"]]
+ 00bb1220 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb1158 bytes 6aa70094
+ 00bb1220 bytes 64a70094
- 00bb117c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:af0:8"]]
- 00bb117c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb1244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
+ 00bb1244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb117c bytes 097905f9
+ 00bb1244 bytes 09d905f9
- 00bb1130 ["COPY", "tmp:0:8", ["const:af8:8"]]
- 00bb1130 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1130 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1130 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb11f8 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00bb11f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb11f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb11f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb1130 bytes 08e12b91
+ 00bb11f8 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ec7a7eb1f2650b7cf10a87403d8458"></a>

### [`00bb118c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb118c.md) → [`00bb1254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md) FUN_00bb1254

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb1120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1120.md) · 呼出先 4件 [`00bb8ff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ff0.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00bb11e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md) · 呼出先 4件 [`00bb90b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb90b8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1288",
      "incomplete_value": false,
      "site": "00bb1288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb11c0",
      "incomplete_value": false,
      "site": "00bb11c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb12a0",
      "incomplete_value": false,
      "site": "00bb12a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb11d8",
      "incomplete_value": false,
      "site": "00bb11d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:320:8"
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
      "definition_site": "00bb12cc",
      "incomplete_value": false,
      "site": "00bb12cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1204",
      "incomplete_value": false,
      "site": "00bb1204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:330:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb1268",
      "READ",
      [
        "storage",
        "010a3348",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1274",
      "READ",
      [
        "storage",
        "010a3318",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1288",
      "WRITE",
      [
        "storage",
        "010a3318",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1268",
      "READ",
      [
        "storage",
        "010a3408",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1274",
      "READ",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1288",
      "WRITE",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1240`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb118c.md#insn-00bb1240) · [`00bb125c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb118c.md#insn-00bb125c) · [`00bb1268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb118c.md#insn-00bb1268)
- 新版 [`00bb1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb1308) · [`00bb1324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb1324) · [`00bb1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb1330)

~~~diff
- 00bb1240 ["INT_ADD", "register:40f0:8", ["const:bb1240:8", "const:4:8"]]
- 00bb1240 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1308 ["INT_ADD", "register:40f0:8", ["const:bb1308:8", "const:4:8"]]
+ 00bb1308 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb1240 bytes 30a70094
+ 00bb1308 bytes 2aa70094
- 00bb125c ["INT_ADD", "register:40f0:8", ["const:bb125c:8", "const:4:8"]]
- 00bb125c ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb1324 ["INT_ADD", "register:40f0:8", ["const:bb1324:8", "const:4:8"]]
+ 00bb1324 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb125c bytes 21a70094
+ 00bb1324 bytes 1ba70094
- 00bb1268 ["INT_ADD", "register:40f0:8", ["const:bb1268:8", "const:4:8"]]
- 00bb1268 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb1330 ["INT_ADD", "register:40f0:8", ["const:bb1330:8", "const:4:8"]]
+ 00bb1330 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb1268 bytes 2ea70094
+ 00bb1330 bytes 28a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03d7d6005f976009ef42e614293611be"></a>

### [`00bb1270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1270.md) → [`00bb1338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__xEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb136c",
      "incomplete_value": false,
      "site": "00bb1370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb12a4",
      "incomplete_value": false,
      "site": "00bb12a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b00:8"
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
      "definition_site": "00bb138c",
      "incomplete_value": false,
      "site": "00bb1390",
      "value": [
        "leaf",
        "const:be5f80:8"
      ]
    },
    "old": {
      "definition_site": "00bb12c4",
      "incomplete_value": false,
      "site": "00bb12c8",
      "value": [
        "leaf",
        "const:be5ed0:8"
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1398",
      "incomplete_value": true,
      "site": "00bb139c",
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
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb12d0",
      "incomplete_value": true,
      "site": "00bb12d4",
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
            "const:b00:8"
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
      "00bb134c",
      "READ",
      [
        "storage",
        "010a2b00",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1358",
      "DATA",
      [
        "storage",
        "00c24830",
        null,
        null
      ]
    ],
    [
      "00bb136c",
      "PARAM",
      [
        "storage",
        "010a2b00",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb134c",
      "READ",
      [
        "storage",
        "010a2bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1358",
      "DATA",
      [
        "storage",
        "00c248e0",
        null,
        null
      ]
    ],
    [
      "00bb136c",
      "PARAM",
      [
        "storage",
        "010a2bc0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb12a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1270.md#insn-00bb12a8) · [`00bb12c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1270.md#insn-00bb12c8) · [`00bb12d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1270.md#insn-00bb12d4)
- 新版 [`00bb1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb1370) · [`00bb1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb1390) · [`00bb139c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb139c)

~~~diff
- 00bb12a8 ["INT_ADD", "register:40f0:8", ["const:bb12a8:8", "const:4:8"]]
- 00bb12a8 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1370 ["INT_ADD", "register:40f0:8", ["const:bb1370:8", "const:4:8"]]
+ 00bb1370 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb12a8 bytes 16a70094
+ 00bb1370 bytes 10a70094
- 00bb12c8 ["INT_ADD", "register:40f0:8", ["const:bb12c8:8", "const:4:8"]]
- 00bb12c8 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb1390 ["INT_ADD", "register:40f0:8", ["const:bb1390:8", "const:4:8"]]
+ 00bb1390 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb12c8 bytes 06a70094
+ 00bb1390 bytes 00a70094
- 00bb12d4 ["INT_ADD", "register:40f0:8", ["const:bb12d4:8", "const:4:8"]]
- 00bb12d4 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb139c ["INT_ADD", "register:40f0:8", ["const:bb139c:8", "const:4:8"]]
+ 00bb139c ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb12d4 bytes 13a70094
+ 00bb139c bytes 0da70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-643c1a89809d00256f0560e80a98108a"></a>

### [`00bb12dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb12dc.md) → [`00bb13a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__xEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dac.md) [`00baf118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf118.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb13e0",
      "incomplete_value": false,
      "site": "00bb13e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1318",
      "incomplete_value": false,
      "site": "00bb131c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b20:8"
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
      "definition_site": "00bb140c",
      "incomplete_value": true,
      "site": "00bb1418",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1344",
      "incomplete_value": true,
      "site": "00bb1350",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:b80:8"
              ]
            ]
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
      "definition_site": "00bb1408",
      "incomplete_value": false,
      "site": "00bb1418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1340",
      "incomplete_value": false,
      "site": "00bb1350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b08:8"
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
      "00bb13bc",
      "READ",
      [
        "storage",
        "010a2b20",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb13c8",
      "DATA",
      [
        "storage",
        "010a2b08",
        null,
        null
      ]
    ],
    [
      "00bb13e0",
      "PARAM",
      [
        "storage",
        "010a2b20",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb13bc",
      "READ",
      [
        "storage",
        "010a2be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb13c8",
      "DATA",
      [
        "storage",
        "010a2bc8",
        null,
        null
      ]
    ],
    [
      "00bb13e0",
      "PARAM",
      [
        "storage",
        "010a2be0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb131c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb12dc.md#insn-00bb131c) · [`00bb1350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb12dc.md#insn-00bb1350) · [`00bb135c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb12dc.md#insn-00bb135c)
- 新版 [`00bb13e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb13e4) · [`00bb1418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb1418) · [`00bb1424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb1424)

~~~diff
- 00bb131c ["INT_ADD", "register:40f0:8", ["const:bb131c:8", "const:4:8"]]
- 00bb131c ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb13e4 ["INT_ADD", "register:40f0:8", ["const:bb13e4:8", "const:4:8"]]
+ 00bb13e4 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb131c bytes f9a60094
+ 00bb13e4 bytes f3a60094
- 00bb1350 ["INT_ADD", "register:40f0:8", ["const:bb1350:8", "const:4:8"]]
- 00bb1350 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb1418 ["INT_ADD", "register:40f0:8", ["const:bb1418:8", "const:4:8"]]
+ 00bb1418 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb1350 bytes e4a60094
+ 00bb1418 bytes dea60094
- 00bb135c ["INT_ADD", "register:40f0:8", ["const:bb135c:8", "const:4:8"]]
- 00bb135c ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb1424 ["INT_ADD", "register:40f0:8", ["const:bb1424:8", "const:4:8"]]
+ 00bb1424 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb135c bytes f1a60094
+ 00bb1424 bytes eba60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfd3a29085461cd426973bc6186a40de"></a>

### [`00bb137c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb137c.md) → [`00bb1444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__XEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 81.48% / 新版 81.48%

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
      "definition_site": "00bb1490",
      "incomplete_value": true,
      "site": "00bb149c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb13c8",
      "incomplete_value": true,
      "site": "00bb13d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00bb148c",
      "incomplete_value": false,
      "site": "00bb149c",
      "value": [
        "leaf",
        "const:c248f8:8"
      ]
    },
    "old": {
      "definition_site": "00bb13c4",
      "incomplete_value": false,
      "site": "00bb13d4",
      "value": [
        "leaf",
        "const:c24848:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1498",
      "incomplete_value": false,
      "site": "00bb149c",
      "value": [
        "leaf",
        "const:be5f80:8"
      ]
    },
    "old": {
      "definition_site": "00bb13d0",
      "incomplete_value": false,
      "site": "00bb13d4",
      "value": [
        "leaf",
        "const:be5ed0:8"
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
      "00bb1458",
      "READ",
      [
        "storage",
        "010a2b28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1464",
      "DATA",
      [
        "storage",
        "00c24848",
        null,
        null
      ]
    ],
    [
      "00bb1478",
      "PARAM",
      [
        "storage",
        "010a2b28",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1458",
      "READ",
      [
        "storage",
        "010a2be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1464",
      "DATA",
      [
        "storage",
        "00c248f8",
        null,
        null
      ]
    ],
    [
      "00bb1478",
      "PARAM",
      [
        "storage",
        "010a2be8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb13d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb137c.md#insn-00bb13d4) · [`00bb13e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb137c.md#insn-00bb13e0) · [`00bb138c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb137c.md#insn-00bb138c)
- 新版 [`00bb149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb149c) · [`00bb14a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb14a8) · [`00bb1454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb1454)

~~~diff
- 00bb13d4 ["INT_ADD", "register:40f0:8", ["const:bb13d4:8", "const:4:8"]]
- 00bb13d4 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb149c ["INT_ADD", "register:40f0:8", ["const:bb149c:8", "const:4:8"]]
+ 00bb149c ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb13d4 bytes c3a60094
+ 00bb149c bytes bda60094
- 00bb13e0 ["INT_ADD", "register:40f0:8", ["const:bb13e0:8", "const:4:8"]]
- 00bb13e0 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb14a8 ["INT_ADD", "register:40f0:8", ["const:bb14a8:8", "const:4:8"]]
+ 00bb14a8 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb13e0 bytes d0a60094
+ 00bb14a8 bytes caa60094
- 00bb138c ["COPY", "tmp:0:8", ["const:b28:8"]]
- 00bb138c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb138c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb138c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb1454 ["COPY", "tmp:0:8", ["const:be8:8"]]
+ 00bb1454 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1454 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1454 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb138c bytes 08a12c91
+ 00bb1454 bytes 08a12f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f8bbb7becfde4e6dc05904dd7c9c682"></a>

### [`00bb13e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb13e8.md) → [`00bb14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__XEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dac.md) [`00baf118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf118.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb14ec",
      "incomplete_value": false,
      "site": "00bb14f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1424",
      "incomplete_value": false,
      "site": "00bb1428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "definition_site": "00bb14fc",
      "incomplete_value": false,
      "site": "00bb1508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1434",
      "incomplete_value": false,
      "site": "00bb1440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "definition_site": "00bb1518",
      "incomplete_value": true,
      "site": "00bb1524",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1450",
      "incomplete_value": true,
      "site": "00bb145c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:b80:8"
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
      "00bb14c8",
      "READ",
      [
        "storage",
        "010a2b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb14d4",
      "DATA",
      [
        "storage",
        "010a2b30",
        null,
        null
      ]
    ],
    [
      "00bb14ec",
      "PARAM",
      [
        "storage",
        "010a2b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb14c8",
      "READ",
      [
        "storage",
        "010a2c08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb14d4",
      "DATA",
      [
        "storage",
        "010a2bf0",
        null,
        null
      ]
    ],
    [
      "00bb14ec",
      "PARAM",
      [
        "storage",
        "010a2c08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb13e8.md#insn-00bb1428) · [`00bb1440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb13e8.md#insn-00bb1440) · [`00bb145c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb13e8.md#insn-00bb145c)
- 新版 [`00bb14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb14f0) · [`00bb1508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb1508) · [`00bb1524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb1524)

~~~diff
- 00bb1428 ["INT_ADD", "register:40f0:8", ["const:bb1428:8", "const:4:8"]]
- 00bb1428 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb14f0 ["INT_ADD", "register:40f0:8", ["const:bb14f0:8", "const:4:8"]]
+ 00bb14f0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb1428 bytes b6a60094
+ 00bb14f0 bytes b0a60094
- 00bb1440 ["INT_ADD", "register:40f0:8", ["const:bb1440:8", "const:4:8"]]
- 00bb1440 ["CALL", null, ["callee:00baf1e0:8"]]
+ 00bb1508 ["INT_ADD", "register:40f0:8", ["const:bb1508:8", "const:4:8"]]
+ 00bb1508 ["CALL", null, ["callee:00baf1e0:8"]]
- 00bb1440 bytes 36f7ff97
+ 00bb1508 bytes 36f7ff97
- 00bb145c ["INT_ADD", "register:40f0:8", ["const:bb145c:8", "const:4:8"]]
- 00bb145c ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb1524 ["INT_ADD", "register:40f0:8", ["const:bb1524:8", "const:4:8"]]
+ 00bb1524 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb145c bytes a1a60094
+ 00bb1524 bytes 9ba60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50f612a3d87b9312ff3689402df8059c"></a>

### [`00bb1488`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1488.md) → [`00bb1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1584",
      "incomplete_value": false,
      "site": "00bb1588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb14bc",
      "incomplete_value": false,
      "site": "00bb14c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b50:8"
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
      "definition_site": "00bb159c",
      "incomplete_value": true,
      "site": "00bb15a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb14d4",
      "incomplete_value": true,
      "site": "00bb14e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4000:8"
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb15a4",
      "incomplete_value": false,
      "site": "00bb15a8",
      "value": [
        "leaf",
        "const:be5f80:8"
      ]
    },
    "old": {
      "definition_site": "00bb14dc",
      "incomplete_value": false,
      "site": "00bb14e0",
      "value": [
        "leaf",
        "const:be5ed0:8"
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
      "00bb1564",
      "READ",
      [
        "storage",
        "010a2b50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1570",
      "DATA",
      [
        "storage",
        "00c24860",
        null,
        "string"
      ]
    ],
    [
      "00bb1584",
      "PARAM",
      [
        "storage",
        "010a2b50",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1564",
      "READ",
      [
        "storage",
        "010a2c10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1570",
      "DATA",
      [
        "storage",
        "00c24910",
        null,
        "string"
      ]
    ],
    [
      "00bb1584",
      "PARAM",
      [
        "storage",
        "010a2c10",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb14c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1488.md#insn-00bb14c0) · [`00bb14e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1488.md#insn-00bb14e0) · [`00bb14ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1488.md#insn-00bb14ec)
- 新版 [`00bb1588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb1588) · [`00bb15a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb15a8) · [`00bb15b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb15b4)

~~~diff
- 00bb14c0 ["INT_ADD", "register:40f0:8", ["const:bb14c0:8", "const:4:8"]]
- 00bb14c0 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1588 ["INT_ADD", "register:40f0:8", ["const:bb1588:8", "const:4:8"]]
+ 00bb1588 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb14c0 bytes 90a60094
+ 00bb1588 bytes 8aa60094
- 00bb14e0 ["INT_ADD", "register:40f0:8", ["const:bb14e0:8", "const:4:8"]]
- 00bb14e0 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb15a8 ["INT_ADD", "register:40f0:8", ["const:bb15a8:8", "const:4:8"]]
+ 00bb15a8 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb14e0 bytes 80a60094
+ 00bb15a8 bytes 7aa60094
- 00bb14ec ["INT_ADD", "register:40f0:8", ["const:bb14ec:8", "const:4:8"]]
- 00bb14ec ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb15b4 ["INT_ADD", "register:40f0:8", ["const:bb15b4:8", "const:4:8"]]
+ 00bb15b4 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb14ec bytes 8da60094
+ 00bb15b4 bytes 87a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca92d72b4cf9ccf04cd4e2fe0bbc0bbf"></a>

### [`00bb14f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb14f4.md) → [`00bb15bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__cEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dac.md) [`00baf118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf118.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb15f8",
      "incomplete_value": false,
      "site": "00bb15fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1530",
      "incomplete_value": false,
      "site": "00bb1534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "00bb1608",
      "incomplete_value": false,
      "site": "00bb1614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1540",
      "incomplete_value": false,
      "site": "00bb154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b58:8"
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
      "definition_site": "00bb1624",
      "incomplete_value": true,
      "site": "00bb1630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb155c",
      "incomplete_value": true,
      "site": "00bb1568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b80:8"
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
      "00bb15d4",
      "READ",
      [
        "storage",
        "010a2b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb15e0",
      "DATA",
      [
        "storage",
        "010a2b58",
        null,
        null
      ]
    ],
    [
      "00bb15f8",
      "PARAM",
      [
        "storage",
        "010a2b70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb15d4",
      "READ",
      [
        "storage",
        "010a2c30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb15e0",
      "DATA",
      [
        "storage",
        "010a2c18",
        null,
        null
      ]
    ],
    [
      "00bb15f8",
      "PARAM",
      [
        "storage",
        "010a2c30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb14f4.md#insn-00bb1534) · [`00bb154c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb14f4.md#insn-00bb154c) · [`00bb1568`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb14f4.md#insn-00bb1568)
- 新版 [`00bb15fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb15fc) · [`00bb1614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb1614) · [`00bb1630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb1630)

~~~diff
- 00bb1534 ["INT_ADD", "register:40f0:8", ["const:bb1534:8", "const:4:8"]]
- 00bb1534 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb15fc ["INT_ADD", "register:40f0:8", ["const:bb15fc:8", "const:4:8"]]
+ 00bb15fc ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb1534 bytes 73a60094
+ 00bb15fc bytes 6da60094
- 00bb154c ["INT_ADD", "register:40f0:8", ["const:bb154c:8", "const:4:8"]]
- 00bb154c ["CALL", null, ["callee:00baf1e0:8"]]
+ 00bb1614 ["INT_ADD", "register:40f0:8", ["const:bb1614:8", "const:4:8"]]
+ 00bb1614 ["CALL", null, ["callee:00baf1e0:8"]]
- 00bb154c bytes f3f6ff97
+ 00bb1614 bytes f3f6ff97
- 00bb1568 ["INT_ADD", "register:40f0:8", ["const:bb1568:8", "const:4:8"]]
- 00bb1568 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb1630 ["INT_ADD", "register:40f0:8", ["const:bb1630:8", "const:4:8"]]
+ 00bb1630 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb1568 bytes 5ea60094
+ 00bb1630 bytes 58a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-752b50042b68cbab3c37f21a13b1a614"></a>

### [`00bb1594`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1594.md) → [`00bb165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__rEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b55/00b55550.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1690",
      "incomplete_value": false,
      "site": "00bb1694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb15c8",
      "incomplete_value": false,
      "site": "00bb15cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "definition_site": "00bb16a8",
      "incomplete_value": true,
      "site": "00bb16b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb15e0",
      "incomplete_value": true,
      "site": "00bb15ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d08:8"
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
      "definition_site": "00bb16a4",
      "incomplete_value": false,
      "site": "00bb16b4",
      "value": [
        "leaf",
        "const:c24928:8"
      ]
    },
    "old": {
      "definition_site": "00bb15dc",
      "incomplete_value": false,
      "site": "00bb15ec",
      "value": [
        "leaf",
        "const:c24878:8"
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
      "00bb1670",
      "READ",
      [
        "storage",
        "010a2b78",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb167c",
      "DATA",
      [
        "storage",
        "00c24878",
        null,
        null
      ]
    ],
    [
      "00bb1690",
      "PARAM",
      [
        "storage",
        "010a2b78",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1670",
      "READ",
      [
        "storage",
        "010a2c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb167c",
      "DATA",
      [
        "storage",
        "00c24928",
        null,
        null
      ]
    ],
    [
      "00bb1690",
      "PARAM",
      [
        "storage",
        "010a2c38",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb15cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1594.md#insn-00bb15cc) · [`00bb15ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1594.md#insn-00bb15ec) · [`00bb15f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1594.md#insn-00bb15f8)
- 新版 [`00bb1694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb1694) · [`00bb16b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb16b4) · [`00bb16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb16c0)

~~~diff
- 00bb15cc ["INT_ADD", "register:40f0:8", ["const:bb15cc:8", "const:4:8"]]
- 00bb15cc ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1694 ["INT_ADD", "register:40f0:8", ["const:bb1694:8", "const:4:8"]]
+ 00bb1694 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb15cc bytes 4da60094
+ 00bb1694 bytes 47a60094
- 00bb15ec ["INT_ADD", "register:40f0:8", ["const:bb15ec:8", "const:4:8"]]
- 00bb15ec ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb16b4 ["INT_ADD", "register:40f0:8", ["const:bb16b4:8", "const:4:8"]]
+ 00bb16b4 ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb15ec bytes 3da60094
+ 00bb16b4 bytes 37a60094
- 00bb15f8 ["INT_ADD", "register:40f0:8", ["const:bb15f8:8", "const:4:8"]]
- 00bb15f8 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb16c0 ["INT_ADD", "register:40f0:8", ["const:bb16c0:8", "const:4:8"]]
+ 00bb16c0 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb15f8 bytes 4aa60094
+ 00bb16c0 bytes 44a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac3f5805d343dd542d85fd9f01b3643f"></a>

### [`00bb1600`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1600.md) → [`00bb16c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__rEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75dac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b75dac.md) [`00baf118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf118.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1704",
      "incomplete_value": false,
      "site": "00bb1708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb163c",
      "incomplete_value": false,
      "site": "00bb1640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "00bb1714",
      "incomplete_value": false,
      "site": "00bb1720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb164c",
      "incomplete_value": false,
      "site": "00bb1658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b80:8"
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
      "definition_site": "00bb1730",
      "incomplete_value": true,
      "site": "00bb173c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1668",
      "incomplete_value": true,
      "site": "00bb1674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b80:8"
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
      "00bb16e0",
      "READ",
      [
        "storage",
        "010a2b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb16ec",
      "DATA",
      [
        "storage",
        "010a2b80",
        null,
        null
      ]
    ],
    [
      "00bb1704",
      "PARAM",
      [
        "storage",
        "010a2b98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb16e0",
      "READ",
      [
        "storage",
        "010a2c58",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb16ec",
      "DATA",
      [
        "storage",
        "010a2c40",
        null,
        null
      ]
    ],
    [
      "00bb1704",
      "PARAM",
      [
        "storage",
        "010a2c58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1600.md#insn-00bb1640) · [`00bb1658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1600.md#insn-00bb1658) · [`00bb1674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb1600.md#insn-00bb1674)
- 新版 [`00bb1708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb1708) · [`00bb1720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb1720) · [`00bb173c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb173c)

~~~diff
- 00bb1640 ["INT_ADD", "register:40f0:8", ["const:bb1640:8", "const:4:8"]]
- 00bb1640 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb1708 ["INT_ADD", "register:40f0:8", ["const:bb1708:8", "const:4:8"]]
+ 00bb1708 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb1640 bytes 30a60094
+ 00bb1708 bytes 2aa60094
- 00bb1658 ["INT_ADD", "register:40f0:8", ["const:bb1658:8", "const:4:8"]]
- 00bb1658 ["CALL", null, ["callee:00baf1e0:8"]]
+ 00bb1720 ["INT_ADD", "register:40f0:8", ["const:bb1720:8", "const:4:8"]]
+ 00bb1720 ["CALL", null, ["callee:00baf1e0:8"]]
- 00bb1658 bytes b0f6ff97
+ 00bb1720 bytes b0f6ff97
- 00bb1674 ["INT_ADD", "register:40f0:8", ["const:bb1674:8", "const:4:8"]]
- 00bb1674 ["CALL", null, ["callee:00bdaf90:8"]]
+ 00bb173c ["INT_ADD", "register:40f0:8", ["const:bb173c:8", "const:4:8"]]
+ 00bb173c ["CALL", null, ["callee:00bdaf90:8"]]
- 00bb1674 bytes 1ba60094
+ 00bb173c bytes 15a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d470a20d91e760fa7d35416063f6e547"></a>

### [`00bb16a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb16a0.md) → [`00bb1768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md) _ZNSt6__ndk110__time_getC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1bc0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 1件 [`00be1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb17bc",
      "incomplete_value": false,
      "site": "00bb17cc",
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
            "const:407:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb16f4",
      "incomplete_value": false,
      "site": "00bb1704",
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
            "const:40e:8"
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
      "00bb17bc",
      "PARAM",
      [
        "storage",
        "002a640e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb17bc",
      "PARAM",
      [
        "storage",
        "002a6407",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb16a0.md#insn-00bb1704) · [`00bb16c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb16a0.md#insn-00bb16c4) · [`00bb16ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb1/00bb16a0.md#insn-00bb16ec)
- 新版 [`00bb17cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb17cc) · [`00bb178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb178c) · [`00bb17b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb17b4)

~~~diff
- 00bb1704 ["INT_ADD", "register:40f0:8", ["const:bb1704:8", "const:4:8"]]
- 00bb1704 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb17cc ["INT_ADD", "register:40f0:8", ["const:bb17cc:8", "const:4:8"]]
+ 00bb17cc ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb1704 bytes addcff97
+ 00bb17cc bytes addcff97
- 00bb16c4 ["INT_ADD", "register:40f0:8", ["const:bb16c4:8", "const:4:8"]]
- 00bb16c4 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb178c ["INT_ADD", "register:40f0:8", ["const:bb178c:8", "const:4:8"]]
+ 00bb178c ["CALL", null, ["callee:00be1520:8"]]
- 00bb16c4 bytes 6bbf0094
+ 00bb178c bytes 65bf0094
- 00bb16ec ["INT_ADD", "register:40f0:8", ["const:bb16ec:8", "const:4:8"]]
- 00bb16ec ["CALL", null, ["callee:0041b298:8"]]
+ 00bb17b4 ["INT_ADD", "register:40f0:8", ["const:bb17b4:8", "const:4:8"]]
+ 00bb17b4 ["CALL", null, ["callee:0041b298:8"]]
- 00bb16ec bytes eba6e197
+ 00bb17b4 bytes b9a6e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b92801d8601bbd81d08e2916814ba523"></a>

### [`00bb3d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3d6c.md) → [`00bb3e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md) _ZNSt6__ndk118__time_get_storageIwE4initERKNS_5ctypeIwEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c20.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdd950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd950.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) [`00be1480`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1480.md)
- 新版 呼出元 1件 [`00be1cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cd0.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb3ebc",
      "incomplete_value": false,
      "site": "00bb3ec4",
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
            "const:75:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb3df4",
      "incomplete_value": false,
      "site": "00bb3dfc",
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
            "const:fe8:8"
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
      "definition_site": "00bb401c",
      "incomplete_value": false,
      "site": "00bb4020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:2b9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb3f54",
      "incomplete_value": false,
      "site": "00bb3f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29c000:8"
          ],
          [
            "leaf",
            "const:22c:8"
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
      "definition_site": "00bb41a4",
      "incomplete_value": false,
      "site": "00bb41ac",
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
            "const:269:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb40dc",
      "incomplete_value": false,
      "site": "00bb40e4",
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
            "const:1dc:8"
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
      "00bb3ebc",
      "PARAM",
      [
        "storage",
        "002a1fe8",
        null,
        null
      ]
    ],
    [
      "00bb401c",
      "PARAM",
      [
        "storage",
        "0029c22c",
        null,
        null
      ]
    ],
    [
      "00bb41a4",
      "PARAM",
      [
        "storage",
        "0029f1dc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb3ebc",
      "PARAM",
      [
        "storage",
        "002a2075",
        null,
        null
      ]
    ],
    [
      "00bb401c",
      "PARAM",
      [
        "storage",
        "0029c2b9",
        null,
        null
      ]
    ],
    [
      "00bb41a4",
      "PARAM",
      [
        "storage",
        "0029f269",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb3dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3d6c.md#insn-00bb3dfc) · [`00bb3f58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3d6c.md#insn-00bb3f58) · [`00bb40e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb3/00bb3d6c.md#insn-00bb40e4)
- 新版 [`00bb3ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb3ec4) · [`00bb4020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb4020) · [`00bb41ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb41ac)

~~~diff
- 00bb3dfc ["INT_ADD", "register:40f0:8", ["const:bb3dfc:8", "const:4:8"]]
- 00bb3dfc ["CALL", null, ["callee:00be1620:8"]]
+ 00bb3ec4 ["INT_ADD", "register:40f0:8", ["const:bb3ec4:8", "const:4:8"]]
+ 00bb3ec4 ["CALL", null, ["callee:00be1620:8"]]
- 00bb3dfc bytes ddb50094
+ 00bb3ec4 bytes d7b50094
- 00bb3f58 ["INT_ADD", "register:40f0:8", ["const:bb3f58:8", "const:4:8"]]
- 00bb3f58 ["CALL", null, ["callee:00be1620:8"]]
+ 00bb4020 ["INT_ADD", "register:40f0:8", ["const:bb4020:8", "const:4:8"]]
+ 00bb4020 ["CALL", null, ["callee:00be1620:8"]]
- 00bb3f58 bytes 86b50094
+ 00bb4020 bytes 80b50094
- 00bb40e4 ["INT_ADD", "register:40f0:8", ["const:bb40e4:8", "const:4:8"]]
- 00bb40e4 ["CALL", null, ["callee:00be1620:8"]]
+ 00bb41ac ["INT_ADD", "register:40f0:8", ["const:bb41ac:8", "const:4:8"]]
+ 00bb41ac ["CALL", null, ["callee:00be1620:8"]]
- 00bb40e4 bytes 23b50094
+ 00bb41ac bytes 1db50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2b7ebc4ed3734a46610448661718ed7"></a>

### [`00bb47e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb47e4.md) → [`00bb48ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md) _ZNSt6__ndk118__time_get_storageIcEC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md) [`00be18e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18e0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be1990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1990.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb48f4",
      "incomplete_value": false,
      "site": "00bb48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb482c",
      "incomplete_value": false,
      "site": "00bb4830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "definition_site": "00bb4914",
      "incomplete_value": true,
      "site": "00bb4918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb484c",
      "incomplete_value": true,
      "site": "00bb4850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb492c",
      "incomplete_value": true,
      "site": "00bb4930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4864",
      "incomplete_value": true,
      "site": "00bb4868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb48f8",
      "DATA",
      [
        "storage",
        "00c15df8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb490c",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4918",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00bb48f8",
      "DATA",
      [
        "storage",
        "00c15ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb490c",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4918",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb47e4.md#insn-00bb4804) · [`00bb4814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb47e4.md#insn-00bb4814) · [`00bb4824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb47e4.md#insn-00bb4824)
- 新版 [`00bb48cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48cc) · [`00bb48dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48dc) · [`00bb48ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48ec)

~~~diff
- 00bb4804 ["INT_ADD", "register:40f0:8", ["const:bb4804:8", "const:4:8"]]
- 00bb4804 ["CALL", null, ["callee:00be1c70:8"]]
+ 00bb48cc ["INT_ADD", "register:40f0:8", ["const:bb48cc:8", "const:4:8"]]
+ 00bb48cc ["CALL", null, ["callee:00be1c70:8"]]
- 00bb4804 bytes efb40094
+ 00bb48cc bytes e9b40094
- 00bb4814 ["INT_ADD", "register:40f0:8", ["const:bb4814:8", "const:4:8"]]
- 00bb4814 ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bb48dc ["INT_ADD", "register:40f0:8", ["const:bb48dc:8", "const:4:8"]]
+ 00bb48dc ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bb4814 bytes 4b9a0094
+ 00bb48dc bytes 459a0094
- 00bb4824 ["INT_ADD", "register:40f0:8", ["const:bb4824:8", "const:4:8"]]
- 00bb4824 ["CALL", null, ["callee:00be1990:8"]]
+ 00bb48ec ["INT_ADD", "register:40f0:8", ["const:bb48ec:8", "const:4:8"]]
+ 00bb48ec ["CALL", null, ["callee:00be1990:8"]]
- 00bb4824 bytes 2fb40094
+ 00bb48ec bytes 29b40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf98f223dfc7f1bf92599a06f73fb697"></a>

### [`00bb4ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4ac4.md) → [`00bb4b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md) _ZNSt6__ndk112ctype_bynameIcED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1900.md) [`00be1c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c30.md) · 呼出先 3件 [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 2件 [`00be19b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19b0.md) [`00be1ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ce0.md) · 呼出先 3件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

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
      "definition_site": "00bb4bac",
      "incomplete_value": true,
      "site": "00bb4bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4ae4",
      "incomplete_value": true,
      "site": "00bb4ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb4bc4",
      "incomplete_value": true,
      "site": "00bb4bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4afc",
      "incomplete_value": true,
      "site": "00bb4b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb4ba4",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4bb0",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb4bbc",
      "READ",
      [
        "storage",
        "00c1be98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb4ba4",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4bb0",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb4bbc",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4ac4.md#insn-00bb4adc) · [`00bb4aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4ac4.md#insn-00bb4aec) · [`00bb4af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4ac4.md#insn-00bb4af4)
- 新版 [`00bb4ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4ba4) · [`00bb4bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4bb4) · [`00bb4bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4b8c.md#insn-00bb4bbc)

~~~diff
- 00bb4adc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00bb4adc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb4ba4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00bb4ba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb4adc bytes 085147f9
+ 00bb4ba4 bytes 08a947f9
- 00bb4aec ["INT_ADD", "register:40f0:8", ["const:bb4aec:8", "const:4:8"]]
- 00bb4aec ["CALL", null, ["callee:00be18e0:8"]]
+ 00bb4bb4 ["INT_ADD", "register:40f0:8", ["const:bb4bb4:8", "const:4:8"]]
+ 00bb4bb4 ["CALL", null, ["callee:00be18e0:8"]]
- 00bb4aec bytes 51b30094
+ 00bb4bb4 bytes 4bb30094
- 00bb4af4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
- 00bb4af4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb4bbc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00bb4bbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb4af4 bytes 084d47f9
+ 00bb4bbc bytes 08a547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eac05c82c481deba47ee102c5c2c6cc"></a>

### [`00bb4b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4b2c.md) → [`00bb4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md) _ZNSt6__ndk118__time_get_storageIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17a0.md) · 呼出先 7件 [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md) [`00be18f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be18f0.md)
- 新版 呼出元 1件 [`00be1850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1850.md) · 呼出先 7件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb4c3c",
      "incomplete_value": false,
      "site": "00bb4c40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:ea8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb4b74",
      "incomplete_value": false,
      "site": "00bb4b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:df8:8"
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
      "definition_site": "00bb4c5c",
      "incomplete_value": true,
      "site": "00bb4c60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4b94",
      "incomplete_value": true,
      "site": "00bb4b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4c74",
      "incomplete_value": true,
      "site": "00bb4c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4bac",
      "incomplete_value": true,
      "site": "00bb4bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb4c40",
      "DATA",
      [
        "storage",
        "00c15df8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4c54",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4c60",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00bb4c40",
      "DATA",
      [
        "storage",
        "00c15ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4c54",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4c60",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4b2c.md#insn-00bb4b4c) · [`00bb4b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4b2c.md#insn-00bb4b5c) · [`00bb4b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4b2c.md#insn-00bb4b6c)
- 新版 [`00bb4c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c14) · [`00bb4c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c24) · [`00bb4c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4bf4.md#insn-00bb4c34)

~~~diff
- 00bb4b4c ["INT_ADD", "register:40f0:8", ["const:bb4b4c:8", "const:4:8"]]
- 00bb4b4c ["CALL", null, ["callee:00be1c80:8"]]
+ 00bb4c14 ["INT_ADD", "register:40f0:8", ["const:bb4c14:8", "const:4:8"]]
+ 00bb4c14 ["CALL", null, ["callee:00be1c80:8"]]
- 00bb4b4c bytes 21b40094
+ 00bb4c14 bytes 1bb40094
- 00bb4b5c ["INT_ADD", "register:40f0:8", ["const:bb4b5c:8", "const:4:8"]]
- 00bb4b5c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bb4c24 ["INT_ADD", "register:40f0:8", ["const:bb4c24:8", "const:4:8"]]
+ 00bb4c24 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bb4b5c bytes 79990094
+ 00bb4c24 bytes 73990094
- 00bb4b6c ["INT_ADD", "register:40f0:8", ["const:bb4b6c:8", "const:4:8"]]
- 00bb4b6c ["CALL", null, ["callee:00be19a0:8"]]
+ 00bb4c34 ["INT_ADD", "register:40f0:8", ["const:bb4c34:8", "const:4:8"]]
+ 00bb4c34 ["CALL", null, ["callee:00be19a0:8"]]
- 00bb4b6c bytes 61b30094
+ 00bb4c34 bytes 5bb30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de8101c06f20feb9dfc17c056ebe51de"></a>

### [`00bb4e0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4e0c.md) → [`00bb4ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md) _ZNSt6__ndk118__time_get_storageIwEC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md) [`00be1910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1910.md) [`00be1920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1920.md) [`00be1bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1bc0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19c0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md) [`00be1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb4f1c",
      "incomplete_value": false,
      "site": "00bb4f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb4e54",
      "incomplete_value": false,
      "site": "00bb4e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "definition_site": "00bb4f3c",
      "incomplete_value": true,
      "site": "00bb4f40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb4e74",
      "incomplete_value": true,
      "site": "00bb4e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb4f20",
      "DATA",
      [
        "storage",
        "00c15e78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4f34",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4f40",
      "DATA",
      [
        "storage",
        "00c13990",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb4f20",
      "DATA",
      [
        "storage",
        "00c15f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4f34",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb4f40",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb4e2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4e0c.md#insn-00bb4e2c) · [`00bb4e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4e0c.md#insn-00bb4e3c) · [`00bb4e4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb4/00bb4e0c.md#insn-00bb4e4c)
- 新版 [`00bb4ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4ef4) · [`00bb4f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4f04) · [`00bb4f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb4ed4.md#insn-00bb4f14)

~~~diff
- 00bb4e2c ["INT_ADD", "register:40f0:8", ["const:bb4e2c:8", "const:4:8"]]
- 00bb4e2c ["CALL", null, ["callee:00be1c70:8"]]
+ 00bb4ef4 ["INT_ADD", "register:40f0:8", ["const:bb4ef4:8", "const:4:8"]]
+ 00bb4ef4 ["CALL", null, ["callee:00be1c70:8"]]
- 00bb4e2c bytes 65b30094
+ 00bb4ef4 bytes 5fb30094
- 00bb4e3c ["INT_ADD", "register:40f0:8", ["const:bb4e3c:8", "const:4:8"]]
- 00bb4e3c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bb4f04 ["INT_ADD", "register:40f0:8", ["const:bb4f04:8", "const:4:8"]]
+ 00bb4f04 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bb4e3c bytes c1980094
+ 00bb4f04 bytes bb980094
- 00bb4e4c ["INT_ADD", "register:40f0:8", ["const:bb4e4c:8", "const:4:8"]]
- 00bb4e4c ["CALL", null, ["callee:00be19c0:8"]]
+ 00bb4f14 ["INT_ADD", "register:40f0:8", ["const:bb4f14:8", "const:4:8"]]
+ 00bb4f14 ["CALL", null, ["callee:00be19c0:8"]]
- 00bb4e4c bytes b1b20094
+ 00bb4f14 bytes abb20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-381ec681b1a8a3d3ec719852cf627ae9"></a>

### [`00bb50c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb50c8.md) → [`00bb5190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md) _ZNSt6__ndk112ctype_bynameIwED1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1940.md) [`00be1c40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c40.md) · 呼出先 2件 [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md) [`00be1920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1920.md)
- 新版 呼出元 2件 [`00be19f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19f0.md) [`00be1cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cf0.md) · 呼出先 2件 [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb51b0",
      "incomplete_value": true,
      "site": "00bb51b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb50e8",
      "incomplete_value": true,
      "site": "00bb50ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb51a8",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb51b4",
      "DATA",
      [
        "storage",
        "00c13990",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb51a8",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb51b4",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb50e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb50c8.md#insn-00bb50e0) · [`00bb50f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb50c8.md#insn-00bb50f0)
- 新版 [`00bb51a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md#insn-00bb51a8) · [`00bb51b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5190.md#insn-00bb51b8)

~~~diff
- 00bb50e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea8:8"]]
- 00bb50e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb51a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
+ 00bb51a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb50e0 bytes 085547f9
+ 00bb51a8 bytes 08ad47f9
- 00bb50f0 ["INT_ADD", "register:40f0:8", ["const:bb50f0:8", "const:4:8"]]
- 00bb50f0 ["CALL", null, ["callee:00be18e0:8"]]
+ 00bb51b8 ["INT_ADD", "register:40f0:8", ["const:bb51b8:8", "const:4:8"]]
+ 00bb51b8 ["CALL", null, ["callee:00be18e0:8"]]
- 00bb50f0 bytes d0b10094
+ 00bb51b8 bytes cab10094
~~~


<a id="compare-924d50b290fb6e2ff90f6933973b0f40"></a>

### [`00bb510c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb510c.md) → [`00bb51d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md) _ZNSt6__ndk118__time_get_storageIwEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17b0.md) · 呼出先 6件 [`00bdb140`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb140.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md) [`00be1920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1920.md) [`00be1930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1930.md) [`00be1bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1bd0.md)
- 新版 呼出元 1件 [`00be1860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1860.md) · 呼出先 6件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be19d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19d0.md) [`00be19e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19e0.md) [`00be1c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c80.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb521c",
      "incomplete_value": false,
      "site": "00bb5220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:f28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5154",
      "incomplete_value": false,
      "site": "00bb5158",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:e78:8"
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
      "definition_site": "00bb523c",
      "incomplete_value": true,
      "site": "00bb5240",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb5174",
      "incomplete_value": true,
      "site": "00bb5178",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb5220",
      "DATA",
      [
        "storage",
        "00c15e78",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb5234",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5240",
      "DATA",
      [
        "storage",
        "00c13990",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00bb5220",
      "DATA",
      [
        "storage",
        "00c15f28",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb5234",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bb5240",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb512c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb510c.md#insn-00bb512c) · [`00bb513c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb510c.md#insn-00bb513c) · [`00bb514c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb510c.md#insn-00bb514c)
- 新版 [`00bb51f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb51f4) · [`00bb5204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb5204) · [`00bb5214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb51d4.md#insn-00bb5214)

~~~diff
- 00bb512c ["INT_ADD", "register:40f0:8", ["const:bb512c:8", "const:4:8"]]
- 00bb512c ["CALL", null, ["callee:00be1c80:8"]]
+ 00bb51f4 ["INT_ADD", "register:40f0:8", ["const:bb51f4:8", "const:4:8"]]
+ 00bb51f4 ["CALL", null, ["callee:00be1c80:8"]]
- 00bb512c bytes a9b20094
+ 00bb51f4 bytes a3b20094
- 00bb513c ["INT_ADD", "register:40f0:8", ["const:bb513c:8", "const:4:8"]]
- 00bb513c ["CALL", null, ["callee:00bdb1f0:8"]]
+ 00bb5204 ["INT_ADD", "register:40f0:8", ["const:bb5204:8", "const:4:8"]]
+ 00bb5204 ["CALL", null, ["callee:00bdb1f0:8"]]
- 00bb513c bytes 01980094
+ 00bb5204 bytes fb970094
- 00bb514c ["INT_ADD", "register:40f0:8", ["const:bb514c:8", "const:4:8"]]
- 00bb514c ["CALL", null, ["callee:00be19e0:8"]]
+ 00bb5214 ["INT_ADD", "register:40f0:8", ["const:bb5214:8", "const:4:8"]]
+ 00bb5214 ["CALL", null, ["callee:00be19e0:8"]]
- 00bb514c bytes f9b10094
+ 00bb5214 bytes f3b10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c01c81be8361d049443d027484f1c70f"></a>

### [`00bb58f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb58f8.md) → [`00bb59c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md) _ZNSt6__ndk110__time_putC1EPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb5a14",
      "incomplete_value": false,
      "site": "00bb5a24",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb594c",
      "incomplete_value": false,
      "site": "00bb595c",
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
            "const:feb:8"
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
      "00bb5a14",
      "PARAM",
      [
        "storage",
        "002a1feb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5a14",
      "PARAM",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb595c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb58f8.md#insn-00bb595c) · [`00bb591c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb58f8.md#insn-00bb591c) · [`00bb5944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb58f8.md#insn-00bb5944)
- 新版 [`00bb5a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb5a24) · [`00bb59e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb59e4) · [`00bb5a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb59c0.md#insn-00bb5a0c)

~~~diff
- 00bb595c ["INT_ADD", "register:40f0:8", ["const:bb595c:8", "const:4:8"]]
- 00bb595c ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb5a24 ["INT_ADD", "register:40f0:8", ["const:bb5a24:8", "const:4:8"]]
+ 00bb5a24 ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb595c bytes 17ccff97
+ 00bb5a24 bytes 17ccff97
- 00bb591c ["INT_ADD", "register:40f0:8", ["const:bb591c:8", "const:4:8"]]
- 00bb591c ["CALL", null, ["callee:00be1520:8"]]
+ 00bb59e4 ["INT_ADD", "register:40f0:8", ["const:bb59e4:8", "const:4:8"]]
+ 00bb59e4 ["CALL", null, ["callee:00be1520:8"]]
- 00bb591c bytes d5ae0094
+ 00bb59e4 bytes cfae0094
- 00bb5944 ["INT_ADD", "register:40f0:8", ["const:bb5944:8", "const:4:8"]]
- 00bb5944 ["CALL", null, ["callee:0041b298:8"]]
+ 00bb5a0c ["INT_ADD", "register:40f0:8", ["const:bb5a0c:8", "const:4:8"]]
+ 00bb5a0c ["CALL", null, ["callee:0041b298:8"]]
- 00bb5944 bytes 5596e197
+ 00bb5a0c bytes 2396e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c257880dd807f101230c2439ed076d6"></a>

### [`00bb59c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb59c0.md) → [`00bb5a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md) _ZNSt6__ndk110__time_putC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17c0.md) · 呼出先 5件 [`00bd6fec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6fec.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb160`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb160.md) [`00be0eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0eb0.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 1件 [`00be1870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1870.md) · 呼出先 5件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb5ae0",
      "incomplete_value": false,
      "site": "00bb5af0",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5a18",
      "incomplete_value": false,
      "site": "00bb5a28",
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
            "const:feb:8"
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
      "00bb5ae0",
      "PARAM",
      [
        "storage",
        "002a1feb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5ae0",
      "PARAM",
      [
        "storage",
        "002a2078",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5a28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb59c0.md#insn-00bb5a28) · [`00bb59f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb59c0.md#insn-00bb59f4) · [`00bb5a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb59c0.md#insn-00bb5a14)
- 新版 [`00bb5af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5af0) · [`00bb5abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5abc) · [`00bb5adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5a88.md#insn-00bb5adc)

~~~diff
- 00bb5a28 ["INT_ADD", "register:40f0:8", ["const:bb5a28:8", "const:4:8"]]
- 00bb5a28 ["CALL", null, ["callee:00bdb210:8"]]
+ 00bb5af0 ["INT_ADD", "register:40f0:8", ["const:bb5af0:8", "const:4:8"]]
+ 00bb5af0 ["CALL", null, ["callee:00bdb210:8"]]
- 00bb5a28 bytes ce950094
+ 00bb5af0 bytes c8950094
- 00bb59f4 ["INT_ADD", "register:40f0:8", ["const:bb59f4:8", "const:4:8"]]
- 00bb59f4 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb5abc ["INT_ADD", "register:40f0:8", ["const:bb5abc:8", "const:4:8"]]
+ 00bb5abc ["CALL", null, ["callee:00be1520:8"]]
- 00bb59f4 bytes 9fae0094
+ 00bb5abc bytes 99ae0094
- 00bb5a14 ["COPY", "register:4000:8", ["const:2a1000:8"]]
+ 00bb5adc ["COPY", "register:4000:8", ["const:2a2000:8"]]
- 00bb5a14 bytes 60b7ff90
+ 00bb5adc bytes 60b7ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ebe466ff7249fe10493bd42f982dd96"></a>

### [`00bb5a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5a5c.md) → [`00bb5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md) _ZNSt6__ndk110__time_putD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c70.md) · 呼出先 4件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 1件 [`00be1d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d20.md) · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb5ba0",
      "incomplete_value": true,
      "site": "00bb5ba0",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5ad8",
      "incomplete_value": true,
      "site": "00bb5ad8",
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
            "const:890:8"
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
      "definition_site": "00bb5b58",
      "incomplete_value": true,
      "site": "00bb5b5c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00bb5a90",
      "incomplete_value": true,
      "site": "00bb5a94",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
    "ordinal": 1,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb5b80",
      "incomplete_value": false,
      "site": "00bb5b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5ab8",
      "incomplete_value": false,
      "site": "00bb5abc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb5b44",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb5b54",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb5b80",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb5b44",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb5b54",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb5b80",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5a5c.md#insn-00bb5abc) · [`00bb5ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5a5c.md#insn-00bb5ad8) · [`00bb5ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5a5c.md#insn-00bb5ae4)
- 新版 [`00bb5b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5b84) · [`00bb5ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5ba0) · [`00bb5bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5b24.md#insn-00bb5bac)

~~~diff
- 00bb5abc ["INT_ADD", "register:40f0:8", ["const:bb5abc:8", "const:4:8"]]
- 00bb5abc ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb5b84 ["INT_ADD", "register:40f0:8", ["const:bb5b84:8", "const:4:8"]]
+ 00bb5b84 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb5abc bytes 11950094
+ 00bb5b84 bytes 0b950094
- 00bb5ad8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:890:8"]]
- 00bb5ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb5ba0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:950:8"]]
+ 00bb5ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb5ad8 bytes a04a04f9
+ 00bb5ba0 bytes a0aa04f9
- 00bb5ae4 ["INT_ADD", "register:40f0:8", ["const:bb5ae4:8", "const:4:8"]]
- 00bb5ae4 ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb5bac ["INT_ADD", "register:40f0:8", ["const:bb5bac:8", "const:4:8"]]
+ 00bb5bac ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb5ae4 bytes 0f950094
+ 00bb5bac bytes 09950094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95d0106146a032540597de10c799fd48"></a>

### [`00bb5b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5b08.md) → [`00bb5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md) _ZNSt6__ndk117moneypunct_bynameIcLb0EE4initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17e0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md)
- 新版 呼出元 1件 [`00be1890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1890.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb5ef8",
      "incomplete_value": false,
      "site": "00bb5f08",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb5e30",
      "incomplete_value": false,
      "site": "00bb5e40",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb5ef8",
      "PARAM",
      [
        "storage",
        "002a1055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb5ef8",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb5e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5b08.md#insn-00bb5e40) · [`00bb5b34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5b08.md#insn-00bb5b34) · [`00bb5b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb5/00bb5b08.md#insn-00bb5b44)
- 新版 [`00bb5f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5f08) · [`00bb5bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5bfc) · [`00bb5c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5bd0.md#insn-00bb5c0c)

~~~diff
- 00bb5e40 ["INT_ADD", "register:40f0:8", ["const:bb5e40:8", "const:4:8"]]
- 00bb5e40 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb5f08 ["INT_ADD", "register:40f0:8", ["const:bb5f08:8", "const:4:8"]]
+ 00bb5f08 ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb5e40 bytes decaff97
+ 00bb5f08 bytes decaff97
- 00bb5b34 ["INT_ADD", "register:40f0:8", ["const:bb5b34:8", "const:4:8"]]
- 00bb5b34 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb5bfc ["INT_ADD", "register:40f0:8", ["const:bb5bfc:8", "const:4:8"]]
+ 00bb5bfc ["CALL", null, ["callee:00be1520:8"]]
- 00bb5b34 bytes 4fae0094
+ 00bb5bfc bytes 49ae0094
- 00bb5b44 ["INT_ADD", "register:40f0:8", ["const:bb5b44:8", "const:4:8"]]
- 00bb5b44 ["CALL", null, ["callee:00be1530:8"]]
+ 00bb5c0c ["INT_ADD", "register:40f0:8", ["const:bb5c0c:8", "const:4:8"]]
+ 00bb5c0c ["CALL", null, ["callee:00be1530:8"]]
- 00bb5b44 bytes 4fae0094
+ 00bb5c0c bytes 49ae0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7704deaebd93558c1a5dcb2a1f0287b"></a>

### [`00bb641c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb641c.md) → [`00bb64e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md) _ZNSt6__ndk117moneypunct_bynameIcLb1EE4initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be17f0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e0fc.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md)
- 新版 呼出元 1件 [`00be18a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18a0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.53% / 新版 99.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb680c",
      "incomplete_value": false,
      "site": "00bb681c",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6744",
      "incomplete_value": false,
      "site": "00bb6754",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb680c",
      "PARAM",
      [
        "storage",
        "002a1055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb680c",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6754`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb641c.md#insn-00bb6754) · [`00bb6448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb641c.md#insn-00bb6448) · [`00bb6458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb641c.md#insn-00bb6458)
- 新版 [`00bb681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb681c) · [`00bb6510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb6510) · [`00bb6520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb64e4.md#insn-00bb6520)

~~~diff
- 00bb6754 ["INT_ADD", "register:40f0:8", ["const:bb6754:8", "const:4:8"]]
- 00bb6754 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb681c ["INT_ADD", "register:40f0:8", ["const:bb681c:8", "const:4:8"]]
+ 00bb681c ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb6754 bytes 99c8ff97
+ 00bb681c bytes 99c8ff97
- 00bb6448 ["INT_ADD", "register:40f0:8", ["const:bb6448:8", "const:4:8"]]
- 00bb6448 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb6510 ["INT_ADD", "register:40f0:8", ["const:bb6510:8", "const:4:8"]]
+ 00bb6510 ["CALL", null, ["callee:00be1520:8"]]
- 00bb6448 bytes 0aac0094
+ 00bb6510 bytes 04ac0094
- 00bb6458 ["INT_ADD", "register:40f0:8", ["const:bb6458:8", "const:4:8"]]
- 00bb6458 ["CALL", null, ["callee:00be1530:8"]]
+ 00bb6520 ["INT_ADD", "register:40f0:8", ["const:bb6520:8", "const:4:8"]]
+ 00bb6520 ["CALL", null, ["callee:00be1530:8"]]
- 00bb6458 bytes 0aac0094
+ 00bb6520 bytes 04ac0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8210490d7253536bdc3bd27b1e0fcbb1"></a>

### [`00bb6804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb6804.md) → [`00bb68cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md) _ZNSt6__ndk117moneypunct_bynameIwLb0EE4initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1800.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8e8.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00baf61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf61c.md)
- 新版 呼出元 1件 [`00be18b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18b0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb6f9c",
      "incomplete_value": false,
      "site": "00bb6fac",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb6ed4",
      "incomplete_value": false,
      "site": "00bb6ee4",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb6f9c",
      "PARAM",
      [
        "storage",
        "002a1055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb6f9c",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb6ee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb6804.md#insn-00bb6ee4) · [`00bb6fac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb6804.md#insn-00bb6fac) · [`00bb6834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb6/00bb6804.md#insn-00bb6834)
- 新版 [`00bb6fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb6fac) · [`00bb7074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb7074) · [`00bb68fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb6/00bb68cc.md#insn-00bb68fc)

~~~diff
- 00bb6ee4 ["INT_ADD", "register:40f0:8", ["const:bb6ee4:8", "const:4:8"]]
- 00bb6ee4 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb6fac ["INT_ADD", "register:40f0:8", ["const:bb6fac:8", "const:4:8"]]
+ 00bb6fac ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb6ee4 bytes b5c6ff97
+ 00bb6fac bytes b5c6ff97
- 00bb6fac ["INT_ADD", "register:40f0:8", ["const:bb6fac:8", "const:4:8"]]
- 00bb6fac ["CALL", null, ["callee:00baf6e4:8"]]
+ 00bb7074 ["INT_ADD", "register:40f0:8", ["const:bb7074:8", "const:4:8"]]
+ 00bb7074 ["CALL", null, ["callee:00baf6e4:8"]]
- 00bb6fac bytes 9ce1ff97
+ 00bb7074 bytes 9ce1ff97
- 00bb6834 ["INT_ADD", "register:40f0:8", ["const:bb6834:8", "const:4:8"]]
- 00bb6834 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb68fc ["INT_ADD", "register:40f0:8", ["const:bb68fc:8", "const:4:8"]]
+ 00bb68fc ["CALL", null, ["callee:00be1520:8"]]
- 00bb6834 bytes 0fab0094
+ 00bb68fc bytes 09ab0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dba57e89911e33caec4065ab58d8679"></a>

### [`00bb7500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7500.md) → [`00bb75c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md) _ZNSt6__ndk117moneypunct_bynameIwLb1EE4initEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1810.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad8e8.md) [`00b7501c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b75/00b7501c.md) [`00ba89b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba8/00ba89b8.md) [`00baf61c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf61c.md)
- 新版 呼出元 1件 [`00be18c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18c0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`006ad8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad8e8.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.78% / 新版 99.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb7c98",
      "incomplete_value": false,
      "site": "00bb7ca8",
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
            "const:e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb7bd0",
      "incomplete_value": false,
      "site": "00bb7be0",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb7c98",
      "PARAM",
      [
        "storage",
        "002a1055",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb7c98",
      "PARAM",
      [
        "storage",
        "002a10e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7be0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7500.md#insn-00bb7be0) · [`00bb7ca8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7500.md#insn-00bb7ca8) · [`00bb7530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7500.md#insn-00bb7530)
- 新版 [`00bb7ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb7ca8) · [`00bb7d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb7d70) · [`00bb75f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb75c8.md#insn-00bb75f8)

~~~diff
- 00bb7be0 ["INT_ADD", "register:40f0:8", ["const:bb7be0:8", "const:4:8"]]
- 00bb7be0 ["CALL", null, ["callee:00ba8a80:8"]]
+ 00bb7ca8 ["INT_ADD", "register:40f0:8", ["const:bb7ca8:8", "const:4:8"]]
+ 00bb7ca8 ["CALL", null, ["callee:00ba8a80:8"]]
- 00bb7be0 bytes 76c3ff97
+ 00bb7ca8 bytes 76c3ff97
- 00bb7ca8 ["INT_ADD", "register:40f0:8", ["const:bb7ca8:8", "const:4:8"]]
- 00bb7ca8 ["CALL", null, ["callee:00baf6e4:8"]]
+ 00bb7d70 ["INT_ADD", "register:40f0:8", ["const:bb7d70:8", "const:4:8"]]
+ 00bb7d70 ["CALL", null, ["callee:00baf6e4:8"]]
- 00bb7ca8 bytes 5ddeff97
+ 00bb7d70 bytes 5ddeff97
- 00bb7530 ["INT_ADD", "register:40f0:8", ["const:bb7530:8", "const:4:8"]]
- 00bb7530 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb75f8 ["INT_ADD", "register:40f0:8", ["const:bb75f8:8", "const:4:8"]]
+ 00bb75f8 ["CALL", null, ["callee:00be1520:8"]]
- 00bb7530 bytes d0a70094
+ 00bb75f8 bytes caa70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b11553e785285dc02a6d395b3932cdb2"></a>

### [`00bb7e40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7e40.md) → [`00bb7f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md) _ZNSt6__ndk17codecvtIwc9mbstate_tED2Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bdd930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd930.md) [`00be1a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1a30.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 2件 [`00bdd9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9e0.md) [`00be1ae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1ae0.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 68.29% / 新版 68.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb7f30",
      "incomplete_value": true,
      "site": "00bb7f34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb7e68",
      "incomplete_value": true,
      "site": "00bb7e6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb7f98",
      "incomplete_value": true,
      "site": "00bb7f98",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb7ed0",
      "incomplete_value": true,
      "site": "00bb7ed0",
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
            "const:890:8"
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
      "definition_site": "00bb7f4c",
      "incomplete_value": true,
      "site": "00bb7f50",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00bb7e84",
      "incomplete_value": true,
      "site": "00bb7e88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a0:8"
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
      "00bb7f28",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f34",
      "DATA",
      [
        "storage",
        "00c13a18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bb7f40",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb7f28",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bb7f34",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bb7f40",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb7eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7e40.md#insn-00bb7eb4) · [`00bb7ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7e40.md#insn-00bb7ecc) · [`00bb7ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb7/00bb7e40.md#insn-00bb7ed0)
- 新版 [`00bb7f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md#insn-00bb7f7c) · [`00bb7f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md#insn-00bb7f94) · [`00bb7f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb7/00bb7f08.md#insn-00bb7f98)

~~~diff
- 00bb7eb4 ["INT_ADD", "register:40f0:8", ["const:bb7eb4:8", "const:4:8"]]
- 00bb7eb4 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb7f7c ["INT_ADD", "register:40f0:8", ["const:bb7f7c:8", "const:4:8"]]
+ 00bb7f7c ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb7eb4 bytes 138c0094
+ 00bb7f7c bytes 0d8c0094
- 00bb7ecc ["INT_ADD", "register:40f0:8", ["const:bb7ecc:8", "const:4:8"]]
- 00bb7ecc ["CALL", null, ["callee:00be1520:8"]]
+ 00bb7f94 ["INT_ADD", "register:40f0:8", ["const:bb7f94:8", "const:4:8"]]
+ 00bb7f94 ["CALL", null, ["callee:00be1520:8"]]
- 00bb7ecc bytes 69a50094
+ 00bb7f94 bytes 63a50094
- 00bb7ed0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:890:8"]]
- 00bb7ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb7f98 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:950:8"]]
+ 00bb7f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb7ed0 bytes a04a04f9
+ 00bb7f98 bytes a0aa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750980522757cacdb1c5a3ecd28d725c"></a>

### [`00bb84c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb84c4.md) → [`00bb858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md) FUN_00bb858c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8558.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00bb8620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8620.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb85ac",
      "incomplete_value": true,
      "site": "00bb85b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb84e4",
      "incomplete_value": true,
      "site": "00bb84e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb85a4",
      "READ",
      [
        "storage",
        "00c1be68",
        null,
        "pointer"
      ]
    ],
    [
      "00bb85b0",
      "DATA",
      [
        "storage",
        "00c15558",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb85a4",
      "READ",
      [
        "storage",
        "00c1bf18",
        null,
        "pointer"
      ]
    ],
    [
      "00bb85b0",
      "DATA",
      [
        "storage",
        "00c15608",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb84dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb84c4.md#insn-00bb84dc) · [`00bb850c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb84c4.md#insn-00bb850c) · [`00bb8528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb84c4.md#insn-00bb8528)
- 新版 [`00bb85a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85a4) · [`00bb85d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85d4) · [`00bb85f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb858c.md#insn-00bb85f0)

~~~diff
- 00bb84dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e68:8"]]
- 00bb84dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb85a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
+ 00bb85a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb84dc bytes 083547f9
+ 00bb85a4 bytes 088d47f9
- 00bb850c ["INT_ADD", "register:40f0:8", ["const:bb850c:8", "const:4:8"]]
- 00bb850c ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb85d4 ["INT_ADD", "register:40f0:8", ["const:bb85d4:8", "const:4:8"]]
+ 00bb85d4 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb850c bytes 958a0094
+ 00bb85d4 bytes 8f8a0094
- 00bb8528 ["INT_ADD", "register:40f0:8", ["const:bb8528:8", "const:4:8"]]
- 00bb8528 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb85f0 ["INT_ADD", "register:40f0:8", ["const:bb85f0:8", "const:4:8"]]
+ 00bb85f0 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb8528 bytes 8e8a0094
+ 00bb85f0 bytes 888a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af8d6e412455d800dab4354d8df5217b"></a>

### [`00bb8584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8584.md) → [`00bb864c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md) FUN_00bb864c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8618`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8618.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00bb86e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb86e0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb866c",
      "incomplete_value": true,
      "site": "00bb8670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb85a4",
      "incomplete_value": true,
      "site": "00bb85a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb8664",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8670",
      "DATA",
      [
        "storage",
        "00c155e0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb8664",
      "READ",
      [
        "storage",
        "00c1bf20",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8670",
      "DATA",
      [
        "storage",
        "00c15690",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb859c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8584.md#insn-00bb859c) · [`00bb85cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8584.md#insn-00bb85cc) · [`00bb85e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8584.md#insn-00bb85e8)
- 新版 [`00bb8664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb8664) · [`00bb8694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb8694) · [`00bb86b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb864c.md#insn-00bb86b0)

~~~diff
- 00bb859c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
- 00bb859c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8664 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
+ 00bb8664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb859c bytes 083947f9
+ 00bb8664 bytes 089147f9
- 00bb85cc ["INT_ADD", "register:40f0:8", ["const:bb85cc:8", "const:4:8"]]
- 00bb85cc ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8694 ["INT_ADD", "register:40f0:8", ["const:bb8694:8", "const:4:8"]]
+ 00bb8694 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb85cc bytes 658a0094
+ 00bb8694 bytes 5f8a0094
- 00bb85e8 ["INT_ADD", "register:40f0:8", ["const:bb85e8:8", "const:4:8"]]
- 00bb85e8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb86b0 ["INT_ADD", "register:40f0:8", ["const:bb86b0:8", "const:4:8"]]
+ 00bb86b0 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb85e8 bytes 5e8a0094
+ 00bb86b0 bytes 588a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-287d306fcba3f2e5afeaf74460a71f25"></a>

### [`00bb8644`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8644.md) → [`00bb870c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md) FUN_00bb870c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb86d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb86d8.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00bb87a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87a0.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb872c",
      "incomplete_value": true,
      "site": "00bb8730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb8664",
      "incomplete_value": true,
      "site": "00bb8668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb8724",
      "READ",
      [
        "storage",
        "00c1be78",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8730",
      "DATA",
      [
        "storage",
        "00c15668",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb8724",
      "READ",
      [
        "storage",
        "00c1bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00bb8730",
      "DATA",
      [
        "storage",
        "00c15718",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb865c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8644.md#insn-00bb865c) · [`00bb868c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8644.md#insn-00bb868c) · [`00bb86a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8644.md#insn-00bb86a8)
- 新版 [`00bb8724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8724) · [`00bb8754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8754) · [`00bb8770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb870c.md#insn-00bb8770)

~~~diff
- 00bb865c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e78:8"]]
- 00bb865c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb8724 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
+ 00bb8724 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb865c bytes 083d47f9
+ 00bb8724 bytes 089547f9
- 00bb868c ["INT_ADD", "register:40f0:8", ["const:bb868c:8", "const:4:8"]]
- 00bb868c ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8754 ["INT_ADD", "register:40f0:8", ["const:bb8754:8", "const:4:8"]]
+ 00bb8754 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb868c bytes 358a0094
+ 00bb8754 bytes 2f8a0094
- 00bb86a8 ["INT_ADD", "register:40f0:8", ["const:bb86a8:8", "const:4:8"]]
- 00bb86a8 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8770 ["INT_ADD", "register:40f0:8", ["const:bb8770:8", "const:4:8"]]
+ 00bb8770 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb86a8 bytes 2e8a0094
+ 00bb8770 bytes 288a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dc54fd93ab809922a2c017a4dd127fd"></a>

### [`00bb8704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8704.md) → [`00bb87cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md) FUN_00bb87cc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bb8798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8798.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md)
- 新版 呼出元 1件 [`00bb8860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8860.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb87ec",
      "incomplete_value": true,
      "site": "00bb87f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb8724",
      "incomplete_value": true,
      "site": "00bb8728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb87e4",
      "READ",
      [
        "storage",
        "00c1be80",
        null,
        "pointer"
      ]
    ],
    [
      "00bb87f0",
      "DATA",
      [
        "storage",
        "00c156f0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00bb87e4",
      "READ",
      [
        "storage",
        "00c1bf30",
        null,
        "pointer"
      ]
    ],
    [
      "00bb87f0",
      "DATA",
      [
        "storage",
        "00c157a0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb871c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8704.md#insn-00bb871c) · [`00bb874c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8704.md#insn-00bb874c) · [`00bb8768`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8704.md#insn-00bb8768)
- 新版 [`00bb87e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb87e4) · [`00bb8814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb8814) · [`00bb8830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb87cc.md#insn-00bb8830)

~~~diff
- 00bb871c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e80:8"]]
- 00bb871c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb87e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
+ 00bb87e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb871c bytes 084147f9
+ 00bb87e4 bytes 089947f9
- 00bb874c ["INT_ADD", "register:40f0:8", ["const:bb874c:8", "const:4:8"]]
- 00bb874c ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8814 ["INT_ADD", "register:40f0:8", ["const:bb8814:8", "const:4:8"]]
+ 00bb8814 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb874c bytes 058a0094
+ 00bb8814 bytes ff890094
- 00bb8768 ["INT_ADD", "register:40f0:8", ["const:bb8768:8", "const:4:8"]]
- 00bb8768 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8830 ["INT_ADD", "register:40f0:8", ["const:bb8830:8", "const:4:8"]]
+ 00bb8830 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb8768 bytes fe890094
+ 00bb8830 bytes f8890094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e96e3bd43cecc496d3a9e35dcf4558a0"></a>

### [`00bb8954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8954.md) → [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) FUN_00bb8a1c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00ba7958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ba7/00ba7958.md) [`00bb896c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb896c.md) [`00bb8ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8ac8.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) [`00bb8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8a2c",
      "incomplete_value": false,
      "site": "00bb8a30",
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
      "definition_site": "00bb8964",
      "incomplete_value": false,
      "site": "00bb8968",
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
      "00bb8a2c",
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
      "00bb8a2c",
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

- 旧版 [`00bb8968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8954.md#insn-00bb8968) · [`00bb8964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8954.md#insn-00bb8964)
- 新版 [`00bb8a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md#insn-00bb8a30) · [`00bb8a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md#insn-00bb8a2c)

~~~diff
- 00bb8968 ["INT_ADD", "register:40f0:8", ["const:bb8968:8", "const:4:8"]]
- 00bb8968 ["CALL", null, ["callee:00418c38:8"]]
+ 00bb8a30 ["INT_ADD", "register:40f0:8", ["const:bb8a30:8", "const:4:8"]]
+ 00bb8a30 ["CALL", null, ["callee:00418c38:8"]]
- 00bb8968 bytes b480e197
+ 00bb8a30 bytes 8280e197
- 00bb8964 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00bb8964 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8964 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb8964 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a2c ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00bb8a2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb8a2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb8964 bytes 00280c91
+ 00bb8a2c bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e68837e8b7b34aea06b7c7729278373"></a>

### [`00bb8c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md) → [`00bb8cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md) FUN_00bb8cec

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bafb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00bafb60.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8d08",
      "incomplete_value": true,
      "site": "00bb8d0c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
    "old": {
      "definition_site": "00bb8c40",
      "incomplete_value": true,
      "site": "00bb8c44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
              ],
              [
                "leaf",
                "const:ce8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8d20",
      "incomplete_value": true,
      "site": "00bb8d24",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
    "old": {
      "definition_site": "00bb8c58",
      "incomplete_value": true,
      "site": "00bb8c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb8d38",
      "incomplete_value": true,
      "site": "00bb8d3c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
              ],
              [
                "leaf",
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb8c70",
      "incomplete_value": true,
      "site": "00bb8c74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a2000:8"
              ],
              [
                "leaf",
                "const:cb8:8"
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
      "00bb8cfc",
      "READ",
      [
        "storage",
        "010a2cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8d08",
      "READ",
      [
        "storage",
        "010a2ce8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d14",
      "READ",
      [
        "storage",
        "010a2cc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb8cfc",
      "READ",
      [
        "storage",
        "010a2d98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb8d08",
      "READ",
      [
        "storage",
        "010a2da8",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb8d14",
      "READ",
      [
        "storage",
        "010a2d80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb8c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md#insn-00bb8c44) · [`00bb8c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md#insn-00bb8c5c) · [`00bb8c74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb8/00bb8c24.md#insn-00bb8c74)
- 新版 [`00bb8d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d0c) · [`00bb8d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d24) · [`00bb8d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md#insn-00bb8d3c)

~~~diff
- 00bb8c44 ["INT_ADD", "register:40f0:8", ["const:bb8c44:8", "const:4:8"]]
- 00bb8c44 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8d0c ["INT_ADD", "register:40f0:8", ["const:bb8d0c:8", "const:4:8"]]
+ 00bb8d0c ["CALL", null, ["callee:00bdb010:8"]]
- 00bb8c44 bytes c7880094
+ 00bb8d0c bytes c1880094
- 00bb8c5c ["INT_ADD", "register:40f0:8", ["const:bb8c5c:8", "const:4:8"]]
- 00bb8c5c ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8d24 ["INT_ADD", "register:40f0:8", ["const:bb8d24:8", "const:4:8"]]
+ 00bb8d24 ["CALL", null, ["callee:00bdb010:8"]]
- 00bb8c5c bytes c1880094
+ 00bb8d24 bytes bb880094
- 00bb8c74 ["INT_ADD", "register:40f0:8", ["const:bb8c74:8", "const:4:8"]]
- 00bb8c74 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bb8d3c ["INT_ADD", "register:40f0:8", ["const:bb8d3c:8", "const:4:8"]]
+ 00bb8d3c ["CALL", null, ["callee:00bdb010:8"]]
- 00bb8c74 bytes bb880094
+ 00bb8d3c bytes b5880094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00b9d766e5f63e8c6408ffe2bef5a787"></a>

### [`00bb903c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md) → [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) FUN_00bb9104

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 96件 [`00b8a910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8a/00b8a910.md) [`00b8d5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d5b8.md) [`00b8dde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8dde8.md) [`00b90a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90a2c.md) [`00b91110`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b91/00b91110.md) · 呼出先 1件 [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md)
- 新版 呼出元 96件 [`00b8a9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8a/00b8a9d8.md) [`00b8d680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d680.md) [`00b8deb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8deb0.md) [`00b90af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b90af4.md) [`00b911d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b91/00b911d8.md) · 呼出先 1件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9128",
      "incomplete_value": true,
      "site": "00bb912c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9060",
      "incomplete_value": true,
      "site": "00bb9064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ed8:8"
              ]
            ]
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
      "00bb9128",
      "READ",
      [
        "storage",
        "00c1bed8",
        null,
        "pointer"
      ]
    ],
    [
      "00bb9128",
      "PARAM",
      [
        "storage",
        "010a29f8",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00bb9128",
      "READ",
      [
        "storage",
        "00c1bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00bb9128",
      "PARAM",
      [
        "storage",
        "010a2ab8",
        "_ZNSt6__ndk16locale2id9__next_idE",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md#insn-00bb9064) · [`00bb9060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb903c.md#insn-00bb9060)
- 新版 [`00bb912c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md#insn-00bb912c) · [`00bb9128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md#insn-00bb9128)

~~~diff
- 00bb9064 ["INT_ADD", "register:40f0:8", ["const:bb9064:8", "const:4:8"]]
- 00bb9064 ["CALL", null, ["callee:00bd6df0:8"]]
+ 00bb912c ["INT_ADD", "register:40f0:8", ["const:bb912c:8", "const:4:8"]]
+ 00bb912c ["CALL", null, ["callee:00bd6df0:8"]]
- 00bb9064 bytes 33770094
+ 00bb912c bytes 31770094
- 00bb9060 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ed8:8"]]
- 00bb9060 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9128 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f88:8"]]
+ 00bb9128 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9060 bytes 216c47f9
+ 00bb9128 bytes 21c447f9
~~~


<a id="compare-b59f7887d328b5af9aa40883a71aa6a6"></a>

### [`00bb9080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9080.md) → [`00bb9148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md) FUN_00bb9148

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb3b0.md) [`00bdee90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee90.md) [`00be1830`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1830.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

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
      "definition_site": "00bb9168",
      "incomplete_value": true,
      "site": "00bb916c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb90a0",
      "incomplete_value": true,
      "site": "00bb90a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb9180",
      "incomplete_value": true,
      "site": "00bb9184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bb90b8",
      "incomplete_value": true,
      "site": "00bb90bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bb9160",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb916c",
      "DATA",
      [
        "storage",
        "00c13928",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb9178",
      "READ",
      [
        "storage",
        "00c1be98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bb9160",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb916c",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00bb9178",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9080.md#insn-00bb9098) · [`00bb90a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9080.md#insn-00bb90a8) · [`00bb90b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9080.md#insn-00bb90b0)
- 新版 [`00bb9160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9160) · [`00bb9170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9170) · [`00bb9178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9148.md#insn-00bb9178)

~~~diff
- 00bb9098 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ea0:8"]]
- 00bb9098 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9160 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00bb9160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb9098 bytes 085147f9
+ 00bb9160 bytes 08a947f9
- 00bb90a8 ["INT_ADD", "register:40f0:8", ["const:bb90a8:8", "const:4:8"]]
- 00bb90a8 ["CALL", null, ["callee:00be18e0:8"]]
+ 00bb9170 ["INT_ADD", "register:40f0:8", ["const:bb9170:8", "const:4:8"]]
+ 00bb9170 ["CALL", null, ["callee:00be18e0:8"]]
- 00bb90a8 bytes e2a10094
+ 00bb9170 bytes dca10094
- 00bb90b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
- 00bb90b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bb9178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00bb9178 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bb90b0 bytes 084d47f9
+ 00bb9178 bytes 08a547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba37557342358666c09335fdbbb2edc5"></a>

### [`00bb91f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb91f0.md) → [`00bb92b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md) FUN_00bb92b8

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b010.md) [`00b8e4f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8e4f0.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c80.md)
- 新版 呼出元 2件 [`00b8b0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b0d8.md) [`00b8e5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e5b8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb93b4",
      "incomplete_value": true,
      "site": "00bb93b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb92ec",
      "incomplete_value": true,
      "site": "00bb92ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9310",
      "incomplete_value": true,
      "site": "00bb9320",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9248",
      "incomplete_value": true,
      "site": "00bb9258",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9394",
      "incomplete_value": false,
      "site": "00bb9398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb92cc",
      "incomplete_value": false,
      "site": "00bb92d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9308",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9310",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9394",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9308",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9310",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9394",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb91f0.md#insn-00bb9224) · [`00bb9258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb91f0.md#insn-00bb9258) · [`00bb92d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb91f0.md#insn-00bb92d0)
- 新版 [`00bb92ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb92ec) · [`00bb9320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb9320) · [`00bb9398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb92b8.md#insn-00bb9398)

~~~diff
- 00bb9224 ["INT_ADD", "register:40f0:8", ["const:bb9224:8", "const:4:8"]]
- 00bb9224 ["CALL", null, ["callee:00bdb220:8"]]
+ 00bb92ec ["INT_ADD", "register:40f0:8", ["const:bb92ec:8", "const:4:8"]]
+ 00bb92ec ["CALL", null, ["callee:00bdb220:8"]]
- 00bb9224 bytes d3870094
+ 00bb92ec bytes cd870094
- 00bb9258 ["INT_ADD", "register:40f0:8", ["const:bb9258:8", "const:4:8"]]
- 00bb9258 ["CALL", null, ["callee:00be1d30:8"]]
+ 00bb9320 ["INT_ADD", "register:40f0:8", ["const:bb9320:8", "const:4:8"]]
+ 00bb9320 ["CALL", null, ["callee:00be1d30:8"]]
- 00bb9258 bytes 8aa20094
+ 00bb9320 bytes 84a20094
- 00bb92d0 ["INT_ADD", "register:40f0:8", ["const:bb92d0:8", "const:4:8"]]
- 00bb92d0 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb9398 ["INT_ADD", "register:40f0:8", ["const:bb9398:8", "const:4:8"]]
+ 00bb9398 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb92d0 bytes 0c870094
+ 00bb9398 bytes 06870094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-455ea70c0f4338a16c4e7ea37bd71539"></a>

### [`00bb9318`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9318.md) → [`00bb93e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md) FUN_00bb93e0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b44c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b44c.md) [`00b8e920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8e920.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c80.md)
- 新版 呼出元 2件 [`00b8b514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b514.md) [`00b8e9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8e9e8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 86.76% / 新版 86.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb94dc",
      "incomplete_value": true,
      "site": "00bb94dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9414",
      "incomplete_value": true,
      "site": "00bb9414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9438",
      "incomplete_value": true,
      "site": "00bb9448",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9370",
      "incomplete_value": true,
      "site": "00bb9380",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb94bc",
      "incomplete_value": false,
      "site": "00bb94c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb93f4",
      "incomplete_value": false,
      "site": "00bb93f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9430",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9438",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb94bc",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9430",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9438",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb94bc",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb934c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9318.md#insn-00bb934c) · [`00bb9380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9318.md#insn-00bb9380) · [`00bb93f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9318.md#insn-00bb93f8)
- 新版 [`00bb9414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb9414) · [`00bb9448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb9448) · [`00bb94c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb93e0.md#insn-00bb94c0)

~~~diff
- 00bb934c ["INT_ADD", "register:40f0:8", ["const:bb934c:8", "const:4:8"]]
- 00bb934c ["CALL", null, ["callee:00bdb220:8"]]
+ 00bb9414 ["INT_ADD", "register:40f0:8", ["const:bb9414:8", "const:4:8"]]
+ 00bb9414 ["CALL", null, ["callee:00bdb220:8"]]
- 00bb934c bytes 89870094
+ 00bb9414 bytes 83870094
- 00bb9380 ["INT_ADD", "register:40f0:8", ["const:bb9380:8", "const:4:8"]]
- 00bb9380 ["CALL", null, ["callee:00be1d30:8"]]
+ 00bb9448 ["INT_ADD", "register:40f0:8", ["const:bb9448:8", "const:4:8"]]
+ 00bb9448 ["CALL", null, ["callee:00be1d30:8"]]
- 00bb9380 bytes 40a20094
+ 00bb9448 bytes 3aa20094
- 00bb93f8 ["INT_ADD", "register:40f0:8", ["const:bb93f8:8", "const:4:8"]]
- 00bb93f8 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb94c0 ["INT_ADD", "register:40f0:8", ["const:bb94c0:8", "const:4:8"]]
+ 00bb94c0 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb93f8 bytes c2860094
+ 00bb94c0 bytes bc860094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66cb671dd4e909e38932a4b487428139"></a>

### [`00bb9440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9440.md) → [`00bb9508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md) FUN_00bb9508

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8b888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8b888.md) [`00b8ed50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8e/00b8ed50.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c90.md)
- 新版 呼出元 2件 [`00b8b950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8b950.md) [`00b8ee18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8e/00b8ee18.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9634",
      "incomplete_value": true,
      "site": "00bb9634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb956c",
      "incomplete_value": true,
      "site": "00bb956c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb957c",
      "incomplete_value": true,
      "site": "00bb958c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb94b4",
      "incomplete_value": true,
      "site": "00bb94c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9614",
      "incomplete_value": false,
      "site": "00bb9618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb954c",
      "incomplete_value": false,
      "site": "00bb9550",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9574",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb957c",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9614",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9574",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb957c",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9614",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb94a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9440.md#insn-00bb94a0) · [`00bb94c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9440.md#insn-00bb94c4) · [`00bb9550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9440.md#insn-00bb9550)
- 新版 [`00bb9568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb9568) · [`00bb958c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb958c) · [`00bb9618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9508.md#insn-00bb9618)

~~~diff
- 00bb94a0 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bb94a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb94a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb94a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb9568 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bb9568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb94a0 bytes 08612291
+ 00bb9568 bytes 08612591
- 00bb94c4 ["INT_ADD", "register:40f0:8", ["const:bb94c4:8", "const:4:8"]]
- 00bb94c4 ["CALL", null, ["callee:00be1d40:8"]]
+ 00bb958c ["INT_ADD", "register:40f0:8", ["const:bb958c:8", "const:4:8"]]
+ 00bb958c ["CALL", null, ["callee:00be1d40:8"]]
- 00bb94c4 bytes f3a10094
+ 00bb958c bytes eda10094
- 00bb9550 ["INT_ADD", "register:40f0:8", ["const:bb9550:8", "const:4:8"]]
- 00bb9550 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb9618 ["INT_ADD", "register:40f0:8", ["const:bb9618:8", "const:4:8"]]
+ 00bb9618 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb9550 bytes 6c860094
+ 00bb9618 bytes 66860094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-094a4101df20a3a6d4a7c5ba32c8fdb7"></a>

### [`00bb9598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md) → [`00bb9660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md) FUN_00bb9660

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8bcc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8b/00b8bcc4.md) [`00b8f180`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f180.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c90.md)
- 新版 呼出元 2件 [`00b8bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8b/00b8bd8c.md) [`00b8f248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f248.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.87% / 新版 89.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9788",
      "incomplete_value": true,
      "site": "00bb9788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb96c0",
      "incomplete_value": true,
      "site": "00bb96c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb96d4",
      "incomplete_value": true,
      "site": "00bb96e4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb960c",
      "incomplete_value": true,
      "site": "00bb961c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9768",
      "incomplete_value": false,
      "site": "00bb976c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb96a0",
      "incomplete_value": false,
      "site": "00bb96a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb96cc",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb96d4",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9768",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb96cc",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb96d4",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9768",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb95f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md#insn-00bb95f8) · [`00bb961c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md#insn-00bb961c) · [`00bb96a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9598.md#insn-00bb96a4)
- 新版 [`00bb96c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb96c0) · [`00bb96e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb96e4) · [`00bb976c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9660.md#insn-00bb976c)

~~~diff
- 00bb95f8 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bb95f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb95f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb95f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bb96c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb96c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb95f8 bytes 08612291
+ 00bb96c0 bytes 08612591
- 00bb961c ["INT_ADD", "register:40f0:8", ["const:bb961c:8", "const:4:8"]]
- 00bb961c ["CALL", null, ["callee:00be1d40:8"]]
+ 00bb96e4 ["INT_ADD", "register:40f0:8", ["const:bb96e4:8", "const:4:8"]]
+ 00bb96e4 ["CALL", null, ["callee:00be1d40:8"]]
- 00bb961c bytes 9da10094
+ 00bb96e4 bytes 97a10094
- 00bb96a4 ["INT_ADD", "register:40f0:8", ["const:bb96a4:8", "const:4:8"]]
- 00bb96a4 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb976c ["INT_ADD", "register:40f0:8", ["const:bb976c:8", "const:4:8"]]
+ 00bb976c ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb96a4 bytes 17860094
+ 00bb976c bytes 11860094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea247adcead39d0491d455cf28921d5b"></a>

### [`00bb96ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb96ec.md) → [`00bb97b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md) FUN_00bb97b4

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8c100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c100.md) [`00b8f5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f5b0.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c90.md)
- 新版 呼出元 2件 [`00b8c1c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c1c8.md) [`00b8f678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8f678.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb98d0",
      "incomplete_value": true,
      "site": "00bb98d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9808",
      "incomplete_value": true,
      "site": "00bb9808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9828",
      "incomplete_value": true,
      "site": "00bb9838",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9760",
      "incomplete_value": true,
      "site": "00bb9770",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb98b0",
      "incomplete_value": false,
      "site": "00bb98b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb97e8",
      "incomplete_value": false,
      "site": "00bb97ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9820",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9828",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98b0",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9820",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9828",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb98b0",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb973c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb96ec.md#insn-00bb973c) · [`00bb974c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb96ec.md#insn-00bb974c) · [`00bb9770`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb96ec.md#insn-00bb9770)
- 新版 [`00bb9804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb9804) · [`00bb9814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb9814) · [`00bb9838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb97b4.md#insn-00bb9838)

~~~diff
- 00bb973c ["INT_ADD", "register:40f0:8", ["const:bb973c:8", "const:4:8"]]
- 00bb973c ["CALL", null, ["callee:00bdb220:8"]]
+ 00bb9804 ["INT_ADD", "register:40f0:8", ["const:bb9804:8", "const:4:8"]]
+ 00bb9804 ["CALL", null, ["callee:00bdb220:8"]]
- 00bb973c bytes 8d860094
+ 00bb9804 bytes 87860094
- 00bb974c ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bb974c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb974c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb974c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb9814 ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bb9814 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9814 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb9814 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb974c bytes 08612291
+ 00bb9814 bytes 08612591
- 00bb9770 ["INT_ADD", "register:40f0:8", ["const:bb9770:8", "const:4:8"]]
- 00bb9770 ["CALL", null, ["callee:00be1d40:8"]]
+ 00bb9838 ["INT_ADD", "register:40f0:8", ["const:bb9838:8", "const:4:8"]]
+ 00bb9838 ["CALL", null, ["callee:00be1d40:8"]]
- 00bb9770 bytes 48a10094
+ 00bb9838 bytes 42a10094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cc6e5486116bde4c0929b60ebc3d04c"></a>

### [`00bb9834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9834.md) → [`00bb98fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md) FUN_00bb98fc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8c53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c53c.md) [`00b8f9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8f9e0.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1c90.md)
- 新版 呼出元 2件 [`00b8c604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8c604.md) [`00b8faa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8faa8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.47% / 新版 89.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9a18",
      "incomplete_value": true,
      "site": "00bb9a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9950",
      "incomplete_value": true,
      "site": "00bb9950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d0:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9970",
      "incomplete_value": true,
      "site": "00bb9980",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb98a8",
      "incomplete_value": true,
      "site": "00bb98b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb99f8",
      "incomplete_value": false,
      "site": "00bb99fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9930",
      "incomplete_value": false,
      "site": "00bb9934",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9968",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9970",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb99f8",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9968",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9970",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb99f8",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9834.md#insn-00bb9884) · [`00bb9894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9834.md#insn-00bb9894) · [`00bb98b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9834.md#insn-00bb98b8)
- 新版 [`00bb994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb994c) · [`00bb995c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb995c) · [`00bb9980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb98fc.md#insn-00bb9980)

~~~diff
- 00bb9884 ["INT_ADD", "register:40f0:8", ["const:bb9884:8", "const:4:8"]]
- 00bb9884 ["CALL", null, ["callee:00bdb220:8"]]
+ 00bb994c ["INT_ADD", "register:40f0:8", ["const:bb994c:8", "const:4:8"]]
+ 00bb994c ["CALL", null, ["callee:00bdb220:8"]]
- 00bb9884 bytes 3b860094
+ 00bb994c bytes 35860094
- 00bb9894 ["COPY", "tmp:0:8", ["const:898:8"]]
- 00bb9894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb9894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb995c ["COPY", "tmp:0:8", ["const:958:8"]]
+ 00bb995c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb995c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb995c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb9894 bytes 08612291
+ 00bb995c bytes 08612591
- 00bb98b8 ["INT_ADD", "register:40f0:8", ["const:bb98b8:8", "const:4:8"]]
- 00bb98b8 ["CALL", null, ["callee:00be1d40:8"]]
+ 00bb9980 ["INT_ADD", "register:40f0:8", ["const:bb9980:8", "const:4:8"]]
+ 00bb9980 ["CALL", null, ["callee:00be1d40:8"]]
- 00bb98b8 bytes f6a00094
+ 00bb9980 bytes f0a00094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95545c59242fda9f8373d7eeb4106155"></a>

### [`00bb997c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb997c.md) → [`00bb9a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md) FUN_00bb9a44

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b8c978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8c978.md) [`00b8fe10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8f/00b8fe10.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb660.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 2件 [`00b8ca40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ca40.md) [`00b8fed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8f/00b8fed8.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb710.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9b30",
      "incomplete_value": false,
      "site": "00bb9b30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9a68",
      "incomplete_value": false,
      "site": "00bb9a68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9b0c",
      "incomplete_value": false,
      "site": "00bb9b10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9a44",
      "incomplete_value": false,
      "site": "00bb9a48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00bb9b1c",
      "incomplete_value": false,
      "site": "00bb9b28",
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
            "const:683:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9a54",
      "incomplete_value": false,
      "site": "00bb9a60",
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
            "const:68a:8"
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
      "00bb9a88",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b0c",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b1c",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9a88",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b0c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9b1c",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9a48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb997c.md#insn-00bb9a48) · [`00bb9a60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb997c.md#insn-00bb9a60) · [`00bb9a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb997c.md#insn-00bb9a68)
- 新版 [`00bb9b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b10) · [`00bb9b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b28) · [`00bb9b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9a44.md#insn-00bb9b30)

~~~diff
- 00bb9a48 ["INT_ADD", "register:40f0:8", ["const:bb9a48:8", "const:4:8"]]
- 00bb9a48 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb9b10 ["INT_ADD", "register:40f0:8", ["const:bb9b10:8", "const:4:8"]]
+ 00bb9b10 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb9a48 bytes 2e850094
+ 00bb9b10 bytes 28850094
- 00bb9a60 ["INT_ADD", "register:40f0:8", ["const:bb9a60:8", "const:4:8"]]
- 00bb9a60 ["CALL", null, ["callee:00be1520:8"]]
+ 00bb9b28 ["INT_ADD", "register:40f0:8", ["const:bb9b28:8", "const:4:8"]]
+ 00bb9b28 ["CALL", null, ["callee:00be1520:8"]]
- 00bb9a60 bytes 849e0094
+ 00bb9b28 bytes 7e9e0094
- 00bb9a68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00bb9a68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9b30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00bb9b30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9a68 bytes 004904f9
+ 00bb9b30 bytes 00a904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb1e6cc7a7ee46432afe60d5e0941f3e"></a>

### [`00bb9a94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md) → [`00bb9b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md) FUN_00bb9b5c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b8cd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8c/00b8cd90.md) [`00b9021c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b9021c.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00bdb670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb670.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md)
- 新版 呼出元 2件 [`00b8ce58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8c/00b8ce58.md) [`00b902e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b902e4.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bdb720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb720.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.19% / 新版 92.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9c48",
      "incomplete_value": false,
      "site": "00bb9c48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9b80",
      "incomplete_value": false,
      "site": "00bb9b80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9c24",
      "incomplete_value": false,
      "site": "00bb9c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9b5c",
      "incomplete_value": false,
      "site": "00bb9b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "definition_site": "00bb9c50",
      "incomplete_value": false,
      "site": "00bb9c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9b88",
      "incomplete_value": false,
      "site": "00bb9b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9ba0",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c24",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c34",
      "PARAM",
      [
        "storage",
        "002a568a",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb9ba0",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c24",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9c34",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md#insn-00bb9b60) · [`00bb9b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md#insn-00bb9b80) · [`00bb9b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9a94.md#insn-00bb9b8c)
- 新版 [`00bb9c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c28) · [`00bb9c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c48) · [`00bb9c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9b5c.md#insn-00bb9c54)

~~~diff
- 00bb9b60 ["INT_ADD", "register:40f0:8", ["const:bb9b60:8", "const:4:8"]]
- 00bb9b60 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb9c28 ["INT_ADD", "register:40f0:8", ["const:bb9c28:8", "const:4:8"]]
+ 00bb9c28 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb9b60 bytes e8840094
+ 00bb9c28 bytes e2840094
- 00bb9b80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:890:8"]]
- 00bb9b80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00bb9c48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00bb9c48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00bb9b80 bytes 004904f9
+ 00bb9c48 bytes 00a904f9
- 00bb9b8c ["INT_ADD", "register:40f0:8", ["const:bb9b8c:8", "const:4:8"]]
- 00bb9b8c ["CALL", null, ["callee:00bdafd0:8"]]
+ 00bb9c54 ["INT_ADD", "register:40f0:8", ["const:bb9c54:8", "const:4:8"]]
+ 00bb9c54 ["CALL", null, ["callee:00bdafd0:8"]]
- 00bb9b8c bytes e5840094
+ 00bb9c54 bytes df840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b682666c200d49aed26ed26dccfe1d"></a>

### [`00bb9bac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9bac.md) → [`00bb9c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md) FUN_00bb9c74

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b8d1a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b8d/00b8d1a8.md) [`00b90628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b90/00b90628.md) · 呼出先 5件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) [`00bdb170`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb170.md) [`00be1470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1470.md) [`00be1ca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ca0.md)
- 新版 呼出元 2件 [`00b8d270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8d270.md) [`00b906f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b90/00b906f0.md) · 呼出先 5件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.06% / 新版 88.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb9d6c",
      "incomplete_value": true,
      "site": "00bb9d6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9ca4",
      "incomplete_value": true,
      "site": "00bb9ca4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:890:8"
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
      "definition_site": "00bb9cc8",
      "incomplete_value": true,
      "site": "00bb9cd4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9c00",
      "incomplete_value": true,
      "site": "00bb9c0c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:890:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb9d4c",
      "incomplete_value": false,
      "site": "00bb9d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb9c84",
      "incomplete_value": false,
      "site": "00bb9c88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:898:8"
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
      "00bb9cc0",
      "READ",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9cc8",
      "READ",
      [
        "storage",
        "010a2890",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d4c",
      "PARAM",
      [
        "storage",
        "010a2898",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb9cc0",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb9cc8",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb9d4c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb9bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9bac.md#insn-00bb9bdc) · [`00bb9c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9bac.md#insn-00bb9c0c) · [`00bb9c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bb9/00bb9bac.md#insn-00bb9c88)
- 新版 [`00bb9ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9ca4) · [`00bb9cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9cd4) · [`00bb9d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9c74.md#insn-00bb9d50)

~~~diff
- 00bb9bdc ["INT_ADD", "register:40f0:8", ["const:bb9bdc:8", "const:4:8"]]
- 00bb9bdc ["CALL", null, ["callee:00bdb220:8"]]
+ 00bb9ca4 ["INT_ADD", "register:40f0:8", ["const:bb9ca4:8", "const:4:8"]]
+ 00bb9ca4 ["CALL", null, ["callee:00bdb220:8"]]
- 00bb9bdc bytes 65850094
+ 00bb9ca4 bytes 5f850094
- 00bb9c0c ["INT_ADD", "register:40f0:8", ["const:bb9c0c:8", "const:4:8"]]
- 00bb9c0c ["CALL", null, ["callee:00be1d50:8"]]
+ 00bb9cd4 ["INT_ADD", "register:40f0:8", ["const:bb9cd4:8", "const:4:8"]]
+ 00bb9cd4 ["CALL", null, ["callee:00be1d50:8"]]
- 00bb9c0c bytes 25a00094
+ 00bb9cd4 bytes 1fa00094
- 00bb9c88 ["INT_ADD", "register:40f0:8", ["const:bb9c88:8", "const:4:8"]]
- 00bb9c88 ["CALL", null, ["callee:00bdafb0:8"]]
+ 00bb9d50 ["INT_ADD", "register:40f0:8", ["const:bb9d50:8", "const:4:8"]]
+ 00bb9d50 ["CALL", null, ["callee:00bdafb0:8"]]
- 00bb9c88 bytes 9e840094
+ 00bb9d50 bytes 98840094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77e1a7d01f6f20787b562fe8b9b4e944"></a>

### [`00bba130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba130.md) → [`00bba1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md) _ZNSt6__ndk111__call_onceERVmPvPFvS2_E

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0de0.md) · 呼出先 4件 [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be10c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10c0.md) [`00be10d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10d0.md)
- 新版 呼出元 1件 [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md) · 呼出先 4件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md) [`00be1180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 85.94% / 新版 85.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba2a0",
      "incomplete_value": false,
      "site": "00bba2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba1d8",
      "incomplete_value": false,
      "site": "00bba1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "definition_site": "00bba2b4",
      "incomplete_value": false,
      "site": "00bba2b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba1ec",
      "incomplete_value": false,
      "site": "00bba1f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "definition_site": "00bba2c8",
      "incomplete_value": true,
      "site": "00bba2cc",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba200",
      "incomplete_value": true,
      "site": "00bba204",
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
            "const:5a8:8"
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
      "00bba21c",
      "PARAM",
      [
        "storage",
        "010a35a8",
        null,
        null
      ]
    ],
    [
      "00bba248",
      "PARAM",
      [
        "storage",
        "010a35d0",
        null,
        null
      ]
    ],
    [
      "00bba24c",
      "PARAM",
      [
        "storage",
        "010a35a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba21c",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba248",
      "PARAM",
      [
        "storage",
        "010a3690",
        null,
        null
      ]
    ],
    [
      "00bba24c",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba1dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba130.md#insn-00bba1dc) · [`00bba1f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba130.md#insn-00bba1f0) · [`00bba204`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba130.md#insn-00bba204)
- 新版 [`00bba2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2a4) · [`00bba2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2b8) · [`00bba2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba1f8.md#insn-00bba2cc)

~~~diff
- 00bba1dc ["INT_ADD", "register:40f0:8", ["const:bba1dc:8", "const:4:8"]]
- 00bba1dc ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba2a4 ["INT_ADD", "register:40f0:8", ["const:bba2a4:8", "const:4:8"]]
+ 00bba2a4 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba1dc bytes 55910094
+ 00bba2a4 bytes 4f910094
- 00bba1f0 ["INT_ADD", "register:40f0:8", ["const:bba1f0:8", "const:4:8"]]
- 00bba1f0 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bba2b8 ["INT_ADD", "register:40f0:8", ["const:bba2b8:8", "const:4:8"]]
+ 00bba2b8 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bba1f0 bytes 4c910094
+ 00bba2b8 bytes 46910094
- 00bba204 ["INT_ADD", "register:40f0:8", ["const:bba204:8", "const:4:8"]]
- 00bba204 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba2cc ["INT_ADD", "register:40f0:8", ["const:bba2cc:8", "const:4:8"]]
+ 00bba2cc ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba204 bytes 4b910094
+ 00bba2cc bytes 45910094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-860a16c821895825c3d4d64e949b8bd2"></a>

### [`00bba244`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba244.md) → [`00bba30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md) FUN_00bba30c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be10c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10c0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba32c",
      "incomplete_value": false,
      "site": "00bba330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba264",
      "incomplete_value": false,
      "site": "00bba268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:5a8:8"
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
      "definition_site": "00bba340",
      "incomplete_value": true,
      "site": "00bba344",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba278",
      "incomplete_value": true,
      "site": "00bba27c",
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
            "const:5a8:8"
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
      "definition_site": "00bba34c",
      "incomplete_value": false,
      "site": "00bba350",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:690:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba284",
      "incomplete_value": false,
      "site": "00bba288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:5d0:8"
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
      "00bba32c",
      "PARAM",
      [
        "storage",
        "010a35a8",
        null,
        null
      ]
    ],
    [
      "00bba340",
      "PARAM",
      [
        "storage",
        "010a35a8",
        null,
        null
      ]
    ],
    [
      "00bba34c",
      "PARAM",
      [
        "storage",
        "010a35d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba32c",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba340",
      "PARAM",
      [
        "storage",
        "010a3668",
        null,
        null
      ]
    ],
    [
      "00bba34c",
      "PARAM",
      [
        "storage",
        "010a3690",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba244.md#insn-00bba268) · [`00bba27c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba244.md#insn-00bba27c) · [`00bba288`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba244.md#insn-00bba288)
- 新版 [`00bba330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba330) · [`00bba344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba344) · [`00bba350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba30c.md#insn-00bba350)

~~~diff
- 00bba268 ["INT_ADD", "register:40f0:8", ["const:bba268:8", "const:4:8"]]
- 00bba268 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bba330 ["INT_ADD", "register:40f0:8", ["const:bba330:8", "const:4:8"]]
+ 00bba330 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bba268 bytes 2e910094
+ 00bba330 bytes 28910094
- 00bba27c ["INT_ADD", "register:40f0:8", ["const:bba27c:8", "const:4:8"]]
- 00bba27c ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba344 ["INT_ADD", "register:40f0:8", ["const:bba344:8", "const:4:8"]]
+ 00bba344 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba27c bytes 2d910094
+ 00bba344 bytes 27910094
- 00bba288 ["INT_ADD", "register:40f0:8", ["const:bba288:8", "const:4:8"]]
- 00bba288 ["CALL", null, ["callee:00be1170:8"]]
+ 00bba350 ["INT_ADD", "register:40f0:8", ["const:bba350:8", "const:4:8"]]
+ 00bba350 ["CALL", null, ["callee:00be1170:8"]]
- 00bba288 bytes 8e9b0094
+ 00bba350 bytes 889b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9aed5e77aa7a905e961fae89a65a200e"></a>

### [`00bba340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba340.md) → [`00bba408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md) _ZNSt6__ndk120__get_collation_nameEPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd8b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd8b0.md) · 呼出先 1件 [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 1件 [`00bdd960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd960.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bba46c",
      "incomplete_value": true,
      "site": "00bba474",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
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
      "definition_site": "00bba3a4",
      "incomplete_value": true,
      "site": "00bba3ac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40a8:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bba440",
      "READ",
      [
        "storage",
        "00c162a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bba440",
      "PARAM",
      [
        "storage",
        "002a6449",
        null,
        "string"
      ]
    ],
    [
      "00bba440",
      "READ",
      [
        "storage",
        "00c160e0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba440",
      "READ",
      [
        "storage",
        "00c16350",
        null,
        "pointer"
      ]
    ],
    [
      "00bba440",
      "PARAM",
      [
        "storage",
        "002a6442",
        null,
        "string"
      ]
    ],
    [
      "00bba440",
      "READ",
      [
        "storage",
        "00c16190",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba340.md#insn-00bba368) · [`00bba37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba340.md#insn-00bba37c) · [`00bba39c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba340.md#insn-00bba39c)
- 新版 [`00bba430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba430) · [`00bba444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba444) · [`00bba464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba408.md#insn-00bba464)

~~~diff
- 00bba368 ["COPY", "register:40a8:8", ["const:c15f30:8"]]
+ 00bba430 ["COPY", "register:40a8:8", ["const:c15fe0:8"]]
- 00bba368 bytes 55de2d10
+ 00bba430 bytes 95dd2d10
- 00bba37c ["INT_ADD", "register:40f0:8", ["const:bba37c:8", "const:4:8"]]
- 00bba37c ["CALL", null, ["callee:00bde980:8"]]
+ 00bba444 ["INT_ADD", "register:40f0:8", ["const:bba444:8", "const:4:8"]]
+ 00bba444 ["CALL", null, ["callee:00bde980:8"]]
- 00bba37c bytes 55910094
+ 00bba444 bytes 4f910094
- 00bba39c ["COPY", "tmp:0:8", ["const:620:8"]]
- 00bba39c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bba39c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bba39c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bba464 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00bba464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bba464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bba464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bba39c bytes 08811891
+ 00bba464 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a73af938ba329d9ba928436d167479a"></a>

### [`00bba584`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba584.md) → [`00bba64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md) __cxa_bad_typeid

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbb04c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb04c.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00be1cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1cb0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbb114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb114.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00be1d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba67c",
      "incomplete_value": true,
      "site": "00bba680",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba5b4",
      "incomplete_value": true,
      "site": "00bba5b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
      "00bba678",
      "READ",
      [
        "storage",
        "00c1bee8",
        null,
        "pointer"
      ]
    ],
    [
      "00bba678",
      "PARAM",
      [
        "storage",
        "00c16af8",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba67c",
      "READ",
      [
        "storage",
        "00c1bef0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba678",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ],
    [
      "00bba678",
      "PARAM",
      [
        "storage",
        "00c16ba8",
        "_ZTISt10bad_typeid",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba67c",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba584.md#insn-00bba5b8) · [`00bba598`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba584.md#insn-00bba598) · [`00bba5a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba584.md#insn-00bba5a0)
- 新版 [`00bba680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba680) · [`00bba660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba660) · [`00bba668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba64c.md#insn-00bba668)

~~~diff
- 00bba5b8 ["INT_ADD", "register:40f0:8", ["const:bba5b8:8", "const:4:8"]]
- 00bba5b8 ["CALL", null, ["callee:00bdb070:8"]]
+ 00bba680 ["INT_ADD", "register:40f0:8", ["const:bba680:8", "const:4:8"]]
+ 00bba680 ["CALL", null, ["callee:00bdb070:8"]]
- 00bba5b8 bytes 82820094
+ 00bba680 bytes 7c820094
- 00bba598 ["INT_ADD", "register:40f0:8", ["const:bba598:8", "const:4:8"]]
- 00bba598 ["CALL", null, ["callee:00bdb050:8"]]
+ 00bba660 ["INT_ADD", "register:40f0:8", ["const:bba660:8", "const:4:8"]]
+ 00bba660 ["CALL", null, ["callee:00bdb050:8"]]
- 00bba598 bytes 82820094
+ 00bba660 bytes 7c820094
- 00bba5a0 ["INT_ADD", "register:40f0:8", ["const:bba5a0:8", "const:4:8"]]
- 00bba5a0 ["CALL", null, ["callee:00be1d60:8"]]
+ 00bba668 ["INT_ADD", "register:40f0:8", ["const:bba668:8", "const:4:8"]]
+ 00bba668 ["CALL", null, ["callee:00be1d60:8"]]
- 00bba5a0 bytes c49d0094
+ 00bba668 bytes be9d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e9af87cc9d8e24e2c914d08060c7284"></a>

### [`00bba5bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5bc.md) → [`00bba684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md) __cxa_throw_bad_array_new_length

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba6b0",
      "incomplete_value": true,
      "site": "00bba6b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba5e8",
      "incomplete_value": true,
      "site": "00bba5f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ce0:8"
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
      "definition_site": "00bba6b4",
      "incomplete_value": true,
      "site": "00bba6b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
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
    "old": {
      "definition_site": "00bba5ec",
      "incomplete_value": true,
      "site": "00bba5f0",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:ce8:8"
              ]
            ]
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
      "00bba6b0",
      "READ",
      [
        "storage",
        "00c1ace0",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6b0",
      "PARAM",
      [
        "storage",
        "00c16808",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6b4",
      "READ",
      [
        "storage",
        "00c1ace8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00bba6b0",
      "READ",
      [
        "storage",
        "00c1ad90",
        null,
        "pointer"
      ]
    ],
    [
      "00bba6b0",
      "PARAM",
      [
        "storage",
        "00c168b8",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00bba6b4",
      "READ",
      [
        "storage",
        "00c1ad98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba5f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5bc.md#insn-00bba5f0) · [`00bba5d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5bc.md#insn-00bba5d0) · [`00bba5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5bc.md#insn-00bba5d8)
- 新版 [`00bba6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba6b8) · [`00bba698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba698) · [`00bba6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba684.md#insn-00bba6a0)

~~~diff
- 00bba5f0 ["INT_ADD", "register:40f0:8", ["const:bba5f0:8", "const:4:8"]]
- 00bba5f0 ["CALL", null, ["callee:00bdb070:8"]]
+ 00bba6b8 ["INT_ADD", "register:40f0:8", ["const:bba6b8:8", "const:4:8"]]
+ 00bba6b8 ["CALL", null, ["callee:00bdb070:8"]]
- 00bba5f0 bytes 74820094
+ 00bba6b8 bytes 6e820094
- 00bba5d0 ["INT_ADD", "register:40f0:8", ["const:bba5d0:8", "const:4:8"]]
- 00bba5d0 ["CALL", null, ["callee:00bdb050:8"]]
+ 00bba698 ["INT_ADD", "register:40f0:8", ["const:bba698:8", "const:4:8"]]
+ 00bba698 ["CALL", null, ["callee:00bdb050:8"]]
- 00bba5d0 bytes 74820094
+ 00bba698 bytes 6e820094
- 00bba5d8 ["INT_ADD", "register:40f0:8", ["const:bba5d8:8", "const:4:8"]]
- 00bba5d8 ["CALL", null, ["callee:00bdb190:8"]]
+ 00bba6a0 ["INT_ADD", "register:40f0:8", ["const:bba6a0:8", "const:4:8"]]
+ 00bba6a0 ["CALL", null, ["callee:00bdb190:8"]]
- 00bba5d8 bytes c2820094
+ 00bba6a0 bytes bc820094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60911775bc5710ca1a7045cc8892f402"></a>

### [`00bba5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md) → [`00bba6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md) __cxa_guard_acquire

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) · 呼出先 5件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be10d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10d0.md) [`00be1cf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1cf0.md)
- 新版 呼出元 1件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) · 呼出先 5件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1180.md) [`00be1da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1da0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.49% / 新版 86.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba6f8",
      "incomplete_value": false,
      "site": "00bba700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba630",
      "incomplete_value": false,
      "site": "00bba638",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00bba780",
      "incomplete_value": false,
      "site": "00bba784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba6b8",
      "incomplete_value": false,
      "site": "00bba6bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00bba7b4",
      "incomplete_value": false,
      "site": "00bba7c0",
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
            "const:810:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba6ec",
      "incomplete_value": false,
      "site": "00bba6f8",
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
            "const:783:8"
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
      "00bba6f8",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ],
    [
      "00bba6fc",
      "DATA",
      [
        "storage",
        "002a7234",
        null,
        "string"
      ]
    ],
    [
      "00bba748",
      "PARAM",
      [
        "storage",
        "010a3628",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba6f8",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba6fc",
      "DATA",
      [
        "storage",
        "002a722d",
        null,
        "string"
      ]
    ],
    [
      "00bba748",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba630`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md#insn-00bba630) · [`00bba638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md#insn-00bba638) · [`00bba6bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md#insn-00bba6bc)
- 新版 [`00bba6f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba6f8) · [`00bba700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba700) · [`00bba784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md#insn-00bba784)

~~~diff
- 00bba630 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00bba630 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba630 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba630 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba6f8 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00bba6f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba6f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba6f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba630 bytes 00001891
+ 00bba6f8 bytes 00001b91
- 00bba638 ["INT_ADD", "register:40f0:8", ["const:bba638:8", "const:4:8"]]
- 00bba638 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bba700 ["INT_ADD", "register:40f0:8", ["const:bba700:8", "const:4:8"]]
+ 00bba700 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bba638 bytes 3a900094
+ 00bba700 bytes 34900094
- 00bba6bc ["INT_ADD", "register:40f0:8", ["const:bba6bc:8", "const:4:8"]]
- 00bba6bc ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba784 ["INT_ADD", "register:40f0:8", ["const:bba784:8", "const:4:8"]]
+ 00bba784 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba6bc bytes 1d900094
+ 00bba784 bytes 17900094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6df8d52616f3665ef5bbec3ce86ba114"></a>

### [`00bba738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba738.md) → [`00bba800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md) __cxa_guard_release

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md) · 呼出先 4件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be10c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10c0.md)
- 新版 呼出元 1件 [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 82.93% / 新版 82.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba83c",
      "incomplete_value": false,
      "site": "00bba840",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba774",
      "incomplete_value": false,
      "site": "00bba778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00bba888",
      "incomplete_value": false,
      "site": "00bba88c",
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
            "const:a76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba7c0",
      "incomplete_value": false,
      "site": "00bba7c4",
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
            "const:9e9:8"
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
      "definition_site": "00bba89c",
      "incomplete_value": false,
      "site": "00bba8a0",
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
            "const:a76:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba7d4",
      "incomplete_value": false,
      "site": "00bba7d8",
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
            "const:9e9:8"
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
      "00bba824",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ],
    [
      "00bba83c",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ],
    [
      "00bba850",
      "PARAM",
      [
        "storage",
        "010a3628",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba824",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba83c",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba850",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba738.md#insn-00bba778) · [`00bba7c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba738.md#insn-00bba7c4) · [`00bba7d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba738.md#insn-00bba7d8)
- 新版 [`00bba840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba840) · [`00bba88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba88c) · [`00bba8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md#insn-00bba8a0)

~~~diff
- 00bba778 ["INT_ADD", "register:40f0:8", ["const:bba778:8", "const:4:8"]]
- 00bba778 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba840 ["INT_ADD", "register:40f0:8", ["const:bba840:8", "const:4:8"]]
+ 00bba840 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba778 bytes ee8f0094
+ 00bba840 bytes e88f0094
- 00bba7c4 ["INT_ADD", "register:40f0:8", ["const:bba7c4:8", "const:4:8"]]
- 00bba7c4 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bba88c ["INT_ADD", "register:40f0:8", ["const:bba88c:8", "const:4:8"]]
+ 00bba88c ["CALL", null, ["callee:00bbb158:8"]]
- 00bba7c4 bytes 33020094
+ 00bba88c bytes 33020094
- 00bba7d8 ["INT_ADD", "register:40f0:8", ["const:bba7d8:8", "const:4:8"]]
- 00bba7d8 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bba8a0 ["INT_ADD", "register:40f0:8", ["const:bba8a0:8", "const:4:8"]]
+ 00bba8a0 ["CALL", null, ["callee:00bbb158:8"]]
- 00bba7d8 bytes 2e020094
+ 00bba8a0 bytes 2e020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-067c6aa84ec6a0d982e0581bdaad7211"></a>

### [`00bba7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba7e0.md) → [`00bba8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) __cxa_guard_abort

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb040`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb040.md) · 呼出先 4件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bde720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde720.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md) [`00be10c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be10c0.md)
- 新版 呼出元 1件 [`00bdb0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0f0.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7d0.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md) [`00be1170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1170.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 81.58% / 新版 81.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba8c0",
      "incomplete_value": false,
      "site": "00bba8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba7f8",
      "incomplete_value": false,
      "site": "00bba7fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00bba8dc",
      "incomplete_value": true,
      "site": "00bba8e0",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba814",
      "incomplete_value": true,
      "site": "00bba818",
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
            "const:600:8"
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
      "definition_site": "00bba924",
      "incomplete_value": false,
      "site": "00bba928",
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
            "const:29d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba85c",
      "incomplete_value": false,
      "site": "00bba860",
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
            "const:2a4:8"
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
      "00bba8c0",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ],
    [
      "00bba8dc",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ],
    [
      "00bba8f0",
      "PARAM",
      [
        "storage",
        "010a3628",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba8c0",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba8dc",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ],
    [
      "00bba8f0",
      "PARAM",
      [
        "storage",
        "010a36e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba7e0.md#insn-00bba7fc) · [`00bba818`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba7e0.md#insn-00bba818) · [`00bba860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba7e0.md#insn-00bba860)
- 新版 [`00bba8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba8c4) · [`00bba8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba8e0) · [`00bba928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md#insn-00bba928)

~~~diff
- 00bba7fc ["INT_ADD", "register:40f0:8", ["const:bba7fc:8", "const:4:8"]]
- 00bba7fc ["CALL", null, ["callee:00bde7d0:8"]]
+ 00bba8c4 ["INT_ADD", "register:40f0:8", ["const:bba8c4:8", "const:4:8"]]
+ 00bba8c4 ["CALL", null, ["callee:00bde7d0:8"]]
- 00bba7fc bytes c98f0094
+ 00bba8c4 bytes c38f0094
- 00bba818 ["INT_ADD", "register:40f0:8", ["const:bba818:8", "const:4:8"]]
- 00bba818 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba8e0 ["INT_ADD", "register:40f0:8", ["const:bba8e0:8", "const:4:8"]]
+ 00bba8e0 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba818 bytes c68f0094
+ 00bba8e0 bytes c08f0094
- 00bba860 ["INT_ADD", "register:40f0:8", ["const:bba860:8", "const:4:8"]]
- 00bba860 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bba928 ["INT_ADD", "register:40f0:8", ["const:bba928:8", "const:4:8"]]
+ 00bba928 ["CALL", null, ["callee:00bbb158:8"]]
- 00bba860 bytes 0c020094
+ 00bba928 bytes 0c020094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ac42115a579d249740fd90fdfae94c2"></a>

### [`00bba87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba87c.md) → [`00bba944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md) FUN_00bba944

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bde730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde730.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bde7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde7e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba95c",
      "incomplete_value": false,
      "site": "00bba960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba894",
      "incomplete_value": false,
      "site": "00bba898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "00bba95c",
      "PARAM",
      [
        "storage",
        "010a3600",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bba95c",
      "PARAM",
      [
        "storage",
        "010a36c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba898`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba87c.md#insn-00bba898) · [`00bba894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba87c.md#insn-00bba894) · [`00bba8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba87c.md#insn-00bba8bc)
- 新版 [`00bba960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba960) · [`00bba95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba95c) · [`00bba984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md#insn-00bba984)

~~~diff
- 00bba898 ["INT_ADD", "register:40f0:8", ["const:bba898:8", "const:4:8"]]
- 00bba898 ["CALL", null, ["callee:00bde7e0:8"]]
+ 00bba960 ["INT_ADD", "register:40f0:8", ["const:bba960:8", "const:4:8"]]
+ 00bba960 ["CALL", null, ["callee:00bde7e0:8"]]
- 00bba898 bytes a68f0094
+ 00bba960 bytes a08f0094
- 00bba894 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00bba894 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba894 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba894 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba95c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00bba95c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba95c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba95c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba894 bytes 00001891
+ 00bba95c bytes 00001b91
- 00bba8bc ["INT_ADD", "register:40f0:8", ["const:bba8bc:8", "const:4:8"]]
- 00bba8bc ["CALL", null, ["callee:00bbb158:8"]]
+ 00bba984 ["INT_ADD", "register:40f0:8", ["const:bba984:8", "const:4:8"]]
+ 00bba984 ["CALL", null, ["callee:00bbb158:8"]]
- 00bba8bc bytes f5010094
+ 00bba984 bytes f5010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30c8778619ba7b33182f98562616b621"></a>

### [`00bba918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md) → [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) FUN_00bba9e0

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bba934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba934.md) [`00bd5f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5f68.md) · 呼出先 1件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md)
- 新版 呼出元 2件 [`00bba9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9fc.md) [`00bd6030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6030.md) · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bba9f4",
      "incomplete_value": false,
      "site": "00bba9f8",
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
            "const:6a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba92c",
      "incomplete_value": false,
      "site": "00bba930",
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
            "const:613:8"
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
      "00bba9f4",
      "PARAM",
      [
        "storage",
        "00293613",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bba9f4",
      "PARAM",
      [
        "storage",
        "002936a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md#insn-00bba930) · [`00bba924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md#insn-00bba924) · [`00bba92c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md#insn-00bba92c)
- 新版 [`00bba9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9f8) · [`00bba9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9ec) · [`00bba9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md#insn-00bba9f4)

~~~diff
- 00bba930 ["INT_ADD", "register:40f0:8", ["const:bba930:8", "const:4:8"]]
- 00bba930 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bba9f8 ["INT_ADD", "register:40f0:8", ["const:bba9f8:8", "const:4:8"]]
+ 00bba9f8 ["CALL", null, ["callee:00bbb158:8"]]
- 00bba930 bytes d8010094
+ 00bba9f8 bytes d8010094
- 00bba924 ["COPY", "register:0:8", ["register:4000:8"]]
- 00bba924 ["INT_ADD", "register:40f0:8", ["const:bba924:8", "const:4:8"]]
- 00bba924 ["CALLIND", null, ["register:0:8"]]
+ 00bba9ec ["COPY", "register:0:8", ["register:4000:8"]]
+ 00bba9ec ["INT_ADD", "register:40f0:8", ["const:bba9ec:8", "const:4:8"]]
+ 00bba9ec ["CALLIND", null, ["register:0:8"]]
- 00bba924 bytes 00003fd6
+ 00bba9ec bytes 00003fd6
- 00bba92c ["COPY", "tmp:0:8", ["const:613:8"]]
- 00bba92c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba92c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba92c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bba9f4 ["COPY", "tmp:0:8", ["const:6a0:8"]]
+ 00bba9f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba9f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bba9f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba92c bytes 004c1891
+ 00bba9f4 bytes 00801a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e33183f14e253a74a4465eeb69e7434"></a>

### [`00bba964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md) → [`00bbaa2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md) FUN_00bbaa2c

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 8件 [`00bba8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba8d8.md) [`00bd507c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd507c.md) [`00bd5184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd5184.md) [`00bd534c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd534c.md) [`00bd55fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd5/00bd55fc.md) · 呼出先 1件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md)
- 新版 呼出元 8件 [`00bba9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9a0.md) [`00bd5144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5144.md) [`00bd524c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd524c.md) [`00bd5414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd5414.md) [`00bd56c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd5/00bd56c4.md) · 呼出先 1件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbaa40",
      "incomplete_value": false,
      "site": "00bbaa44",
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
            "const:b51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bba978",
      "incomplete_value": false,
      "site": "00bba97c",
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
            "const:ac4:8"
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
      "00bbaa40",
      "PARAM",
      [
        "storage",
        "00298ac4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaa40",
      "PARAM",
      [
        "storage",
        "00298b51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bba97c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md#insn-00bba97c) · [`00bba970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md#insn-00bba970) · [`00bba978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba964.md#insn-00bba978)
- 新版 [`00bbaa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa44) · [`00bbaa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa38) · [`00bbaa40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa2c.md#insn-00bbaa40)

~~~diff
- 00bba97c ["INT_ADD", "register:40f0:8", ["const:bba97c:8", "const:4:8"]]
- 00bba97c ["CALL", null, ["callee:00bbb158:8"]]
+ 00bbaa44 ["INT_ADD", "register:40f0:8", ["const:bbaa44:8", "const:4:8"]]
+ 00bbaa44 ["CALL", null, ["callee:00bbb158:8"]]
- 00bba97c bytes c5010094
+ 00bbaa44 bytes c5010094
- 00bba970 ["COPY", "register:0:8", ["register:4000:8"]]
- 00bba970 ["INT_ADD", "register:40f0:8", ["const:bba970:8", "const:4:8"]]
- 00bba970 ["CALLIND", null, ["register:0:8"]]
+ 00bbaa38 ["COPY", "register:0:8", ["register:4000:8"]]
+ 00bbaa38 ["INT_ADD", "register:40f0:8", ["const:bbaa38:8", "const:4:8"]]
+ 00bbaa38 ["CALLIND", null, ["register:0:8"]]
- 00bba970 bytes 00003fd6
+ 00bbaa38 bytes 00003fd6
- 00bba978 ["COPY", "tmp:0:8", ["const:ac4:8"]]
- 00bba978 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bba978 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bba978 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa40 ["COPY", "tmp:0:8", ["const:b51:8"]]
+ 00bbaa40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbaa40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bba978 bytes 00102b91
+ 00bbaa40 bytes 00442d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d8dafaa7f9e7e72a38f0801bec3d5f2"></a>

### [`00bba9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba9a8.md) → [`00bbaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md) FUN_00bbaa70

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00bba8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba8d8.md) [`00bba950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba950.md) [`00bbab48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab48.md) · 呼出先 6件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbb3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb3b4.md) [`00bd4ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ecc.md) [`00bd4ed8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd4/00bd4ed8.md) [`00be1ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1ce0.md)
- 新版 呼出元 3件 [`00bba9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9a0.md) [`00bbaa18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa18.md) [`00bbac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbac10.md) · 呼出先 6件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbb47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md) [`00bd4f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4f94.md) [`00bd4fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd4/00bd4fa0.md) [`00be1d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1d90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.78% / 新版 91.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbaae0",
      "incomplete_value": true,
      "site": "00bbaae4",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbaa18",
      "incomplete_value": true,
      "site": "00bbaa1c",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4040:8"
              ],
              [
                "leaf",
                "const:8a0:8"
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
      "00bbaadc",
      "PARAM",
      [
        "storage",
        "002a01be",
        null,
        "string"
      ]
    ],
    [
      "00bbaae0",
      "READ",
      [
        "storage",
        "00c248a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaae0",
      "PARAM",
      [
        "storage",
        "002999fd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbaadc",
      "PARAM",
      [
        "storage",
        "002a024b",
        null,
        "string"
      ]
    ],
    [
      "00bbaae0",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaae0",
      "PARAM",
      [
        "storage",
        "00299a8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbaa1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba9a8.md#insn-00bbaa1c) · [`00bba9bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba9a8.md#insn-00bba9bc) · [`00bba9d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba9a8.md#insn-00bba9d4)
- 新版 [`00bbaae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaae4) · [`00bbaa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaa84) · [`00bbaa9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md#insn-00bbaa9c)

~~~diff
- 00bbaa1c ["INT_ADD", "register:40f0:8", ["const:bbaa1c:8", "const:4:8"]]
- 00bbaa1c ["CALL", null, ["callee:00bbb158:8"]]
+ 00bbaae4 ["INT_ADD", "register:40f0:8", ["const:bbaae4:8", "const:4:8"]]
+ 00bbaae4 ["CALL", null, ["callee:00bbb158:8"]]
- 00bbaa1c bytes 9d010094
+ 00bbaae4 bytes 9d010094
- 00bba9bc ["INT_ADD", "register:40f0:8", ["const:bba9bc:8", "const:4:8"]]
- 00bba9bc ["CALL", null, ["callee:00be1d90:8"]]
+ 00bbaa84 ["INT_ADD", "register:40f0:8", ["const:bbaa84:8", "const:4:8"]]
+ 00bbaa84 ["CALL", null, ["callee:00be1d90:8"]]
- 00bba9bc bytes c99c0094
+ 00bbaa84 bytes c39c0094
- 00bba9d4 ["INT_ADD", "register:40f0:8", ["const:bba9d4:8", "const:4:8"]]
- 00bba9d4 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bbaa9c ["INT_ADD", "register:40f0:8", ["const:bbaa9c:8", "const:4:8"]]
+ 00bbaa9c ["CALL", null, ["callee:00bbb158:8"]]
- 00bba9d4 bytes af010094
+ 00bbaa9c bytes af010094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82f26159aaf0038f9ada00043b253df8"></a>

### [`00bbaaf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md) → [`00bbabbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md) FUN_00bbabbc

採用 · 移動量 `+0xc8` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00bba8c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba8c4.md) [`00bba934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba934.md) [`00bbab14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbab14.md) · 呼出先 1件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 3件 [`00bba98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba98c.md) [`00bba9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9fc.md) [`00bbabdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabdc.md) · 呼出先 1件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bbabd4",
      "incomplete_value": true,
      "site": "00bbabd4",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbab0c",
      "incomplete_value": true,
      "site": "00bbab0c",
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
            "const:8a0:8"
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
      "00bbabd4",
      "WRITE",
      [
        "storage",
        "00c248a0",
        null,
        "pointer"
      ]
    ],
    [
      "00bbabd4",
      "DATA",
      [
        "storage",
        "002a1122",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbabd4",
      "WRITE",
      [
        "storage",
        "00c24950",
        null,
        "pointer"
      ]
    ],
    [
      "00bbabd4",
      "DATA",
      [
        "storage",
        "002a11af",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbab0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md#insn-00bbab0c) · [`00bbab08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md#insn-00bbab08) · [`00bbab10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbaaf4.md#insn-00bbab10)
- 新版 [`00bbabd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd4) · [`00bbabd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd0) · [`00bbabd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbabbc.md#insn-00bbabd8)

~~~diff
- 00bbab0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8a0:8"]]
- 00bbab0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bbabd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
+ 00bbabd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bbab0c bytes 095104f9
+ 00bbabd4 bytes 09a904f9
- 00bbab08 ["COPY", "tmp:0:8", ["const:122:8"]]
- 00bbab08 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bbab08 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bbab08 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bbabd0 ["COPY", "tmp:0:8", ["const:1af:8"]]
+ 00bbabd0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bbabd0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bbabd0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bbab08 bytes 29890491
+ 00bbabd0 bytes 29bd0691
- 00bbab10 ["INT_ADD", "register:40f0:8", ["const:bbab10:8", "const:4:8"]]
- 00bbab10 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bbabd8 ["INT_ADD", "register:40f0:8", ["const:bbabd8:8", "const:4:8"]]
+ 00bbabd8 ["CALL", null, ["callee:00bdb180:8"]]
- 00bbab10 bytes 70810094
+ 00bbabd8 bytes 6a810094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb98261b804f750f910449dea5e848cb"></a>

### [`00bbade0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md) → [`00bbaea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) _ZNSt14overflow_errorD1Ev

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006ad854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/006ad/006ad854.md) [`00b7320c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b7320c.md) [`00b73974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b73/00b73974.md) [`00bdd970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd970.md) [`00be0e70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0e70.md) · 呼出先 3件 [`00bd6d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb390.md)
- 新版 呼出元 8件 [`006ad854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ad/006ad854.md) [`00b732d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b732d4.md) [`00b73a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b73/00b73a3c.md) [`00bdda20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda20.md) [`00be0f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f20.md) · 呼出先 3件 [`00bd6df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6df0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbaec8",
      "incomplete_value": true,
      "site": "00bbaed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00bbae00",
      "incomplete_value": true,
      "site": "00bbae08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00bbaec0",
      "READ",
      [
        "storage",
        "00c1bb68",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaed0",
      "DATA",
      [
        "storage",
        "00c16858",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00bbaec0",
      "READ",
      [
        "storage",
        "00c1bc18",
        null,
        "pointer"
      ]
    ],
    [
      "00bbaed0",
      "DATA",
      [
        "storage",
        "00c16908",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbadf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md#insn-00bbadf8) · [`00bbae10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md#insn-00bbae10) · [`00bbae20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbade0.md#insn-00bbae20)
- 新版 [`00bbaec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaec0) · [`00bbaed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaed8) · [`00bbaee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md#insn-00bbaee8)

~~~diff
- 00bbadf8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b68:8"]]
- 00bbadf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbaec0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
+ 00bbaec0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbadf8 bytes 08b545f9
+ 00bbaec0 bytes 080d46f9
- 00bbae10 ["INT_ADD", "register:40f0:8", ["const:bbae10:8", "const:4:8"]]
- 00bbae10 ["CALL", null, ["callee:00bd6df0:8"]]
+ 00bbaed8 ["INT_ADD", "register:40f0:8", ["const:bbaed8:8", "const:4:8"]]
+ 00bbaed8 ["CALL", null, ["callee:00bd6df0:8"]]
- 00bbae10 bytes c86f0094
+ 00bbaed8 bytes c66f0094
- 00bbae20 ["INT_ADD", "register:40f0:8", ["const:bbae20:8", "const:4:8"]]
- 00bbae20 ["CALL", null, ["callee:00bdb010:8"]]
+ 00bbaee8 ["INT_ADD", "register:40f0:8", ["const:bbaee8:8", "const:4:8"]]
+ 00bbaee8 ["CALL", null, ["callee:00bdb010:8"]]
- 00bbae20 bytes 50800094
+ 00bbaee8 bytes 4a800094
~~~


<a id="compare-247f8f5c79c1895110a19dceb1ef6ad8"></a>

### [`00bbb024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb024.md) → [`00bbb0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0ec.md) _ZNKSt8bad_cast4whatEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bbb0f4",
      "incomplete_value": false,
      "site": "00bbb0f8",
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
            "const:505:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb02c",
      "incomplete_value": false,
      "site": "00bbb030",
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
            "const:478:8"
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
      "00bbb0f4",
      "DATA",
      [
        "storage",
        "00294478",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb0f4",
      "DATA",
      [
        "storage",
        "00294505",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb02c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb024.md#insn-00bbb02c)
- 新版 [`00bbb0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb0ec.md#insn-00bbb0f4)

~~~diff
- 00bbb02c ["COPY", "tmp:0:8", ["const:478:8"]]
- 00bbb02c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb02c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb02c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbb0f4 ["COPY", "tmp:0:8", ["const:505:8"]]
+ 00bbb0f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb0f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb0f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbb02c bytes 00e01191
+ 00bbb0f4 bytes 00141491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9bf7bc499a4614498c91ebdb6f83c13"></a>

### [`00bbb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb080.md) → [`00bbb148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb148.md) _ZNKSt10bad_typeid4whatEv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00bbb150",
      "incomplete_value": false,
      "site": "00bbb154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:775:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb088",
      "incomplete_value": false,
      "site": "00bbb08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ad000:8"
          ],
          [
            "leaf",
            "const:77e:8"
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
      "00bbb150",
      "DATA",
      [
        "storage",
        "002ad77e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbb150",
      "DATA",
      [
        "storage",
        "002ad775",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb080.md#insn-00bbb088)
- 新版 [`00bbb150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb148.md#insn-00bbb150)

~~~diff
- 00bbb088 ["COPY", "tmp:0:8", ["const:77e:8"]]
- 00bbb088 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb088 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bbb088 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bbb150 ["COPY", "tmp:0:8", ["const:775:8"]]
+ 00bbb150 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb150 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bbb150 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bbb088 bytes 00f81d91
+ 00bbb150 bytes 00d41d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47ed39b93c80b8267cc485a53e4b39d8"></a>

### [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) → [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) FUN_00bbb158

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 22件 [`00bba5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba5f4.md) [`00bba738`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba738.md) [`00bba7e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba7e0.md) [`00bba87c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba87c.md) [`00bba918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba918.md) · 呼出先 10件 [`00bdd2d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd2d0.md) [`00bdd330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd330.md) [`00bde1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1c0.md) [`00be1610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1610.md) [`00be1db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1db0.md)
- 新版 呼出元 22件 [`00bba6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba6bc.md) [`00bba800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba800.md) [`00bba8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) [`00bba944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba944.md) [`00bba9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba9e0.md) · 呼出先 10件 [`00bdd380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd380.md) [`00bdd3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3e0.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md) [`00be16c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be16c0.md) [`00be1e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1e60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb1b4",
      "incomplete_value": true,
      "site": "00bbb1b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb0ec",
      "incomplete_value": true,
      "site": "00bbb0f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb248",
      "incomplete_value": false,
      "site": "00bbb250",
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
            "const:d0d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb180",
      "incomplete_value": false,
      "site": "00bbb188",
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
            "const:c80:8"
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
      "00bbb1b0",
      "READ",
      [
        "storage",
        "00c1bc48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb230",
      "PARAM",
      [
        "storage",
        "002ae6ac",
        null,
        "string"
      ]
    ],
    [
      "00bbb248",
      "PARAM",
      [
        "storage",
        "0029dc80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bbb1b0",
      "READ",
      [
        "storage",
        "00c1bcf8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb230",
      "PARAM",
      [
        "storage",
        "002ae618",
        null,
        "string"
      ]
    ],
    [
      "00bbb248",
      "PARAM",
      [
        "storage",
        "0029dd0d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb0f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md#insn-00bbb0f0) · [`00bbb188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md#insn-00bbb188) · [`00bbb0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md#insn-00bbb0e8)
- 新版 [`00bbb1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb1b8) · [`00bbb250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb250) · [`00bbb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md#insn-00bbb1b0)

~~~diff
- 00bbb0f0 ["INT_ADD", "register:40f0:8", ["const:bbb0f0:8", "const:4:8"]]
- 00bbb0f0 ["CALL", null, ["callee:00bdd380:8"]]
+ 00bbb1b8 ["INT_ADD", "register:40f0:8", ["const:bbb1b8:8", "const:4:8"]]
+ 00bbb1b8 ["CALL", null, ["callee:00bdd380:8"]]
- 00bbb0f0 bytes 78880094
+ 00bbb1b8 bytes 72880094
- 00bbb188 ["INT_ADD", "register:40f0:8", ["const:bbb188:8", "const:4:8"]]
- 00bbb188 ["CALL", null, ["callee:00be1e90:8"]]
+ 00bbb250 ["INT_ADD", "register:40f0:8", ["const:bbb250:8", "const:4:8"]]
+ 00bbb250 ["CALL", null, ["callee:00be1e90:8"]]
- 00bbb188 bytes 169b0094
+ 00bbb250 bytes 109b0094
- 00bbb0e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c48:8"]]
- 00bbb0e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbb1b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00bbb1b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbb0e8 bytes 942646f9
+ 00bbb1b0 bytes 947e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf85da8687d3c16d3d2a83a76c39496"></a>

### [`00bbb3b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb3b4.md) → [`00bbb47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md) FUN_00bbb47c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bba9a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bba9a8.md) · 呼出先 2件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 1件 [`00bbaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaa70.md) · 呼出先 2件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.22% / 新版 93.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbb4b0",
      "incomplete_value": true,
      "site": "00bbb4c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "live",
            "register:4010:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb3e8",
      "incomplete_value": true,
      "site": "00bbb3fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4010:8"
              ],
              [
                "leaf",
                "const:f50:8"
              ]
            ]
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
      "00bbb4ac",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4b0",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4b0",
      "PARAM",
      [
        "storage",
        "00c16b28",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbb4ac",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4b0",
      "READ",
      [
        "storage",
        "00c1c000",
        null,
        "pointer"
      ]
    ],
    [
      "00bbb4b0",
      "PARAM",
      [
        "storage",
        "00c16bd8",
        "_ZTIN10__cxxabiv117__class_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb3b4.md#insn-00bbb3fc) · [`00bbb3e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb3b4.md#insn-00bbb3e0) · [`00bbb3e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb3b4.md#insn-00bbb3e4)
- 新版 [`00bbb4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4c4) · [`00bbb4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4a8) · [`00bbb4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb47c.md#insn-00bbb4ac)

~~~diff
- 00bbb3fc ["INT_ADD", "register:40f0:8", ["const:bbb3fc:8", "const:4:8"]]
- 00bbb3fc ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbb4c4 ["INT_ADD", "register:40f0:8", ["const:bbb4c4:8", "const:4:8"]]
+ 00bbb4c4 ["CALL", null, ["callee:00bdb770:8"]]
- 00bbb3fc bytes b1800094
+ 00bbb4c4 bytes ab800094
- 00bbb3e0 ["COPY", "register:4010:8", ["const:c1b000:8"]]
+ 00bbb4a8 ["COPY", "register:4010:8", ["const:c1c000:8"]]
- 00bbb3e0 bytes 02030090
+ 00bbb4a8 bytes 020300b0
- 00bbb3e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00bbb3e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbb4ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff8:8"]]
+ 00bbb4ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbb3e4 bytes 08a547f9
+ 00bbb4ac bytes 08fd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce1b251897c3270fc1b58f1d1b4f7b01"></a>

### [`00bbb998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb998.md) → [`00bbba60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md) FUN_00bbba60

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbac0",
      "incomplete_value": true,
      "site": "00bbbac4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbb9f8",
      "incomplete_value": true,
      "site": "00bbb9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "definition_site": "00bbbab0",
      "incomplete_value": true,
      "site": "00bbbac4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
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
      "definition_site": "00bbb9e8",
      "incomplete_value": true,
      "site": "00bbb9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
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
      "00bbbaac",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbab0",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbab0",
      "PARAM",
      [
        "storage",
        "00c16b40",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbaac",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbab0",
      "READ",
      [
        "storage",
        "00c1c008",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbab0",
      "PARAM",
      [
        "storage",
        "00c16bf0",
        "_ZTIN10__cxxabiv117__pbase_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbb9fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb998.md#insn-00bbb9fc) · [`00bbb9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb998.md#insn-00bbb9c4) · [`00bbb9dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb998.md#insn-00bbb9dc)
- 新版 [`00bbbac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbbac4) · [`00bbba8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbba8c) · [`00bbbaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbba60.md#insn-00bbbaa4)

~~~diff
- 00bbb9fc ["INT_ADD", "register:40f0:8", ["const:bbb9fc:8", "const:4:8"]]
- 00bbb9fc ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbbac4 ["INT_ADD", "register:40f0:8", ["const:bbbac4:8", "const:4:8"]]
+ 00bbbac4 ["CALL", null, ["callee:00bdb770:8"]]
- 00bbb9fc bytes 317f0094
+ 00bbbac4 bytes 2b7f0094
- 00bbb9c4 ["INT_ADD", "register:40f0:8", ["const:bbb9c4:8", "const:4:8"]]
- 00bbb9c4 ["CALL", null, ["callee:00bde980:8"]]
+ 00bbba8c ["INT_ADD", "register:40f0:8", ["const:bbba8c:8", "const:4:8"]]
+ 00bbba8c ["CALL", null, ["callee:00bde980:8"]]
- 00bbb9c4 bytes c38b0094
+ 00bbba8c bytes bd8b0094
- 00bbb9dc ["COPY", "register:4010:8", ["const:c1b000:8"]]
+ 00bbbaa4 ["COPY", "register:4010:8", ["const:c1c000:8"]]
- 00bbb9dc bytes 02030090
+ 00bbbaa4 bytes 020300b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b4b13ef3ad9be33b818a26b28480e86a"></a>

### [`00bbba44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md) → [`00bbbb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md) FUN_00bbbb0c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bbbd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md) [`00bbbdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbdf4.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bbbdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) [`00bbbebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbebc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 89.14% / 新版 89.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 9件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbb38",
      "incomplete_value": true,
      "site": "00bbbb3c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00bbba70",
      "incomplete_value": true,
      "site": "00bbba74",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00bbbc4c",
      "incomplete_value": true,
      "site": "00bbbc50",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
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
      "definition_site": "00bbbb84",
      "incomplete_value": true,
      "site": "00bbbb88",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:4040:8"
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
    "ordinal": 13,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbbd4",
      "incomplete_value": true,
      "site": "00bbbbe0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbb0c",
      "incomplete_value": true,
      "site": "00bbbb18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "00bbbb34",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbb9c",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbb9c",
      "PARAM",
      [
        "storage",
        "00c16b10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbb34",
      "READ",
      [
        "storage",
        "00c1c010",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbb9c",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbb9c",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md#insn-00bbbad4) · [`00bbbb18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md#insn-00bbbb18) · [`00bbbb9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md#insn-00bbbb9c)
- 新版 [`00bbbb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbb9c) · [`00bbbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbbe0) · [`00bbbc64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md#insn-00bbbc64)

~~~diff
- 00bbbad4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f48:8"]]
- 00bbbad4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbbb9c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 00bbbb9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbad4 bytes 21a447f9
+ 00bbbb9c bytes 21fc47f9
- 00bbbb18 ["INT_ADD", "register:40f0:8", ["const:bbbb18:8", "const:4:8"]]
- 00bbbb18 ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbbbe0 ["INT_ADD", "register:40f0:8", ["const:bbbbe0:8", "const:4:8"]]
+ 00bbbbe0 ["CALL", null, ["callee:00bdb770:8"]]
- 00bbbb18 bytes ea7e0094
+ 00bbbbe0 bytes e47e0094
- 00bbbb9c ["INT_ADD", "register:40f0:8", ["const:bbbb9c:8", "const:4:8"]]
- 00bbbb9c ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbbc64 ["INT_ADD", "register:40f0:8", ["const:bbbc64:8", "const:4:8"]]
+ 00bbbc64 ["CALL", null, ["callee:00bdb770:8"]]
- 00bbbb9c bytes c97e0094
+ 00bbbc64 bytes c37e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e94091185e52a6be70a46f45fd78a02c"></a>

### [`00bbbd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md) → [`00bbbdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md) FUN_00bbbdc8

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbba44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md) · 呼出先 2件 [`00bbbdf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbdf4.md) [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md)
- 新版 呼出元 1件 [`00bbbb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbb0c.md) · 呼出先 2件 [`00bbbebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbebc.md) [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbe68",
      "incomplete_value": true,
      "site": "00bbbe74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbda0",
      "incomplete_value": true,
      "site": "00bbbdac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "definition_site": "00bbbe6c",
      "incomplete_value": true,
      "site": "00bbbe74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbda4",
      "incomplete_value": true,
      "site": "00bbbdac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f80:8"
              ]
            ]
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
      "00bbbdec",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbdf0",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe00",
      "PARAM",
      [
        "storage",
        "00c16b10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbdec",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbdf0",
      "READ",
      [
        "storage",
        "00c1c018",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbe00",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbdac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md#insn-00bbbdac) · [`00bbbd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md#insn-00bbbd1c) · [`00bbbd24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbd00.md#insn-00bbbd24)
- 新版 [`00bbbe74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbe74) · [`00bbbde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbde4) · [`00bbbdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbdc8.md#insn-00bbbdec)

~~~diff
- 00bbbdac ["INT_ADD", "register:40f0:8", ["const:bbbdac:8", "const:4:8"]]
- 00bbbdac ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbbe74 ["INT_ADD", "register:40f0:8", ["const:bbbe74:8", "const:4:8"]]
+ 00bbbe74 ["CALL", null, ["callee:00bdb770:8"]]
- 00bbbdac bytes 457e0094
+ 00bbbe74 bytes 3f7e0094
- 00bbbd1c ["COPY", "register:40a8:8", ["const:c1b000:8"]]
+ 00bbbde4 ["COPY", "register:40a8:8", ["const:c1c000:8"]]
- 00bbbd1c bytes 15030090
+ 00bbbde4 bytes 150300b0
- 00bbbd24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f48:8"]]
- 00bbbd24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbbdec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00bbbdec ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbd24 bytes 94a647f9
+ 00bbbdec bytes 94fe47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8340ce8479ec6e2134df1e28dd611903"></a>

### [`00bbbe94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md) → [`00bbbf5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md) FUN_00bbbf5c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb6c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb6c0.md) [`00bde8d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde8d0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb770.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbbfcc",
      "incomplete_value": true,
      "site": "00bbbfdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf04",
      "incomplete_value": true,
      "site": "00bbbf14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "definition_site": "00bbbfd8",
      "incomplete_value": true,
      "site": "00bbbfdc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:c1c000:8"
              ],
              [
                "leaf",
                "const:28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf10",
      "incomplete_value": true,
      "site": "00bbbf14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbc000",
      "incomplete_value": true,
      "site": "00bbc00c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ff8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbbf38",
      "incomplete_value": true,
      "site": "00bbbf44",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f48:8"
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
      "00bbbf7c",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbfcc",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbfcc",
      "PARAM",
      [
        "storage",
        "00c16b10",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00bbbf7c",
      "READ",
      [
        "storage",
        "00c1c010",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbfcc",
      "READ",
      [
        "storage",
        "00c1bff8",
        null,
        "pointer"
      ]
    ],
    [
      "00bbbfcc",
      "PARAM",
      [
        "storage",
        "00c16bc0",
        "_ZTIN10__cxxabiv116__shim_type_infoE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbbeb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md#insn-00bbbeb4) · [`00bbbf14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md#insn-00bbbf14) · [`00bbbf44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md#insn-00bbbf44)
- 新版 [`00bbbf7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbbf7c) · [`00bbbfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbbfdc) · [`00bbc00c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md#insn-00bbc00c)

~~~diff
- 00bbbeb4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
- 00bbbeb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bbbf7c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:10:8"]]
+ 00bbbf7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bbbeb4 bytes 08b147f9
+ 00bbbf7c bytes 080940f9
- 00bbbf14 ["INT_ADD", "register:40f0:8", ["const:bbbf14:8", "const:4:8"]]
- 00bbbf14 ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbbfdc ["INT_ADD", "register:40f0:8", ["const:bbbfdc:8", "const:4:8"]]
+ 00bbbfdc ["CALL", null, ["callee:00bdb770:8"]]
- 00bbbf14 bytes eb7d0094
+ 00bbbfdc bytes e57d0094
- 00bbbf44 ["INT_ADD", "register:40f0:8", ["const:bbbf44:8", "const:4:8"]]
- 00bbbf44 ["CALL", null, ["callee:00bdb770:8"]]
+ 00bbc00c ["INT_ADD", "register:40f0:8", ["const:bbc00c:8", "const:4:8"]]
+ 00bbc00c ["CALL", null, ["callee:00bdb770:8"]]
- 00bbbf44 bytes df7d0094
+ 00bbc00c bytes d97d0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3324f0831d8f66f3bd556af7f8e7a8"></a>

### [`00bbcb04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md) → [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) __cxa_demangle

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1d30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be1/00be1d30.md) · 呼出先 10件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md)
- 新版 呼出元 1件 [`00be1de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1de0.md) · 呼出先 10件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbcf14",
      "incomplete_value": false,
      "site": "00bbcf14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:9e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbce4c",
      "incomplete_value": false,
      "site": "00bbce4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:938:8"
          ]
        ]
      ]
    },
    "ordinal": 90,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbd164",
      "incomplete_value": false,
      "site": "00bbd16c",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd09c",
      "incomplete_value": false,
      "site": "00bbd0a4",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbcf14",
      "DATA",
      [
        "storage",
        "00c19938",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd06c",
      "PARAM",
      [
        "storage",
        "002a9176",
        null,
        "string"
      ]
    ],
    [
      "00bbd164",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bbcf14",
      "DATA",
      [
        "storage",
        "00c199e8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd06c",
      "PARAM",
      [
        "storage",
        "002a90e2",
        null,
        "string"
      ]
    ],
    [
      "00bbd164",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd0a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md#insn-00bbd0a4) · [`00bbcb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md#insn-00bbcb60) · [`00bbccec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md#insn-00bbccec)
- 新版 [`00bbd16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbd16c) · [`00bbcc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbcc28) · [`00bbcdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md#insn-00bbcdb4)

~~~diff
- 00bbd0a4 ["INT_ADD", "register:40f0:8", ["const:bbd0a4:8", "const:4:8"]]
- 00bbd0a4 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bbd16c ["INT_ADD", "register:40f0:8", ["const:bbd16c:8", "const:4:8"]]
+ 00bbd16c ["CALL", null, ["callee:00bbb158:8"]]
- 00bbd0a4 bytes fbf7ff97
+ 00bbd16c bytes fbf7ff97
- 00bbcb60 ["INT_ADD", "register:40f0:8", ["const:bbcb60:8", "const:4:8"]]
- 00bbcb60 ["CALL", null, ["callee:00bdb140:8"]]
+ 00bbcc28 ["INT_ADD", "register:40f0:8", ["const:bbcc28:8", "const:4:8"]]
+ 00bbcc28 ["CALL", null, ["callee:00bdb140:8"]]
- 00bbcb60 bytes 4c790094
+ 00bbcc28 bytes 46790094
- 00bbccec ["INT_ADD", "register:40f0:8", ["const:bbccec:8", "const:4:8"]]
- 00bbccec ["CALL", null, ["callee:00bbde18:8"]]
+ 00bbcdb4 ["INT_ADD", "register:40f0:8", ["const:bbcdb4:8", "const:4:8"]]
+ 00bbcdb4 ["CALL", null, ["callee:00bbde18:8"]]
- 00bbccec bytes 19040094
+ 00bbcdb4 bytes 19040094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be4b6524bb12f82041563cac099ec756"></a>

### [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) → [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) FUN_00bbd2c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`00bbcb04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc47d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc4/00bc47d4.md) · 呼出先 31件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc10.md) [`00bbdc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md)
- 新版 呼出元 5件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc4/00bc489c.md) · 呼出先 31件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.42% / 新版 98.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbd4ec",
      "incomplete_value": false,
      "site": "00bbd4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd424",
      "incomplete_value": false,
      "site": "00bbd424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bbd930",
      "incomplete_value": false,
      "site": "00bbd930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:908:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbd868",
      "incomplete_value": false,
      "site": "00bbd868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:858:8"
          ]
        ]
      ]
    },
    "ordinal": 67,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbdb34",
      "incomplete_value": false,
      "site": "00bbdb40",
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
            "const:454:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbda6c",
      "incomplete_value": false,
      "site": "00bbda78",
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
            "const:45b:8"
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
      "00bbd4ec",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd790",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7b4",
      "DATA",
      [
        "storage",
        "002a020f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbd4ec",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd790",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbd7b4",
      "DATA",
      [
        "storage",
        "002a029c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbd7a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md#insn-00bbd7a0) · [`00bbda78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md#insn-00bbda78) · [`00bbdbc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md#insn-00bbdbc0)
- 新版 [`00bbd868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbd868) · [`00bbdb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbdb40) · [`00bbdc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md#insn-00bbdc88)

~~~diff
- 00bbd7a0 ["INT_ADD", "register:40f0:8", ["const:bbd7a0:8", "const:4:8"]]
- 00bbd7a0 ["CALL", null, ["local:b0:8"]]
+ 00bbd868 ["INT_ADD", "register:40f0:8", ["const:bbd868:8", "const:4:8"]]
+ 00bbd868 ["CALL", null, ["local:b0:8"]]
- 00bbd7a0 bytes 97feff97
+ 00bbd868 bytes 97feff97
- 00bbda78 ["INT_ADD", "register:40f0:8", ["const:bbda78:8", "const:4:8"]]
- 00bbda78 ["CALL", null, ["callee:00bbdd64:8"]]
+ 00bbdb40 ["INT_ADD", "register:40f0:8", ["const:bbdb40:8", "const:4:8"]]
+ 00bbdb40 ["CALL", null, ["callee:00bbdd64:8"]]
- 00bbda78 bytes 89000094
+ 00bbdb40 bytes 89000094
- 00bbdbc0 ["INT_ADD", "register:40f0:8", ["const:bbdbc0:8", "const:4:8"]]
- 00bbdbc0 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bbdc88 ["INT_ADD", "register:40f0:8", ["const:bbdc88:8", "const:4:8"]]
+ 00bbdc88 ["CALL", null, ["callee:00bbb158:8"]]
- 00bbdbc0 bytes 34f5ff97
+ 00bbdc88 bytes 34f5ff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76374fa903a446d9d21da74a7270880"></a>

### [`00bbdc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md) → [`00bbdd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md) FUN_00bbdd64

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bbcb04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb090.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 2件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 3件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.56% / 新版 95.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbddd4",
      "incomplete_value": true,
      "site": "00bbddd4",
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
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdd0c",
      "incomplete_value": true,
      "site": "00bbdd0c",
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
            "const:6a8:8"
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
      "00bbddd4",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbddd4",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbdcd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md#insn-00bbdcd4) · [`00bbdcfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md#insn-00bbdcfc) · [`00bbdd04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc9c.md#insn-00bbdd04)
- 新版 [`00bbdd9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbdd9c) · [`00bbddc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbddc4) · [`00bbddcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdd64.md#insn-00bbddcc)

~~~diff
- 00bbdcd4 ["INT_ADD", "register:40f0:8", ["const:bbdcd4:8", "const:4:8"]]
- 00bbdcd4 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bbdd9c ["INT_ADD", "register:40f0:8", ["const:bbdd9c:8", "const:4:8"]]
+ 00bbdd9c ["CALL", null, ["callee:00bdd180:8"]]
- 00bbdcd4 bytes ff7c0094
+ 00bbdd9c bytes f97c0094
- 00bbdcfc ["INT_ADD", "register:40f0:8", ["const:bbdcfc:8", "const:4:8"]]
- 00bbdcfc ["CALL", null, ["callee:00bdb140:8"]]
+ 00bbddc4 ["INT_ADD", "register:40f0:8", ["const:bbddc4:8", "const:4:8"]]
+ 00bbddc4 ["CALL", null, ["callee:00bdb140:8"]]
- 00bbdcfc bytes e5740094
+ 00bbddc4 bytes df740094
- 00bbdd04 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bbdd04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bbdd04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bbdd04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bbddcc ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bbddcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbddcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbddcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bbdd04 bytes 08a11a91
+ 00bbddcc bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33ec3213693ec8ba68555d3fd26af285"></a>

### [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) → [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) FUN_00bbde18

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 15件 [`00bbcb04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbcb04.md) [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 38件 [`00bbdc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc10.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bbfcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfcec.md) [`00bc1260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1260.md)
- 新版 呼出元 15件 [`00bbcbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcbcc.md) [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 38件 [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bbfdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfdb4.md) [`00bc1328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1328.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbdf7c",
      "incomplete_value": false,
      "site": "00bbdf7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdeb4",
      "incomplete_value": false,
      "site": "00bbdeb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00bbdffc",
      "incomplete_value": false,
      "site": "00bbdffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbdf34",
      "incomplete_value": false,
      "site": "00bbdf34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "definition_site": "00bbe0dc",
      "incomplete_value": false,
      "site": "00bbe0dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbe014",
      "incomplete_value": false,
      "site": "00bbe014",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:798:8"
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
      "00bbde64",
      "DATA",
      [
        "storage",
        "002fcb68",
        "switchD_00bbdda4::switchdataD_002fcb68",
        "ushort"
      ]
    ],
    [
      "00bbdf7c",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbdffc",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbde64",
      "DATA",
      [
        "storage",
        "002fcb68",
        "switchD_00bbde6c::switchdataD_002fcb68",
        "ushort"
      ]
    ],
    [
      "00bbdf7c",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbdffc",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbe354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md#insn-00bbe354) · [`00bbdd98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md#insn-00bbdd98) · [`00bbde54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md#insn-00bbde54)
- 新版 [`00bbe41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbe41c) · [`00bbde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbde60) · [`00bbdf1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md#insn-00bbdf1c)

~~~diff
- 00bbe354 ["COPY", "tmp:0:8", ["const:798:8"]]
- 00bbe354 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bbe354 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bbe354 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bbe41c ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00bbe41c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbe41c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbe41c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bbe354 bytes 08611e91
+ 00bbe41c bytes 08212191
- 00bbdd98 ["COPY", "register:4070:8", ["const:bbdda8:8"]]
+ 00bbde60 ["COPY", "register:4070:8", ["const:bbde70:8"]]
- 00bbdd98 bytes 8e000010
+ 00bbde60 bytes 8e000010
- 00bbde54 ["INT_ADD", "register:40f0:8", ["const:bbde54:8", "const:4:8"]]
- 00bbde54 ["CALL", null, ["callee:00bd1734:8"]]
+ 00bbdf1c ["INT_ADD", "register:40f0:8", ["const:bbdf1c:8", "const:4:8"]]
+ 00bbdf1c ["CALL", null, ["callee:00bd1734:8"]]
- 00bbde54 bytes 064e0094
+ 00bbdf1c bytes 064e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68208e9b41fd7ea620f0b8167c73dfd5"></a>

### [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) → [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) FUN_00bbf358

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 7件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bc5a44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5a44.md) · 呼出先 19件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdc10.md) [`00bbf0e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf0e8.md) [`00bbf290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md) [`00bc00b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc00b4.md)
- 新版 呼出元 7件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc5b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc5/00bc5b0c.md) · 呼出先 19件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbdcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbdcd8.md) [`00bbf1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf1b0.md) [`00bbf358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md) [`00bc017c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc017c.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.24% / 新版 98.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbf754",
      "incomplete_value": false,
      "site": "00bbf754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbf68c",
      "incomplete_value": false,
      "site": "00bbf68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:798:8"
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbf778",
      "incomplete_value": false,
      "site": "00bbf778",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbf6b0",
      "incomplete_value": false,
      "site": "00bbf6b0",
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
            "const:9c:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bbfa40",
      "incomplete_value": false,
      "site": "00bbfa40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbf978",
      "incomplete_value": false,
      "site": "00bbf978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:698:8"
          ]
        ]
      ]
    },
    "ordinal": 74,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bbf4b8",
      "PARAM",
      [
        "storage",
        "002a1156",
        null,
        "string"
      ]
    ],
    [
      "00bbf638",
      "DATA",
      [
        "storage",
        "00c19698",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbf754",
      "DATA",
      [
        "storage",
        "00c17798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbf4b8",
      "PARAM",
      [
        "storage",
        "002a11e3",
        null,
        "string"
      ]
    ],
    [
      "00bbf638",
      "DATA",
      [
        "storage",
        "00c19748",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbf754",
      "DATA",
      [
        "storage",
        "00c17848",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbf320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md#insn-00bbf320) · [`00bbf370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md#insn-00bbf370) · [`00bbf37c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf290.md#insn-00bbf37c)
- 新版 [`00bbf3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf3e8) · [`00bbf438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf438) · [`00bbf444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbf358.md#insn-00bbf444)

~~~diff
- 00bbf320 ["INT_ADD", "register:40f0:8", ["const:bbf320:8", "const:4:8"]]
- 00bbf320 ["CALL", null, ["callee:00bc15a0:8"]]
+ 00bbf3e8 ["INT_ADD", "register:40f0:8", ["const:bbf3e8:8", "const:4:8"]]
+ 00bbf3e8 ["CALL", null, ["callee:00bc15a0:8"]]
- 00bbf320 bytes 6e080094
+ 00bbf3e8 bytes 6e080094
- 00bbf370 ["INT_ADD", "register:40f0:8", ["const:bbf370:8", "const:4:8"]]
- 00bbf370 ["CALL", null, ["callee:00bdd200:8"]]
+ 00bbf438 ["INT_ADD", "register:40f0:8", ["const:bbf438:8", "const:4:8"]]
+ 00bbf438 ["CALL", null, ["callee:00bdd200:8"]]
- 00bbf370 bytes 78770094
+ 00bbf438 bytes 72770094
- 00bbf37c ["INT_ADD", "register:40f0:8", ["const:bbf37c:8", "const:4:8"]]
- 00bbf37c ["CALL", null, ["callee:00bde270:8"]]
+ 00bbf444 ["INT_ADD", "register:40f0:8", ["const:bbf444:8", "const:4:8"]]
+ 00bbf444 ["CALL", null, ["callee:00bde270:8"]]
- 00bbf37c bytes 917b0094
+ 00bbf444 bytes 8b7b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba49a37d450841a91cb8c18c3a1c16bf"></a>

### [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) → [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) FUN_00bbfa8c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 13件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbdd50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbdd50.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md)
- 新版 呼出元 4件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 13件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbde18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbde18.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bbfd04",
      "incomplete_value": false,
      "site": "00bbfd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:806:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbfc3c",
      "incomplete_value": false,
      "site": "00bbfc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:295000:8"
          ],
          [
            "leaf",
            "const:779:8"
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
      "00bbfcbc",
      "DATA",
      [
        "storage",
        "00c19708",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfcbc",
      "DATA",
      [
        "storage",
        "00c19778",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd04",
      "PARAM",
      [
        "storage",
        "00295779",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bbfcbc",
      "DATA",
      [
        "storage",
        "00c197b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfcbc",
      "DATA",
      [
        "storage",
        "00c19828",
        null,
        "undefined *"
      ]
    ],
    [
      "00bbfd04",
      "PARAM",
      [
        "storage",
        "00295806",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfc40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md#insn-00bbfc40) · [`00bbfa34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md#insn-00bbfa34) · [`00bbfa5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md#insn-00bbfa5c)
- 新版 [`00bbfd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfd08) · [`00bbfafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfafc) · [`00bbfb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md#insn-00bbfb24)

~~~diff
- 00bbfc40 ["INT_ADD", "register:40f0:8", ["const:bbfc40:8", "const:4:8"]]
- 00bbfc40 ["CALL", null, ["callee:00bdb130:8"]]
+ 00bbfd08 ["INT_ADD", "register:40f0:8", ["const:bbfd08:8", "const:4:8"]]
+ 00bbfd08 ["CALL", null, ["callee:00bdb130:8"]]
- 00bbfc40 bytes 106d0094
+ 00bbfd08 bytes 0a6d0094
- 00bbfa34 ["INT_ADD", "register:40f0:8", ["const:bbfa34:8", "const:4:8"]]
- 00bbfa34 ["CALL", null, ["callee:00bbd2c4:8"]]
+ 00bbfafc ["INT_ADD", "register:40f0:8", ["const:bbfafc:8", "const:4:8"]]
+ 00bbfafc ["CALL", null, ["callee:00bbd2c4:8"]]
- 00bbfa34 bytes f2f5ff97
+ 00bbfafc bytes f2f5ff97
- 00bbfa5c ["INT_ADD", "register:40f0:8", ["const:bbfa5c:8", "const:4:8"]]
- 00bbfa5c ["CALL", null, ["callee:00bc2ec8:8"]]
+ 00bbfb24 ["INT_ADD", "register:40f0:8", ["const:bbfb24:8", "const:4:8"]]
+ 00bbfb24 ["CALL", null, ["callee:00bc2ec8:8"]]
- 00bbfa5c bytes e90c0094
+ 00bbfb24 bytes e90c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c156f642a8430bf631f5d6adecc39d99"></a>

### [`00bbfdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfdc4.md) → [`00bbfe8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md) FUN_00bbfe8c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bbfef0",
      "incomplete_value": false,
      "site": "00bbfef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbfe28",
      "incomplete_value": false,
      "site": "00bbfe28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:7e8:8"
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
      "00bbfef0",
      "DATA",
      [
        "storage",
        "00c197e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bbfef0",
      "DATA",
      [
        "storage",
        "00c19898",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfdf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfdc4.md#insn-00bbfdf8) · [`00bbfe1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfdc4.md#insn-00bbfe1c) · [`00bbfe60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfdc4.md#insn-00bbfe60)
- 新版 [`00bbfec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbfec0) · [`00bbfee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbfee4) · [`00bbff28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfe8c.md#insn-00bbff28)

~~~diff
- 00bbfdf8 ["INT_ADD", "register:40f0:8", ["const:bbfdf8:8", "const:4:8"]]
- 00bbfdf8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bbfec0 ["INT_ADD", "register:40f0:8", ["const:bbfec0:8", "const:4:8"]]
+ 00bbfec0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bbfdf8 bytes b6740094
+ 00bbfec0 bytes b0740094
- 00bbfe1c ["COPY", "tmp:0:8", ["const:7e8:8"]]
- 00bbfe1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bbfe1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bbfe1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bbfee4 ["COPY", "tmp:0:8", ["const:898:8"]]
+ 00bbfee4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbfee4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bbfee4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bbfe1c bytes 08a11f91
+ 00bbfee4 bytes 08612291
- 00bbfe60 ["INT_ADD", "register:40f0:8", ["const:bbfe60:8", "const:4:8"]]
- 00bbfe60 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bbff28 ["INT_ADD", "register:40f0:8", ["const:bbff28:8", "const:4:8"]]
+ 00bbff28 ["CALL", null, ["callee:00bdb180:8"]]
- 00bbfe60 bytes 9c6c0094
+ 00bbff28 bytes 966c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4adf1c40939be4962c12b59b92658506"></a>

### [`00bbfe64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md) → [`00bbff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md) FUN_00bbff2c

採用 · 移動量 `+0xc8` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) [`00bbf9c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbf9c4.md) [`00bc1648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc1/00bc1648.md) [`00bc2394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2394.md) [`00bc2e00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc2/00bc2e00.md) · 呼出先 4件 [`00bbb090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbb090.md) [`00bdaff0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaff0.md) [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 10件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) [`00bbfa8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) [`00bc1710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1710.md) [`00bc245c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc245c.md) [`00bc2ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc2/00bc2ec8.md) · 呼出先 4件 [`00bbb158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb158.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.40% / 新版 95.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc0050",
      "incomplete_value": false,
      "site": "00bc0060",
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
            "const:10a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbff88",
      "incomplete_value": false,
      "site": "00bbff98",
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
            "const:7d:8"
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
      "definition_site": "00bc0058",
      "incomplete_value": false,
      "site": "00bc0060",
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
            "const:866:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbff90",
      "incomplete_value": false,
      "site": "00bbff98",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bc0070",
      "incomplete_value": false,
      "site": "00bc0080",
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
            "const:10a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bbffa8",
      "incomplete_value": false,
      "site": "00bbffb8",
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
            "const:7d:8"
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
      "00bc0050",
      "PARAM",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ],
    [
      "00bc0058",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc0070",
      "PARAM",
      [
        "storage",
        "002a207d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0050",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ],
    [
      "00bc0058",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00bc0070",
      "PARAM",
      [
        "storage",
        "002a210a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bbfed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md#insn-00bbfed0) · [`00bbff98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md#insn-00bbff98) · [`00bbffb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbfe64.md#insn-00bbffb8)
- 新版 [`00bbff98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bbff98) · [`00bc0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bc0060) · [`00bc0080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbff2c.md#insn-00bc0080)

~~~diff
- 00bbfed0 ["INT_ADD", "register:40f0:8", ["const:bbfed0:8", "const:4:8"]]
- 00bbfed0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bbff98 ["INT_ADD", "register:40f0:8", ["const:bbff98:8", "const:4:8"]]
+ 00bbff98 ["CALL", null, ["callee:00bdd180:8"]]
- 00bbfed0 bytes 80740094
+ 00bbff98 bytes 7a740094
- 00bbff98 ["INT_ADD", "register:40f0:8", ["const:bbff98:8", "const:4:8"]]
- 00bbff98 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bc0060 ["INT_ADD", "register:40f0:8", ["const:bc0060:8", "const:4:8"]]
+ 00bc0060 ["CALL", null, ["callee:00bbb158:8"]]
- 00bbff98 bytes 3eecff97
+ 00bc0060 bytes 3eecff97
- 00bbffb8 ["INT_ADD", "register:40f0:8", ["const:bbffb8:8", "const:4:8"]]
- 00bbffb8 ["CALL", null, ["callee:00bbb158:8"]]
+ 00bc0080 ["INT_ADD", "register:40f0:8", ["const:bc0080:8", "const:4:8"]]
+ 00bc0080 ["CALL", null, ["callee:00bbb158:8"]]
- 00bbffb8 bytes 36ecff97
+ 00bc0080 bytes 36ecff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bbd5180f94a0c1f78e8e84752431530"></a>

### [`00bbffc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbffc0.md) → [`00bc0088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md) FUN_00bc0088

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0110",
      "incomplete_value": false,
      "site": "00bc0110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0048",
      "incomplete_value": false,
      "site": "00bc0048",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c19000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00bc0110",
      "DATA",
      [
        "storage",
        "00c198c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0110",
      "DATA",
      [
        "storage",
        "00c19978",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0018`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbffc0.md#insn-00bc0018) · [`00bc003c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbffc0.md#insn-00bc003c) · [`00bc00b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbf/00bbffc0.md#insn-00bc00b0)
- 新版 [`00bc00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc00e0) · [`00bc0104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc0104) · [`00bc0178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0088.md#insn-00bc0178)

~~~diff
- 00bc0018 ["INT_ADD", "register:40f0:8", ["const:bc0018:8", "const:4:8"]]
- 00bc0018 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc00e0 ["INT_ADD", "register:40f0:8", ["const:bc00e0:8", "const:4:8"]]
+ 00bc00e0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0018 bytes 2e740094
+ 00bc00e0 bytes 28740094
- 00bc003c ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00bc003c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc003c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc003c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0104 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00bc0104 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0104 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0104 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc003c bytes 08212391
+ 00bc0104 bytes 08e12591
- 00bc00b0 ["INT_ADD", "register:40f0:8", ["const:bc00b0:8", "const:4:8"]]
- 00bc00b0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc0178 ["INT_ADD", "register:40f0:8", ["const:bc0178:8", "const:4:8"]]
+ 00bc0178 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc00b0 bytes 086c0094
+ 00bc0178 bytes 026c0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9d2472598e97dc3fd966b6d0528ee69"></a>

### [`00bc0294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0294.md) → [`00bc035c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md) FUN_00bc035c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc03c0",
      "incomplete_value": false,
      "site": "00bc03c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc02f8",
      "incomplete_value": false,
      "site": "00bc02f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc03e4",
      "incomplete_value": false,
      "site": "00bc03e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:381:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc031c",
      "incomplete_value": false,
      "site": "00bc031c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2aa000:8"
          ],
          [
            "leaf",
            "const:37b:8"
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
      "00bc03c0",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc03e4",
      "DATA",
      [
        "storage",
        "002aa37b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc03c0",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc03e4",
      "DATA",
      [
        "storage",
        "002aa381",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc02c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0294.md#insn-00bc02c8) · [`00bc02ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0294.md#insn-00bc02ec) · [`00bc0314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0294.md#insn-00bc0314)
- 新版 [`00bc0390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc0390) · [`00bc03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc03b4) · [`00bc03dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc035c.md#insn-00bc03dc)

~~~diff
- 00bc02c8 ["INT_ADD", "register:40f0:8", ["const:bc02c8:8", "const:4:8"]]
- 00bc02c8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0390 ["INT_ADD", "register:40f0:8", ["const:bc0390:8", "const:4:8"]]
+ 00bc0390 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc02c8 bytes 82730094
+ 00bc0390 bytes 7c730094
- 00bc02ec ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc02ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc02ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc02ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc03b4 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc03b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc02ec bytes 08a11a91
+ 00bc03b4 bytes 08611d91
- 00bc0314 ["COPY", "tmp:0:8", ["const:37b:8"]]
- 00bc0314 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0314 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0314 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc03dc ["COPY", "tmp:0:8", ["const:381:8"]]
+ 00bc03dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc03dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0314 bytes 08ed0d91
+ 00bc03dc bytes 08050e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31b6838f35d5b653da551b4b039ccc2b"></a>

### [`00bc0344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0344.md) → [`00bc040c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md) FUN_00bc040c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0470",
      "incomplete_value": false,
      "site": "00bc0470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc03a8",
      "incomplete_value": false,
      "site": "00bc03a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc0494",
      "incomplete_value": false,
      "site": "00bc0494",
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
            "const:1ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc03cc",
      "incomplete_value": false,
      "site": "00bc03cc",
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
            "const:12d:8"
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
      "00bc0470",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0494",
      "DATA",
      [
        "storage",
        "002a112d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0470",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0494",
      "DATA",
      [
        "storage",
        "002a11ba",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0344.md#insn-00bc0378) · [`00bc039c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0344.md#insn-00bc039c) · [`00bc03c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0344.md#insn-00bc03c4)
- 新版 [`00bc0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc0440) · [`00bc0464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc0464) · [`00bc048c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc040c.md#insn-00bc048c)

~~~diff
- 00bc0378 ["INT_ADD", "register:40f0:8", ["const:bc0378:8", "const:4:8"]]
- 00bc0378 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0440 ["INT_ADD", "register:40f0:8", ["const:bc0440:8", "const:4:8"]]
+ 00bc0440 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0378 bytes 56730094
+ 00bc0440 bytes 50730094
- 00bc039c ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc039c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc039c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc039c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0464 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0464 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0464 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0464 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc039c bytes 08a11a91
+ 00bc0464 bytes 08611d91
- 00bc03c4 ["COPY", "tmp:0:8", ["const:12d:8"]]
- 00bc03c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc03c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc03c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc048c ["COPY", "tmp:0:8", ["const:1ba:8"]]
+ 00bc048c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc048c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc048c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc03c4 bytes 08b50491
+ 00bc048c bytes 08e90691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5a2aab680d975d11f16242a9d7225f0"></a>

### [`00bc03f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc03f4.md) → [`00bc04bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md) FUN_00bc04bc

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0520",
      "incomplete_value": false,
      "site": "00bc0520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0458",
      "incomplete_value": false,
      "site": "00bc0458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00bc0520",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0520",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc03f4.md#insn-00bc0428) · [`00bc044c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc03f4.md#insn-00bc044c) · [`00bc04a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc03f4.md#insn-00bc04a0)
- 新版 [`00bc04f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc04f0) · [`00bc0514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc0514) · [`00bc0568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc04bc.md#insn-00bc0568)

~~~diff
- 00bc0428 ["INT_ADD", "register:40f0:8", ["const:bc0428:8", "const:4:8"]]
- 00bc0428 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc04f0 ["INT_ADD", "register:40f0:8", ["const:bc04f0:8", "const:4:8"]]
+ 00bc04f0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0428 bytes 2a730094
+ 00bc04f0 bytes 24730094
- 00bc044c ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc044c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc044c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc044c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0514 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0514 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0514 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0514 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc044c bytes 08a11a91
+ 00bc0514 bytes 08611d91
- 00bc04a0 ["INT_ADD", "register:40f0:8", ["const:bc04a0:8", "const:4:8"]]
- 00bc04a0 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc0568 ["INT_ADD", "register:40f0:8", ["const:bc0568:8", "const:4:8"]]
+ 00bc0568 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc04a0 bytes 0c6b0094
+ 00bc0568 bytes 066b0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f3e424abc6ed7cfcabdc62216a9b935"></a>

### [`00bc04a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc04a4.md) → [`00bc056c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md) FUN_00bc056c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc05d0",
      "incomplete_value": false,
      "site": "00bc05d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0508",
      "incomplete_value": false,
      "site": "00bc0508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc05f4",
      "incomplete_value": false,
      "site": "00bc05f4",
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
            "const:fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc052c",
      "incomplete_value": false,
      "site": "00bc052c",
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
            "const:6f:8"
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
      "00bc05d0",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc05f4",
      "DATA",
      [
        "storage",
        "002a206f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc05d0",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc05f4",
      "DATA",
      [
        "storage",
        "002a20fc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc04d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc04a4.md#insn-00bc04d8) · [`00bc04fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc04a4.md#insn-00bc04fc) · [`00bc0524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc04a4.md#insn-00bc0524)
- 新版 [`00bc05a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05a0) · [`00bc05c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05c4) · [`00bc05ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc056c.md#insn-00bc05ec)

~~~diff
- 00bc04d8 ["INT_ADD", "register:40f0:8", ["const:bc04d8:8", "const:4:8"]]
- 00bc04d8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc05a0 ["INT_ADD", "register:40f0:8", ["const:bc05a0:8", "const:4:8"]]
+ 00bc05a0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc04d8 bytes fe720094
+ 00bc05a0 bytes f8720094
- 00bc04fc ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc04fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc04fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc04fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc05c4 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc05c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc05c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc05c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc04fc bytes 08a11a91
+ 00bc05c4 bytes 08611d91
- 00bc0524 ["COPY", "tmp:0:8", ["const:6f:8"]]
- 00bc0524 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0524 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0524 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc05ec ["COPY", "tmp:0:8", ["const:fc:8"]]
+ 00bc05ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc05ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc05ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0524 bytes 08bd0191
+ 00bc05ec bytes 08f10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7feb9d548b003db755e44564bde3f38"></a>

### [`00bc0554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0554.md) → [`00bc061c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md) FUN_00bc061c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0680",
      "incomplete_value": false,
      "site": "00bc0680",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc05b8",
      "incomplete_value": false,
      "site": "00bc05b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc06a4",
      "incomplete_value": false,
      "site": "00bc06a4",
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
            "const:a93:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc05dc",
      "incomplete_value": false,
      "site": "00bc05dc",
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
            "const:a06:8"
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
      "00bc0680",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc06a4",
      "DATA",
      [
        "storage",
        "00299a06",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0680",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc06a4",
      "DATA",
      [
        "storage",
        "00299a93",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0554.md#insn-00bc0588) · [`00bc05ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0554.md#insn-00bc05ac) · [`00bc05d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0554.md#insn-00bc05d4)
- 新版 [`00bc0650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc0650) · [`00bc0674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc0674) · [`00bc069c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc061c.md#insn-00bc069c)

~~~diff
- 00bc0588 ["INT_ADD", "register:40f0:8", ["const:bc0588:8", "const:4:8"]]
- 00bc0588 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0650 ["INT_ADD", "register:40f0:8", ["const:bc0650:8", "const:4:8"]]
+ 00bc0650 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0588 bytes d2720094
+ 00bc0650 bytes cc720094
- 00bc05ac ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc05ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0674 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc05ac bytes 08a11a91
+ 00bc0674 bytes 08611d91
- 00bc05d4 ["COPY", "tmp:0:8", ["const:a06:8"]]
- 00bc05d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc05d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc069c ["COPY", "tmp:0:8", ["const:a93:8"]]
+ 00bc069c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc069c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc069c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc05d4 bytes 08192891
+ 00bc069c bytes 084d2a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b434d08c29ce84b67c46758322fc65d8"></a>

### [`00bc07b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc07b4.md) → [`00bc087c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md) FUN_00bc087c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc08e0",
      "incomplete_value": false,
      "site": "00bc08e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0818",
      "incomplete_value": false,
      "site": "00bc0818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc0904",
      "incomplete_value": false,
      "site": "00bc0904",
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
            "const:104:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc083c",
      "incomplete_value": false,
      "site": "00bc083c",
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
            "const:198:8"
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
      "00bc08e0",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0904",
      "DATA",
      [
        "storage",
        "002a9198",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc08e0",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0904",
      "DATA",
      [
        "storage",
        "002a9104",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc07e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc07b4.md#insn-00bc07e8) · [`00bc080c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc07b4.md#insn-00bc080c) · [`00bc0834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc07b4.md#insn-00bc0834)
- 新版 [`00bc08b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08b0) · [`00bc08d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08d4) · [`00bc08fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc087c.md#insn-00bc08fc)

~~~diff
- 00bc07e8 ["INT_ADD", "register:40f0:8", ["const:bc07e8:8", "const:4:8"]]
- 00bc07e8 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc08b0 ["INT_ADD", "register:40f0:8", ["const:bc08b0:8", "const:4:8"]]
+ 00bc08b0 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc07e8 bytes 3a720094
+ 00bc08b0 bytes 34720094
- 00bc080c ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc080c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc080c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc080c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc08d4 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc08d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc08d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc08d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc080c bytes 08a11a91
+ 00bc08d4 bytes 08611d91
- 00bc0834 ["COPY", "tmp:0:8", ["const:198:8"]]
- 00bc0834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc08fc ["COPY", "tmp:0:8", ["const:104:8"]]
+ 00bc08fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc08fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc08fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0834 bytes 08610691
+ 00bc08fc bytes 08110491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc53b45991ba398f20e0e385adfbb439"></a>

### [`00bc0864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0864.md) → [`00bc092c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md) FUN_00bc092c

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

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
      "definition_site": "00bc0994",
      "incomplete_value": false,
      "site": "00bc0994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc08cc",
      "incomplete_value": false,
      "site": "00bc08cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:728:8"
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
      "00bc0994",
      "DATA",
      [
        "storage",
        "00c17728",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0994",
      "DATA",
      [
        "storage",
        "00c177d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc089c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0864.md#insn-00bc089c) · [`00bc08c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0864.md#insn-00bc08c0) · [`00bc0908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0864.md#insn-00bc0908)
- 新版 [`00bc0964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc0964) · [`00bc0988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc0988) · [`00bc09d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc092c.md#insn-00bc09d0)

~~~diff
- 00bc089c ["INT_ADD", "register:40f0:8", ["const:bc089c:8", "const:4:8"]]
- 00bc089c ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0964 ["INT_ADD", "register:40f0:8", ["const:bc0964:8", "const:4:8"]]
+ 00bc0964 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc089c bytes 0d720094
+ 00bc0964 bytes 07720094
- 00bc08c0 ["COPY", "tmp:0:8", ["const:728:8"]]
- 00bc08c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc08c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0988 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00bc0988 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0988 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0988 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc08c0 bytes 08a11c91
+ 00bc0988 bytes 08611f91
- 00bc0908 ["INT_ADD", "register:40f0:8", ["const:bc0908:8", "const:4:8"]]
- 00bc0908 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc09d0 ["INT_ADD", "register:40f0:8", ["const:bc09d0:8", "const:4:8"]]
+ 00bc09d0 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc0908 bytes f2690094
+ 00bc09d0 bytes ec690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-682855ff98bd899482f53b53f32e3126"></a>

### [`00bc090c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc090c.md) → [`00bc09d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md) FUN_00bc09d4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0a38",
      "incomplete_value": false,
      "site": "00bc0a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0970",
      "incomplete_value": false,
      "site": "00bc0970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "definition_site": "00bc0a5c",
      "incomplete_value": false,
      "site": "00bc0a5c",
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
            "const:273:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0994",
      "incomplete_value": false,
      "site": "00bc0994",
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
            "const:1e6:8"
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
      "00bc0a38",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0a5c",
      "DATA",
      [
        "storage",
        "002a01e6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0a38",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0a5c",
      "DATA",
      [
        "storage",
        "002a0273",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc090c.md#insn-00bc0940) · [`00bc0964`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc090c.md#insn-00bc0964) · [`00bc098c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc090c.md#insn-00bc098c)
- 新版 [`00bc0a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a08) · [`00bc0a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a2c) · [`00bc0a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc09d4.md#insn-00bc0a54)

~~~diff
- 00bc0940 ["INT_ADD", "register:40f0:8", ["const:bc0940:8", "const:4:8"]]
- 00bc0940 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0a08 ["INT_ADD", "register:40f0:8", ["const:bc0a08:8", "const:4:8"]]
+ 00bc0a08 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0940 bytes e4710094
+ 00bc0a08 bytes de710094
- 00bc0964 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc0964 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0964 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0964 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a2c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0964 bytes 08a11a91
+ 00bc0a2c bytes 08611d91
- 00bc098c ["COPY", "tmp:0:8", ["const:1e6:8"]]
- 00bc098c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc098c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc098c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a54 ["COPY", "tmp:0:8", ["const:273:8"]]
+ 00bc0a54 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a54 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0a54 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc098c bytes 08990791
+ 00bc0a54 bytes 08cd0991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9984c93127e22da602db447e264f32a8"></a>

### [`00bc09bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc09bc.md) → [`00bc0a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md) FUN_00bc0a84

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0ae8",
      "incomplete_value": false,
      "site": "00bc0ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0a20",
      "incomplete_value": false,
      "site": "00bc0a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00bc0ae8",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00bc0ae8",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc09f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc09bc.md#insn-00bc09f0) · [`00bc0a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc09bc.md#insn-00bc0a14) · [`00bc0a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc09bc.md#insn-00bc0a68)
- 新版 [`00bc0ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0ab8) · [`00bc0adc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0adc) · [`00bc0b30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0a84.md#insn-00bc0b30)

~~~diff
- 00bc09f0 ["INT_ADD", "register:40f0:8", ["const:bc09f0:8", "const:4:8"]]
- 00bc09f0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0ab8 ["INT_ADD", "register:40f0:8", ["const:bc0ab8:8", "const:4:8"]]
+ 00bc0ab8 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc09f0 bytes b8710094
+ 00bc0ab8 bytes b2710094
- 00bc0a14 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc0a14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0a14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0adc ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0a14 bytes 08a11a91
+ 00bc0adc bytes 08611d91
- 00bc0a68 ["INT_ADD", "register:40f0:8", ["const:bc0a68:8", "const:4:8"]]
- 00bc0a68 ["CALL", null, ["callee:00bdb180:8"]]
+ 00bc0b30 ["INT_ADD", "register:40f0:8", ["const:bc0b30:8", "const:4:8"]]
+ 00bc0b30 ["CALL", null, ["callee:00bdb180:8"]]
- 00bc0a68 bytes 9a690094
+ 00bc0b30 bytes 94690094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f2f0e1bace04416acbd3e46670f735a"></a>

### [`00bc0a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0a6c.md) → [`00bc0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md) FUN_00bc0b34

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bbd1fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbd/00bbd1fc.md) · 呼出先 2件 [`00bdb0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0d0.md) [`00bdd0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdd0d0.md)
- 新版 呼出元 1件 [`00bbd2c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbd/00bbd2c4.md) · 呼出先 2件 [`00bdb180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb180.md) [`00bdd180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd180.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.02% / 新版 93.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bc0b98",
      "incomplete_value": false,
      "site": "00bc0b98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bc0ad0",
      "incomplete_value": false,
      "site": "00bc0ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c17000:8"
          ],
          [
            "leaf",
            "const:6a8:8"
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
      "00bc0b98",
      "DATA",
      [
        "storage",
        "00c176a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0bbc",
      "DATA",
      [
        "storage",
        "00298b10",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bc0b98",
      "DATA",
      [
        "storage",
        "00c17758",
        null,
        "undefined *"
      ]
    ],
    [
      "00bc0bbc",
      "DATA",
      [
        "storage",
        "00298b9d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bc0aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0a6c.md#insn-00bc0aa0) · [`00bc0ac4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0a6c.md#insn-00bc0ac4) · [`00bc0ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc0/00bc0a6c.md#insn-00bc0ae4)
- 新版 [`00bc0b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0b68) · [`00bc0b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0b8c) · [`00bc0bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc0/00bc0b34.md#insn-00bc0bac)

~~~diff
- 00bc0aa0 ["INT_ADD", "register:40f0:8", ["const:bc0aa0:8", "const:4:8"]]
- 00bc0aa0 ["CALL", null, ["callee:00bdd180:8"]]
+ 00bc0b68 ["INT_ADD", "register:40f0:8", ["const:bc0b68:8", "const:4:8"]]
+ 00bc0b68 ["CALL", null, ["callee:00bdd180:8"]]
- 00bc0aa0 bytes 8c710094
+ 00bc0b68 bytes 86710094
- 00bc0ac4 ["COPY", "tmp:0:8", ["const:6a8:8"]]
- 00bc0ac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0ac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bc0ac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b8c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00bc0b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bc0b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bc0ac4 bytes 08a11a91
+ 00bc0b8c bytes 08611d91
- 00bc0ae4 ["COPY", "tmp:0:8", ["const:b10:8"]]
- 00bc0ae4 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00bc0ae4 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00bc0ae4 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00bc0bac ["COPY", "tmp:0:8", ["const:b9d:8"]]
+ 00bc0bac ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00bc0bac ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00bc0bac ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00bc0ae4 bytes 6b412c91
+ 00bc0bac bytes 6b752e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

