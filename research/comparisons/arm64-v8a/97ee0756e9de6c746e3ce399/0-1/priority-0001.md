# v15.7.2 → v15.7.3 · 最優先の変更候補 (1)

[一覧の目次](README.md)

<a id="compare-9aa03e10d9014cdf4a2dfa4ec5a5b710"></a>

### [`00418338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md) → [`00418338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md) _INIT_3

採用 · 移動量 `+0x0` · 根拠 `code_and_unique_call_neighborhood` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b7d194`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b7d/00b7d194.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b7d25c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7d/00b7d25c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 65.22% / 新版 65.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418354",
      "incomplete_value": false,
      "site": "00418358",
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
            "const:a00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418354",
      "incomplete_value": false,
      "site": "00418358",
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
            "const:940:8"
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
      "definition_site": "0041836c",
      "incomplete_value": true,
      "site": "00418378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041836c",
      "incomplete_value": true,
      "site": "00418378",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c70:8"
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
      "definition_site": "00418368",
      "incomplete_value": false,
      "site": "00418378",
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
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418368",
      "incomplete_value": false,
      "site": "00418378",
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
            "const:918:8"
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
      "00418348",
      "READ",
      [
        "storage",
        "00c24940",
        null,
        "undefined1"
      ]
    ],
    [
      "00418354",
      "PARAM",
      [
        "storage",
        "00c24940",
        null,
        "undefined1"
      ]
    ],
    [
      "00418368",
      "PARAM",
      [
        "storage",
        "00c24918",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00418348",
      "READ",
      [
        "storage",
        "00c24a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00418354",
      "PARAM",
      [
        "storage",
        "00c24a00",
        null,
        "undefined1"
      ]
    ],
    [
      "00418368",
      "PARAM",
      [
        "storage",
        "00c249d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418344`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md#insn-00418344) · [`00418354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md#insn-00418354) · [`00418368`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418338.md#insn-00418368)
- 新版 [`00418344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md#insn-00418344) · [`00418354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md#insn-00418354) · [`00418368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418338.md#insn-00418368)

~~~diff
- 00418344 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00418344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418344 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00418344 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418344 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418344 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418344 bytes 08012591
+ 00418344 bytes 08012891
- 00418354 ["COPY", "tmp:0:8", ["const:940:8"]]
- 00418354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00418354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00418354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00418354 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00418354 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00418354 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00418354 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00418354 bytes 00002591
+ 00418354 bytes 00002891
- 00418368 ["COPY", "tmp:0:8", ["const:918:8"]]
- 00418368 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00418368 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00418368 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00418368 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00418368 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00418368 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00418368 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00418368 bytes 21602491
+ 00418368 bytes 21602791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6b7ddd173413b688eaeeac00007553b"></a>

### [`004183ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md) → [`004183ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md) Java_jp_co_ponos_battlecats_MyActivity_appInit

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0053c/0053c5e8.md) [`00547c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00547/00547c90.md) [`00acb928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb928.md) [`00acc23c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc23c.md) [`00acce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0053c5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053c/0053c5e8.md) [`00547c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00547/00547c90.md) [`00acb9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f0.md) [`00acc304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc304.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination, store_value

命令の説明率　旧版 82.22% / 新版 82.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00418430",
      "incomplete_value": false,
      "site": "0041843c",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418430",
      "incomplete_value": false,
      "site": "0041843c",
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
            "const:ee8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
            "const:a10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
                "const:a10:8"
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
      "definition_site": "00418454",
      "incomplete_value": false,
      "site": "00418454",
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
                "const:950:8"
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
    "ordinal": 10,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00418400",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ],
    [
      "0041843c",
      "DATA",
      [
        "storage",
        "00be5ee8",
        null,
        "undefined *"
      ]
    ],
    [
      "00418450",
      "READ",
      [
        "storage",
        "00c24958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00418400",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      "0041843c",
      "DATA",
      [
        "storage",
        "00be5f98",
        null,
        "undefined *"
      ]
    ],
    [
      "00418450",
      "READ",
      [
        "storage",
        "00c24a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md#insn-00418400) · [`00418430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md#insn-00418430) · [`0041844c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004183ec.md#insn-0041844c)
- 新版 [`00418400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md#insn-00418400) · [`00418430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md#insn-00418430) · [`0041844c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004183ec.md#insn-0041844c)

~~~diff
- 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
- 00418400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418400 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a10:8"]]
+ 00418400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00418400 bytes c8aa44f9
+ 00418400 bytes c80a45f9
- 00418430 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00418430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418430 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00418430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418430 bytes 08a13b91
+ 00418430 bytes 08613e91
- 0041844c ["COPY", "tmp:0:8", ["const:950:8"]]
- 0041844c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041844c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041844c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041844c ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 0041844c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041844c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041844c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041844c bytes 08412591
+ 0041844c bytes 08412891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3836766a32bfa633f068f6649ccf1432"></a>

### [`004184bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md) → [`004184bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md) Java_jp_co_ponos_battlecats_MyActivity_appUpdateDraw

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0053257c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00532/0053257c.md) [`0056cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md) [`00acb930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acb930.md) [`00acd35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd35c.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0053257c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00532/0053257c.md) [`0056cb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) [`00acb9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md) [`00acd424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd424.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 78.95% / 新版 78.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00418528",
      "incomplete_value": true,
      "site": "00418528",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418528",
      "incomplete_value": true,
      "site": "00418528",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00418588",
      "incomplete_value": true,
      "site": "00418588",
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
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418588",
      "incomplete_value": true,
      "site": "00418588",
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
            "const:960:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418504",
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418504",
      "incomplete_value": true,
      "site": "0041851c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "004184e8",
      "READ",
      [
        "storage",
        "00c24968",
        null,
        "undefined1"
      ]
    ],
    [
      "004184f4",
      "READ",
      [
        "storage",
        "00c24960",
        null,
        "undefined8"
      ]
    ],
    [
      "00418504",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004184e8",
      "READ",
      [
        "storage",
        "00c24a28",
        null,
        "undefined1"
      ]
    ],
    [
      "004184f4",
      "READ",
      [
        "storage",
        "00c24a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00418504",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418528`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md#insn-00418528) · [`00418588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md#insn-00418588) · [`004184e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004184bc.md#insn-004184e4)
- 新版 [`00418528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md#insn-00418528) · [`00418588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md#insn-00418588) · [`004184e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004184bc.md#insn-004184e4)

~~~diff
- 00418528 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:960:8"]]
- 00418528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00418528 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a20:8"]]
+ 00418528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00418528 bytes b3b204f9
+ 00418528 bytes b31205f9
- 00418588 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:960:8"]]
- 00418588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00418588 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a20:8"]]
+ 00418588 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00418588 bytes a0b204f9
+ 00418588 bytes a01205f9
- 004184e4 ["COPY", "tmp:0:8", ["const:968:8"]]
- 004184e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004184e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004184e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004184e4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 004184e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004184e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004184e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004184e4 bytes 08a12591
+ 004184e4 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ca650d05e9e8a6234e5367633811f56"></a>

### [`004185a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md) → [`004185a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md) Java_jp_co_ponos_battlecats_MyActivity_gfxInit

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`004186bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004186bc.md) [`0056c8a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056c8a4.md) [`0056f4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056f/0056f4d8.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`004186bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004186bc.md) [`0056c8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c8a4.md) [`0056f4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056f/0056f4d8.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.51% / 新版 85.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004185f0",
      "incomplete_value": false,
      "site": "004185f0",
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
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004185f0",
      "incomplete_value": false,
      "site": "004185f0",
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
            "const:970:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "004185f4",
      "incomplete_value": true,
      "site": "004185f4",
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
      "definition_site": "004185f4",
      "incomplete_value": true,
      "site": "004185f4",
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
      "definition_site": "00418654",
      "incomplete_value": true,
      "site": "00418658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418654",
      "incomplete_value": true,
      "site": "00418658",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:970:8"
              ]
            ]
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
      "004185cc",
      "READ",
      [
        "storage",
        "00c24980",
        null,
        "undefined1"
      ]
    ],
    [
      "004185e8",
      "READ",
      [
        "storage",
        "00c24978",
        null,
        "undefined8"
      ]
    ],
    [
      "004185f0",
      "WRITE",
      [
        "storage",
        "00c24970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004185cc",
      "READ",
      [
        "storage",
        "00c24a40",
        null,
        "undefined1"
      ]
    ],
    [
      "004185e8",
      "READ",
      [
        "storage",
        "00c24a38",
        null,
        "undefined8"
      ]
    ],
    [
      "004185f0",
      "WRITE",
      [
        "storage",
        "00c24a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004185c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md#insn-004185c8) · [`004185e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md#insn-004185e0) · [`00418654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/004185a8.md#insn-00418654)
- 新版 [`004185c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md#insn-004185c8) · [`004185e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md#insn-004185e0) · [`00418654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/004185a8.md#insn-00418654)

~~~diff
- 004185c8 ["COPY", "tmp:0:8", ["const:980:8"]]
- 004185c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004185c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004185c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004185c8 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 004185c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004185c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004185c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004185c8 bytes 08012691
+ 004185c8 bytes 08012991
- 004185e0 ["COPY", "tmp:0:8", ["const:970:8"]]
- 004185e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004185e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004185e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004185e0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 004185e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004185e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004185e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004185e0 bytes 08c12591
+ 004185e0 bytes 08c12891
- 00418654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:970:8"]]
- 00418654 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418654 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a30:8"]]
+ 00418654 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00418654 bytes 00b944f9
+ 00418654 bytes 001945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfddd59bdb35eb79f318922a35d32867"></a>

### [`0041870c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041870c.md) → [`0041870c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041870c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableWidth

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418714",
      "incomplete_value": true,
      "site": "00418718",
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
      "definition_site": "00418714",
      "incomplete_value": true,
      "site": "00418718",
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
      "00418714",
      "READ",
      [
        "storage",
        "00c24cc8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418714",
      "READ",
      [
        "storage",
        "00c24d88",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041870c.md#insn-00418710)
- 新版 [`00418710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041870c.md#insn-00418710)

~~~diff
- 00418710 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418710 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418710 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418710 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418710 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418710 bytes 08c13291
+ 00418710 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf48c583da3d44e617d0f07e801862a3"></a>

### [`0041871c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041871c.md) → [`0041871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041871c.md) Java_jp_co_ponos_battlecats_MyActivity_getDrawableHeight

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418724",
      "incomplete_value": true,
      "site": "00418728",
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
      "definition_site": "00418724",
      "incomplete_value": true,
      "site": "00418728",
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
      "00418724",
      "READ",
      [
        "storage",
        "00c24ccc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418724",
      "READ",
      [
        "storage",
        "00c24d8c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041871c.md#insn-00418720)
- 新版 [`00418720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041871c.md#insn-00418720)

~~~diff
- 00418720 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418720 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418720 bytes 08c13291
+ 00418720 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d36c8be1fb03ea5e633ea3609767995"></a>

### [`0041872c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041872c.md) → [`0041872c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041872c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowWidth

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418734",
      "incomplete_value": true,
      "site": "00418738",
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
      "definition_site": "00418734",
      "incomplete_value": true,
      "site": "00418738",
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
      "00418734",
      "READ",
      [
        "storage",
        "00c24cb8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418734",
      "READ",
      [
        "storage",
        "00c24d78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418730`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041872c.md#insn-00418730)
- 新版 [`00418730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041872c.md#insn-00418730)

~~~diff
- 00418730 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418730 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418730 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418730 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418730 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418730 bytes 08c13291
+ 00418730 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00cb0787d238281dd100ab92ad07b840"></a>

### [`0041873c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041873c.md) → [`0041873c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041873c.md) Java_jp_co_ponos_battlecats_MyActivity_getWindowHeight

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418744",
      "incomplete_value": true,
      "site": "00418748",
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
      "definition_site": "00418744",
      "incomplete_value": true,
      "site": "00418748",
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
      "00418744",
      "READ",
      [
        "storage",
        "00c24cbc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418744",
      "READ",
      [
        "storage",
        "00c24d7c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418740`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041873c.md#insn-00418740)
- 新版 [`00418740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041873c.md#insn-00418740)

~~~diff
- 00418740 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418740 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418740 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418740 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418740 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418740 bytes 08c13291
+ 00418740 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d53fbf7fe9679f2be179281d91c9044"></a>

### [`0041874c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041874c.md) → [`0041874c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041874c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeWidth

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418754",
      "incomplete_value": true,
      "site": "00418758",
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
      "definition_site": "00418754",
      "incomplete_value": true,
      "site": "00418758",
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
      "00418754",
      "READ",
      [
        "storage",
        "00c24cc0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418754",
      "READ",
      [
        "storage",
        "00c24d80",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041874c.md#insn-00418750)
- 新版 [`00418750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041874c.md#insn-00418750)

~~~diff
- 00418750 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418750 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418750 bytes 08c13291
+ 00418750 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e46a39ee3ee99ea867b5ddb3ee8a103"></a>

### [`0041875c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041875c.md) → [`0041875c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041875c.md) Java_jp_co_ponos_battlecats_MyActivity_getSizeHeight

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00418764",
      "incomplete_value": true,
      "site": "00418768",
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
      "definition_site": "00418764",
      "incomplete_value": true,
      "site": "00418768",
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
      "00418764",
      "READ",
      [
        "storage",
        "00c24cc4",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418764",
      "READ",
      [
        "storage",
        "00c24d84",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041875c.md#insn-00418760)
- 新版 [`00418760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041875c.md#insn-00418760)

~~~diff
- 00418760 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00418760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00418760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00418760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00418760 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00418760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00418760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00418760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00418760 bytes 08c13291
+ 00418760 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9983eb49e312c6b5e4bc13c144820e84"></a>

### [`0041876c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041876c.md) → [`0041876c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md) Java_jp_co_ponos_battlecats_MyActivity_gfxResize

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0056cb70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0056c/0056cb70.md) [`00acce84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acce84.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0056cb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056cb70.md) [`00accf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00accf4c.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 74.47% / 新版 74.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
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
            "const:2c:8"
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
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
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
      "definition_site": "004187c8",
      "incomplete_value": true,
      "site": "004187c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:2c:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004187f4",
      "incomplete_value": true,
      "site": "004187f4",
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
            "const:2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004187f4",
      "incomplete_value": true,
      "site": "004187f4",
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
            "const:2c:8"
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
      "00418784",
      "READ",
      [
        "storage",
        "00c1ac80",
        null,
        "pointer"
      ]
    ],
    [
      "00418788",
      "READ",
      [
        "storage",
        "00c1ac88",
        null,
        "pointer"
      ]
    ],
    [
      "00418794",
      "READ",
      [
        "storage",
        "00c2649c",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418784",
      "READ",
      [
        "storage",
        "00c1ad30",
        null,
        "pointer"
      ]
    ],
    [
      "00418788",
      "READ",
      [
        "storage",
        "00c1ad38",
        null,
        "pointer"
      ]
    ],
    [
      "00418794",
      "READ",
      [
        "storage",
        "00c2655c",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418784`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041876c.md#insn-00418784) · [`00418788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041876c.md#insn-00418788) · [`00418798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/0041876c.md#insn-00418798)
- 新版 [`00418784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md#insn-00418784) · [`00418788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md#insn-00418788) · [`00418798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/0041876c.md#insn-00418798)

~~~diff
- 00418784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c80:8"]]
- 00418784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d30:8"]]
+ 00418784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00418784 bytes 084146f9
+ 00418784 bytes 089946f9
- 00418788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:c88:8"]]
- 00418788 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d38:8"]]
+ 00418788 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00418788 bytes 294546f9
+ 00418788 bytes 299d46f9
- 00418798 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:c90:8"]]
- 00418798 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418798 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d40:8"]]
+ 00418798 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00418798 bytes 4a4946f9
+ 00418798 bytes 4aa146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2523c6d9c6d525b7f651949369dde7b5"></a>

### [`00418828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md) → [`00418828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md) Java_jp_co_ponos_battlecats_MyActivity_appTouch

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00acd284`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd284.md) [`00acd2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd2cc.md) [`00acd314`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acd/00acd314.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00acd34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd34c.md) [`00acd394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd394.md) [`00acd3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acd3dc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 83.33% / 新版 83.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004188d0",
      "incomplete_value": true,
      "site": "004188d0",
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
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d0",
      "incomplete_value": true,
      "site": "004188d0",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004188d4",
      "incomplete_value": true,
      "site": "004188d4",
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
            "const:a4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004188d4",
      "incomplete_value": true,
      "site": "004188d4",
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
            "const:98c:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418874",
      "incomplete_value": true,
      "site": "0041887c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418874",
      "incomplete_value": true,
      "site": "0041887c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "00418874",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ],
    [
      "00418898",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ],
    [
      "004188a8",
      "READ",
      [
        "storage",
        "00c24988",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00418874",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00418898",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      "004188a8",
      "READ",
      [
        "storage",
        "00c24a48",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004188d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md#insn-004188d0) · [`004188d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md#insn-004188d4) · [`00418874`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418828.md#insn-00418874)
- 新版 [`004188d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md#insn-004188d0) · [`004188d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md#insn-004188d4) · [`00418874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418828.md#insn-00418874)

~~~diff
- 004188d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 004188d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:4"]]
+ 004188d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 004188d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5120:4"]]
- 004188d0 bytes 698a09bd
+ 004188d0 bytes 694a0abd
- 004188d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:98c:8"]]
- 004188d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:4"]]
+ 004188d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a4c:8"]]
+ 004188d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5100:4"]]
- 004188d4 bytes 888e09bd
+ 004188d4 bytes 884e0abd
- 00418874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00418874 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418874 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a10:8"]]
+ 00418874 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00418874 bytes 00a944f9
+ 00418874 bytes 000945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b5a5c0a0147cf913a0ebbb3670b5f0b"></a>

### [`00418b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md) → [`00418b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md) Java_jp_co_ponos_battlecats_MyActivity_kill

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00acbc08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md) [`00acc460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00acbcd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acbcd0.md) [`00acc528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418b30",
      "incomplete_value": true,
      "site": "00418b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418b30",
      "incomplete_value": true,
      "site": "00418b34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
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
      "00418b30",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ],
    [
      "00418b38",
      "READ",
      [
        "storage",
        "00c24950",
        null,
        "undefined8"
      ]
    ],
    [
      "00418b40",
      "READ",
      [
        "storage",
        "00c24958",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00418b30",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00418b38",
      "READ",
      [
        "storage",
        "00c24a10",
        null,
        "undefined8"
      ]
    ],
    [
      "00418b40",
      "READ",
      [
        "storage",
        "00c24a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418b18.md#insn-00418b28)
- 新版 [`00418b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418b18.md#insn-00418b28)

~~~diff
- 00418b28 ["COPY", "tmp:0:8", ["const:950:8"]]
- 00418b28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00418b28 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00418b28 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00418b28 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00418b28 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00418b28 bytes 94422591
+ 00418b28 bytes 94422891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-164a009c82618d6b3a9d371f91de18e5"></a>

### [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) → [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) FUN_00418c24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 272件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041ac3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e10c.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 272件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00418c30",
      "incomplete_value": false,
      "site": "00418c34",
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
            "const:1b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c30",
      "incomplete_value": false,
      "site": "00418c34",
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
            "const:246:8"
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
      "00418c30",
      "PARAM",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00418c30",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md#insn-00418c30)
- 新版 [`00418c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md#insn-00418c30)

~~~diff
- 00418c30 ["COPY", "tmp:0:8", ["const:246:8"]]
- 00418c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00418c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00418c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00418c30 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 00418c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00418c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00418c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00418c30 bytes 00180991
+ 00418c30 bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a48d531c5c3c59e52e9225fa1c994e7d"></a>

### [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md) → [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md) FUN_00418c38

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 223件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) [`00420bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bd8.md) [`00426e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e78.md) [`00439eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439eb4.md) · 呼出先 4件 [`00418c88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c88.md) [`00bbad50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbad50.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 223件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`00420bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) [`00426e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) [`00439eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439eb4.md) · 呼出先 4件 [`00418c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c88.md) [`00bbae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00418c68",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c68",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
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
      "definition_site": "00418c6c",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00418c6c",
      "incomplete_value": true,
      "site": "00418c70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca8:8"
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
      "00418c68",
      "READ",
      [
        "storage",
        "00c1aca0",
        null,
        "pointer"
      ]
    ],
    [
      "00418c68",
      "PARAM",
      [
        "storage",
        "00c16930",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00418c6c",
      "READ",
      [
        "storage",
        "00c1aca8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00418c68",
      "READ",
      [
        "storage",
        "00c1ad50",
        null,
        "pointer"
      ]
    ],
    [
      "00418c68",
      "PARAM",
      [
        "storage",
        "00c169e0",
        "_ZTISt12length_error",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00418c6c",
      "READ",
      [
        "storage",
        "00c1ad58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00418c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md#insn-00418c68) · [`00418c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md#insn-00418c6c)
- 新版 [`00418c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md#insn-00418c68) · [`00418c6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md#insn-00418c6c)

~~~diff
- 00418c68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ca0:8"]]
- 00418c68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418c68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d50:8"]]
+ 00418c68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00418c68 bytes 215046f9
+ 00418c68 bytes 21a846f9
- 00418c6c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:ca8:8"]]
- 00418c6c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00418c6c ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d58:8"]]
+ 00418c6c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00418c6c bytes 425446f9
+ 00418c6c bytes 42ac46f9
~~~


<a id="compare-d5f00d02fe4bad81a43e1009d44d2094"></a>

### [`00419248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419248.md) → [`00419248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419248.md) FUN_00419248

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
      "definition_site": "0041924c",
      "incomplete_value": false,
      "site": "00419250",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041924c",
      "incomplete_value": false,
      "site": "00419250",
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
            "const:ee8:8"
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
      "00419250",
      "DATA",
      [
        "storage",
        "00be5ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00419250",
      "DATA",
      [
        "storage",
        "00be5f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041924c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419248.md#insn-0041924c)
- 新版 [`0041924c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419248.md#insn-0041924c)

~~~diff
- 0041924c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0041924c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041924c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041924c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041924c ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 0041924c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041924c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041924c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041924c bytes 08a13b91
+ 0041924c bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2da63b5547ed3c381a1945d3fad138ec"></a>

### [`00419258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419258.md) → [`00419258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419258.md) FUN_00419258

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
      "definition_site": "00419268",
      "incomplete_value": false,
      "site": "00419270",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419268",
      "incomplete_value": false,
      "site": "00419270",
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
            "const:ee8:8"
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
      "00419270",
      "DATA",
      [
        "storage",
        "00be5ee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00419270",
      "DATA",
      [
        "storage",
        "00be5f98",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00419268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419258.md#insn-00419268)
- 新版 [`00419268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419258.md#insn-00419268)

~~~diff
- 00419268 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00419268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00419268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00419268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00419268 ["COPY", "tmp:0:8", ["const:f98:8"]]
+ 00419268 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00419268 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00419268 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00419268 bytes 08a13b91
+ 00419268 bytes 08613e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee3328f79fed53bd55db0645489d307a"></a>

### [`00419294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419294.md) → [`00419294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419294.md) _INIT_4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418330.md) [`00418394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418394.md) [`00418cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418cb8.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418394.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.24% / 新版 84.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 3件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004192d0",
      "incomplete_value": true,
      "site": "004192ec",
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
      "definition_site": "004192d0",
      "incomplete_value": true,
      "site": "004192ec",
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
      "definition_site": "004192f4",
      "incomplete_value": true,
      "site": "00419310",
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
      "definition_site": "004192f4",
      "incomplete_value": true,
      "site": "00419310",
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
      "definition_site": "00419314",
      "incomplete_value": true,
      "site": "00419330",
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
      "definition_site": "00419314",
      "incomplete_value": true,
      "site": "00419330",
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
      "004192d0",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "004192f4",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00419314",
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
      "004192d0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "004192f4",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00419314",
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

- 旧版 [`004192c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419294.md#insn-004192c0) · [`004192c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419294.md#insn-004192c8)
- 新版 [`004192c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419294.md#insn-004192c0) · [`004192c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419294.md#insn-004192c8)

~~~diff
- 004192c0 ["COPY", "tmp:0:8", ["const:900:8"]]
- 004192c0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004192c0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004192c0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004192c0 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 004192c0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004192c0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004192c0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004192c0 bytes 73022491
+ 004192c0 bytes 73022791
- 004192c8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004192c8 bytes 69f4ffd0
+ 004192c8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 004192c8 bytes 69f4ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bf677faf7c740b9334ab58fe8f39b75"></a>

### [`00419640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md) → [`00419640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md) _INIT_5

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/0041969c.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/0041969c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041965c",
      "incomplete_value": false,
      "site": "00419660",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041965c",
      "incomplete_value": false,
      "site": "00419660",
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
            "const:9b0:8"
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
      "definition_site": "00419674",
      "incomplete_value": false,
      "site": "00419680",
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
    "old": {
      "definition_site": "00419674",
      "incomplete_value": false,
      "site": "00419680",
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
            "const:9a8:8"
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
      "definition_site": "0041967c",
      "incomplete_value": false,
      "site": "00419680",
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
      "definition_site": "0041967c",
      "incomplete_value": false,
      "site": "00419680",
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
      "00419650",
      "READ",
      [
        "storage",
        "00c249b0",
        null,
        "undefined1"
      ]
    ],
    [
      "0041965c",
      "PARAM",
      [
        "storage",
        "00c249b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00419674",
      "PARAM",
      [
        "storage",
        "00c249a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00419650",
      "READ",
      [
        "storage",
        "00c24a70",
        null,
        "undefined1"
      ]
    ],
    [
      "0041965c",
      "PARAM",
      [
        "storage",
        "00c24a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00419674",
      "PARAM",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041964c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md#insn-0041964c) · [`0041965c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md#insn-0041965c) · [`00419674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419640.md#insn-00419674)
- 新版 [`0041964c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md#insn-0041964c) · [`0041965c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md#insn-0041965c) · [`00419674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419640.md#insn-00419674)

~~~diff
- 0041964c ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 0041964c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041964c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041964c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041964c ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0041964c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041964c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041964c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041964c bytes 08c12691
+ 0041964c bytes 08c12991
- 0041965c ["COPY", "tmp:0:8", ["const:9b0:8"]]
- 0041965c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041965c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041965c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0041965c ["COPY", "tmp:0:8", ["const:a70:8"]]
+ 0041965c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0041965c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0041965c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041965c bytes 00c02691
+ 0041965c bytes 00c02991
- 00419674 ["COPY", "tmp:0:8", ["const:9a8:8"]]
- 00419674 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00419674 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00419674 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00419674 ["COPY", "tmp:0:8", ["const:a68:8"]]
+ 00419674 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00419674 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00419674 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00419674 bytes 21a02691
+ 00419674 bytes 21a02991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58ed527947406e26d95da7b1a9a78e7d"></a>

### [`004196bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004196bc.md) → [`004196bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md) _INIT_6

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/0041969c.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041969c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/0041969c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.57% / 新版 69.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004196d8",
      "incomplete_value": false,
      "site": "004196dc",
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
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004196d8",
      "incomplete_value": false,
      "site": "004196dc",
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
            "const:9c0:8"
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
      "definition_site": "004196f0",
      "incomplete_value": false,
      "site": "004196fc",
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
    "old": {
      "definition_site": "004196f0",
      "incomplete_value": false,
      "site": "004196fc",
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
            "const:9b8:8"
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
      "definition_site": "004196f8",
      "incomplete_value": false,
      "site": "004196fc",
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
      "definition_site": "004196f8",
      "incomplete_value": false,
      "site": "004196fc",
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
      "004196cc",
      "READ",
      [
        "storage",
        "00c249c0",
        null,
        "undefined1"
      ]
    ],
    [
      "004196d8",
      "PARAM",
      [
        "storage",
        "00c249c0",
        null,
        "undefined1"
      ]
    ],
    [
      "004196f0",
      "PARAM",
      [
        "storage",
        "00c249b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004196cc",
      "READ",
      [
        "storage",
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      "004196d8",
      "PARAM",
      [
        "storage",
        "00c24a80",
        null,
        "undefined1"
      ]
    ],
    [
      "004196f0",
      "PARAM",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004196c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004196bc.md#insn-004196c8) · [`004196d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004196bc.md#insn-004196d8) · [`004196f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/004196bc.md#insn-004196f0)
- 新版 [`004196c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md#insn-004196c8) · [`004196d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md#insn-004196d8) · [`004196f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/004196bc.md#insn-004196f0)

~~~diff
- 004196c8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 004196c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004196c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004196c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004196c8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 004196c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004196c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004196c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004196c8 bytes 08012791
+ 004196c8 bytes 08012a91
- 004196d8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
- 004196d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004196d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004196d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004196d8 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 004196d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004196d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004196d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004196d8 bytes 00002791
+ 004196d8 bytes 00002a91
- 004196f0 ["COPY", "tmp:0:8", ["const:9b8:8"]]
- 004196f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004196f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004196f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004196f0 ["COPY", "tmp:0:8", ["const:a78:8"]]
+ 004196f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004196f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004196f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004196f0 bytes 21e02691
+ 004196f0 bytes 21e02991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-590b124952a5a39efc0eb6a0a402e5c6"></a>

### [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) → [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) FUN_00419718

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00420580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420580.md) [`00420858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041aa74.md) [`0041ac3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md)
- 新版 呼出元 2件 [`00420580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420580.md) [`00420858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420858.md) · 呼出先 49件 [`0041aa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041aa74.md) [`0041ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041ba38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 11件, `store_value` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004198a0",
      "incomplete_value": true,
      "site": "004198a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004198a0",
      "incomplete_value": true,
      "site": "004198a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00419984",
      "incomplete_value": false,
      "site": "00419984",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:520:8"
              ]
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
      "definition_site": "00419984",
      "incomplete_value": false,
      "site": "00419984",
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
                "const:be8000:8"
              ],
              [
                "leaf",
                "const:470:8"
              ]
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
      "definition_site": "00419ac0",
      "incomplete_value": true,
      "site": "00419ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:66b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00419ac0",
      "incomplete_value": true,
      "site": "00419ac0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:674:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004197e4",
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      "00419890",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ],
    [
      "00419984",
      "DATA",
      [
        "storage",
        "00be8480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004197e4",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "00419890",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ],
    [
      "00419984",
      "DATA",
      [
        "storage",
        "00be8530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004197e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md#insn-004197e4) · [`00419888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md#insn-00419888) · [`00419978`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md#insn-00419978)
- 新版 [`004197e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md#insn-004197e4) · [`00419888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md#insn-00419888) · [`00419978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md#insn-00419978)

~~~diff
- 004197e4 ["COPY", "tmp:0:8", ["const:253:8"]]
- 004197e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004197e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004197e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004197e4 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 004197e4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004197e4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004197e4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004197e4 bytes 214c0991
+ 004197e4 bytes 21fc0691
- 00419888 ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 00419888 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00419888 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00419888 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00419888 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 00419888 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00419888 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00419888 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00419888 bytes 29152391
+ 00419888 bytes 29492591
- 00419978 ["COPY", "tmp:0:8", ["const:470:8"]]
- 00419978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00419978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00419978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00419978 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00419978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00419978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00419978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00419978 bytes 08c11191
+ 00419978 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c7b52ef93c1069bd53b6325ee500af6"></a>

### [`0041ac3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md) → [`0041ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) FUN_0041ac3c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`0041e10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e10c.md) [`00464f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464f48.md) [`0046517c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/0046517c.md) [`004652a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00465/004652a0.md)
- 新版 呼出元 2件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) · 呼出先 13件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`0041e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046517c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046517c.md) [`004652a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004652a0.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 95.81% / 新版 95.81%

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
      "definition_site": "0041aed8",
      "incomplete_value": true,
      "site": "0041aedc",
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
      "definition_site": "0041aed8",
      "incomplete_value": true,
      "site": "0041aedc",
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
      "definition_site": "0041aed4",
      "incomplete_value": true,
      "site": "0041aee0",
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
      "definition_site": "0041aed4",
      "incomplete_value": true,
      "site": "0041aee0",
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
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0041aeec",
      "incomplete_value": true,
      "site": "0041aeec",
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
      "definition_site": "0041aeec",
      "incomplete_value": true,
      "site": "0041aeec",
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
      "0041aec8",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "0041aecc",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0041aed4",
      "READ",
      [
        "storage",
        "00c13358",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0041aec8",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0041aecc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0041aed4",
      "READ",
      [
        "storage",
        "00c13408",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041aec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md#insn-0041aec8) · [`0041aecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md#insn-0041aecc) · [`0041aef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md#insn-0041aef4)
- 新版 [`0041aec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md#insn-0041aec8) · [`0041aecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md#insn-0041aecc) · [`0041aef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md#insn-0041aef4)

~~~diff
- 0041aec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 0041aec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041aec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 0041aec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041aec8 bytes 086146f9
+ 0041aec8 bytes 08b946f9
- 0041aecc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:cc8:8"]]
- 0041aecc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041aecc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d78:8"]]
+ 0041aecc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0041aecc bytes f76646f9
+ 0041aecc bytes f7be46f9
- 0041aef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 0041aef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041aef4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d80:8"]]
+ 0041aef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041aef4 bytes 086946f9
+ 0041aef4 bytes 08c146f9
~~~


<a id="compare-af07524e2ea8b00d845eb8891e844e39"></a>

### [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) → [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) FUN_0041b064

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 39件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) [`0041cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md) [`00421b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 39件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`00421b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041b214",
      "incomplete_value": false,
      "site": "0041b21c",
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
            "const:8ca:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b214",
      "incomplete_value": false,
      "site": "0041b21c",
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
            "const:83d:8"
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
      "0041b214",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0041b214",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041b214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md#insn-0041b214)
- 新版 [`0041b214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md#insn-0041b214)

~~~diff
- 0041b214 ["COPY", "tmp:0:8", ["const:83d:8"]]
- 0041b214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041b214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041b214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041b214 ["COPY", "tmp:0:8", ["const:8ca:8"]]
+ 0041b214 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041b214 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041b214 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041b214 bytes 21f42091
+ 0041b214 bytes 21282391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7754376c921a8963edd496ff6821fe1"></a>

### [`0041b338`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b338.md) → [`0041b338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b338.md) FUN_0041b338

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0045fc34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaf30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf30.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`0045fc34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045f/0045fc34.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041b354",
      "incomplete_value": true,
      "site": "0041b358",
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
      "definition_site": "0041b354",
      "incomplete_value": true,
      "site": "0041b358",
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
      "0041b34c",
      "READ",
      [
        "storage",
        "00c1acb8",
        null,
        "pointer"
      ]
    ],
    [
      "0041b358",
      "DATA",
      [
        "storage",
        "00be8480",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0041b34c",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0041b358",
      "DATA",
      [
        "storage",
        "00be8530",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041b34c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b338.md#insn-0041b34c)
- 新版 [`0041b34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b338.md#insn-0041b34c)

~~~diff
- 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb8:8"]]
- 0041b34c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041b34c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d68:8"]]
+ 0041b34c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041b34c bytes 085d46f9
+ 0041b34c bytes 08b546f9
~~~


<a id="compare-a6ef4d624b00f52707df2da6368d877f"></a>

### [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) → [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) FUN_0041b470

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00420674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420674.md) [`00420678`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420678.md) [`00420704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420704.md) [`00420708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420708.md)
- 新版 呼出元 2件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) · 呼出先 20件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00420674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420674.md) [`00420678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420678.md) [`00420704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420704.md) [`00420708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420708.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041b664",
      "incomplete_value": false,
      "site": "0041b664",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b664",
      "incomplete_value": false,
      "site": "0041b664",
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
            "const:178:8"
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
      "definition_site": "0041b688",
      "incomplete_value": false,
      "site": "0041b688",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b688",
      "incomplete_value": false,
      "site": "0041b688",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041b69c",
      "incomplete_value": false,
      "site": "0041b69c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041b69c",
      "incomplete_value": false,
      "site": "0041b69c",
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
            "const:278:8"
          ]
        ]
      ]
    },
    "ordinal": 33,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041b4c0",
      "PARAM",
      [
        "storage",
        "0029583f",
        null,
        "undefined4"
      ]
    ],
    [
      "0041b5c8",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0041b5c8",
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0041b4c0",
      "PARAM",
      [
        "storage",
        "002958cc",
        null,
        "undefined4"
      ]
    ],
    [
      "0041b5c8",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0041b5c8",
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

- 旧版 [`0041b4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md#insn-0041b4c0) · [`0041b5c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md#insn-0041b5c8) · [`0041b660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md#insn-0041b660)
- 新版 [`0041b4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md#insn-0041b4c0) · [`0041b5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md#insn-0041b5c8) · [`0041b660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md#insn-0041b660)

~~~diff
- 0041b4c0 ["COPY", "tmp:0:8", ["const:83f:8"]]
- 0041b4c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041b4c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041b4c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041b4c0 ["COPY", "tmp:0:8", ["const:8cc:8"]]
+ 0041b4c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041b4c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041b4c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041b4c0 bytes 21fc2091
+ 0041b4c0 bytes 21302391
- 0041b5c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 0041b5c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041b5c8 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0041b5c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0041b5c8 bytes 006c46f9
+ 0041b5c8 bytes 00c446f9
- 0041b660 ["COPY", "tmp:0:8", ["const:178:8"]]
- 0041b660 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041b660 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041b660 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0041b660 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0041b660 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0041b660 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0041b660 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041b660 bytes 29e10591
+ 0041b660 bytes 29a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fae2ccbe7442912d79c25295b6438af6"></a>

### [`0041ba38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md) → [`0041ba38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md) FUN_0041ba38

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004203a4.md) [`004203a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004203a8.md) [`00420430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420430.md) [`00420434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420434.md) [`00420578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420578.md)
- 新版 呼出元 1件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) · 呼出先 11件 [`004203a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203a4.md) [`004203a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203a8.md) [`00420430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420430.md) [`00420434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420434.md) [`00420578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420578.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.40% / 新版 94.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041baf0",
      "incomplete_value": false,
      "site": "0041baf0",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041baf0",
      "incomplete_value": false,
      "site": "0041baf0",
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
            "const:fc8:8"
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
      "definition_site": "0041bb14",
      "incomplete_value": false,
      "site": "0041bb14",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb14",
      "incomplete_value": false,
      "site": "0041bb14",
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
            "const:58:8"
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
      "definition_site": "0041bb28",
      "incomplete_value": false,
      "site": "0041bb28",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bb28",
      "incomplete_value": false,
      "site": "0041bb28",
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
            "const:e8:8"
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
      "0041ba68",
      "READ",
      [
        "storage",
        "00c1acd8",
        null,
        "pointer"
      ]
    ],
    [
      "0041ba68",
      "PARAM",
      [
        "storage",
        "00c25d10",
        null,
        "undefined1"
      ]
    ],
    [
      "0041baf0",
      "DATA",
      [
        "storage",
        "00be5fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0041ba68",
      "READ",
      [
        "storage",
        "00c1ad88",
        null,
        "pointer"
      ]
    ],
    [
      "0041ba68",
      "PARAM",
      [
        "storage",
        "00c25dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "0041baf0",
      "DATA",
      [
        "storage",
        "00be6078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ba68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md#insn-0041ba68) · [`0041bae8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md#insn-0041bae8) · [`0041baec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041ba38.md#insn-0041baec)
- 新版 [`0041ba68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md#insn-0041ba68) · [`0041bae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md#insn-0041bae8) · [`0041baec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041ba38.md#insn-0041baec)

~~~diff
- 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:cd8:8"]]
- 0041ba68 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041ba68 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:d88:8"]]
+ 0041ba68 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0041ba68 bytes 006c46f9
+ 0041ba68 bytes 00c446f9
- 0041bae8 ["COPY", "register:4048:8", ["const:be5000:8"]]
+ 0041bae8 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 0041bae8 bytes 493e00d0
+ 0041bae8 bytes 493e00f0
- 0041baec ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0041baec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041baec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041baec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0041baec ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0041baec ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0041baec ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0041baec ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041baec bytes 29213f91
+ 0041baec bytes 29e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc29dd99eb08bbe6e1bb4cd132d1d24b"></a>

### [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) → [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) FUN_0041be0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 38件 [`0060468c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bf20.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 38件 [`0060468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 5件 [`0041be9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041be40",
      "incomplete_value": false,
      "site": "0041be44",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be40",
      "incomplete_value": false,
      "site": "0041be44",
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
            "const:a20:8"
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
      "definition_site": "0041be50",
      "incomplete_value": false,
      "site": "0041be54",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be50",
      "incomplete_value": false,
      "site": "0041be54",
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
            "const:9c8:8"
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
      "definition_site": "0041be64",
      "incomplete_value": false,
      "site": "0041be70",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041be64",
      "incomplete_value": false,
      "site": "0041be70",
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
            "const:9c8:8"
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
      "0041be20",
      "READ",
      [
        "storage",
        "00c24a20",
        null,
        "undefined1"
      ]
    ],
    [
      "0041be2c",
      "DATA",
      [
        "storage",
        "00c249c8",
        null,
        null
      ]
    ],
    [
      "0041be40",
      "PARAM",
      [
        "storage",
        "00c24a20",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0041be20",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "0041be2c",
      "DATA",
      [
        "storage",
        "00c24a88",
        null,
        null
      ]
    ],
    [
      "0041be40",
      "PARAM",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041be1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md#insn-0041be1c) · [`0041be2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md#insn-0041be2c) · [`0041be40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md#insn-0041be40)
- 新版 [`0041be1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md#insn-0041be1c) · [`0041be2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md#insn-0041be2c) · [`0041be40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md#insn-0041be40)

~~~diff
- 0041be1c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 0041be1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041be1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041be1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041be1c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0041be1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041be1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041be1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041be1c bytes 08812891
+ 0041be1c bytes 08812b91
- 0041be2c ["COPY", "tmp:0:8", ["const:9c8:8"]]
- 0041be2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041be2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041be2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0041be2c ["COPY", "tmp:0:8", ["const:a88:8"]]
+ 0041be2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0041be2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0041be2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041be2c bytes 00202791
+ 0041be2c bytes 00202a91
- 0041be40 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 0041be40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041be40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041be40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0041be40 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0041be40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0041be40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0041be40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041be40 bytes 00802891
+ 0041be40 bytes 00802b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbdeb0e47655aed68a7e094574f9ffdd"></a>

### [`0041bf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bf20.md) → [`0041bf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) FUN_0041bf20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`00419718`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419718.md) [`0041be0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be0c.md) [`00420940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420940.md) · 呼出先 4件 [`00ad3aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad3/00ad3aec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 3件 [`00419718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419718.md) [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`00420940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md) · 呼出先 4件 [`00ad3bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
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
                "const:21c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
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
                "const:18f:8"
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
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
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
      "definition_site": "0041bf88",
      "incomplete_value": true,
      "site": "0041bf9c",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041bfa0",
      "incomplete_value": true,
      "site": "0041bfa0",
      "value": [
        "LOAD",
        "8",
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
                "const:1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041bfa0",
      "incomplete_value": true,
      "site": "0041bfa0",
      "value": [
        "LOAD",
        "8",
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
                "const:1e:8"
              ]
            ]
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
      "0041bf88",
      "READ",
      [
        "storage",
        "0029e18f",
        null,
        "string"
      ]
    ],
    [
      "0041bf88",
      "READ",
      [
        "storage",
        "0029e19f",
        null,
        "string"
      ]
    ],
    [
      "0041bf90",
      "READ",
      [
        "storage",
        "0029e1ad",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0041bf88",
      "READ",
      [
        "storage",
        "0029e21c",
        null,
        "string"
      ]
    ],
    [
      "0041bf88",
      "READ",
      [
        "storage",
        "0029e22c",
        null,
        "string"
      ]
    ],
    [
      "0041bf90",
      "READ",
      [
        "storage",
        "0029e23a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041bf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bf20.md#insn-0041bf80) · [`0041bf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bf20.md#insn-0041bf84)
- 新版 [`0041bf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md#insn-0041bf80) · [`0041bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md#insn-0041bf84)

~~~diff
- 0041bf80 ["COPY", "tmp:0:8", ["const:18f:8"]]
- 0041bf80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041bf80 ["COPY", "tmp:0:8", ["const:21c:8"]]
+ 0041bf80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041bf80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041bf80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041bf80 bytes 083d0691
+ 0041bf80 bytes 08710891
- 0041bf84 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0041bf84 bytes a9f4ffd0
+ 0041bf84 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 0041bf84 bytes a9f4ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebb820ccfba2e4c36d20c5b80abeb017"></a>

### [`0041c120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md) → [`0041c120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md) FUN_0041c120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 9件 [`0073496c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00734/0073496c.md) [`0081fa64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00821/00821350.md) [`0084c390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084c/0084c390.md) [`0084f35c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b470.md) [`00428d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428d08.md) [`0045e558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md)
- 新版 呼出元 9件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) [`0081fa64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081fa64.md) [`00821350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00821/00821350.md) [`0084c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c390.md) [`0084f35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084f/0084f35c.md) · 呼出先 24件 [`0041ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041a/0041ac3c.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041b470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b470.md) [`00428d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428d08.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041c3cc",
      "incomplete_value": true,
      "site": "0041c3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c3cc",
      "incomplete_value": true,
      "site": "0041c3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041c634",
      "incomplete_value": false,
      "site": "0041c63c",
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
            "const:381:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c634",
      "incomplete_value": false,
      "site": "0041c63c",
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
            "const:2f4:8"
          ]
        ]
      ]
    },
    "ordinal": 54,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041c268",
      "READ",
      [
        "storage",
        "00c1acb8",
        null,
        "pointer"
      ]
    ],
    [
      "0041c2d4",
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      "0041c3cc",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0041c268",
      "READ",
      [
        "storage",
        "00c1ad68",
        null,
        "pointer"
      ]
    ],
    [
      "0041c2d4",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0041c3cc",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041c268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md#insn-0041c268) · [`0041c27c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md#insn-0041c27c) · [`0041c3c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c120.md#insn-0041c3c8)
- 新版 [`0041c268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md#insn-0041c268) · [`0041c27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md#insn-0041c27c) · [`0041c3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c120.md#insn-0041c3c8)

~~~diff
- 0041c268 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cb8:8"]]
- 0041c268 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041c268 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d68:8"]]
+ 0041c268 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0041c268 bytes 295d46f9
+ 0041c268 bytes 29b546f9
- 0041c27c ["COPY", "tmp:0:8", ["const:253:8"]]
- 0041c27c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0041c27c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0041c27c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0041c27c ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0041c27c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0041c27c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0041c27c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0041c27c bytes d64e0991
+ 0041c27c bytes d6fe0691
- 0041c3c8 ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 0041c3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041c3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041c3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041c3c8 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 0041c3c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041c3c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041c3c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041c3c8 bytes 08152391
+ 0041c3c8 bytes 08492591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ffa5ff47a0d301d25b21186b57e1f8"></a>

### [`0041c8f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md) → [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) FUN_0041c8f8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 25件 [`0060468c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b9c.md) [`00ad3d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad3/00ad3d8c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 25件 [`0060468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00604/0060468c.md) [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`0068d484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0068d/0068d484.md) [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b9c.md) [`00ad3e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3e54.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

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
      "definition_site": "0041c924",
      "incomplete_value": false,
      "site": "0041c92c",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041c924",
      "incomplete_value": false,
      "site": "0041c92c",
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
            "const:418:8"
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
      "0041c92c",
      "DATA",
      [
        "storage",
        "00be6418",
        null,
        "undefined *"
      ]
    ],
    [
      "0041c960",
      "READ",
      [
        "storage",
        "00be6438",
        null,
        "pointer"
      ]
    ],
    [
      "0041c960",
      "READ",
      [
        "storage",
        "00be6440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0041c92c",
      "DATA",
      [
        "storage",
        "00be64c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0041c960",
      "READ",
      [
        "storage",
        "00be64e8",
        null,
        "pointer"
      ]
    ],
    [
      "0041c960",
      "READ",
      [
        "storage",
        "00be64f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041c924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8f8.md#insn-0041c924)
- 新版 [`0041c924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md#insn-0041c924)

~~~diff
- 0041c924 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0041c924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041c924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041c924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041c924 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0041c924 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041c924 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041c924 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041c924 bytes 08611091
+ 0041c924 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50dd3aaf4ff85aa78f814b023c2441ef"></a>

### [`0041c9f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c9f4.md) → [`0041c9f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9f4.md) FUN_0041c9f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00acc460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acc/00acc460.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b9c.md) [`00ad3d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad3/00ad3d8c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00acc528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acc/00acc528.md) · 呼出先 4件 [`00420b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b98.md) [`00420b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b9c.md) [`00ad3e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3e54.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041ca14",
      "incomplete_value": false,
      "site": "0041ca24",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041ca14",
      "incomplete_value": false,
      "site": "0041ca24",
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
            "const:418:8"
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
      "0041ca24",
      "DATA",
      [
        "storage",
        "00be6418",
        null,
        "undefined *"
      ]
    ],
    [
      "0041ca58",
      "READ",
      [
        "storage",
        "00be6438",
        null,
        "pointer"
      ]
    ],
    [
      "0041ca58",
      "READ",
      [
        "storage",
        "00be6440",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0041ca24",
      "DATA",
      [
        "storage",
        "00be64c8",
        null,
        "undefined *"
      ]
    ],
    [
      "0041ca58",
      "READ",
      [
        "storage",
        "00be64e8",
        null,
        "pointer"
      ]
    ],
    [
      "0041ca58",
      "READ",
      [
        "storage",
        "00be64f0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ca14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c9f4.md#insn-0041ca14)
- 新版 [`0041ca14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c9f4.md#insn-0041ca14)

~~~diff
- 0041ca14 ["COPY", "tmp:0:8", ["const:418:8"]]
- 0041ca14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0041ca14 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 0041ca14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0041ca14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0041ca14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041ca14 bytes 29611091
+ 0041ca14 bytes 29211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3103f46d3c666208cb9f39119c9b1fe9"></a>

### [`0041cad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cad8.md) → [`0041cad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md) FUN_0041cad8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041c8ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420938.md) [`0042093c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042093c.md) [`00420b18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b18.md) [`00420b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b1c.md) [`00ad3af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad3/00ad3af0.md)
- 新版 呼出元 1件 [`0041c8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8ec.md) · 呼出先 6件 [`00420938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420938.md) [`0042093c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042093c.md) [`00420b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b18.md) [`00420b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b1c.md) [`00ad3bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad3/00ad3bb8.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.94% / 新版 91.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0041caf8",
      "incomplete_value": false,
      "site": "0041cb1c",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041caf8",
      "incomplete_value": false,
      "site": "0041cb1c",
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
            "const:2f8:8"
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
      "definition_site": "0041cb14",
      "incomplete_value": false,
      "site": "0041cb20",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb14",
      "incomplete_value": false,
      "site": "0041cb20",
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
            "const:388:8"
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
      "definition_site": "0041cb2c",
      "incomplete_value": false,
      "site": "0041cb40",
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
            "const:21c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cb2c",
      "incomplete_value": false,
      "site": "0041cb40",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041cb1c",
      "DATA",
      [
        "storage",
        "00be62f8",
        null,
        "undefined *"
      ]
    ],
    [
      "0041cb20",
      "DATA",
      [
        "storage",
        "00be6388",
        null,
        "undefined *"
      ]
    ],
    [
      "0041cb2c",
      "PARAM",
      [
        "storage",
        "0029e18f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0041cb1c",
      "DATA",
      [
        "storage",
        "00be63a8",
        null,
        "undefined *"
      ]
    ],
    [
      "0041cb20",
      "DATA",
      [
        "storage",
        "00be6438",
        null,
        "undefined *"
      ]
    ],
    [
      "0041cb2c",
      "PARAM",
      [
        "storage",
        "0029e21c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041caf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cad8.md#insn-0041caf8) · [`0041cb14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cad8.md#insn-0041cb14) · [`0041cb2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cad8.md#insn-0041cb2c)
- 新版 [`0041caf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md#insn-0041caf8) · [`0041cb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md#insn-0041cb14) · [`0041cb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cad8.md#insn-0041cb2c)

~~~diff
- 0041caf8 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0041caf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0041caf8 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0041caf8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0041caf8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0041caf8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041caf8 bytes 29e10b91
+ 0041caf8 bytes 29a10e91
- 0041cb14 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0041cb14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0041cb14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0041cb14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0041cb14 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 0041cb14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0041cb14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0041cb14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0041cb14 bytes 08210e91
+ 0041cb14 bytes 08e11091
- 0041cb2c ["COPY", "tmp:0:8", ["const:18f:8"]]
- 0041cb2c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0041cb2c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0041cb2c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0041cb2c ["COPY", "tmp:0:8", ["const:21c:8"]]
+ 0041cb2c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0041cb2c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0041cb2c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0041cb2c bytes 633c0691
+ 0041cb2c bytes 63700891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05cd917caf19c5d2b9f8a5992ed0652"></a>

### [`0041cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md) → [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) FUN_0041cddc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00a2ba24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a2b/00a2ba24.md) [`00ab1cbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ab1/00ab1cbc.md) · 呼出先 23件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e54c.md) [`00420bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bd8.md) [`0045e558`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045e/0045e558.md)
- 新版 呼出元 2件 [`00a2ba24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2b/00a2ba24.md) [`00ab1d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ab1/00ab1d84.md) · 呼出先 23件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00420bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) [`0045e558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045e558.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041cf60",
      "incomplete_value": true,
      "site": "0041cf60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:952:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041cf60",
      "incomplete_value": true,
      "site": "0041cf60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c5:8"
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
      "definition_site": "0041d3c8",
      "incomplete_value": true,
      "site": "0041d3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:74e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d3c8",
      "incomplete_value": true,
      "site": "0041d3d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 84,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0041d530",
      "incomplete_value": true,
      "site": "0041d548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2fe:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041d530",
      "incomplete_value": true,
      "site": "0041d548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:271:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 93,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041ce48",
      "PARAM",
      [
        "storage",
        "002a9253",
        null,
        null
      ]
    ],
    [
      "0041cf50",
      "READ",
      [
        "storage",
        "002978c5",
        null,
        "string"
      ]
    ],
    [
      "0041d094",
      "READ",
      [
        "storage",
        "00294539",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0041ce48",
      "PARAM",
      [
        "storage",
        "002a91bf",
        null,
        null
      ]
    ],
    [
      "0041cf50",
      "READ",
      [
        "storage",
        "00297952",
        null,
        "string"
      ]
    ],
    [
      "0041d094",
      "READ",
      [
        "storage",
        "002945c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041ce48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md#insn-0041ce48) · [`0041cf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md#insn-0041cf48) · [`0041d088`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md#insn-0041d088)
- 新版 [`0041ce48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md#insn-0041ce48) · [`0041cf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md#insn-0041cf48) · [`0041d088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md#insn-0041d088)

~~~diff
- 0041ce48 ["COPY", "tmp:0:8", ["const:253:8"]]
- 0041ce48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041ce48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041ce48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041ce48 ["COPY", "tmp:0:8", ["const:1bf:8"]]
+ 0041ce48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041ce48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041ce48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041ce48 bytes 214c0991
+ 0041ce48 bytes 21fc0691
- 0041cf48 ["COPY", "tmp:0:8", ["const:8c5:8"]]
- 0041cf48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0041cf48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0041cf48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0041cf48 ["COPY", "tmp:0:8", ["const:952:8"]]
+ 0041cf48 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0041cf48 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0041cf48 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0041cf48 bytes 29152391
+ 0041cf48 bytes 29492591
- 0041d088 ["COPY", "tmp:0:8", ["const:539:8"]]
- 0041d088 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 0041d088 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 0041d088 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 0041d088 ["COPY", "tmp:0:8", ["const:5c6:8"]]
+ 0041d088 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 0041d088 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 0041d088 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 0041d088 bytes 6be51491
+ 0041d088 bytes 6b191791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eedfe7db2f2e7937dff0b7842d4db036"></a>

### [`0041e03c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md) → [`0041e03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md) FUN_0041e03c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`00692224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00692/00692224.md) [`007da86c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007da/007da86c.md) [`007e5fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/007e5/007e5fa4.md) [`0086b704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md) [`00bdb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb070.md)
- 新版 呼出元 4件 [`00692224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00692/00692224.md) [`007da86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007da/007da86c.md) [`007e5fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007e5/007e5fa4.md) [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 75.00% / 新版 75.00%

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
      "definition_site": "0041e06c",
      "incomplete_value": true,
      "site": "0041e074",
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
      "definition_site": "0041e06c",
      "incomplete_value": true,
      "site": "0041e074",
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
      "definition_site": "0041e078",
      "incomplete_value": true,
      "site": "0041e078",
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
      "definition_site": "0041e078",
      "incomplete_value": true,
      "site": "0041e078",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0041e088",
      "incomplete_value": true,
      "site": "0041e088",
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
                "register:4000:8"
              ],
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
      "definition_site": "0041e088",
      "incomplete_value": true,
      "site": "0041e088",
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
                "register:4000:8"
              ],
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
      "0041e058",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "0041e05c",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "0041e068",
      "READ",
      [
        "storage",
        "00c13358",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "0041e058",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0041e05c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "0041e068",
      "READ",
      [
        "storage",
        "00c13408",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041e058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md#insn-0041e058) · [`0041e05c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md#insn-0041e05c) · [`0041e060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e03c.md#insn-0041e060)
- 新版 [`0041e058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md#insn-0041e058) · [`0041e05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e03c.md#insn-0041e05c)

~~~diff
- 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 0041e058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041e058 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 0041e058 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0041e058 bytes 086146f9
+ 0041e058 bytes 08b946f9
- 0041e05c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc8:8"]]
- 0041e05c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041e05c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 0041e05c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0041e05c bytes d66646f9
+ 0041e05c bytes d6be46f9
- 0041e060 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 0041e060 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2100cba132aa863707c11cda0f8bfc99"></a>

### [`0041e380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md) → [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) FUN_0041e380

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 535件 [`0041cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md) [`0041e10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e10c.md) [`00439bc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00439/00439bc0.md) [`0043aca0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043a/0043aca0.md) [`0043ec60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbac28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbac28.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md) [`00bdb0e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 535件 [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) [`0041e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00439bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439bc0.md) [`0043aca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aca0.md) [`0043ec60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043ec60.md) · 呼出先 4件 [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 84.62% / 新版 84.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041e3a8",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3a8",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0041e3ac",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041e3ac",
      "incomplete_value": true,
      "site": "0041e3b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0041e3a8",
      "READ",
      [
        "storage",
        "00c1ace0",
        null,
        "pointer"
      ]
    ],
    [
      "0041e3a8",
      "PARAM",
      [
        "storage",
        "00c16808",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0041e3ac",
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
      "0041e3a8",
      "READ",
      [
        "storage",
        "00c1ad90",
        null,
        "pointer"
      ]
    ],
    [
      "0041e3a8",
      "PARAM",
      [
        "storage",
        "00c168b8",
        "_ZTISt20bad_array_new_length",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0041e3ac",
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

- 旧版 [`0041e3a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md#insn-0041e3a8) · [`0041e3ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e380.md#insn-0041e3ac)
- 新版 [`0041e3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md#insn-0041e3a8) · [`0041e3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md#insn-0041e3ac)

~~~diff
- 0041e3a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ce0:8"]]
- 0041e3a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041e3a8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:d90:8"]]
+ 0041e3a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0041e3a8 bytes 217046f9
+ 0041e3a8 bytes 21c846f9
- 0041e3ac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:ce8:8"]]
- 0041e3ac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041e3ac ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:d98:8"]]
+ 0041e3ac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0041e3ac bytes 427446f9
+ 0041e3ac bytes 42cc46f9
~~~


<a id="compare-003e4ebb285e7d9a429f65eeba49c011"></a>

### [`0041e41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md) → [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) FUN_0041e41c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 43件 [`0041e10c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e10c.md) [`00450668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00450/00450668.md) [`004629d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00462/004629d4.md) [`0049100c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00491/0049100c.md) [`0049b54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 43件 [`0041e10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e10c.md) [`00450668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00450/00450668.md) [`004629d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00462/004629d4.md) [`0049100c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md) [`0049b54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0049b/0049b54c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "0041e428",
      "incomplete_value": false,
      "site": "0041e42c",
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
      "definition_site": "0041e428",
      "incomplete_value": false,
      "site": "0041e42c",
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
      "0041e428",
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
      "0041e428",
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

- 旧版 [`0041e428`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e41c.md#insn-0041e428)
- 新版 [`0041e428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md#insn-0041e428)

~~~diff
- 0041e428 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 0041e428 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041e428 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041e428 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0041e428 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 0041e428 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0041e428 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0041e428 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041e428 bytes 00280c91
+ 0041e428 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca22a84b464ada42d540b2622ebd15c8"></a>

### [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md) → [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) FUN_0041e778

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`0041e650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e650.md) [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md) [`005f1af0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f1/005f1af0.md) [`005f5668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md)
- 新版 呼出元 4件 [`0041e650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e650.md) [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`005f1af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f1/005f1af0.md) [`005f5668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005f5/005f5668.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041e8e8",
      "incomplete_value": false,
      "site": "0041e8f0",
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
      "definition_site": "0041e8e8",
      "incomplete_value": false,
      "site": "0041e8f0",
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
      "definition_site": "0041e9a0",
      "incomplete_value": false,
      "site": "0041e9a8",
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
      "definition_site": "0041e9a0",
      "incomplete_value": false,
      "site": "0041e9a8",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041eccc",
      "incomplete_value": false,
      "site": "0041ecdc",
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
      "definition_site": "0041eccc",
      "incomplete_value": false,
      "site": "0041ecdc",
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
    "ordinal": 20,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041e8e8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0041e9a0",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0041eccc",
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
      "0041e8e8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0041e9a0",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0041eccc",
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

- 旧版 [`0041e8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md#insn-0041e8e8) · [`0041e9a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md#insn-0041e9a0) · [`0041eccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md#insn-0041eccc)
- 新版 [`0041e8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md#insn-0041e8e8) · [`0041e9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md#insn-0041e9a0) · [`0041eccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md#insn-0041eccc)

~~~diff
- 0041e8e8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 0041e8e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041e8e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041e8e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041e8e8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0041e8e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041e8e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041e8e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041e8e8 bytes 21440c91
+ 0041e8e8 bytes 21280c91
- 0041e9a0 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0041e9a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041e9a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041e9a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041e9a0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0041e9a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041e9a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041e9a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041e9a0 bytes 21d40b91
+ 0041e9a0 bytes 21b80b91
- 0041eccc ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0041eccc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0041eccc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0041eccc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0041eccc ["COPY", "tmp:0:8", ["const:672:8"]]
+ 0041eccc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0041eccc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0041eccc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0041eccc bytes 63941791
+ 0041eccc bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8db5cf01ed9d8ca6a17c0341beec4ef"></a>

### [`0041f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md) → [`0041f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) FUN_0041f3d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md) [`0041f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md) [`0045a988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0045a/0045a988.md) [`0046ff30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046f/0046ff30.md) [`00710214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 7件 [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`0041f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) [`0045a988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045a/0045a988.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`00710214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00710/00710214.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.01% / 新版 99.01%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041f53c",
      "incomplete_value": false,
      "site": "0041f544",
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
      "definition_site": "0041f53c",
      "incomplete_value": false,
      "site": "0041f544",
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
      "definition_site": "0041f5f4",
      "incomplete_value": false,
      "site": "0041f5fc",
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
      "definition_site": "0041f5f4",
      "incomplete_value": false,
      "site": "0041f5fc",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041f8cc",
      "incomplete_value": false,
      "site": "0041f8dc",
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
      "definition_site": "0041f8cc",
      "incomplete_value": false,
      "site": "0041f8dc",
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
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0041f53c",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0041f5f4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "0041f8cc",
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
      "0041f53c",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0041f5f4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "0041f8cc",
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

- 旧版 [`0041f53c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md#insn-0041f53c) · [`0041f5f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md#insn-0041f5f4) · [`0041f8cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md#insn-0041f8cc)
- 新版 [`0041f53c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md#insn-0041f53c) · [`0041f5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md#insn-0041f5f4) · [`0041f8cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md#insn-0041f8cc)

~~~diff
- 0041f53c ["COPY", "tmp:0:8", ["const:311:8"]]
- 0041f53c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041f53c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041f53c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041f53c ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 0041f53c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041f53c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041f53c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041f53c bytes 21440c91
+ 0041f53c bytes 21280c91
- 0041f5f4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0041f5f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0041f5f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0041f5f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0041f5f4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0041f5f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0041f5f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0041f5f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0041f5f4 bytes 21d40b91
+ 0041f5f4 bytes 21b80b91
- 0041f8cc ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 0041f8cc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 0041f8cc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 0041f8cc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 0041f8cc ["COPY", "tmp:0:8", ["const:672:8"]]
+ 0041f8cc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 0041f8cc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 0041f8cc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 0041f8cc bytes 63941791
+ 0041f8cc bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8f42ed75039a426f3a1000c105002fa"></a>

### [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) → [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) FUN_0041fddc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 130件 [`0041e778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e778.md) [`0041f280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f354.md) [`0041f3d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f3d4.md) [`00424280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md)
- 新版 呼出元 130件 [`0041e778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e778.md) [`0041f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f280.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`0041f3d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f3d4.md) [`00424280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)

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
      "definition_site": "0041fde8",
      "incomplete_value": false,
      "site": "0041fdec",
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
            "const:1b2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fde8",
      "incomplete_value": false,
      "site": "0041fdec",
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
            "const:246:8"
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
      "0041fde8",
      "PARAM",
      [
        "storage",
        "002a9246",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0041fde8",
      "PARAM",
      [
        "storage",
        "002a91b2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041fde8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md#insn-0041fde8)
- 新版 [`0041fde8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md#insn-0041fde8)

~~~diff
- 0041fde8 ["COPY", "tmp:0:8", ["const:246:8"]]
- 0041fde8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0041fde8 ["COPY", "tmp:0:8", ["const:1b2:8"]]
+ 0041fde8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0041fde8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0041fde8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0041fde8 bytes 00180991
+ 0041fde8 bytes 00c80691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ed75f75d70459a32cfc7fc708969be"></a>

### [`0041fdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md) → [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) FUN_0041fdf0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 222件 [`0041fddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fddc.md) [`00463ea0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00463/00463ea0.md) [`0047c518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c518.md) [`0047c52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0047c/0047c540.md) · 呼出先 4件 [`0041fe40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fe40.md) [`00bbad50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bba/00bbad50.md) [`00bdafa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafa0.md) [`00bdafc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdafc0.md)
- 新版 呼出元 222件 [`0041fddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fddc.md) [`00463ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00463/00463ea0.md) [`0047c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c518.md) [`0047c52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c52c.md) [`0047c540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c540.md) · 呼出先 4件 [`0041fe40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fe40.md) [`00bbae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbae18.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0041fe20",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fe20",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf0:8"
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
      "definition_site": "0041fe24",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0041fe24",
      "incomplete_value": true,
      "site": "0041fe28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
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
      "0041fe20",
      "READ",
      [
        "storage",
        "00c1acf0",
        null,
        "pointer"
      ]
    ],
    [
      "0041fe20",
      "PARAM",
      [
        "storage",
        "00c16970",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0041fe24",
      "READ",
      [
        "storage",
        "00c1acf8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0041fe20",
      "READ",
      [
        "storage",
        "00c1ada0",
        null,
        "pointer"
      ]
    ],
    [
      "0041fe20",
      "PARAM",
      [
        "storage",
        "00c16a20",
        "_ZTISt12out_of_range",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0041fe24",
      "READ",
      [
        "storage",
        "00c1ada8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0041fe20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md#insn-0041fe20) · [`0041fe24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041fdf0.md#insn-0041fe24)
- 新版 [`0041fe20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md#insn-0041fe20) · [`0041fe24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md#insn-0041fe24)

~~~diff
- 0041fe20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:cf0:8"]]
- 0041fe20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041fe20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:da0:8"]]
+ 0041fe20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0041fe20 bytes 217846f9
+ 0041fe20 bytes 21d046f9
- 0041fe24 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:cf8:8"]]
- 0041fe24 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 0041fe24 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:da8:8"]]
+ 0041fe24 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 0041fe24 bytes 427c46f9
+ 0041fe24 bytes 42d446f9
~~~


<a id="compare-35c9f7a9b318ebdecbcb9c4d385d7f74"></a>

### [`00420234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420234.md) → [`00420234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420234.md) FUN_00420234

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
      "definition_site": "00420248",
      "incomplete_value": false,
      "site": "0042024c",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420248",
      "incomplete_value": false,
      "site": "0042024c",
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
            "const:f38:8"
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
      "0042024c",
      "DATA",
      [
        "storage",
        "00be5f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042024c",
      "DATA",
      [
        "storage",
        "00be5fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420248`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420234.md#insn-00420248)
- 新版 [`00420248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420234.md#insn-00420248)

~~~diff
- 00420248 ["COPY", "tmp:0:8", ["const:f38:8"]]
- 00420248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420248 ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 00420248 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420248 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420248 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420248 bytes 08e13c91
+ 00420248 bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c95b9cd99b72691d2d3efd40785a3163"></a>

### [`00420258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420258.md) → [`00420258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420258.md) FUN_00420258

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
      "definition_site": "0042025c",
      "incomplete_value": false,
      "site": "00420260",
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
            "const:fe8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042025c",
      "incomplete_value": false,
      "site": "00420260",
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
      "00420260",
      "DATA",
      [
        "storage",
        "00be5f38",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420260",
      "DATA",
      [
        "storage",
        "00be5fe8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042025c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420258.md#insn-0042025c)
- 新版 [`0042025c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420258.md#insn-0042025c)

~~~diff
- 0042025c ["COPY", "tmp:0:8", ["const:f38:8"]]
- 0042025c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042025c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042025c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042025c ["COPY", "tmp:0:8", ["const:fe8:8"]]
+ 0042025c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042025c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042025c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042025c bytes 08e13c91
+ 0042025c bytes 08a13f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8b83ff8bda9ac86252478862ea4cc69"></a>

### [`0042035c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042035c.md) → [`0042035c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042035c.md) FUN_0042035c

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
      "definition_site": "00420380",
      "incomplete_value": false,
      "site": "00420380",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420380",
      "incomplete_value": false,
      "site": "00420380",
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
            "const:fc8:8"
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
      "00420380",
      "DATA",
      [
        "storage",
        "00be5fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420380",
      "DATA",
      [
        "storage",
        "00be6078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042035c.md#insn-00420378) · [`0042037c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042035c.md#insn-0042037c)
- 新版 [`00420378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042035c.md#insn-00420378) · [`0042037c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042035c.md#insn-0042037c)

~~~diff
- 00420378 ["COPY", "register:4040:8", ["const:be5000:8"]]
+ 00420378 ["COPY", "register:4040:8", ["const:be6000:8"]]
- 00420378 bytes 283e00b0
+ 00420378 bytes 283e00d0
- 0042037c ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 0042037c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042037c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042037c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042037c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0042037c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042037c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042037c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042037c bytes 08213f91
+ 0042037c bytes 08e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad472f8da4a392136e43089692038b26"></a>

### [`00420390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420390.md) → [`00420390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420390.md) FUN_00420390

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
      "definition_site": "0042039c",
      "incomplete_value": false,
      "site": "0042039c",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042039c",
      "incomplete_value": false,
      "site": "0042039c",
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
            "const:fc8:8"
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
      "0042039c",
      "DATA",
      [
        "storage",
        "00be5fc8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042039c",
      "DATA",
      [
        "storage",
        "00be6078",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420390.md#insn-00420394) · [`00420398`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420390.md#insn-00420398)
- 新版 [`00420394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420390.md#insn-00420394) · [`00420398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420390.md#insn-00420398)

~~~diff
- 00420394 ["COPY", "register:4048:8", ["const:be5000:8"]]
+ 00420394 ["COPY", "register:4048:8", ["const:be6000:8"]]
- 00420394 bytes 293e00b0
+ 00420394 bytes 293e00d0
- 00420398 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00420398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00420398 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00420398 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00420398 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00420398 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420398 bytes 29213f91
+ 00420398 bytes 29e10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8575aaf853475dcd39c139c8d9313e10"></a>

### [`004203e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004203e8.md) → [`004203e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203e8.md) FUN_004203e8

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
      "definition_site": "0042040c",
      "incomplete_value": false,
      "site": "0042040c",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042040c",
      "incomplete_value": false,
      "site": "0042040c",
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
      "0042040c",
      "DATA",
      [
        "storage",
        "00be6058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042040c",
      "DATA",
      [
        "storage",
        "00be6108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004203e8.md#insn-00420408)
- 新版 [`00420408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004203e8.md#insn-00420408)

~~~diff
- 00420408 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00420408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420408 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00420408 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420408 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420408 bytes 08610191
+ 00420408 bytes 08210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2825654187a7991c9ac0743ed40b812"></a>

### [`0042041c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042041c.md) → [`0042041c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042041c.md) FUN_0042041c

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
      "definition_site": "00420428",
      "incomplete_value": false,
      "site": "00420428",
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
            "const:108:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420428",
      "incomplete_value": false,
      "site": "00420428",
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
      "00420428",
      "DATA",
      [
        "storage",
        "00be6058",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420428",
      "DATA",
      [
        "storage",
        "00be6108",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420424`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042041c.md#insn-00420424)
- 新版 [`00420424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042041c.md#insn-00420424)

~~~diff
- 00420424 ["COPY", "tmp:0:8", ["const:58:8"]]
- 00420424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00420424 ["COPY", "tmp:0:8", ["const:108:8"]]
+ 00420424 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00420424 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00420424 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420424 bytes 29610191
+ 00420424 bytes 29210491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfd40ca5381886276da37e7190771f9e"></a>

### [`00420530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420530.md) → [`00420530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420530.md) FUN_00420530

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
      "definition_site": "00420554",
      "incomplete_value": false,
      "site": "00420554",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420554",
      "incomplete_value": false,
      "site": "00420554",
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
            "const:e8:8"
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
      "00420554",
      "DATA",
      [
        "storage",
        "00be60e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420554",
      "DATA",
      [
        "storage",
        "00be6198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420550`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420530.md#insn-00420550)
- 新版 [`00420550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420530.md#insn-00420550)

~~~diff
- 00420550 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00420550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420550 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00420550 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420550 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420550 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420550 bytes 08a10391
+ 00420550 bytes 08610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098d15415be7a5af634ce51451569ce4"></a>

### [`00420564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420564.md) → [`00420564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420564.md) FUN_00420564

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
      "definition_site": "00420570",
      "incomplete_value": false,
      "site": "00420570",
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
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420570",
      "incomplete_value": false,
      "site": "00420570",
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
            "const:e8:8"
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
      "00420570",
      "DATA",
      [
        "storage",
        "00be60e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420570",
      "DATA",
      [
        "storage",
        "00be6198",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042056c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420564.md#insn-0042056c)
- 新版 [`0042056c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420564.md#insn-0042056c)

~~~diff
- 0042056c ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0042056c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0042056c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0042056c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0042056c ["COPY", "tmp:0:8", ["const:198:8"]]
+ 0042056c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0042056c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0042056c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0042056c bytes 29a10391
+ 0042056c bytes 29610691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45b6ac5b332eb8b1f52c7a80eb419913"></a>

### [`0042062c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042062c.md) → [`0042062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042062c.md) FUN_0042062c

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
      "definition_site": "00420650",
      "incomplete_value": false,
      "site": "00420650",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420650",
      "incomplete_value": false,
      "site": "00420650",
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
            "const:178:8"
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
      "00420650",
      "DATA",
      [
        "storage",
        "00be6178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420650",
      "DATA",
      [
        "storage",
        "00be6228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042064c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042062c.md#insn-0042064c)
- 新版 [`0042064c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042062c.md#insn-0042064c)

~~~diff
- 0042064c ["COPY", "tmp:0:8", ["const:178:8"]]
- 0042064c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042064c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042064c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042064c ["COPY", "tmp:0:8", ["const:228:8"]]
+ 0042064c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042064c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042064c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042064c bytes 08e10591
+ 0042064c bytes 08a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80b2dcb238d12b6044d10ad2763a0ae4"></a>

### [`00420660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420660.md) → [`00420660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420660.md) FUN_00420660

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
      "definition_site": "0042066c",
      "incomplete_value": false,
      "site": "0042066c",
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
            "const:228:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042066c",
      "incomplete_value": false,
      "site": "0042066c",
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
      "0042066c",
      "DATA",
      [
        "storage",
        "00be6178",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042066c",
      "DATA",
      [
        "storage",
        "00be6228",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420660.md#insn-00420668)
- 新版 [`00420668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420660.md#insn-00420668)

~~~diff
- 00420668 ["COPY", "tmp:0:8", ["const:178:8"]]
- 00420668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00420668 ["COPY", "tmp:0:8", ["const:228:8"]]
+ 00420668 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00420668 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00420668 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420668 bytes 29e10591
+ 00420668 bytes 29a10891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09055db03d8f9810ea62172534a094ca"></a>

### [`004206bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004206bc.md) → [`004206bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206bc.md) FUN_004206bc

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
      "definition_site": "004206e0",
      "incomplete_value": false,
      "site": "004206e0",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206e0",
      "incomplete_value": false,
      "site": "004206e0",
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
            "const:1f8:8"
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
      "004206e0",
      "DATA",
      [
        "storage",
        "00be61f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004206e0",
      "DATA",
      [
        "storage",
        "00be62a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004206dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004206bc.md#insn-004206dc)
- 新版 [`004206dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206bc.md#insn-004206dc)

~~~diff
- 004206dc ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 004206dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004206dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004206dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004206dc ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 004206dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004206dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004206dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004206dc bytes 08e10791
+ 004206dc bytes 08a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02aa612e9645ad085551b812025d10a9"></a>

### [`004206f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004206f0.md) → [`004206f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206f0.md) FUN_004206f0

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
      "definition_site": "004206fc",
      "incomplete_value": false,
      "site": "004206fc",
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
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004206fc",
      "incomplete_value": false,
      "site": "004206fc",
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
            "const:1f8:8"
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
      "004206fc",
      "DATA",
      [
        "storage",
        "00be61f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004206fc",
      "DATA",
      [
        "storage",
        "00be62a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004206f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/004206f0.md#insn-004206f8)
- 新版 [`004206f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/004206f0.md#insn-004206f8)

~~~diff
- 004206f8 ["COPY", "tmp:0:8", ["const:1f8:8"]]
- 004206f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004206f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004206f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004206f8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
+ 004206f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004206f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004206f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004206f8 bytes 29e10791
+ 004206f8 bytes 29a10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42768063456dfdd9d851aff1262ccfa4"></a>

### [`00420808`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420808.md) → [`00420808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420808.md) FUN_00420808

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
      "definition_site": "0042082c",
      "incomplete_value": false,
      "site": "0042082c",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042082c",
      "incomplete_value": false,
      "site": "0042082c",
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
            "const:278:8"
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
      "0042082c",
      "DATA",
      [
        "storage",
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042082c",
      "DATA",
      [
        "storage",
        "00be6328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420808.md#insn-00420828)
- 新版 [`00420828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420808.md#insn-00420828)

~~~diff
- 00420828 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00420828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420828 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00420828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420828 bytes 08e10991
+ 00420828 bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91a2991b0d8bbd68ab862515fbb25cfa"></a>

### [`0042083c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042083c.md) → [`0042083c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042083c.md) FUN_0042083c

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
      "definition_site": "00420848",
      "incomplete_value": false,
      "site": "00420848",
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
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420848",
      "incomplete_value": false,
      "site": "00420848",
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
            "const:278:8"
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
      "00420848",
      "DATA",
      [
        "storage",
        "00be6278",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420848",
      "DATA",
      [
        "storage",
        "00be6328",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/0042083c.md#insn-00420844)
- 新版 [`00420844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/0042083c.md#insn-00420844)

~~~diff
- 00420844 ["COPY", "tmp:0:8", ["const:278:8"]]
- 00420844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00420844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00420844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00420844 ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00420844 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00420844 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00420844 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00420844 bytes 29e10991
+ 00420844 bytes 29a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c650dfdefd6f2051092c441761d8b528"></a>

### [`00420904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420904.md) → [`00420904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420904.md) FUN_00420904

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
      "definition_site": "00420918",
      "incomplete_value": false,
      "site": "0042091c",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420918",
      "incomplete_value": false,
      "site": "0042091c",
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
            "const:2f8:8"
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
      "0042091c",
      "DATA",
      [
        "storage",
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042091c",
      "DATA",
      [
        "storage",
        "00be63a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420904.md#insn-00420918)
- 新版 [`00420918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420904.md#insn-00420918)

~~~diff
- 00420918 ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 00420918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420918 ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00420918 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420918 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420918 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420918 bytes 08e10b91
+ 00420918 bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd92a1aa67460830ac2dbf3a8b79c184"></a>

### [`00420928`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420928.md) → [`00420928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420928.md) FUN_00420928

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
      "definition_site": "0042092c",
      "incomplete_value": false,
      "site": "00420930",
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
            "const:3a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042092c",
      "incomplete_value": false,
      "site": "00420930",
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
            "const:2f8:8"
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
      "00420930",
      "DATA",
      [
        "storage",
        "00be62f8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420930",
      "DATA",
      [
        "storage",
        "00be63a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042092c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420928.md#insn-0042092c)
- 新版 [`0042092c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420928.md#insn-0042092c)

~~~diff
- 0042092c ["COPY", "tmp:0:8", ["const:2f8:8"]]
- 0042092c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042092c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042092c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042092c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 0042092c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042092c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042092c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042092c bytes 08e10b91
+ 0042092c bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b90768696d9f266681fce8ad866608a3"></a>

### [`00420940`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420940.md) → [`00420940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md) FUN_00420940

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041be9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041bf20.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041be9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be9c.md) [`0041bf20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041bf20.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 78.31% / 新版 78.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004209d4",
      "incomplete_value": false,
      "site": "004209d4",
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
            "const:abc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209d4",
      "incomplete_value": false,
      "site": "004209d4",
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
            "const:9fc:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004209fc",
      "incomplete_value": false,
      "site": "00420a00",
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
            "const:ae0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004209fc",
      "incomplete_value": false,
      "site": "00420a00",
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
            "const:a20:8"
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
      "definition_site": "00420a0c",
      "incomplete_value": false,
      "site": "00420a10",
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
            "const:a88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420a0c",
      "incomplete_value": false,
      "site": "00420a10",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00420990",
      "READ",
      [
        "storage",
        "00c24a20",
        null,
        "undefined1"
      ]
    ],
    [
      "004209c4",
      "READ",
      [
        "storage",
        "00c24a20",
        null,
        "undefined1"
      ]
    ],
    [
      "004209d4",
      "WRITE",
      [
        "storage",
        "00c249fc",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00420990",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "004209c4",
      "READ",
      [
        "storage",
        "00c24ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "004209d4",
      "WRITE",
      [
        "storage",
        "00c24abc",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004209d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420940.md#insn-004209d4) · [`0042098c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420940.md#insn-0042098c) · [`004209c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420940.md#insn-004209c0)
- 新版 [`004209d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md#insn-004209d4) · [`0042098c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md#insn-0042098c) · [`004209c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420940.md#insn-004209c0)

~~~diff
- 004209d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9fc:8"]]
- 004209d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 004209d4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:abc:8"]]
+ 004209d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 004209d4 bytes 28fd09b9
+ 004209d4 bytes 28bd0ab9
- 0042098c ["COPY", "tmp:0:8", ["const:a20:8"]]
- 0042098c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042098c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042098c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042098c ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 0042098c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042098c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042098c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042098c bytes 08812891
+ 0042098c bytes 08812b91
- 004209c0 ["COPY", "tmp:0:8", ["const:a20:8"]]
- 004209c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004209c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004209c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004209c0 ["COPY", "tmp:0:8", ["const:ae0:8"]]
+ 004209c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004209c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004209c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004209c0 bytes 08812891
+ 004209c0 bytes 08812b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5a0b50721e2330c83aec5b40637b9d"></a>

### [`00420ae4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420ae4.md) → [`00420ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ae4.md) FUN_00420ae4

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
      "definition_site": "00420af8",
      "incomplete_value": false,
      "site": "00420afc",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420af8",
      "incomplete_value": false,
      "site": "00420afc",
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
            "const:388:8"
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
      "00420afc",
      "DATA",
      [
        "storage",
        "00be6388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420afc",
      "DATA",
      [
        "storage",
        "00be6438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420af8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420ae4.md#insn-00420af8)
- 新版 [`00420af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ae4.md#insn-00420af8)

~~~diff
- 00420af8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00420af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420af8 ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00420af8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420af8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420af8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420af8 bytes 08210e91
+ 00420af8 bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-36b54e18346de527c4b8eec25437cd20"></a>

### [`00420b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b08.md) → [`00420b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b08.md) FUN_00420b08

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
      "definition_site": "00420b0c",
      "incomplete_value": false,
      "site": "00420b10",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b0c",
      "incomplete_value": false,
      "site": "00420b10",
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
            "const:388:8"
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
      "00420b10",
      "DATA",
      [
        "storage",
        "00be6388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420b10",
      "DATA",
      [
        "storage",
        "00be6438",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b08.md#insn-00420b0c)
- 新版 [`00420b0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b08.md#insn-00420b0c)

~~~diff
- 00420b0c ["COPY", "tmp:0:8", ["const:388:8"]]
- 00420b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420b0c ["COPY", "tmp:0:8", ["const:438:8"]]
+ 00420b0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b0c bytes 08210e91
+ 00420b0c bytes 08e11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63690a2cc7418ff9accd7be5c60d5467"></a>

### [`00420b20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b20.md) → [`00420b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b20.md) FUN_00420b20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 60.00% / 新版 60.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00420b2c",
      "incomplete_value": true,
      "site": "00420b2c",
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
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b2c",
      "incomplete_value": true,
      "site": "00420b2c",
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
            "const:44:8"
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
      "00420b28",
      "READ",
      [
        "storage",
        "00c1ac78",
        null,
        "pointer"
      ]
    ],
    [
      "00420b2c",
      "WRITE",
      [
        "storage",
        "00c24cf4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00420b28",
      "READ",
      [
        "storage",
        "00c1ad28",
        null,
        "pointer"
      ]
    ],
    [
      "00420b2c",
      "WRITE",
      [
        "storage",
        "00c24db4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b20.md#insn-00420b28)
- 新版 [`00420b28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b20.md#insn-00420b28)

~~~diff
- 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c78:8"]]
- 00420b28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00420b28 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d28:8"]]
+ 00420b28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00420b28 bytes 083d46f9
+ 00420b28 bytes 089546f9
~~~


<a id="compare-90dac5cce6804b06e60610c8d0d2ce23"></a>

### [`00420b64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b64.md) → [`00420b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b64.md) FUN_00420b64

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
      "definition_site": "00420b78",
      "incomplete_value": false,
      "site": "00420b7c",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b78",
      "incomplete_value": false,
      "site": "00420b7c",
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
            "const:418:8"
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
      "00420b7c",
      "DATA",
      [
        "storage",
        "00be6418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420b7c",
      "DATA",
      [
        "storage",
        "00be64c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b64.md#insn-00420b78)
- 新版 [`00420b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b64.md#insn-00420b78)

~~~diff
- 00420b78 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00420b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420b78 ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00420b78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b78 bytes 08611091
+ 00420b78 bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-535de52186afc663ee0cf1e99cc961bd"></a>

### [`00420b88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b88.md) → [`00420b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b88.md) FUN_00420b88

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
      "definition_site": "00420b8c",
      "incomplete_value": false,
      "site": "00420b90",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420b8c",
      "incomplete_value": false,
      "site": "00420b90",
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
            "const:418:8"
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
      "00420b90",
      "DATA",
      [
        "storage",
        "00be6418",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00420b90",
      "DATA",
      [
        "storage",
        "00be64c8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420b88.md#insn-00420b8c)
- 新版 [`00420b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420b88.md#insn-00420b8c)

~~~diff
- 00420b8c ["COPY", "tmp:0:8", ["const:418:8"]]
- 00420b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420b8c ["COPY", "tmp:0:8", ["const:4c8:8"]]
+ 00420b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420b8c bytes 08611091
+ 00420b8c bytes 08211391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-819eeef95fced5a02dd1001f2cd3f59a"></a>

### [`00420ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420ba0.md) → [`00420ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ba0.md) FUN_00420ba0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00420ba8",
      "incomplete_value": false,
      "site": "00420ba8",
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
                "const:d70:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00420ba8",
      "incomplete_value": false,
      "site": "00420ba8",
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
                "const:cb0:8"
              ]
            ]
          ],
          [
            "leaf",
            "const:44:8"
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
      "00420ba8",
      "WRITE",
      [
        "storage",
        "00c24cf4",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00420ba8",
      "WRITE",
      [
        "storage",
        "00c24db4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00420ba4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420ba0.md#insn-00420ba4)
- 新版 [`00420ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420ba0.md#insn-00420ba4)

~~~diff
- 00420ba4 ["COPY", "tmp:0:8", ["const:cb0:8"]]
- 00420ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00420ba4 ["COPY", "tmp:0:8", ["const:d70:8"]]
+ 00420ba4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00420ba4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00420ba4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00420ba4 bytes 08c13291
+ 00420ba4 bytes 08c13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c66d923e1f94ad0b177c4aaf46122fd4"></a>

### [`00420bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bd8.md) → [`00420bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md) FUN_00420bd8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0041cddc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0041cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041cddc.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00420be4",
      "incomplete_value": false,
      "site": "00420be8",
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
      "definition_site": "00420be4",
      "incomplete_value": false,
      "site": "00420be8",
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
      "00420be4",
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
      "00420be4",
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

- 旧版 [`00420be4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bd8.md#insn-00420be4)
- 新版 [`00420be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bd8.md#insn-00420be4)

~~~diff
- 00420be4 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00420be4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00420be4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00420be4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00420be4 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00420be4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00420be4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00420be4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00420be4 bytes 00280c91
+ 00420be4 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcdf855afbdc65f87d1df850b0db65a4"></a>

### [`00420bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bec.md) → [`00420bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bec.md) _INIT_7

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
      "definition_site": "00420c28",
      "incomplete_value": true,
      "site": "00420c44",
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
      "definition_site": "00420c28",
      "incomplete_value": true,
      "site": "00420c44",
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
      "definition_site": "00420c4c",
      "incomplete_value": true,
      "site": "00420c68",
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
      "definition_site": "00420c4c",
      "incomplete_value": true,
      "site": "00420c68",
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
      "definition_site": "00420c6c",
      "incomplete_value": true,
      "site": "00420c88",
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
      "definition_site": "00420c6c",
      "incomplete_value": true,
      "site": "00420c88",
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
      "00420c28",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00420c4c",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00420c6c",
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
      "00420c28",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00420c4c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00420c6c",
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

- 旧版 [`00420c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bec.md#insn-00420c18) · [`00420c20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420bec.md#insn-00420c20)
- 新版 [`00420c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bec.md#insn-00420c18) · [`00420c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420bec.md#insn-00420c20)

~~~diff
- 00420c18 ["COPY", "tmp:0:8", ["const:990:8"]]
- 00420c18 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00420c18 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00420c18 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00420c18 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 00420c18 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00420c18 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00420c18 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00420c18 bytes 73422691
+ 00420c18 bytes 73422991
- 00420c20 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00420c20 bytes 29f4fff0
+ 00420c20 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00420c20 bytes 29f4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a8877d7ad248b64bbb78530a76ea190"></a>

### [`00420f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420f7c.md) → [`00420f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420f7c.md) _INIT_8

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
      "definition_site": "00420fb8",
      "incomplete_value": true,
      "site": "00420fd4",
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
      "definition_site": "00420fb8",
      "incomplete_value": true,
      "site": "00420fd4",
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
      "definition_site": "00420fdc",
      "incomplete_value": true,
      "site": "00420ff8",
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
      "definition_site": "00420fdc",
      "incomplete_value": true,
      "site": "00420ff8",
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
      "definition_site": "00420ffc",
      "incomplete_value": true,
      "site": "00421018",
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
      "definition_site": "00420ffc",
      "incomplete_value": true,
      "site": "00421018",
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
      "00420fb8",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "00420fdc",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00420ffc",
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
      "00420fb8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00420fdc",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00420ffc",
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

- 旧版 [`00420fa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420f7c.md#insn-00420fa8) · [`00420fb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00420/00420f7c.md#insn-00420fb0)
- 新版 [`00420fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420f7c.md#insn-00420fa8) · [`00420fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00420/00420f7c.md#insn-00420fb0)

~~~diff
- 00420fa8 ["COPY", "tmp:0:8", ["const:a28:8"]]
- 00420fa8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00420fa8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00420fa8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00420fa8 ["COPY", "tmp:0:8", ["const:ae8:8"]]
+ 00420fa8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00420fa8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00420fa8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00420fa8 bytes 73a22891
+ 00420fa8 bytes 73a22b91
- 00420fb0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00420fb0 bytes 29f4fff0
+ 00420fb0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00420fb0 bytes 29f4fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-816bdfe1be9a001d3d68a0c11de47a30"></a>

### [`0042130c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/0042130c.md) → [`0042130c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/0042130c.md) FUN_0042130c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428010`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00bd6d60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d60.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 1件 [`00428010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428010.md) · 呼出先 8件 [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 75.64% / 新版 75.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 22件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004213d0",
      "incomplete_value": false,
      "site": "004213d0",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004213d0",
      "incomplete_value": false,
      "site": "004213d0",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00421408",
      "incomplete_value": false,
      "site": "00421408",
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
            "const:b34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421408",
      "incomplete_value": false,
      "site": "00421408",
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
            "const:a74:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042145c",
      "incomplete_value": false,
      "site": "0042145c",
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
                "const:b18:8"
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
      "definition_site": "0042145c",
      "incomplete_value": false,
      "site": "0042145c",
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
                "const:a58:8"
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
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042133c",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00421348",
      "READ",
      [
        "storage",
        "00c24a60",
        null,
        "undefined8"
      ]
    ],
    [
      "00421350",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042133c",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00421348",
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined8"
      ]
    ],
    [
      "00421350",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004213d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/0042130c.md#insn-004213d0) · [`00421408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/0042130c.md#insn-00421408) · [`0042132c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/0042130c.md#insn-0042132c)
- 新版 [`004213d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/0042130c.md#insn-004213d0) · [`00421408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/0042130c.md#insn-00421408) · [`0042132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/0042130c.md#insn-0042132c)

~~~diff
- 004213d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a70:8"]]
- 004213d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 004213d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b30:8"]]
+ 004213d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 004213d0 bytes 09710ab9
+ 004213d0 bytes 09310bb9
- 00421408 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00421408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:a74:8"]]
- 00421408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00421408 ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00421408 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:b34:8"]]
+ 00421408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00421408 bytes 09d12939
+ 00421408 bytes 09d12c39
- 0042132c ["COPY", "tmp:0:8", ["const:a88:8"]]
- 0042132c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 0042132c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 0042132c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 0042132c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 0042132c ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 0042132c ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 0042132c ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 0042132c bytes f7222a91
+ 0042132c bytes f7222d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-286e042339f6d81c8557b02c5868860c"></a>

### [`004215a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md) → [`004215a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md) FUN_004215a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 6件 [`0081f58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0081f/0081f58c.md) [`0084004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md) [`008406e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md) [`00840b80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/00840b80.md) [`00844bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 6件 [`0081f58c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f58c.md) [`0084004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) [`008406e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) [`00840b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/00840b80.md) [`00844bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) · 呼出先 4件 [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 62.07% / 新版 62.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004215f0",
      "incomplete_value": false,
      "site": "004215f0",
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
                "const:b18:8"
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
      "definition_site": "004215f0",
      "incomplete_value": false,
      "site": "004215f0",
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
                "const:a58:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:b18:8"
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
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:a58:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:8:8"
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
      "definition_site": "004215f4",
      "incomplete_value": false,
      "site": "004215f4",
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
                "const:8:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004215b0",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "004215bc",
      "DATA",
      [
        "storage",
        "00c24a58",
        null,
        "undefined8"
      ]
    ],
    [
      "004215cc",
      "PARAM",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004215b0",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "004215bc",
      "DATA",
      [
        "storage",
        "00c24b18",
        null,
        "undefined8"
      ]
    ],
    [
      "004215cc",
      "PARAM",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004215ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md#insn-004215ac) · [`004215bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md#insn-004215bc) · [`004215cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/004215a0.md#insn-004215cc)
- 新版 [`004215ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md#insn-004215ac) · [`004215bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md#insn-004215bc) · [`004215cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/004215a0.md#insn-004215cc)

~~~diff
- 004215ac ["COPY", "tmp:0:8", ["const:a88:8"]]
- 004215ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004215ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004215ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004215ac ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004215ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004215ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004215ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004215ac bytes 08212a91
+ 004215ac bytes 08212d91
- 004215bc ["COPY", "tmp:0:8", ["const:a58:8"]]
- 004215bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004215bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004215bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004215bc ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004215bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004215bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004215bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004215bc bytes 00602991
+ 004215bc bytes 00602c91
- 004215cc ["COPY", "tmp:0:8", ["const:a88:8"]]
- 004215cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004215cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004215cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004215cc ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004215cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004215cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004215cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004215cc bytes 00202a91
+ 004215cc bytes 00202d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-202796e037c38d262b779890b04566f2"></a>

### [`00421614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421614.md) → [`00421614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md) FUN_00421614

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00428080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md) [`00bdaf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf20.md)
- 新版 呼出元 1件 [`00428080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) · 呼出先 6件 [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)

変更の種類 branch_value, call_argument_candidate, call_target, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 64.29% / 新版 64.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 29件, `call_target` 1件, `store_destination` 38件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
            "const:a60:8"
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
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
                "const:b20:8"
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
      "definition_site": "00421668",
      "incomplete_value": false,
      "site": "00421668",
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
                "const:a60:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "004216ec",
      "incomplete_value": true,
      "site": "004216ec",
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
            "const:b34:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004216ec",
      "incomplete_value": true,
      "site": "004216ec",
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
            "const:a74:8"
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
      "00421628",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00421634",
      "READ",
      [
        "storage",
        "00c24a60",
        null,
        "undefined8"
      ]
    ],
    [
      "0042163c",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00421628",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00421634",
      "READ",
      [
        "storage",
        "00c24b20",
        null,
        "undefined8"
      ]
    ],
    [
      "0042163c",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004216ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421614.md#insn-004216ec) · [`00421624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421614.md#insn-00421624) · [`00421634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421614.md#insn-00421634)
- 新版 [`004216ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md#insn-004216ec) · [`00421624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md#insn-00421624) · [`00421634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md#insn-00421634)

~~~diff
- 004216ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 004216ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 004216ec ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:a74:8"]]
- 004216ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 004216ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 004216ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 004216ec ["INT_ADD", "tmp:2:8", ["register:4098:8", "const:b34:8"]]
+ 004216ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 004216ec bytes 7fd22939
+ 004216ec bytes 7fd22c39
- 00421624 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00421624 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
- 00421624 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
- 00421624 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
+ 00421624 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00421624 ["INT_CARRY", "register:105:1", ["register:40a0:8", "tmp:0:8"]]
+ 00421624 ["INT_SCARRY", "register:106:1", ["register:40a0:8", "tmp:0:8"]]
+ 00421624 ["INT_ADD", "tmp:1:8", ["register:40a0:8", "tmp:0:8"]]
- 00421624 bytes 94222a91
+ 00421624 bytes 94222d91
- 00421634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a60:8"]]
- 00421634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00421634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b20:8"]]
+ 00421634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00421634 bytes 683245f9
+ 00421634 bytes 689245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f8b9091d874617d2adf6631c9554d8"></a>

### [`00421924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md) → [`00421924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) FUN_00421924

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`004235ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md) [`00428080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md) [`00423ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423ad4.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md)
- 新版 呼出元 2件 [`004235ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00428080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) · 呼出先 10件 [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`00423ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423ad4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.69% / 新版 89.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00421a80",
      "incomplete_value": false,
      "site": "00421a80",
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
                "const:b18:8"
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
      "definition_site": "00421a80",
      "incomplete_value": false,
      "site": "00421a80",
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
                "const:a58:8"
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:b18:8"
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
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:a58:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:8:8"
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
      "definition_site": "00421a84",
      "incomplete_value": false,
      "site": "00421a84",
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
                "const:8:8"
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004219f4",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00421a5c",
      "PARAM",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00421a6c",
      "PARAM",
      [
        "storage",
        "00c24a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "004219f4",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00421a5c",
      "PARAM",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00421a6c",
      "PARAM",
      [
        "storage",
        "00c24b18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004219f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md#insn-004219f0) · [`00421a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md#insn-00421a5c) · [`00421a6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md#insn-00421a6c)
- 新版 [`004219f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md#insn-004219f0) · [`00421a5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md#insn-00421a5c) · [`00421a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md#insn-00421a6c)

~~~diff
- 004219f0 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 004219f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004219f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004219f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004219f0 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004219f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004219f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004219f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004219f0 bytes 08212a91
+ 004219f0 bytes 08212d91
- 00421a5c ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00421a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00421a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00421a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00421a5c ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00421a5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00421a5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00421a5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00421a5c bytes 00202a91
+ 00421a5c bytes 00202d91
- 00421a6c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00421a6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00421a6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00421a6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00421a6c ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 00421a6c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00421a6c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00421a6c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00421a6c bytes 21602991
+ 00421a6c bytes 21602c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a795463d8c4170922254120004830261"></a>

### [`00421b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b40.md) → [`00421b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) FUN_00421b40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0084004c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`00422098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/00422098.md) [`00424230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424230.md) [`0052dd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd44.md)
- 新版 呼出元 1件 [`0084004c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/0084004c.md) · 呼出先 13件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`00422098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md) [`00424230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424230.md) [`0052dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.64% / 新版 99.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00421dcc",
      "incomplete_value": false,
      "site": "00421dd0",
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
            "const:1c4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00421dcc",
      "incomplete_value": false,
      "site": "00421dd0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00421dcc",
      "PARAM",
      [
        "storage",
        "002a9258",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00421dcc",
      "PARAM",
      [
        "storage",
        "002a91c4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00421dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b40.md#insn-00421dcc)
- 新版 [`00421dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md#insn-00421dcc)

~~~diff
- 00421dcc ["COPY", "tmp:0:8", ["const:258:8"]]
- 00421dcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00421dcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00421dcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00421dcc ["COPY", "tmp:0:8", ["const:1c4:8"]]
+ 00421dcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00421dcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00421dcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00421dcc bytes 00600991
+ 00421dcc bytes 00100791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2744ceb77fc8b8d57a12173ea92fe484"></a>

### [`00422098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/00422098.md) → [`00422098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md) FUN_00422098

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00421b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00419/00419064.md) [`0042818c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/0042818c.md) [`00464a54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00421b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421b40.md) · 呼出先 14件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0042818c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/0042818c.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 91.47% / 新版 91.47%

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
      "definition_site": "004220d8",
      "incomplete_value": false,
      "site": "004220dc",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004220d8",
      "incomplete_value": false,
      "site": "004220dc",
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
            "const:498:8"
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
      "definition_site": "004221f4",
      "incomplete_value": true,
      "site": "004221f8",
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
      "definition_site": "004221f4",
      "incomplete_value": true,
      "site": "004221f8",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004221f0",
      "incomplete_value": true,
      "site": "004221fc",
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
      "definition_site": "004221f0",
      "incomplete_value": true,
      "site": "004221fc",
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
      "004220dc",
      "DATA",
      [
        "storage",
        "00be6498",
        null,
        "undefined *"
      ]
    ],
    [
      "004221e4",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "004221e8",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004220dc",
      "DATA",
      [
        "storage",
        "00be6548",
        null,
        "undefined *"
      ]
    ],
    [
      "004221e4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "004221e8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004220d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/00422098.md#insn-004220d8) · [`004221e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/00422098.md#insn-004221e4) · [`004221e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/00422098.md#insn-004221e8)
- 新版 [`004220d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md#insn-004220d8) · [`004221e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md#insn-004221e4) · [`004221e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/00422098.md#insn-004221e8)

~~~diff
- 004220d8 ["COPY", "tmp:0:8", ["const:498:8"]]
- 004220d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004220d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004220d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004220d8 ["COPY", "tmp:0:8", ["const:548:8"]]
+ 004220d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004220d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004220d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004220d8 bytes 08611291
+ 004220d8 bytes 08211591
- 004221e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 004221e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004221e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 004221e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004221e4 bytes 086146f9
+ 004221e4 bytes 08b946f9
- 004221e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc8:8"]]
- 004221e8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004221e8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 004221e8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 004221e8 bytes d66646f9
+ 004221e8 bytes d6be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df631a3719baaaa58f4e499bf4b89f1"></a>

### [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) → [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) FUN_004222e0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`008406e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00840/008406e4.md) [`00844bd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`004235ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md) [`00423798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md) [`00423878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423878.md) [`00424280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md)
- 新版 呼出元 2件 [`008406e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00840/008406e4.md) [`00844bd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00844/00844bd8.md) · 呼出先 42件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`004235ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00423798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`00423878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423878.md) [`00424280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.44% / 新版 93.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 1件, `store_value` 23件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0042232c",
      "incomplete_value": false,
      "site": "00422330",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042232c",
      "incomplete_value": false,
      "site": "00422330",
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
            "const:498:8"
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
      "definition_site": "00422384",
      "incomplete_value": true,
      "site": "00422388",
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
      "definition_site": "00422384",
      "incomplete_value": true,
      "site": "00422388",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00422380",
      "incomplete_value": true,
      "site": "0042238c",
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
      "definition_site": "00422380",
      "incomplete_value": true,
      "site": "0042238c",
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
      "00422330",
      "DATA",
      [
        "storage",
        "00be6498",
        null,
        "undefined *"
      ]
    ],
    [
      "00422374",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "00422378",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00422330",
      "DATA",
      [
        "storage",
        "00be6548",
        null,
        "undefined *"
      ]
    ],
    [
      "00422374",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "00422378",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042232c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md#insn-0042232c) · [`00422374`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md#insn-00422374) · [`00422378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md#insn-00422378)
- 新版 [`0042232c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md#insn-0042232c) · [`00422374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md#insn-00422374) · [`00422378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md#insn-00422378)

~~~diff
- 0042232c ["COPY", "tmp:0:8", ["const:498:8"]]
- 0042232c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042232c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042232c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042232c ["COPY", "tmp:0:8", ["const:548:8"]]
+ 0042232c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042232c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042232c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042232c bytes 08611291
+ 0042232c bytes 08211591
- 00422374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00422374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00422374 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00422374 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00422374 bytes 086146f9
+ 00422374 bytes 08b946f9
- 00422378 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:cc8:8"]]
- 00422378 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00422378 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d78:8"]]
+ 00422378 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00422378 bytes 5a6746f9
+ 00422378 bytes 5abf46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbcc7ef913d7d1a1f636fa8bb9d6657f"></a>

### [`004235ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md) → [`004235ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) FUN_004235ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md) [`0052dccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dccc.md) [`00bd6d90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd6/00bd6d90.md)
- 新版 呼出元 1件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) · 呼出先 11件 [`00421924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`0052dccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dccc.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.09% / 新版 90.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423668",
      "incomplete_value": false,
      "site": "00423668",
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
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00423668",
      "incomplete_value": false,
      "site": "00423668",
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
            "const:a70:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0042373c",
      "incomplete_value": false,
      "site": "0042373c",
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
                "const:b18:8"
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
      "definition_site": "0042373c",
      "incomplete_value": false,
      "site": "0042373c",
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
                "const:a58:8"
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
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423740",
      "incomplete_value": false,
      "site": "00423740",
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
                "const:b18:8"
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
      "definition_site": "00423740",
      "incomplete_value": false,
      "site": "00423740",
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
                "const:a58:8"
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
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00423658",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00423668",
      "WRITE",
      [
        "storage",
        "00c24a70",
        null,
        "undefined4"
      ]
    ],
    [
      "00423710",
      "PARAM",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00423658",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00423668",
      "WRITE",
      [
        "storage",
        "00c24b30",
        null,
        "undefined4"
      ]
    ],
    [
      "00423710",
      "PARAM",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00423668`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md#insn-00423668) · [`00423654`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md#insn-00423654) · [`00423708`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md#insn-00423708)
- 新版 [`00423668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md#insn-00423668) · [`00423654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md#insn-00423654) · [`00423708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md#insn-00423708)

~~~diff
- 00423668 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a70:8"]]
- 00423668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
+ 00423668 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:b30:8"]]
+ 00423668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:4"]]
- 00423668 bytes 20710ab9
+ 00423668 bytes 20310bb9
- 00423654 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00423654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00423654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00423654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00423654 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423654 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00423654 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00423654 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00423654 bytes 08212a91
+ 00423654 bytes 08212d91
- 00423708 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00423708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00423708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00423708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00423708 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423708 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00423708 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00423708 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00423708 bytes 08212a91
+ 00423708 bytes 08212d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dbdfd89512ffa972148b7c8dc7e17fa"></a>

### [`00423798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md) → [`00423798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) FUN_00423798

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00421924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md) [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`004235ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/004235ac.md) [`00423bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b064.md) [`0052dd5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd5c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 4件 [`00421924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`004235ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/004235ac.md) [`00423bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md) · 呼出先 4件 [`0041b064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b064.md) [`0052dd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd5c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004237e0",
      "incomplete_value": true,
      "site": "004237e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004237e0",
      "incomplete_value": true,
      "site": "004237e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd3:8"
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
      "004237cc",
      "READ",
      [
        "storage",
        "00298bd3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004237cc",
      "READ",
      [
        "storage",
        "00298c60",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004237c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md#insn-004237c4)
- 新版 [`004237c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md#insn-004237c4)

~~~diff
- 004237c4 ["COPY", "tmp:0:8", ["const:bd3:8"]]
- 004237c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004237c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004237c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004237c4 ["COPY", "tmp:0:8", ["const:c60:8"]]
+ 004237c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004237c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004237c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004237c4 bytes 294d2f91
+ 004237c4 bytes 29813191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afab626404d00c55805f50ca4fe8882e"></a>

### [`00423bbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bbc.md) → [`00423bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md) FUN_00423bbc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00423fe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423798.md) [`004782e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00478/004782e4.md) [`0052dd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd44.md) [`0052dd48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0052d/0052dd48.md)
- 新版 呼出元 1件 [`00423fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe4.md) · 呼出先 16件 [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00423798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423798.md) [`004782e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00478/004782e4.md) [`0052dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd44.md) [`0052dd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0052d/0052dd48.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 81.08% / 新版 81.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 20件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423d80",
      "incomplete_value": false,
      "site": "00423d80",
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
                "const:b18:8"
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
      "definition_site": "00423d80",
      "incomplete_value": false,
      "site": "00423d80",
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
                "const:a58:8"
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
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:b18:8"
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
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:a58:8"
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:8:8"
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
      "definition_site": "00423d84",
      "incomplete_value": false,
      "site": "00423d84",
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
                "const:8:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00423bf0",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00423c00",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00423c38",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00423bf0",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00423c00",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00423c38",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00423bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bbc.md#insn-00423bec) · [`00423c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bbc.md#insn-00423c44) · [`00423c68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423bbc.md#insn-00423c68)
- 新版 [`00423bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md#insn-00423bec) · [`00423c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md#insn-00423c44) · [`00423c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423bbc.md#insn-00423c68)

~~~diff
- 00423bec ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00423bec ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00423bec ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00423bec ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00423bec ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00423bec ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00423bec ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00423bec ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00423bec bytes f7222a91
+ 00423bec bytes f7222d91
- 00423c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a58:8"]]
- 00423c44 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00423c44 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b18:8"]]
+ 00423c44 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00423c44 bytes 142d45f9
+ 00423c44 bytes 148d45f9
- 00423c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00423c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00423c68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b38:8"]]
+ 00423c68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00423c68 bytes 083d45f9
+ 00423c68 bytes 089d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f1a385bba695d1d8ec7d96e363ecf73"></a>

### [`00423f2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423f2c.md) → [`00423f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423f2c.md) FUN_00423f2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb060.md) [`00bdb070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 73.91% / 新版 73.91%

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
      "definition_site": "00423f5c",
      "incomplete_value": true,
      "site": "00423f64",
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
      "definition_site": "00423f5c",
      "incomplete_value": true,
      "site": "00423f64",
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
      "definition_site": "00423f68",
      "incomplete_value": true,
      "site": "00423f68",
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
      "definition_site": "00423f68",
      "incomplete_value": true,
      "site": "00423f68",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00423f78",
      "incomplete_value": true,
      "site": "00423f78",
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
                "register:4000:8"
              ],
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
      "definition_site": "00423f78",
      "incomplete_value": true,
      "site": "00423f78",
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
                "register:4000:8"
              ],
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
      "00423f48",
      "READ",
      [
        "storage",
        "00c1acc0",
        null,
        "pointer"
      ]
    ],
    [
      "00423f4c",
      "READ",
      [
        "storage",
        "00c1acc8",
        null,
        "pointer"
      ]
    ],
    [
      "00423f58",
      "READ",
      [
        "storage",
        "00c13358",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00423f48",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "00423f4c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00423f58",
      "READ",
      [
        "storage",
        "00c13408",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00423f48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423f2c.md#insn-00423f48) · [`00423f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423f2c.md#insn-00423f4c) · [`00423f50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423f2c.md#insn-00423f50)
- 新版 [`00423f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423f2c.md#insn-00423f48) · [`00423f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423f2c.md#insn-00423f4c)

~~~diff
- 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00423f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00423f48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
+ 00423f48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00423f48 bytes 086146f9
+ 00423f48 bytes 08b946f9
- 00423f4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:cc8:8"]]
- 00423f4c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00423f4c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
+ 00423f4c ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 00423f4c bytes d66646f9
+ 00423f4c bytes d6be46f9
- 00423f50 ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00423f50 bytes f50300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bdfe97bf76dd8eb475dc23c243db4d2"></a>

### [`00423fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423fe8.md) → [`00423fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe8.md) FUN_00423fe8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00423ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/004240ec.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1b0.md) [`00bdb1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb1c0.md)
- 新版 呼出元 1件 [`00423ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423ad4.md) · 呼出先 6件 [`004240ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/004240ec.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb260.md) [`00bdb270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb270.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0042409c",
      "incomplete_value": false,
      "site": "004240a0",
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
      "definition_site": "0042409c",
      "incomplete_value": false,
      "site": "004240a0",
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
      "0042409c",
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
      "0042409c",
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

- 旧版 [`0042409c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00423/00423fe8.md#insn-0042409c)
- 新版 [`0042409c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00423/00423fe8.md#insn-0042409c)

~~~diff
- 0042409c ["COPY", "tmp:0:8", ["const:544:8"]]
- 0042409c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042409c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042409c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042409c ["COPY", "tmp:0:8", ["const:5d1:8"]]
+ 0042409c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042409c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042409c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042409c bytes 21101591
+ 0042409c bytes 21441791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09f1155ffd854606f02fb59b7e6584f2"></a>

### [`00424280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md) → [`00424280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) FUN_00424280

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`00424280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00424280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "004243d4",
      "incomplete_value": false,
      "site": "004243dc",
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
      "definition_site": "004243d4",
      "incomplete_value": false,
      "site": "004243dc",
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
      "definition_site": "00424490",
      "incomplete_value": false,
      "site": "00424498",
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
      "definition_site": "00424490",
      "incomplete_value": false,
      "site": "00424498",
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
      "definition_site": "00424800",
      "incomplete_value": false,
      "site": "00424810",
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
      "definition_site": "00424800",
      "incomplete_value": false,
      "site": "00424810",
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
      "004243d4",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00424490",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00424800",
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
      "004243d4",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00424490",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00424800",
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

- 旧版 [`004243d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md#insn-004243d4) · [`00424490`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md#insn-00424490) · [`00424800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md#insn-00424800)
- 新版 [`004243d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md#insn-004243d4) · [`00424490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md#insn-00424490) · [`00424800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md#insn-00424800)

~~~diff
- 004243d4 ["COPY", "tmp:0:8", ["const:311:8"]]
- 004243d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004243d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004243d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004243d4 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 004243d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004243d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004243d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004243d4 bytes 21440c91
+ 004243d4 bytes 21280c91
- 00424490 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00424490 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00424490 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00424490 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00424490 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00424490 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00424490 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00424490 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00424490 bytes 21d40b91
+ 00424490 bytes 21b80b91
- 00424800 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00424800 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00424800 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00424800 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00424800 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00424800 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00424800 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00424800 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00424800 bytes 63941791
+ 00424800 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-839a76f129a4a6f0263a6c2f1884dc52"></a>

### [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) → [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) FUN_00424bb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 27件 [`00424280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424280.md) [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004264e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md) [`00426e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md) [`005be404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 27件 [`00424280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424280.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`00426e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) [`005be404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00424d08",
      "incomplete_value": false,
      "site": "00424d10",
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
      "definition_site": "00424d08",
      "incomplete_value": false,
      "site": "00424d10",
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
      "definition_site": "00424e60",
      "incomplete_value": false,
      "site": "00424e68",
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
      "definition_site": "00424e60",
      "incomplete_value": false,
      "site": "00424e68",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00424f08",
      "incomplete_value": false,
      "site": "00424f14",
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
    "old": {
      "definition_site": "00424f08",
      "incomplete_value": false,
      "site": "00424f14",
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
      "00424d08",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00424e60",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00424f08",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00424d08",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00424e60",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00424f08",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00424d08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md#insn-00424d08) · [`00424e60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md#insn-00424e60) · [`00424f08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md#insn-00424f08)
- 新版 [`00424d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md#insn-00424d08) · [`00424e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md#insn-00424e60) · [`00424f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md#insn-00424f08)

~~~diff
- 00424d08 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00424d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00424d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00424d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00424d08 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00424d08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00424d08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00424d08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00424d08 bytes 21440c91
+ 00424d08 bytes 21280c91
- 00424e60 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00424e60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00424e60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00424e60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00424e60 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00424e60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00424e60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00424e60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00424e60 bytes 21d40b91
+ 00424e60 bytes 21b80b91
- 00424f08 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00424f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00424f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00424f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00424f08 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00424f08 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00424f08 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00424f08 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00424f08 bytes 21681f91
+ 00424f08 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562d687b895d54f8e08ae65ffdd9f773"></a>

### [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) → [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) FUN_004253b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 170件 [`00424bb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md) [`00458974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00458/00458974.md) [`0059fbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0059f/0059fbec.md) [`005a45f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 170件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00458974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00458/00458974.md) [`0059fbec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0059f/0059fbec.md) [`005a45f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005a4/005a45f4.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00425504",
      "incomplete_value": false,
      "site": "0042550c",
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
      "definition_site": "00425504",
      "incomplete_value": false,
      "site": "0042550c",
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
      "definition_site": "0042565c",
      "incomplete_value": false,
      "site": "00425664",
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
      "definition_site": "0042565c",
      "incomplete_value": false,
      "site": "00425664",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00425704",
      "incomplete_value": false,
      "site": "00425710",
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
    "old": {
      "definition_site": "00425704",
      "incomplete_value": false,
      "site": "00425710",
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
      "00425504",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "0042565c",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00425704",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00425504",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0042565c",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00425704",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00425504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md#insn-00425504) · [`0042565c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md#insn-0042565c) · [`00425704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/004253b4.md#insn-00425704)
- 新版 [`00425504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md#insn-00425504) · [`0042565c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md#insn-0042565c) · [`00425704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md#insn-00425704)

~~~diff
- 00425504 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00425504 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00425504 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00425504 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00425504 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00425504 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00425504 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00425504 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00425504 bytes 21440c91
+ 00425504 bytes 21280c91
- 0042565c ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 0042565c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0042565c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0042565c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0042565c ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 0042565c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0042565c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0042565c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0042565c bytes 21d40b91
+ 0042565c bytes 21b80b91
- 00425704 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00425704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00425704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00425704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00425704 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00425704 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00425704 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00425704 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00425704 bytes 21681f91
+ 00425704 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e46741b8a0b6b88c6cbd1268dfd21a4b"></a>

### [`00425ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md) → [`00425ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) FUN_00425ba0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`00425ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00425ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) · 呼出先 23件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

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
      "definition_site": "00425cf8",
      "incomplete_value": false,
      "site": "00425d00",
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
      "definition_site": "00425cf8",
      "incomplete_value": false,
      "site": "00425d00",
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
      "definition_site": "00425db4",
      "incomplete_value": false,
      "site": "00425dbc",
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
      "definition_site": "00425db4",
      "incomplete_value": false,
      "site": "00425dbc",
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
      "definition_site": "00426128",
      "incomplete_value": false,
      "site": "00426138",
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
      "definition_site": "00426128",
      "incomplete_value": false,
      "site": "00426138",
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
      "00425cf8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00425db4",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00426128",
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
      "00425cf8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00425db4",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00426128",
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

- 旧版 [`00425cf8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md#insn-00425cf8) · [`00425db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md#insn-00425db4) · [`00426128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md#insn-00426128)
- 新版 [`00425cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md#insn-00425cf8) · [`00425db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md#insn-00425db4) · [`00426128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md#insn-00426128)

~~~diff
- 00425cf8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00425cf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00425cf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00425cf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00425cf8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00425cf8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00425cf8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00425cf8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00425cf8 bytes 21440c91
+ 00425cf8 bytes 21280c91
- 00425db4 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00425db4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00425db4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00425db4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00425db4 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00425db4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00425db4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00425db4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00425db4 bytes 21d40b91
+ 00425db4 bytes 21b80b91
- 00426128 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00426128 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00426128 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00426128 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00426128 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00426128 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00426128 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00426128 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00426128 bytes 63941791
+ 00426128 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2e64505083d14e709631de45762b024"></a>

### [`004264e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md) → [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) FUN_004264e8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`00425ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00425/00425ba0.md) [`004264e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md) [`005be404`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005be/005be404.md) [`005fa9ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005fa/005fa9ec.md) [`005fd41c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 10件 [`00425ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/00425ba0.md) [`004264e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md) [`005be404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005be/005be404.md) [`005fa9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fa/005fa9ec.md) [`005fd41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005fd/005fd41c.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.92% / 新版 98.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00426640",
      "incomplete_value": false,
      "site": "00426648",
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
      "definition_site": "00426640",
      "incomplete_value": false,
      "site": "00426648",
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
      "definition_site": "00426798",
      "incomplete_value": false,
      "site": "004267a0",
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
      "definition_site": "00426798",
      "incomplete_value": false,
      "site": "004267a0",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00426840",
      "incomplete_value": false,
      "site": "0042684c",
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
    "old": {
      "definition_site": "00426840",
      "incomplete_value": false,
      "site": "0042684c",
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
      "00426640",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00426798",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00426840",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00426640",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00426798",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00426840",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00426640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md#insn-00426640) · [`00426798`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md#insn-00426798) · [`00426840`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/004264e8.md#insn-00426840)
- 新版 [`00426640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md#insn-00426640) · [`00426798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md#insn-00426798) · [`00426840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/004264e8.md#insn-00426840)

~~~diff
- 00426640 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00426640 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00426640 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00426640 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00426640 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00426640 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00426640 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00426640 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00426640 bytes 21440c91
+ 00426640 bytes 21280c91
- 00426798 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00426798 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00426798 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00426798 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00426798 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00426798 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00426798 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00426798 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00426798 bytes 21d40b91
+ 00426798 bytes 21b80b91
- 00426840 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00426840 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00426840 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00426840 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00426840 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00426840 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00426840 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00426840 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00426840 bytes 21681f91
+ 00426840 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a158936e270de55e866a73841ca1d5"></a>

### [`00426e78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e78.md) → [`00426e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md) FUN_00426e78

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`00426cec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426cec.md) [`004c2f88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/004c2/004c2f88.md) [`005aca98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005ac/005aca98.md) [`005af810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005af/005af810.md) [`0073ea18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c38.md)
- 新版 呼出元 8件 [`00426cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426cec.md) [`004c2f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c2/004c2f88.md) [`005aca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005ac/005aca98.md) [`005af810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005af/005af810.md) [`0073ea18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ea18.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)

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
      "definition_site": "00426e84",
      "incomplete_value": false,
      "site": "00426e88",
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
      "definition_site": "00426e84",
      "incomplete_value": false,
      "site": "00426e88",
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
      "00426e84",
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
      "00426e84",
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

- 旧版 [`00426e84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e78.md#insn-00426e84)
- 新版 [`00426e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e78.md#insn-00426e84)

~~~diff
- 00426e84 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00426e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00426e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00426e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00426e84 ["COPY", "tmp:0:8", ["const:303:8"]]
+ 00426e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00426e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00426e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00426e84 bytes 00280c91
+ 00426e84 bytes 000c0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfc2135c055fc4dbd2ec4dabc8641646"></a>

### [`00426e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md) → [`00426e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) FUN_00426e8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`00426e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md) [`0046c588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0046c/0046c588.md) [`005b7004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 4件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00426e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md) [`0046c588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046c/0046c588.md) [`005b7004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b7/005b7004.md) · 呼出先 21件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.03% / 新版 99.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00426ff8",
      "incomplete_value": false,
      "site": "00427000",
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
      "definition_site": "00426ff8",
      "incomplete_value": false,
      "site": "00427000",
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
      "definition_site": "004270b8",
      "incomplete_value": false,
      "site": "004270c0",
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
      "definition_site": "004270b8",
      "incomplete_value": false,
      "site": "004270c0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00427394",
      "incomplete_value": false,
      "site": "004273a4",
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
      "definition_site": "00427394",
      "incomplete_value": false,
      "site": "004273a4",
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
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00426ff8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "004270b8",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00427394",
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
      "00426ff8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "004270b8",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00427394",
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

- 旧版 [`00426ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md#insn-00426ff8) · [`004270b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md#insn-004270b8) · [`00427394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00426/00426e8c.md#insn-00427394)
- 新版 [`00426ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md#insn-00426ff8) · [`004270b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md#insn-004270b8) · [`00427394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00426/00426e8c.md#insn-00427394)

~~~diff
- 00426ff8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 00426ff8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00426ff8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00426ff8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00426ff8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 00426ff8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00426ff8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00426ff8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00426ff8 bytes 21440c91
+ 00426ff8 bytes 21280c91
- 004270b8 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 004270b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004270b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004270b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004270b8 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 004270b8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004270b8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004270b8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004270b8 bytes 21d40b91
+ 004270b8 bytes 21b80b91
- 00427394 ["COPY", "tmp:0:8", ["const:5e5:8"]]
- 00427394 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00427394 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00427394 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00427394 ["COPY", "tmp:0:8", ["const:672:8"]]
+ 00427394 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00427394 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00427394 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00427394 bytes 63941791
+ 00427394 bytes 63c81991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0ae49c1c2486194fc0fe8e8a11be635"></a>

### [`00427778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427778.md) → [`00427778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md) FUN_00427778

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`004222e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00422/004222e0.md) [`00427778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`004222e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00422/004222e0.md) [`00427778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.90% / 新版 98.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004278c8",
      "incomplete_value": false,
      "site": "004278d0",
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
      "definition_site": "004278c8",
      "incomplete_value": false,
      "site": "004278d0",
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
      "definition_site": "00427a20",
      "incomplete_value": false,
      "site": "00427a28",
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
      "definition_site": "00427a20",
      "incomplete_value": false,
      "site": "00427a28",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00427ac8",
      "incomplete_value": false,
      "site": "00427ad4",
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
    "old": {
      "definition_site": "00427ac8",
      "incomplete_value": false,
      "site": "00427ad4",
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
      "004278c8",
      "PARAM",
      [
        "storage",
        "002a7311",
        null,
        null
      ]
    ],
    [
      "00427a20",
      "PARAM",
      [
        "storage",
        "002a52f5",
        null,
        null
      ]
    ],
    [
      "00427ac8",
      "PARAM",
      [
        "storage",
        "002967da",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004278c8",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "00427a20",
      "PARAM",
      [
        "storage",
        "002a52ee",
        null,
        null
      ]
    ],
    [
      "00427ac8",
      "PARAM",
      [
        "storage",
        "00296867",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004278c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427778.md#insn-004278c8) · [`00427a20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427778.md#insn-00427a20) · [`00427ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427778.md#insn-00427ac8)
- 新版 [`004278c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md#insn-004278c8) · [`00427a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md#insn-00427a20) · [`00427ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427778.md#insn-00427ac8)

~~~diff
- 004278c8 ["COPY", "tmp:0:8", ["const:311:8"]]
- 004278c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004278c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004278c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004278c8 ["COPY", "tmp:0:8", ["const:30a:8"]]
+ 004278c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004278c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004278c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004278c8 bytes 21440c91
+ 004278c8 bytes 21280c91
- 00427a20 ["COPY", "tmp:0:8", ["const:2f5:8"]]
- 00427a20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00427a20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00427a20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00427a20 ["COPY", "tmp:0:8", ["const:2ee:8"]]
+ 00427a20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00427a20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00427a20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00427a20 bytes 21d40b91
+ 00427a20 bytes 21b80b91
- 00427ac8 ["COPY", "tmp:0:8", ["const:7da:8"]]
- 00427ac8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00427ac8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00427ac8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00427ac8 ["COPY", "tmp:0:8", ["const:867:8"]]
+ 00427ac8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00427ac8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00427ac8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00427ac8 bytes 21681f91
+ 00427ac8 bytes 219c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbea4600e839c849bbd8ec7f87e56f82"></a>

### [`00427f68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427f68.md) → [`00427f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f68.md) FUN_00427f68

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
      "definition_site": "00427f7c",
      "incomplete_value": false,
      "site": "00427f80",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f7c",
      "incomplete_value": false,
      "site": "00427f80",
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
            "const:510:8"
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
      "00427f80",
      "DATA",
      [
        "storage",
        "00be6510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00427f80",
      "DATA",
      [
        "storage",
        "00be65c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427f7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427f68.md#insn-00427f7c)
- 新版 [`00427f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f68.md#insn-00427f7c)

~~~diff
- 00427f7c ["COPY", "tmp:0:8", ["const:510:8"]]
- 00427f7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427f7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427f7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00427f7c ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00427f7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00427f7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00427f7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427f7c bytes 08411491
+ 00427f7c bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e79d1667083e0affe162cf2b4142bd6"></a>

### [`00427f8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427f8c.md) → [`00427f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f8c.md) FUN_00427f8c

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
      "definition_site": "00427f90",
      "incomplete_value": false,
      "site": "00427f94",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427f90",
      "incomplete_value": false,
      "site": "00427f94",
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
            "const:510:8"
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
      "00427f94",
      "DATA",
      [
        "storage",
        "00be6510",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00427f94",
      "DATA",
      [
        "storage",
        "00be65c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427f8c.md#insn-00427f90)
- 新版 [`00427f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427f8c.md#insn-00427f90)

~~~diff
- 00427f90 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00427f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00427f90 ["COPY", "tmp:0:8", ["const:5c0:8"]]
+ 00427f90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00427f90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00427f90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427f90 bytes 08411491
+ 00427f90 bytes 08011791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ace05eb1a57433c5ad37c8e2f1ecf72"></a>

### [`00427fd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427fd4.md) → [`00427fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427fd4.md) FUN_00427fd4

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
      "definition_site": "00427fe8",
      "incomplete_value": false,
      "site": "00427fec",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427fe8",
      "incomplete_value": false,
      "site": "00427fec",
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
            "const:590:8"
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
      "00427fec",
      "DATA",
      [
        "storage",
        "00be6590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00427fec",
      "DATA",
      [
        "storage",
        "00be6640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427fd4.md#insn-00427fe8)
- 新版 [`00427fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427fd4.md#insn-00427fe8)

~~~diff
- 00427fe8 ["COPY", "tmp:0:8", ["const:590:8"]]
- 00427fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00427fe8 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00427fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00427fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00427fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427fe8 bytes 08411691
+ 00427fe8 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff5f61dadc2c85ab0cab7aafe02f5c3"></a>

### [`00427ff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427ff8.md) → [`00427ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427ff8.md) FUN_00427ff8

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
      "definition_site": "00427ffc",
      "incomplete_value": false,
      "site": "00428000",
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
            "const:640:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00427ffc",
      "incomplete_value": false,
      "site": "00428000",
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
            "const:590:8"
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
      "00428000",
      "DATA",
      [
        "storage",
        "00be6590",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00428000",
      "DATA",
      [
        "storage",
        "00be6640",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00427ffc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00427/00427ff8.md#insn-00427ffc)
- 新版 [`00427ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00427/00427ff8.md#insn-00427ffc)

~~~diff
- 00427ffc ["COPY", "tmp:0:8", ["const:590:8"]]
- 00427ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00427ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00427ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00427ffc ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00427ffc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00427ffc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00427ffc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00427ffc bytes 08411691
+ 00427ffc bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfa73aeb2b46021873c6c67b9b34e9a0"></a>

### [`00428044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428044.md) → [`00428044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428044.md) FUN_00428044

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
      "definition_site": "00428058",
      "incomplete_value": false,
      "site": "0042805c",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428058",
      "incomplete_value": false,
      "site": "0042805c",
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
            "const:610:8"
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
      "0042805c",
      "DATA",
      [
        "storage",
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0042805c",
      "DATA",
      [
        "storage",
        "00be66c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428058`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428044.md#insn-00428058)
- 新版 [`00428058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428044.md#insn-00428058)

~~~diff
- 00428058 ["COPY", "tmp:0:8", ["const:610:8"]]
- 00428058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428058 ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 00428058 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428058 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428058 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428058 bytes 08411891
+ 00428058 bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50c4a354c8efe08dcd309baf31b27d83"></a>

### [`00428068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428068.md) → [`00428068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428068.md) FUN_00428068

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
      "definition_site": "0042806c",
      "incomplete_value": false,
      "site": "00428070",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042806c",
      "incomplete_value": false,
      "site": "00428070",
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
            "const:610:8"
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
      "00428070",
      "DATA",
      [
        "storage",
        "00be6610",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00428070",
      "DATA",
      [
        "storage",
        "00be66c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0042806c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428068.md#insn-0042806c)
- 新版 [`0042806c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428068.md#insn-0042806c)

~~~diff
- 0042806c ["COPY", "tmp:0:8", ["const:610:8"]]
- 0042806c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0042806c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0042806c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0042806c ["COPY", "tmp:0:8", ["const:6c0:8"]]
+ 0042806c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0042806c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0042806c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0042806c bytes 08411891
+ 0042806c bytes 08011b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a19ba50044de04608e62f9f36039cc2"></a>

### [`00428080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md) → [`00428080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md) FUN_00428080

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00421614`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421614.md) [`00421924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00421/00421ad4.md) [`00bdaee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaee0.md) [`00bdaf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf00.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00421614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421614.md) [`00421924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421924.md) [`00421ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00421/00421ad4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 65.62% / 新版 65.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 5件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004280dc",
      "incomplete_value": false,
      "site": "004280dc",
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
                "const:b18:8"
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
      "definition_site": "004280dc",
      "incomplete_value": false,
      "site": "004280dc",
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
                "const:a58:8"
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
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:b18:8"
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
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:a58:8"
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:8:8"
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
      "definition_site": "004280e0",
      "incomplete_value": false,
      "site": "004280e0",
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
                "const:8:8"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0042809c",
      "READ",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ],
    [
      "004280a8",
      "PARAM",
      [
        "storage",
        "00c24a58",
        null,
        "undefined8"
      ]
    ],
    [
      "004280b8",
      "PARAM",
      [
        "storage",
        "00c24a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0042809c",
      "READ",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ],
    [
      "004280a8",
      "PARAM",
      [
        "storage",
        "00c24b18",
        null,
        "undefined8"
      ]
    ],
    [
      "004280b8",
      "PARAM",
      [
        "storage",
        "00c24b48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428098`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md#insn-00428098) · [`004280a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md#insn-004280a8) · [`004280b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428080.md#insn-004280b8)
- 新版 [`00428098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md#insn-00428098) · [`004280a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md#insn-004280a8) · [`004280b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428080.md#insn-004280b8)

~~~diff
- 00428098 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 00428098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428098 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 00428098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428098 bytes 08212a91
+ 00428098 bytes 08212d91
- 004280a8 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 004280a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004280a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004280a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004280a8 ["COPY", "tmp:0:8", ["const:b18:8"]]
+ 004280a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004280a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004280a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004280a8 bytes 00602991
+ 004280a8 bytes 00602c91
- 004280b8 ["COPY", "tmp:0:8", ["const:a88:8"]]
- 004280b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004280b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004280b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004280b8 ["COPY", "tmp:0:8", ["const:b48:8"]]
+ 004280b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004280b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004280b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004280b8 bytes 00202a91
+ 004280b8 bytes 00202d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be540d2194ccf2443d63e8a64e2675cf"></a>

### [`00428290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428290.md) → [`00428290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428290.md) _INIT_9

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
      "definition_site": "004282cc",
      "incomplete_value": true,
      "site": "004282e8",
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
      "definition_site": "004282cc",
      "incomplete_value": true,
      "site": "004282e8",
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
      "definition_site": "004282f0",
      "incomplete_value": true,
      "site": "0042830c",
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
      "definition_site": "004282f0",
      "incomplete_value": true,
      "site": "0042830c",
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
      "definition_site": "00428310",
      "incomplete_value": true,
      "site": "0042832c",
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
      "definition_site": "00428310",
      "incomplete_value": true,
      "site": "0042832c",
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
      "004282cc",
      "READ",
      [
        "storage",
        "002a72e4",
        null,
        "string"
      ]
    ],
    [
      "004282f0",
      "READ",
      [
        "storage",
        "002a72f7",
        null,
        "string"
      ]
    ],
    [
      "00428310",
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
      "004282cc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "004282f0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00428310",
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

- 旧版 [`004282bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428290.md#insn-004282bc) · [`004282c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428290.md#insn-004282c4)
- 新版 [`004282bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428290.md#insn-004282bc) · [`004282c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428290.md#insn-004282c4)

~~~diff
- 004282bc ["COPY", "tmp:0:8", ["const:a40:8"]]
- 004282bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 004282bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 004282bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 004282bc ["COPY", "tmp:0:8", ["const:b00:8"]]
+ 004282bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 004282bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 004282bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 004282bc bytes 73022991
+ 004282bc bytes 73022c91
- 004282c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 004282c4 bytes e9f3fff0
+ 004282c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 004282c4 bytes e9f3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21145eed823479873d6b6584e9ef8db3"></a>

### [`00428620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428620.md) → [`00428620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428620.md) FUN_00428620

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0042d2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042d/0042d2a8.md) · 呼出先 0件 
- 新版 呼出元 1件 [`0042d2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d2a8.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042862c",
      "incomplete_value": true,
      "site": "0042863c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:675:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042862c",
      "incomplete_value": true,
      "site": "0042863c",
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
                "const:2ac000:8"
              ],
              [
                "leaf",
                "const:67e:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00428640",
      "incomplete_value": true,
      "site": "00428640",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428640",
      "incomplete_value": true,
      "site": "00428640",
      "value": [
        "LOAD",
        "8",
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
      "0042862c",
      "READ",
      [
        "storage",
        "002ac67e",
        null,
        "string"
      ]
    ],
    [
      "00428634",
      "READ",
      [
        "storage",
        "002ac68c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0042862c",
      "READ",
      [
        "storage",
        "002ac675",
        null,
        "string"
      ]
    ],
    [
      "00428634",
      "READ",
      [
        "storage",
        "002ac683",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428620.md#insn-00428628)
- 新版 [`00428628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428620.md#insn-00428628)

~~~diff
- 00428628 ["COPY", "tmp:0:8", ["const:67e:8"]]
- 00428628 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00428628 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00428628 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00428628 ["COPY", "tmp:0:8", ["const:675:8"]]
+ 00428628 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00428628 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00428628 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00428628 bytes 4af91991
+ 00428628 bytes 4ad51991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb3c091307a4c961ac25bc1a197598c3"></a>

### [`00428648`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428648.md) → [`00428648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md) FUN_00428648

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00605bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00605/00605bdc.md) [`006091c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00609/006091c4.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md)
- 新版 呼出元 3件 [`00605bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00605/00605bdc.md) [`006091c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/006091c4.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428670",
      "incomplete_value": true,
      "site": "00428680",
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
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428670",
      "incomplete_value": true,
      "site": "00428680",
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
                "const:70a:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00428684",
      "incomplete_value": true,
      "site": "00428684",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428684",
      "incomplete_value": true,
      "site": "00428684",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 7,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428690",
      "incomplete_value": false,
      "site": "00428698",
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
            "const:686:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428690",
      "incomplete_value": false,
      "site": "00428698",
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
            "const:5f9:8"
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
      "00428670",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00428678",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00428690",
      "PARAM",
      [
        "storage",
        "002925f9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428670",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00428678",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00428690",
      "PARAM",
      [
        "storage",
        "00292686",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428664`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428648.md#insn-00428664) · [`00428690`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428648.md#insn-00428690)
- 新版 [`00428664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md#insn-00428664) · [`00428690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428648.md#insn-00428690)

~~~diff
- 00428664 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00428664 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00428664 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00428664 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00428664 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00428664 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00428664 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00428664 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00428664 bytes 29291c91
+ 00428664 bytes 29d91991
- 00428690 ["COPY", "tmp:0:8", ["const:5f9:8"]]
- 00428690 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00428690 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00428690 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00428690 ["COPY", "tmp:0:8", ["const:686:8"]]
+ 00428690 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00428690 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00428690 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00428690 bytes 21e41791
+ 00428690 bytes 21181a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cd23c710de749a4954e9f1da3f3ba7a"></a>

### [`00428714`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428714.md) → [`00428714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md) FUN_00428714

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00429a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00429/00429a14.md) [`0079bdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00574/00574744.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb020`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb020.md) [`00bdb030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb030.md)
- 新版 呼出元 4件 [`00429a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00429/00429a14.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) [`00868124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00868/00868124.md) · 呼出先 5件 [`00574744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574744.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428740",
      "incomplete_value": true,
      "site": "00428750",
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
                "const:676:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428740",
      "incomplete_value": true,
      "site": "00428750",
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
                "const:70a:8"
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
      "definition_site": "00428754",
      "incomplete_value": true,
      "site": "00428754",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00428754",
      "incomplete_value": true,
      "site": "00428754",
      "value": [
        "LOAD",
        "8",
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00428760",
      "incomplete_value": false,
      "site": "00428768",
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
            "const:30d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428760",
      "incomplete_value": false,
      "site": "00428768",
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
            "const:314:8"
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
      "00428740",
      "READ",
      [
        "storage",
        "002ae70a",
        null,
        "string"
      ]
    ],
    [
      "00428748",
      "READ",
      [
        "storage",
        "002ae718",
        null,
        "string"
      ]
    ],
    [
      "00428760",
      "PARAM",
      [
        "storage",
        "002a7314",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428740",
      "READ",
      [
        "storage",
        "002ae676",
        null,
        "string"
      ]
    ],
    [
      "00428748",
      "READ",
      [
        "storage",
        "002ae684",
        null,
        "string"
      ]
    ],
    [
      "00428760",
      "PARAM",
      [
        "storage",
        "002a730d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428734`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428714.md#insn-00428734) · [`00428760`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428714.md#insn-00428760)
- 新版 [`00428734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md#insn-00428734) · [`00428760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428714.md#insn-00428760)

~~~diff
- 00428734 ["COPY", "tmp:0:8", ["const:70a:8"]]
- 00428734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00428734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00428734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00428734 ["COPY", "tmp:0:8", ["const:676:8"]]
+ 00428734 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00428734 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00428734 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00428734 bytes 29291c91
+ 00428734 bytes 29d91991
- 00428760 ["COPY", "tmp:0:8", ["const:314:8"]]
- 00428760 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00428760 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00428760 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00428760 ["COPY", "tmp:0:8", ["const:30d:8"]]
+ 00428760 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00428760 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00428760 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00428760 bytes 21500c91
+ 00428760 bytes 21340c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9b0bc459ba4972076fae14fa51eb88b"></a>

### [`004288b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md) → [`004288b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md) FUN_004288b4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 10件 [`0042f000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0042f/0042fd7c.md) [`00432904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432904.md) [`00432e80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00432/00432e80.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 10件 [`0042f000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f000.md) [`0042f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042f610.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00432904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432904.md) [`00432e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00432/00432e80.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.00% / 新版 85.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:241:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
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
                "const:2a1000:8"
              ],
              [
                "leaf",
                "const:1b4:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
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
      "definition_site": "004288e4",
      "incomplete_value": true,
      "site": "004288f0",
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
      "004288e4",
      "READ",
      [
        "storage",
        "002a11b4",
        null,
        "string"
      ]
    ],
    [
      "004288e4",
      "READ",
      [
        "storage",
        "002a11c4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004288e4",
      "READ",
      [
        "storage",
        "002a1241",
        null,
        "string"
      ]
    ],
    [
      "004288e4",
      "READ",
      [
        "storage",
        "002a1251",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004288e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/004288b4.md#insn-004288e0)
- 新版 [`004288e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/004288b4.md#insn-004288e0)

~~~diff
- 004288e0 ["COPY", "tmp:0:8", ["const:1b4:8"]]
- 004288e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004288e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004288e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004288e0 ["COPY", "tmp:0:8", ["const:241:8"]]
+ 004288e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004288e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004288e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004288e0 bytes 08d10691
+ 004288e0 bytes 08050991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f85450bdd1b4c4096a738e201414d1e0"></a>

### [`00428904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428904.md) → [`00428904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428904.md) FUN_00428904

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 4件 [`004303e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/004303e0.md) [`0057ecc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057e/0057ecc8.md) [`0057fee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/0057f/0057fee8.md) [`00581790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00581/00581790.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 4件 [`004303e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/004303e0.md) [`0057ecc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057e/0057ecc8.md) [`0057fee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0057f/0057fee8.md) [`00581790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00581/00581790.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
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
                "const:869:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
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
                "const:7dc:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
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
      "definition_site": "00428928",
      "incomplete_value": true,
      "site": "0042893c",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428940",
      "incomplete_value": true,
      "site": "00428940",
      "value": [
        "LOAD",
        "8",
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
                "const:1e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00428940",
      "incomplete_value": true,
      "site": "00428940",
      "value": [
        "LOAD",
        "8",
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
                "const:1e:8"
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
      "00428928",
      "READ",
      [
        "storage",
        "002967dc",
        null,
        "string"
      ]
    ],
    [
      "00428928",
      "READ",
      [
        "storage",
        "002967ec",
        null,
        "string"
      ]
    ],
    [
      "00428930",
      "READ",
      [
        "storage",
        "002967fa",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428928",
      "READ",
      [
        "storage",
        "00296869",
        null,
        "string"
      ]
    ],
    [
      "00428928",
      "READ",
      [
        "storage",
        "00296879",
        null,
        "string"
      ]
    ],
    [
      "00428930",
      "READ",
      [
        "storage",
        "00296887",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428904.md#insn-00428920) · [`00428924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428904.md#insn-00428924)
- 新版 [`00428920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428904.md#insn-00428920) · [`00428924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428904.md#insn-00428924)

~~~diff
- 00428920 ["COPY", "tmp:0:8", ["const:7dc:8"]]
- 00428920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428920 ["COPY", "tmp:0:8", ["const:869:8"]]
+ 00428920 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428920 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428920 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428920 bytes 08711f91
+ 00428920 bytes 08a52191
- 00428924 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 00428924 bytes 49f4ffb0
+ 00428924 ["COPY", "register:4048:8", ["const:2b1000:8"]]
+ 00428924 bytes 49f4ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55de744ba7fa0a1efe51b1dd08023749"></a>

### [`00428954`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428954.md) → [`00428954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428954.md) FUN_00428954

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00430dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00430/00430dd8.md) · 呼出先 1件 [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md)
- 新版 呼出元 1件 [`00430dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00430/00430dd8.md) · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.00% / 新版 70.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
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
                "const:2a9000:8"
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
    "old": {
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
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
                "const:2a9000:8"
              ],
              [
                "leaf",
                "const:25c:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
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
      "definition_site": "00428978",
      "incomplete_value": true,
      "site": "00428988",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0042898c",
      "incomplete_value": true,
      "site": "00428990",
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
                "const:1a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0042898c",
      "incomplete_value": true,
      "site": "00428990",
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
                "const:1a:8"
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
      "00428978",
      "READ",
      [
        "storage",
        "002a925c",
        null,
        "string"
      ]
    ],
    [
      "00428978",
      "READ",
      [
        "storage",
        "002a926c",
        null,
        "string"
      ]
    ],
    [
      "0042898c",
      "READ",
      [
        "storage",
        "002a9276",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00428978",
      "READ",
      [
        "storage",
        "002a91c8",
        null,
        "string"
      ]
    ],
    [
      "00428978",
      "READ",
      [
        "storage",
        "002a91d8",
        null,
        "string"
      ]
    ],
    [
      "0042898c",
      "READ",
      [
        "storage",
        "002a91e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00428970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428954.md#insn-00428970) · [`00428974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00428/00428954.md#insn-00428974)
- 新版 [`00428970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428954.md#insn-00428970) · [`00428974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428954.md#insn-00428974)

~~~diff
- 00428970 ["COPY", "tmp:0:8", ["const:25c:8"]]
- 00428970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00428970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00428970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00428970 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00428970 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00428970 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00428970 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00428970 bytes 08710991
+ 00428970 bytes 08210791
- 00428974 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00428974 bytes 49f4ff90
+ 00428974 ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 00428974 bytes 49f4ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

